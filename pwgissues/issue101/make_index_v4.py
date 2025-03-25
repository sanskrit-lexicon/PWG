# coding=utf-8
""" make_index_v4.py for sahityadarpana_mw
"""
from __future__ import print_function
import sys, re, codecs
import json

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 print(len(lines),"read from",filein)
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"lines written to",fileout)

def make_outlines1(lines):
 outlines = []
 for iline,line in enumerate(lines):
  parts = line.split('\t')
  if iline == 0:
   outline = '\t'.join(parts[:5])
   outlines.append(outline)
   continue
  ipage = parts[1]
  if not re.search(r'^[0-9]+$',ipage):
   continue
  pari = parts[2]
  if pari == 'x':
   continue
  if len(parts) == 3:
   parts.append('-')
   parts.append('-')
  if len(parts) != 5:
   print('error. line#%s\n%s' %(iline+1,line))
   parts.pop()
  outline = '\t'.join(parts[:5])
  outlines.append(outline)
  continue
 print(len(outlines),"lines returned from make_outlines1")
 return outlines

def make_outlines2(lines):
 outlines = []
 prev_tov = None
 for iline,line in enumerate(lines):
  if iline == 0:
   outlines.append(line)
   continue
  parts = line.split('\t')
  page,ipage,pari,fromv,tov = parts
  if fromv == '-':
   assert tov == '-'
   #fromv = prev_tov + 'x'
   #fromv = re.sub(r'xx$','x',fromv)
   fromv = prev_tov
   tov = fromv
   newparts = [page,pari,fromv,tov,ipage]
   newline = '\t'.join(newparts)
   prev_tov = tov
  else:
   newparts = [page,pari,fromv,tov,ipage]
   newline = '\t'.join(newparts)
   prev_tov = tov
  outlines.append(newline)
 return outlines

if __name__ == "__main__":
 filein=sys.argv[1]  # tab-delimited index file with kanda
 fileout = sys.argv[2]  # index file without kanda, and only kanda=2
 lines = read_lines(filein)
 outlines1 = make_outlines1(lines)
 #write_lines('temp.txt',outlines1)
 outlines2 = make_outlines2(outlines1)
 write_lines(fileout,outlines2)

