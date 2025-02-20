# coding=utf-8
""" change_page.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

if __name__=="__main__":
 filein = sys.argv[1]  # index file
 fileout = sys.argv[2] # output file
 lines = read_lines(filein)
 outarr = []
 for iline,line in enumerate(lines):
  if iline == 0:
   newline = line
  else:
   parts = line.split('\t')
   # page is 2nd value
   page = int(parts[1])
   newpage = str(page - 3)
   parts[1] = newpage
   newline = '\t'.join(parts)
  outarr.append(newline)
 write_lines(fileout,outarr)
 
 

