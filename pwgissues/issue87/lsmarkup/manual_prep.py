# coding=utf-8
""" manual_prep.py 
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


def main_1(lines):
 outarr = []
 outarr.append(' d = {')
 for line in lines:
  outarr.append(" '%s' :" % line)
  outarr.append(" '%s'" % line)
  outarr.append(' ,')
 outarr.append(' }')
 return outarr

if __name__=="__main__":
 option = sys.argv[1]
 filein = sys.argv[2] 
 fileout = sys.argv[3]
 lines = read_lines(filein)
 if option == '1':
  outlines = main_1(lines)
 else:
  print('manual_prep.py ERROR option',option)
  exit(1)
 write_lines(fileout,outlines)
 
 
