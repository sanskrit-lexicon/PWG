# coding=utf-8
""" prep_index.py
"""
from __future__ import print_function
import sys, re, codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def get_outlines():
 outlines = []
 title = 'epage\ttantra\tfromv\ttov\tipage'
 outlines.append(title)
 for ipage in range(1,64+1):
  epage = ipage + 7
  tantra = 't'
  fromv = 'x'
  tov = 'y'
  line = f'{epage}\t{tantra}\t{fromv}\t{tov}\t{ipage}'
  outlines.append(line)
 return outlines

def write_lines(fileout,outlines):

 with codecs.open(fileout,"w","utf-8") as f:
  for out in outlines:
   f.write(out + '\n')
  
 print('data written to',fileout)

if __name__ == "__main__":
 fileout = sys.argv[1]
 outlines = get_outlines()
 write_lines(fileout,outlines)

 
 
