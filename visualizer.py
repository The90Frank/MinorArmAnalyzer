#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import copy
import json
import argparse

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

def main():
   parser = argparse.ArgumentParser(description="descrizione da mettere")
   parser.add_argument("-f", "--file", help="file da parsare", type=str, required=True)
   parser.add_argument("-fs", "--functionstart", help="funzione da cui iniziare", type=str, default="", required=False)
   parser.add_argument("-cs", "--ciclestart", help="ciclo da cui iniziare", type=int, default=0, required=False)
   parser.add_argument("-ce", "--cicleend", help="ciclo con cui terminare", type=int, default=None, required=False)
   parser.add_argument("-i", "--int", help="valore dei registri intero", action='store_true', default=False, required=False)
   argms = parser.parse_args()

   print(str(type(argms.int)) + " " + str(argms.int))

   if not (os.path.isfile(argms.file)):
      parser.print_help()
      sys.exit()

   path = argms.file
   f = open(path, "r")
   tracefile = f.read()
   tracelist = tracefile.split("\n")
   
   with open('config.json', 'r') as f:
      lablemap = json.load(f)

   stagelist=[
      'icache',
      'fetch1.transfers',
      'fetch1',
      'f1ToF2',
      'f2ToF1',
      'fetch2',
      'f2ToD',
      'decode',
      'dToE',
      'execute.inputBuffer0',
      'stall',
      'scoreboard',
      'execute',
      'eToF1',
      'execute.fu.0',
      'execute.fu.1',
      'execute.fu.2',
      'execute.fu.3',
      'execute.fu.4',
      'execute.fu.5',
      'execute.fu.6',
      'execute.fu.7',
      'execute.inFlightInsts0',
      'execute.lsq.transfers',
      'execute.lsq.storeBuffer',
      'execute.inFUMemInsts0',
      'dcache',
      'completed'
   ]

   Emptystagedump={
      'icache'  : [],
      'fetch1.transfers': [],
      'fetch1'  : [],
      'f1ToF2'  : [],
      'f2ToF1'  : [],
      'fetch2'  : [],
      'f2ToD'   : [],
      'decode'  : [],
      'dToE'    : [],
      'execute.inputBuffer0' : [],
      'stall'   : [],
      'scoreboard' : [],
      'execute' : [],
      'eToF1'   : [],
      'execute.fu.0' : [],
      'execute.fu.1' : [],
      'execute.fu.2' : [],
      'execute.fu.3' : [],
      'execute.fu.4' : [],
      'execute.fu.5' : [],
      'execute.fu.6' : [],
      'execute.fu.7' : [],
      'execute.inFlightInsts0' : [],
      'execute.lsq.transfers'  : [],
      'execute.lsq.storeBuffer': [],
      'execute.inFUMemInsts0'  : [],
      'dcache'    : [],
      'completed' : []
   }

   lasttime = -1
   stagedump={}
   functionstartcicle = None
   functionstartinst = None
   code_inst = {"-":"-", "":"", "R":"-"}
   code_pc = {"-":"-", "":""}
   code_trace = {}

   def codeToInst(s):
      cc = s
      if s.count('.') == 1:
         try: cc = code_inst[s]
         except: cc = s
      elif s.count('.') == 2:
         ss = s[:s.rfind('.')]
         try: cc = code_inst[ss]
         except: cc = s
      else: 
         return cc
      return cc

   def codeToPc(s):
      cc = '??'
      if s.count('.') == 1:
         try: cc = code_pc[s]
         except: cc = '??'
      elif s.count('.') == 2:
         ss = s[:s.rfind('.')]
         try: cc = code_pc[ss]
         except: cc = '??'
      else: 
         try: cc = code_pc[s]
         except: cc = '??'
      return cc

   def appendtupinlist(tup,lista):
      for t in tup:
         lista.append(t)
   
   def codetupler(lin):
      tup = []
      dp = lin.rfind('),(')
      lsp = lin.rfind('),-')
      rsp = lin.find('-,(')
      np = lin.find('-,-')
      if dp != -1: 
         ftup = lin.split('),(')
         for ft in reversed(ftup):
            subtup = ft.replace("(","").replace(")","").split(',')
            for st in subtup:
               tup.append(st)

      if lsp != -1:
         tup.append("-")
         tup.append("-")
         ftup = lin.split('),-')
         for ft in reversed(ftup):
            subtup = ft.replace("(","").replace(")","").split(',')
            for st in subtup:
               tup.append(st)
         
      if rsp != -1: 
         ftup = lin.split('),-')
         for ft in reversed(ftup):
            subtup = ft.replace("(","").replace(")","").split(',')
            for st in subtup:
               tup.append(st)
         tup.append("-")
         tup.append("-")

      if np != -1: tup = ['-','-','-','-']
      return tup
      

   scoreboardtrace = {}

   registers = []
   for i in range(0,16):
      registers.append('0')
   registers_trace = { 0 : registers }

   for line in tracelist:
      try:
         time = int ( int(line[:line.find(':')].replace(" ","")) / 500 )
      except:
         continue

      if lasttime != time:
         try: 
            if(stagedump[lasttime] == Emptystagedump): stagedump[lasttime]={}
         except: pass
         lasttime=time
         stagedump[time] = copy.deepcopy(Emptystagedump)

      if (argms.functionstart != "") and (line.find("system.cpu ") != -1) and (line.find(argms.functionstart) != -1):
         if functionstartcicle is None:
            functionstartcicle = time
            functionstartinst = line[find_nth(line,':',3)+1:find_nth(line,':',4)].strip()

      if (line.find("system.cpu.icache: access for ReadReq") != -1):
         mess = line[line.find('ReadReq')+7:]
         stagedump[time]['icache'].append(mess)

      if (line.find("system.cpu.icache: Block") != -1):
         mess = line[line.find('Block')+5:]
         stagedump[time]['icache'].append(mess)

      if (line.find("system.cpu.fetch1.transfers: MinorTrace:") != -1):
         tup = codetupler(line[line.find("lines=")+6:])
         appendtupinlist(tup,stagedump[time]['fetch1.transfers'])

      if (line.find("system.cpu.fetch1: MinorLine") != -1):
         code = line[line.rfind("id=")+3:line.rfind("size")].replace(" ","")
         fsize = line[line.rfind("size=")+5:line.rfind("vaddr")].replace(" ","")
         fvaddr = line[line.rfind("vaddr=")+6:line.rfind("paddr")].replace(" ","")
         fpaddr = line[line.rfind("paddr=")+6:].replace(" ","")
         code_inst[code]=(fsize,fvaddr,fpaddr)

      if (line.find("system.cpu.fetch1: Processing fetched line:") != -1):
         code = line[line.rfind(":")+1:].replace(" ","")
         stagedump[time]['fetch1'].append(code)

      if (line.find("system.cpu.f1ToF2: MinorTrace:") != -1):
         tup = codetupler(line[line.find("lines=")+6:])
         appendtupinlist(tup,stagedump[time]['f1ToF2'])

      if (line.find("system.cpu.f2ToF1: MinorTrace:") != -1):
         tup = codetupler(line[line.find("prediction=")+11:])
         appendtupinlist(tup,stagedump[time]['f2ToF1'])

      if (line.find("system.cpu.fetch2: MinorTrace:") != -1):
         tup = line[line.find("insts=")+6:].replace('(', '').replace(')', '').split(',')
         appendtupinlist(tup,stagedump[time]['fetch2'])

      if (line.find("system.cpu.fetch2: decoder inst") != -1):
         code = line[line.find("inst")+4:line.find("pc")].replace(" ","")
         pc = line[line.find("pc:")+3:line.rfind("(")].replace(" ","")
         inst=line[line.find("(")+1:line.find(")")].strip()
         code_inst[code]=inst
         if argms.int: pc=str( int(pc,16) )
         code_pc[code] = pc

      if (line.find("system.cpu.f2ToD: MinorTrace:") != -1):
         tup = codetupler(line[line.find("insts=")+6:])
         appendtupinlist(tup,stagedump[time]['f2ToD'])

      if (line.find("system.cpu.decode: Passing on inst:") != -1):
         code = line[line.find("inst:")+5:line.find("pc")].replace(" ","")
         stagedump[time]['decode'].append(code)

      if (line.find("system.cpu.dToE: MinorTrace: insts") != -1):
         tup = codetupler(line[line.find("insts=")+6:])
         appendtupinlist(tup,stagedump[time]['dToE'])

      if (line.find("system.cpu.execute.inputBuffer0: MinorTrace: insts=") != -1):
         tup = ( line[line.find("insts=")+6:].replace("(","").replace(")","") ).split(',')
         appendtupinlist(tup,stagedump[time]['execute.inputBuffer0'])

      if (line.find('system.cpu.execute.lsq.transfers: MinorTrace:') != -1):
         tup = ( line[line.find("addr=")+5:] ).split(',')
         for t in tup:
            tt = t.split(';')
            try: stagedump[time]['execute.lsq.transfers'].append(tt[1])
            except: pass

      if (line.find("system.cpu.execute.lsq.storeBuffer: MinorTrace:") != -1):
         tup = ( line[line.find("addr=")+5:line.find("num_")-1] ).split(',')
         for t in tup:
            tt = t.split(';')
            try: stagedump[time]['execute.lsq.storeBuffer'].append(tt[1])
            except: pass

      if (line.find("system.cpu.execute: MinorInst:") != -1):
         code=line[line.find("id=")+3:line.find("addr=")].replace(" ","")
         codecut = code[:code.rfind('.')]
         inst=line
         if (line.find("inst=") != -1):
            inst=line[line.find("inst=")+5:line.find("class=")].replace('"',"").strip()
         elif (line.find("fault=") != -1):
            inst=line[line.find("fault=")+6:].replace('"', '')
            ##################################################
            pc=line[line.find("addr=")+5:line.find("fault=")]
            if argms.int: pc=str( int(pc,16) )
            code_pc[codecut]=pc
            ##################################################
         code_inst[codecut]=inst
         stagedump[time]['execute'].append(code)
      
      if (line.find("system.cpu.execute: Didn't issue inst:") != -1):
         code = line[line.find('inst:')+6:line.find(' pc')]
         stagedump[time]['stall'].append(code)

      if (line.find("system.cpu.execute.fu.") != -1):
         tup = ( line[line.find("insts=")+6:] ).split(',')
         try: core = int ( line[line.find(".fu.")+4:line.find(": MinorTrace:")] )
         except: continue
         for j in range(0,len(tup)):
            code = tup[j]
            stagedump[time]['execute.fu.'+str(core)].insert(0,code)

      if (line.find("system.cpu.eToF1: MinorTrace:") != -1):
         tup = codetupler(line[line.find("branch=")+7:])
         appendtupinlist(tup,stagedump[time]['eToF1'])

      if (line.find("system.cpu.execute: Completed inst:") != -1):
         code = line[line.find("inst:")+5:line.find("pc")].replace(" ","")
         pc = line[line.find("pc:")+3:line.rfind("(")].replace(" ","")
         stagedump[time]['completed'].append(code)

      if (line.find("system.cpu.execute.inFlightInsts0: MinorTrace:") != -1):
         tup = ( line[line.find("insts=")+6:] ).split(',')
         for t in tup:
            stagedump[time]['execute.inFlightInsts0'].append(t)

      if (line.find("system.cpu.dcache: access for ReadReq") != -1):
         mess = line[line.find('ReadReq')+7:]
         stagedump[time]['dcache'].append(mess)

      if (line.find("system.cpu.dcache: Block") != -1):
         mess = line[line.find('Block')+5:]
         stagedump[time]['dcache'].append(mess)

      if (line.find("system.cpu.execute.inFUMemInsts0: MinorTrace:") != -1):
         tup = ( line[line.find("insts=")+6:] ).split(',')
         appendtupinlist(tup,stagedump[time]['execute.inFUMemInsts0'])

      if (line.find(": Setting int reg ") != -1):
         reg = int ( line[line.find('(')+1:line.find(')')] )
         if reg < 16:
            val = line[line.find('to')+2:-1]
            try: 
               registers_trace[time]
            except: 
               for i in reversed(range(0,time)):
                  try:
                     registers_trace[time] = registers_trace[i].copy()
                     break
                  except: 
                     continue
            if argms.int == False: registers_trace[time][reg] = val 
            else: registers_trace[time][reg] = int(val,16)
      
      if (line.find(": system.cpu.execute.scoreboard0: MinorTrace: busy=(") != -1):
         obj = line[line.find('('):]
         sbi = obj.split('),(')
         scoreboarditem = []
         for i in sbi:
            aux = i.replace('(', '')
            aux = aux.replace(')', '')
            aux2 = aux.split(',')
            reg = aux2[0]
            aux2 = aux2[1].split('/')
            end = aux2[2]
            inst = aux2[3]
            stagedump[time]['scoreboard'].append((reg,end,inst))


   timelist = list(stagedump.keys())
   timelist.sort()

   if not (functionstartcicle is None):
      codeselected=''
      for t in stagedump[functionstartcicle]['completed']:
         if codeToInst(t) == functionstartinst:
            codeselected=t[:t.rfind('.')]
            break
      for i in range(min(timelist), functionstartcicle):
         if i in stagedump.keys():
            try:
               if codeselected in stagedump[i]['fetch2']:
                  argms.ciclestart = i
            except:
               pass

   start = argms.ciclestart
   end = max(timelist) + 1
   if not (argms.cicleend is None):
      end = argms.cicleend + 1

   def condprint(s):
      if i>= start and i <= end:
         print(str(s))

   lasttime = {'reg':0}
   lung = max(len(x) for x in stagelist)    

   for i in range(min(timelist), end):
      if i in stagedump.keys():
         condprint(("clockCicle").ljust(lung, " ")+": "+str(i))
         
         try:
            for k in stagelist:
               if (k in lablemap) and (lablemap[k] != ""):
                  lable = lablemap[k].ljust(lung, " ")+": "
                  array = []
                  
                  if k == "scoreboard":
                     for r in stagedump[i][k]:
                        try:
                           for rr in stagedump[i]['execute.inFlightInsts0']:
                              execnumber = rr[rr.rfind('.')+1:]
                              if (execnumber == r[2]):
                                 if len(codeToInst(rr)) > 0:
                                    array.append( ('R'+r[0] , 'StableClock: '+r[1], 'Dependency: '+codeToInst(rr)) )
                        except Exception as e:
                           #condprint(e)
                           pass
                  else:
                     for r in reversed(stagedump[i][k]):
                        if len(codeToInst(r)) > 0:
                           array.append( (codeToPc(r) , codeToInst(r)) )
                     
                  condprint(lable + str(array))
         except Exception as e: 
            #condprint(e)
            pass

         #stampa del dump dei registri
         arraryreg = []
         try:
            index = 0
            for r in registers_trace[i]:
               arraryreg.append( 'R' + str(index) + ': ' + str(r) )
               index = index+1
            lasttime['reg'] = i
         except:
            index = 0
            for r in registers_trace[lasttime['reg']]:
               arraryreg.append( 'R' + str(index) + ': ' + str(r) )
               index = index+1
         condprint(arraryreg)
         
         condprint('')

main()