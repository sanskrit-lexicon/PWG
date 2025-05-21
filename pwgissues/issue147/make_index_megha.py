# coding=utf-8
""" make_index_megha.py 
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

def drop_pages(lines,drops):
 newlines = []
 for line in lines:
  parts = line.split('\t')
  page = int(parts[1])
  if page in drops:
   pass
  else:
   newlines.append(line)
 return newlines

def drop_remarks(lines):
 newlines = []
 for line in lines:
  parts = line.split('\t')
  assert len(parts) == 5
  newparts = parts[:-1]  # drop last part, remark field
  newline = '\t'.join(newparts)
  newlines.append(newline)
 return newlines
 
if __name__ == "__main__":
 filein = sys.argv[1]  # index_orig
 fileout = sys.argv[2]  # index file
 lines = read_lines(filein)
 title = lines[0]
 # drop title lines
 lines1 = lines[1:]
 # drop first 2 lines and last line
 lines1a = lines1[2:-1]
 outlines = [title] + lines1a
 # drop remarks field
 outlines1 = drop_remarks(outlines)
 write_lines(fileout,outlines1)

 
 
