#-*- coding:utf-8 -*-
"""onegreekletter.py
 
"""
from __future__ import print_function
import sys,re,codecs
import digentry  

class Change(object):
 def __init__(self,metaline,lnum0,line0,lnum,line,newline):
  self.metaline = metaline
  self.lnum0 = lnum0
  self.line0 = line0
  self.lnum = lnum
  self.line = line
  self.newline = newline
  
def write_changes(fileout,changes):
 outrecs=[]
 prevmeta = None
 for change in changes:
  outarr=[]
  lnum0 = change.lnum0
  line0 = change.line0
  lnum = change.lnum
  line = change.line
  newline = change.newline
  metaline = change.metaline
  metaline = re.sub(r'<k2>.*$','',metaline)
  if prevmeta != metaline:
   outarr.append('; --------------------------------------------------')
   outarr.append('; %s' % metaline)
  else:
   outarr.append(';')
  prevmeta = metaline
  outarr.append('%s old %s' %(lnum0,line0))
  outarr.append('%s new %s' %(lnum0,line0))
  outarr.append(';')
  outarr.append('%s old %s' %(lnum,line))
  outarr.append('%s new %s' %(lnum,newline))
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
    for out in outarr:
     f.write(out+'\n')
 print(len(changes),"changes written to",fileout)

def make_changes(entries):
 changes = []
 singlegreek = '<lang n="greek">(.)</lang>'
 for ientry,entry in enumerate(entries):
  for iline,line in enumerate(entry.datalines):
   newline = re.sub(singlegreek,r'\1',line)
   if newline != line:
    # output previous line and this line
    iline0 = iline - 1
    line0 = entry.datalines[iline0]
    lnum0 = entry.linenum1 + iline0 + 1
    lnum = entry.linenum1 + iline + 1
    metaline = entry.metaline
    change = Change(metaline,lnum0,line0,lnum,line,newline)
    changes.append(change)
 return changes

if __name__=="__main__":
 filein = sys.argv[1] # pwg.txt
 fileout = sys.argv[2] #  

 entries = digentry.init(filein)
 digentry.Entry.Ldict = {}

 changes = make_changes(entries)
 write_changes(fileout,changes)

 
