# coding=utf-8
""" make_index.py for ŚĀKUNTALA
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
 prev_tov = None
 for iline,line in enumerate(lines):
  parts = line.split('\t')
  page,adhy,fromv,tov,ipage = parts
  if fromv == '---':
   assert tov == '---'
   fromv = prev_tov + 'c'
   fromv = re.sub(r'cc$','c',fromv)
   tov = fromv
   newparts = [page,adhy,fromv,tov,ipage]
   newline = '\t'.join(newparts)
   prev_tov = tov
  else:
   newline = '\t'.join(parts)
   prev_tov = tov
  outlines.append(newline)
 return outlines

if __name__ == "__main__":
 filein=sys.argv[1]  # tab-delimited index file with kanda
 fileout = sys.argv[2]  # index file without kanda, and only kanda=2
 lines = read_lines(filein)
 outlines = make_outlines(lines)
 write_lines(fileout,outlines)

 
 
