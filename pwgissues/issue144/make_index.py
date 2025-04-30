# coding=utf-8
""" make_index.py for TAITTIRĪYA BRĀHMAṆA
"""
from __future__ import print_function
import sys, re, codecs
# import json

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
 # remove lines whose 4th parameter contains '-' or 'X'
 # drop the last (9th) parameter (remark)
 outlines = []
 prev_tov = None
 ndrop = 0
 for iline,line in enumerate(lines):
  parts = line.split('\t')
  assert len(parts) == 9
  #if parts[3] in ('---','X'):
  if "==" in line:
   # drop line
   ndrop = ndrop + 1
   print('drop line',line)
   continue
  lnum = iline + 1
  if lnum == 45:
   # correct error
   assert parts[0] == ''
   parts[0] = 'I'  # correction
  if lnum == 635:
   assert parts[5] == '1c'
   parts[5] = '1b'
   assert parts[6] == '1c'
   parts[6] = '1b'
  if lnum == 342:
   assert parts[3] == '3'
   parts[3] = '5'
  # correct ipage (parts[7])
  if lnum in range(263,480):
   ipagestr = parts[7]
   ipage = int(ipagestr)
   ipagenew = ipage + 40
   ipagestrnew = str(ipagenew)
   parts[7] = ipagestrnew
  # remove remark
  newparts = parts[0:8]
  newline = '\t'.join(newparts)
  outlines.append(newline)
 print(ndrop,"lines dropped")
 return outlines

if __name__ == "__main__":
 filein=sys.argv[1]  # tab-delimited index file 
 fileout = sys.argv[2]  # revised index file without
 lines = read_lines(filein)
 outlines = make_outlines(lines)
 write_lines(fileout,outlines)

 
