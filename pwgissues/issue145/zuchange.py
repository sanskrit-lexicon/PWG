# coding=utf-8
""" zu at end of line
"""
from __future__ import print_function
import sys, re,codecs
import digentry1
from make_js_index import *

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

def outrec_entry(entry):
 outarr = []
 outarr.append(entry.metaline)
 for line in entry.datalines:
  outarr.append(line)
 outarr.append(entry.lend)
 return outarr

def outrec_nonentry(nonentry):
 outarr = []
 outarr.append(nonentry.line)
 return outarr

def write_recs(fileout,recs):
 with codecs.open(fileout,"w","utf-8") as f:
  for rec in recs:
   if type(rec) == digentry1.Entry:
    outlines = outrec_entry(rec)
   elif type(rec) == digentry1.nonEntry:
    outlines = outrec_nonentry(rec)
   for out in outlines:
    f.write(out+'\n')
 print('write_recs output to',fileout)

def adjust1(recs):
 # remove space at end of lines of Entry records
 nchg = 0
 for rec in recs:
  if type(rec) == digentry1.nonEntry:
   # no change
   continue
  assert type(rec) == digentry1.Entry
  entry = rec
  newlines = []
  for line in entry.datalines:
   newline = re.sub(r' +$','',line)
   if newline != line:
    nchg = nchg + 1
   newlines.append(newline)
  entry.datalines = newlines
 print('adjust1 change to %s lines' % nchg)

def adjust1a(recs):
 # remove spaces at start of lines in entries
 nchg = 0
 for rec in recs:
  if type(rec) == digentry1.nonEntry:
   # no change
   continue
  assert type(rec) == digentry1.Entry
  entry = rec
  newlines = []
  for line in entry.datalines:
   newline = re.sub(r'^ +','',line)
   if newline != line:
    nchg = nchg + 1
   newlines.append(newline)
  entry.datalines = newlines
 print('adjust1a change to %s lines' % nchg)

def adjust2(recs):
 # " zu\n<ls>X</ls>Y" -> "zu<ls>X</ls>\nY"  Note Y could be empty
 nchg = 0
 nempty = 0
 for rec in recs:
  if type(rec) == digentry1.nonEntry:
   # no change
   continue
  assert type(rec) == digentry1.Entry
  entry = rec
  oldlines = entry.datalines
  txtold = '\n'.join(oldlines)
  txtnew = re.sub(r' zu\n(<ls.*?</ls>) *',r' zu \1\n',txtold,re.DOTALL)
  if txtold == txtnew:
   # no change
   continue
  newlines = txtnew.split('\n')
  # update nchg
  assert len(oldlines) == len(newlines)
  for iline,newline in enumerate(newlines):
   line = oldlines[iline]
   if newline != line:
    nchg = nchg + 1
  entry.datalines = newlines
 print('adjust2 change to %s lines' % nchg)

def adjust3(recs):
 # " zu\n[Page..]<ls>X</ls>Y" -> "zu<ls>X</ls>\nY"  Note Y could be empty
 nchg = 0
 nempty = 0
 for rec in recs:
  if type(rec) == digentry1.nonEntry:
   # no change
   continue
  assert type(rec) == digentry1.Entry
  entry = rec
  oldlines = entry.datalines
  txtold = '\n'.join(oldlines)
  txtnew = re.sub(r' zu\n(\[Page.*?\])\n(<ls.*?</ls>) *',
                  r' zu \2\n\1\n',txtold,re.DOTALL)
  if txtold == txtnew:
   # no change
   continue
  newlines = txtnew.split('\n')
  # update nchg
  assert len(oldlines) == len(newlines)
  for iline,newline in enumerate(newlines):
   line = oldlines[iline]
   if newline != line:
    nchg = nchg + 1
  entry.datalines = newlines
 print('adjust3 change to %s lines' % nchg)

if __name__=="__main__":
 filein = sys.argv[1]  # xxx.txt
 fileout = sys.argv[2] # output file  adjusted xxx
 recs = digentry1.init(filein)
 adjust1(recs)  # remove spaces at end
 adjust1a(recs) # remove spaces at beginning
 adjust2(recs)  # merge zu\n<ls>X</ls.
 adjust3(recs)  # with [Page..]
 write_recs(fileout,recs)


