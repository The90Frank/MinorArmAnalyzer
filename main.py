#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import copy
import json
import time
import argparse
import subprocess
import ntpath

def main():
    parser = argparse.ArgumentParser(description="descrizione da mettere")
    parser.add_argument("--install", help="installa il necessario", action='store_true', default=False, required=False)

    parser.add_argument("-f", "--file", help="file assembly", type=str, default=None, required=False)
    
    parser.add_argument("-mi", "--maxinst", help="numero massimo di istruzioni da simulare (default: 1000)", type=int, default=1000, required=False)
    
    parser.add_argument("-fs", "--functionstart", help="funzione da cui iniziare", type=str, default="", required=False)
    parser.add_argument("-cs", "--ciclestart", help="ciclo da cui iniziare", type=int, default=0, required=False)
    parser.add_argument("-ce", "--cicleend", help="ciclo con cui terminare", type=int, default=None, required=False)
    parser.add_argument("-i", "--int", help="valore dei registri e del program counter intero", action='store_true', default=False, required=False)
    
    argms = parser.parse_args()
    
    if (argms.install):
        print("Requires: python3, pip3")
        subprocess.run(["pip", "install", "argparse"])
        #TO DO

    elif not(argms.file is None):

        path = ntpath.realpath(argms.file)
        if not os.name == 'nt':
            path=path.replace('\\', '/')
        filename = ntpath.basename(argms.file)
        pathobject = path+".o"
        traceoutfile = 'm5out/'+filename+".trace"
        visualtrace = filename+".out"
        maxinst = str(argms.maxinst)
        visualarray = ["./visualizer.py", "-f", traceoutfile, "-cs", str(argms.ciclestart)]
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
        subprocess.run(["arm-linux-gnueabihf-gcc", "-nostdlib", "--static", "-o", pathobject, path])
        print('Fine compilazione')

        time.sleep(1)
        
        print('Inizio Simulazione')
        subprocess.run(["../gem5/build/ARM/gem5.debug", "--debug-flags=All", "--debug-file="+traceoutfile, "--debug-start=0", "../gem5/configs/example/se.py", "--maxinst="+maxinst, "--cpu-type=MinorCPU", "--caches", "-c", pathobject], stderr=nullfile)
        subprocess.run(visualarray, stdout=visualtracefile)
        print('dumped on '+visualtrace)
        print('Fine Simulazione')

        visualtracefile.close()
        nullfile.close()

    else:
        parser.print_help()
        sys.exit()

main()