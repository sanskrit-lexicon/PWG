# coding=utf-8
""" prepare_printchange.py
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
 print(len(outarr),"cases written to",fileout)

def get_replacements(lines):
 ans = []  # list of Change objects
 n = 0
 d = {} # for unique
 ndup = 0 # number of duplicate lines
 for line in lines:
  n = n + 1
  parts = line.split('\t')
  old = parts[0]
  new = parts[1]
  repl = (old,new)
  if old in d:
   ndup = ndup + 1
   print('skipping dup:',old)
   continue
  else:
   change = Change(old,new)
   ans.append(change)
 print(len(ans),"replacements found")
 print(ndup,"duplicates noticed")
 return ans

class Change:
 def __init__(self,old,new):
  self.old = old
  self.new = new
  self.metas= []
  self.used = 0

def write_changes(fileout,changes):
 outarr = []
 n = 0 # number not changed
 for change in changes:
  old = change.old
  new = change.new
  if change.used == 0:
   print('change not used ....')
   out = 'None : None : %s : %s' % (old,new)
  else:
   for meta in change.metas:
    m = re.search(r'<L>(.*?)<pc>.*?<k1>(.*?)<k2',meta)
    L = m.group(1)
    k1 = m.group(2)
    fields = []
    fields.append(L.ljust(10))
    fields.append(k1.ljust(10))
    fields.append(old.ljust(50))
    fields.append(new)
    out = ' : '.join(fields)
    #out = '%s : %s : %s : %s' % (L,k1,old,new)
  outarr.append(out)
 write_lines(fileout,outarr)

def apply_repls(lines,repls):
 newlines = []
 nchg = 0 # number of lines changed
 for line in lines:
  if line.startswith('<L>'):
   metaline = line
   continue
  newline = line
  for repl in repls:
   old = repl.old
   new = repl.new
   newline1= newline.replace(old,new)
   if newline1 != newline:
    repl.metas.append(metaline)
    repl.used = repl.used + 1
 

if __name__=="__main__":
 filein = sys.argv[1]  # kosha
 filein1 = sys.argv[2] # line string replacements
 fileout = sys.argv[3] # revised kosha
 lines = read_lines(filein)
 lines1 = read_lines(filein1,commentFlag=True)
 
 repls = get_replacements(lines1)
 apply_repls(lines,repls)
 write_changes(fileout,repls)
 
 
