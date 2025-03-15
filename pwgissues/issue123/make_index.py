# coding=utf-8
""" make_index.py for Hemacandra.Anekarthasangraha.1807.pdf
"""
from __future__ import print_function
import sys, re, codecs
import json

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

def make_outlines(lines):
 outlines = []
 for iline,line in enumerate(lines):
  parts = line.split('\t')
  kanda = parts.pop(1)  # alters parts
  newline = '\t'.join(parts)
  if iline == 0:
   outlines.append(newline)
  elif kanda == '2':
   outlines.append(newline)
  else:
   pass  # skip kanda != 2
 return outlines

if __name__ == "__main__":
 filein=sys.argv[1]  # tab-delimited index file with kanda
 fileout = sys.argv[2]  # index file without kanda, and only kanda=2
 lines = read_lines(filein)
 outlines = make_outlines(lines)
 write_lines(fileout,outlines)

 
 
