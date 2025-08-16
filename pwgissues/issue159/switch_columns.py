# coding=utf-8
""" switch_columns.py
"""
from __future__ import print_function
import sys, re, codecs
import json


class Pagerec(object):
 """
""" 
 def __init__(self,line,iline):
  line = line.rstrip('\r\n')
  self.line = line
  self.iline = iline
  self.parts = re.split('\t',line)
  self.newparts = []

 
def init_pagerecs(filein):
 """ filein is a tsv file
 """
 recs = []
 with codecs.open(filein,"r","utf-8") as f:
  for iline,line in enumerate(f):
   pagerec = Pagerec(line,iline)
   recs.append(pagerec)
 print(len(recs),'Success: Page records read from',filein)
 return recs

def newparts(recs):
 for rec in recs:
  rec.newparts = [part for part in rec.parts]
  # interchange 2 and 3
  rec.newparts[2] = rec.parts[3]
  rec.newparts[3] = rec.parts[2]
  
def write_recs(fileout,recs):
 with codecs.open(fileout,"w","utf-8") as f:
  for rec in recs:
   out = '\t'.join(rec.newparts)
   f.write(out + '\n')
  
 print(len(recs),'lines writting to',fileout)

if __name__ == "__main__":
 filein=sys.argv[1]  # tab-delimited index file
 fileout = sys.argv[2]
 pagerecs = init_pagerecs(filein)
 newparts(pagerecs)
 write_recs(fileout,pagerecs)

 
 
