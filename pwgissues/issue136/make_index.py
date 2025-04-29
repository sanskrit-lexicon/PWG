# coding=utf-8
""" make_index.py for KĀTYĀYANA'S ŚRAUTASŪTRĀṆI
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
 # page, adhy, kand,fromv,tov,ipage,remarks
 # 0      1     2    3     4    5    6 
 outlines = []
 prev_tov = None
 for iline,line in enumerate(lines):
  parts = line.split('\t')
  lnum = iline + 1
  try:
   page, adhy, kand,fromv,tov,ipage,remarks = parts
  except:
   print('ERROR @ line# %s, # parts=%s' %(lnum,len(parts)))
   print(line)
   exit(1)
  if iline == 1: # first non-title record
   fromv = '0'
   tov = '0'
   newparts = [page, adhy, kand,fromv,tov,ipage]
   newline = '\t'.join(newparts)
   prev_tov = tov
  elif fromv == ' -':
   assert tov == ' --'
   fromv = prev_tov
   tov = fromv
   newparts = [page, adhy, kand,fromv,tov,ipage]
   newline = '\t'.join(newparts)
   prev_tov = tov
  elif ' (' in line:
   fromv = re.sub(r' .*$','',fromv)
   tov = re.sub(r' .*$','',tov)
   newparts = [page, adhy, kand,fromv,tov,ipage]
   newline = '\t'.join(newparts)
   prev_tov = tov
  else:
   newparts = [page, adhy, kand,fromv,tov,ipage]
   newline = '\t'.join(newparts)
   prev_tov = tov
  if adhy == ' -':
   print('dropping line # %s: %s' %(lnum,line))
  else:
   outlines.append(newline)
 return outlines

if __name__ == "__main__":
 filein=sys.argv[1]  # tab-delimited index file with kanda
 fileout = sys.argv[2]  # index file without kanda, and only kanda=2
 lines = read_lines(filein)
 outlines = make_outlines(lines)
 write_lines(fileout,outlines)

 
 
