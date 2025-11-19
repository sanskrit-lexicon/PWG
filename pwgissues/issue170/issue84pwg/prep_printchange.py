# coding=utf-8
""" prep_printchange.py  
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

def get_newlines(lines):
 ans = []
 for line in lines:
  # <L>840<pc>1-0063<k1>acCAvAka<k2>acCAvAka
  m = re.search(r'<L>([^<]*)<pc>([^<]*)<k1>([^<]*)<k2>',line)
  if m == None:
   ans.append(line)
  else:
   ans.append(line)
   L = m.group(1)
   k1 = m.group(3)
   out = f'pc: {L} : {k1} : old : new : '
   ans.append(out)
  pass
 return ans
if __name__=="__main__":
 filein = sys.argv[1]  # change file
 fileout = sys.argv[2] # 
 lines = read_lines(filein)
 newlines = get_newlines(lines)
 write_lines(fileout,newlines)
