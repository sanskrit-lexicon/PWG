# coding=utf-8
""" change_from_lsfix.py
"""
from __future__ import print_function
import sys, re, codecs

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

class unused_REPL:
 def __init__(self,line):
  self.line = line
  parts = line.split('\t')
  assert len(parts) == 5
  self.status = parts[0]
  self.nparm = int(parts[1])
  self.lnum = int(parts[2])
  self.old = parts[3]
  self.new = parts[4]
  
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

class FIXDATA:
 def __init__(self,line):
  self.line = line
  parts = line.split('\t') # split at tabs
  self.parts = parts
  self.status = parts[0]
  self.nparm = parts[1]
  self.lnum = parts[2] # a string
  self.lsold = parts[3]
  self.lsnew = parts[4]

def remove1(recs):
 ans = []
 LS = 'VARĀH. BṚH. S.'
 regexes = [
   r'<ls n="%s">[0-9.]+</ls>' % LS,
   r'<ls>%s [0-9.]+</ls>' % LS,
  ]
 for rec in recs:
  flag = True  # keep record
  for regex in regexes:
   if re.search(regex,rec.lsold):
    flag = False
    break
  if flag:
   ans.append(rec)
 return ans

def write_recs(fileout,recs):
 outlines = []
 for rec in recs:
  parts = rec.parts
  parts[4] = parts[3]
  out = '\t'.join(parts)
  outlines.append(out)
 write_lines(fileout,outlines)
 
if __name__=="__main__":
 filein = sys.argv[1]  # lsfix2_x.txt
 fileout = sys.argv[2] # 
 lines = read_lines(filein)

 recs = [FIXDATA(line) for line in lines]
 # keep only None, False
 recs1 = [rec for rec in recs if rec.status not in ('True','fixed')]
 recs2 = remove1(recs1)
 write_recs(fileout,recs2)
 
