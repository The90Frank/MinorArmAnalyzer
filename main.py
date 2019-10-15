#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import copy
import json
import time
import ntpath
import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser(description="descrizione da mettere")
    parser.add_argument("--install", help="installa il necessario", action='store_true', default=False, required=False)

    parser.add_argument("-f", "--file", help="file assembly", type=str, default=None, required=False)
    parser.add_argument("-nostdlib", help="compila senza stdlib", action='store_true', default=False, required=False)
    parser.add_argument("-td", help="compilazione a 32 bit", action='store_true', default=False, required=False)

    parser.add_argument("-mi", "--maxinst", help="numero massimo di istruzioni da simulare (default: 1000)", type=int, default=1000, required=False)
    
    parser.add_argument("-fs", "--functionstart", help="funzione da cui iniziare", type=str, default="", required=False)
    parser.add_argument("-cs", "--ciclestart", help="ciclo da cui iniziare", type=int, default=0, required=False)
    parser.add_argument("-ce", "--cicleend", help="ciclo con cui terminare", type=int, default=None, required=False)
    parser.add_argument("-i", "--int", help="valore dei registri intero", action='store_true', default=False, required=False)
    
    argms = parser.parse_args()
    
    if (argms.install):
        print("Inizio Installazione")
        subprocess.run(["sudo", "apt-get", "update"])
        subprocess.run(["sudo", "apt-get", "upgrade"])
        subprocess.run(["sudo", "apt-get", "install", "mercurial", "scons", "swig", "gcc", "m4", "python", "python-dev", "libgoogle-perftools-dev", "g++", "python3", "python3-pip", "python-pip", "libc6-armel-cross", "libc6-dev-armel-cross", "binutils-arm-linux-gnueabi", "libncurses5-dev", "gcc-arm-linux-gnueabihf", "gcc-aarch64-linux-gnu", "g++-arm-linux-gnueabihf", "git-core", "libboost-dev", "zlib1g-dev"])
        subprocess.run(["pip3", "install", "argparse", "six", "capstone"])
        subprocess.run(["pip", "install", "argparse", "six", "capstone"])
        subprocess.run(["git", "clone", "https://github.com/gem5/gem5.git"])
        subprocess.run(["scons", "build/ARM/gem5.debug", "-j4"],cwd='gem5')
        subprocess.run([sys.argv[0], "-f", "Programmi/test.s", "-nostdlib", "-mi", "100", "-fs", "_start", "-td"])
        print("Fine Installazione")

    elif not(argms.file is None):

        path = ntpath.realpath(argms.file)
        path=path.replace('\\', '/')
        filename = ntpath.basename(argms.file)
        
        pathobject = path+".o"
        if os.path.exists(pathobject):
            os.remove(pathobject)

        traceoutfile = filename+".trace"
        traceoutfilepath = 'm5out/'+traceoutfile
        if os.path.exists(traceoutfilepath):
            os.remove(traceoutfilepath)

        visualtrace = filename+".out"
        if os.path.exists(visualtrace):
            os.remove(visualtrace)
        
        maxinst = str(argms.maxinst)
        visualarray = ["./visualizer.py", "-f", traceoutfilepath, "-cs", str(argms.ciclestart)]
        if argms.functionstart != '':
            visualarray.insert(3, argms.functionstart)
            visualarray.insert(3, "-fs")
        if not(argms.cicleend is None): 
            visualarray.insert(3, str(argms.cicleend))
            visualarray.insert(3, "-ce")
        if argms.int:
            visualarray.insert(3, "-i")
        
        visualtracefile = open(visualtrace, "w")
        nullfile = open("/dev/null","w")

        print('Inizio compilazione')
        if not argms.td :
            if argms.nostdlib : subprocess.run(["aarch64-linux-gnu-gcc", "-nostdlib", "-march=armv8-a", "--static", "-o", pathobject, path])
            else: subprocess.run(["aarch64-linux-gnu-gcc", "--static", "-march=armv8-a", "-o", pathobject, path])
        else:
            if argms.nostdlib : subprocess.run(["arm-linux-gnueabihf-gcc", "-nostdlib", "-mcpu=cortex-a7", "--static", "-o", pathobject, path])
            else: subprocess.run(["arm-linux-gnueabihf-gcc", "--static", "-mcpu=cortex-a7", "-o", pathobject, path])
        if not os.path.exists(pathobject):
            print('Compilazione fallita')
            sys.exit()
        print('Fine compilazione')
        time.sleep(1)
        
        print('Inizio Simulazione')
        subprocess.run(["gem5/build/ARM/gem5.debug", "--debug-flags=All", "--debug-file="+traceoutfile, "--debug-start=0", "gem5/configs/example/se.py", "--maxinst="+maxinst, "--cpu-type=MinorCPU", "--caches", "-c", pathobject], stderr=nullfile)
        if not os.path.exists(traceoutfilepath):
            print('Simulazione fallita')
            sys.exit()
        subprocess.run(visualarray, stdout=visualtracefile)
        print('dumped on '+visualtrace)
        print('Fine Simulazione')

        visualtracefile.close()
        nullfile.close()

    else:
        parser.print_help()
        sys.exit()

main()