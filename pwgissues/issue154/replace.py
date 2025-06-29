# coding=utf-8
""" replace.py
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
   ans.append(repl)
 print(len(ans),"replacements found")
 print(ndup,"duplicates noticed")
 return ans

def mark_strings(lines,strings):
 newlines = []
 markc = '@'  # this character
 print('marking strings with "%s"' % markc)
 n = 0 # number of lines with at least one string marked
 for line in lines:
  newline = line
  for s in strings:
   if s in newline:
    # '@' does not occur in
    newline = newline.replace(s,markc+s)
  newlines.append(newline)
  if newline != line:
   n = n + 1
 print(n,'lines marked')
 return newlines


class unused_Change:
 def __init__(self,string):
  self.old = string
  self.new = None
  self.method = None
  make_change(self)

def write_changes(fileout,changes):
 outarr = []
 # sort output by method
 changes1 = sorted(changes, key = lambda x: str(x.method) + str(x.old))
 n = 0 # number not changed
 for change in changes1:
  new = change.new
  if new == None:
   new = '?'
   n = n + 1
  method = change.method
  out = '%s\t%s\tmethod=%s' %(change.old,change.new,change.method)
  outarr.append(out)
 write_lines(fileout,outarr)
 print(n,"changes not yet done")

def apply_repls(lines,repls):
 newlines = []
 nchg = 0 # number of lines changed
 for line in lines:
  newline = line
  for repl in repls:
   old,new = repl
   newline = newline.replace(old,new)
  newlines.append(newline)
  if newline != line:
   nchg = nchg + 1
 print('apply_repls: %s lines changed' % nchg)
 return newlines

if __name__=="__main__":
 filein = sys.argv[1]  # kosha
 filein1 = sys.argv[2] # line string replacements
 fileout = sys.argv[3] # revised kosha
 lines = read_lines(filein)
 lines1 = read_lines(filein1,commentFlag=True)
 
 repls = get_replacements(lines1)
 newlines = apply_repls(lines,repls)
 write_lines(fileout,newlines)
 
