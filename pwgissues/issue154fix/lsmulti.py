# coding=utf-8
""" lsmulti.py
"""
from __future__ import print_function
import sys, re, codecs
from lsmulti_parm import multiobj
from lsfix import get_REGEXes_standard

def read_lines(filein,commentFlag=False):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines1 = [x.rstrip('\r\n') for x in f]
 if commentFlag:
  # remove 'comments' - lines start with ';'
  lines = [x for x in lines1 if not x.startswith(';')]
  print(len(lines),"kept.")
  print(len(lines1),'lines read from',filein)
 else:
  lines = lines1
  print(len(lines1),'lines read from',filein)
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"lines written to",fileout)

class REPL:
 def __init__(self,line):
  self.line = line
  parts = line.split('\t')
  assert len(parts) == 4
  self.status = parts[0]
  self.lnum = int(parts[1])
  self.old = parts[2]
  self.new = parts[3]
  self.multi_status = None
  
def repls_d(repls):
 d = {}
 for repl in repls:
  if repl.status != 'fixed':
   continue
  lnum = repl.lnum
  if lnum not in d:
   d[lnum] = []
  d[lnum].append(repl)
 lnums = d.keys()
 print(len(lnums),'lines to change')
 return d

def apply_repls(lines,replsd):
 newlines = []
 nchg = 0 # number of lines changed
 for iline,line in enumerate(lines):
  lnum = iline + 1
  if lnum not in replsd:
   newlines.append(line)
   continue
  repls = replsd[lnum]
  newline = line
  for repl in repls:
   newline = newline.replace(repl.old,repl.new)
  newlines.append(newline)
  assert newline != line
  nchg = nchg + 1
 print('apply_repls: %s lines changed' % nchg)
 return newlines

class Multi_standard:
 def __init__(self,multiparm,regexes_standard):
  self.lscode = multiparm['lscode']
  self.status = multiparm['status']
  self.nparm  = multiparm['nparm']
  self.regexes_raw = regexes_standard
  self.regexes = [re.compile(reg) for reg in regexes_standard]
  self.multi_status = None
 
def check(repl,multi_standards):
 # 1. get multi_standard with same status as repl
 multi_standard0 = [ms for ms in multi_standards if repl.status == str(ms.status)]
 if len(multi_standard0) != 1:
  print('check error 1',repl.status, len(multi_standard0))
  # print('multi_standards=',multi_standards)
  for ms in multi_standards:
   print(ms.lscode, ms.status, ms.nparm,repl.status, repl.status == ms.status,type(repl.status), type(ms.status))
  exit(1)
 multi_status = None
 multi_standard = multi_standard0[0]
 # 2.
 regexes_standard = multi_standard.regexes
 old = repl.old
 for regex in regexes_standard:
  if re.search(regex,old):
    multi_status = True
    break
 repl.multi_status = multi_status
 
if __name__=="__main__":
 code = sys.argv[1]
 filein = sys.argv[2]  # lsfix output file, used as input
 fileout = sys.argv[3] # output file
 if code not in multiobj:
  print('Unknown code:',code)
  exit(1)
 multiparms = multiobj[code] # an array of (anonymous) objects
 multi_standards = [] # list of Multi_standard objecte
 dbg = False
 for multiparm in multiparms:
  if dbg: print('multiparm=',multiparm)
  REGEXes_standard = get_REGEXes_standard(multiparm)
  if dbg:
   for reg in REGEXes_standard:
    print('standard regex:',reg.regex)
  if dbg:print('--------------------')
  a = [reg.regex for reg in REGEXes_standard]
  regexes_standard = sorted(a,key = lambda x: len(x),reverse=True)
  multi_standard = Multi_standard(multiparm,regexes_standard)
  multi_standards.append(multi_standard)
 lines = read_lines(filein,commentFlag=True)
 repls = [REPL(line) for line in lines]
 nprob = 0
 for repl in repls:
  check(repl,multi_standards)
  if not repl.multi_status:
   print('PROBLEM:',repl.line)
   nprob = nprob + 1
 print('lsmulti finds %s problems' % nprob)
 exit(1)
  
 # d = repls_d(repls)
 newlines = apply_repls(lines,d)
 write_lines(fileout,newlines)
 
