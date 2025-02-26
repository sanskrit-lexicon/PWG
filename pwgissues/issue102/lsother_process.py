# coding=utf-8
""" lsother_process.py  
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 print(len(lines),"lines read from",filein)
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

class Replace:
 def __init__(self,line,lnum):
  self.line = line
  self.old,self.new = line.split('\t')
  self.lnum = lnum
  self.used = 0
  # check both old and new are <ls.*
  try:
   assert self.old.startswith('<ls')
   assert self.old.endswith('</ls>')
   #assert self.new.startswith('<ls')
   #assert self.new.endswith('</ls>')
  except:
   print('problem at line',lnum)
   
def init_replacements(filein):
 lines = read_lines(filein)
 recs = []
 for iline,line in enumerate(lines):
  rec = Replace(line,iline+1)
  recs.append(rec)
 return recs

def replacement_dict(recs):
 d = {}
 n = 0 # number of problematic duplicates
 for rec in recs:
  key = rec.old
  val = rec.new
  if key not in d:
   d[key] = rec
   continue
  # key is duplicate. Is value the same?
  rec1 = d[key]
  assert key == rec1.old
  val1 = rec1.new
  if val != val1:
   print('DUPLICATE PROBLEM')
   print('key = ',key)
   print('val = ',val)
   print('val1= ',val1)
   n = n + 1
 print(n,"problematic duplicates")
 if n != 0:
  print('EXITING.')
  exit(1)
 recs1 = []
 for key in d:
  rec = d[key]
  recs1.append(rec)
 return d,recs1

def check_recs_used(recs):
 ntot = 0
 notused = []
 for rec in recs:
  ntot = ntot + rec.used
  if rec.used == 0:
   notused.append(rec.line)
 print('ntot=%s, notused=%s' %(ntot,len(notused)))
 filename = 'lsother_process_notused.txt'
 write_lines(filename,notused)
 
def apply_one(line,dchange):
 # Our changes are of form <ls.*?</ls> -> something
 newline = line
 lsarr = re.findall(r'<ls.*?</ls>',line)
 for ls in lsarr:
  if ls in dchange:
   rec = dchange[ls]
   new = rec.new
   newline = newline.replace(ls,new)
   rec.used = rec.used + 1
 return newline

def apply_replacements(lines,dchange):
 newlines = []
 n = 0 # number of lines changed
 for line in lines:
  newline = apply_one(line,dchange)
  newlines.append(newline)
  if newline != line:
   n = n + 1
 print(n,'lines changed')
 return newlines
if __name__=="__main__":
 filein = sys.argv[1]  # xxx.txt
 filein1 = sys.argv[2] # lsother_all.txt
 fileout = sys.argv[3] # output file xxx.txt
 lines = read_lines(filein)
 recs = init_replacements(filein1)
 dchange,recs1 =  replacement_dict(recs)
 newlines = apply_replacements(lines,dchange)
 # write the new dictionary
 write_lines(fileout,newlines)
 # check recs1 for unused
 check_recs_used(recs1)
 
