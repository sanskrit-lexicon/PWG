# coding=utf-8
""" make_index.py for kumaras
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

def alter_missing(lines):
 # vol., page, sarga, from v., to v., ipage, remark(s)
 #  0     1      2*     3*       4*       5      6
 newlines = []
 prev = None
 for line in lines:
  parts = line.split('\t')
  assert len(parts) == 7
  if parts[2] != '---':
   newline = line
  else:
   assert parts[3] == '---'
   assert parts[4] == '---'
   newparts = []
   prevparts = prev.split('\t')
   for ipart,part in enumerate(parts):
    if ipart == 2:
     newpart = prevparts[ipart]
    elif ipart == 3:
     newpart = prevparts[4]
    elif ipart == 4:
     newpart = prevparts[4]
    else:
     newpart = part
    newparts.append(newpart)
   newline = '\t'.join(newparts)
  newlines.append(newline)
  prev = newline
 return newlines

def drop_remarks(lines):
 newlines = []
 for line in lines:
  parts = line.split('\t')
  assert len(parts) == 6
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
 # drop last 3 lines
 lines1a = lines1[:-3]
 outlines = [title] + lines1a
 # drop remarks field
 outlines1 = drop_remarks(outlines)
 write_lines(fileout,outlines1)

 
 
