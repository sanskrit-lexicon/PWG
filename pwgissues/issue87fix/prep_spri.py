# coding=utf-8
""" prep_spri.py
    
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

class REPL:
 def __init__(self,line):
  self.line = line
  parts = line.split('\t')
  assert len(parts) == 5
  self.status = parts[0]
  self.nparm = int(parts[1])
  self.lnum = int(parts[2])
  self.old = parts[3]
  self.new = parts[4]
  assert self.new == ''
  
def repls_d(repls):
 d = {}
 for repl in repls:
  if repl.status != 'fixed':
   print('Cannot split',repl.line)
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

def split_main(s):
 assert s.endswith('</ls>')
 s = s.replace('</ls>','')
 start0 = '<ls n="Spr.">(I) '
 start1 = '<ls n="Spr. (I)">'
 start2 = '<ls>Spr. (I) '
 start = None
 for x in [start0,start1,start2]:
  if s.startswith(x):
   start = x
   break
 if start == None:
  return None
 rest = s[len(start):]
 rest = rest.replace('2844.fg.',  '2844. fg.')
 end ='</ls>'
 parts = rest.split(' ')
 splits = []
 dbg = True
 for ipart,part in enumerate(parts):
  if part in ('fg.','fgg.', 'v.', 'l.'):
   split = splits.pop()
   split1 = split.replace(end,'')
   split2 = split1 + ' ' + part + end
   splits.append(split2)
   if dbg:print(part,s)
   continue
  if not re.search(r'^[0-9]+[.,]?$',part):
   # can't handle
   return None
  if ipart == 0:
   split = '%s%s</ls>' %(start,part)
  else:
   split = '%s%s</ls>' %(start1,part)
  splits.append(split)
 splitval = ' '.join(splits)
 return splitval

def split(repls):
 for repl in repls:
  replnew = split_main(repl.old)
  if replnew == None:
   repl.new = repl.old  # program can't handle
  else:
   repl.new = replnew
   repl.status = 'fixed'

def get_newlines(repls):
 ans = []
 for repl in repls:
  parts = (repl.status, repl.nparm,repl.lnum,repl.old,repl.new)
  parts1 = [str(part) for part in parts]
  line = '\t'.join(parts1)
  ans.append(line)
 return ans
if __name__=="__main__":
 filein = sys.argv[1] 
 fileout = sys.argv[2] 
 lines = read_lines(filein)
 repls = [REPL(line) for line in lines]
 split(repls)
 newlines = get_newlines(repls)
 write_lines(fileout,newlines)
 
