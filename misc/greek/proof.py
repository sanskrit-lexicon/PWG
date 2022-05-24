#-*- coding:utf-8 -*-
"""proof.py
 
"""
from __future__ import print_function
import sys,re,codecs
import digentry  



def check_entries_L(Ldict,Ldictab):
 s = set(Ldict.keys())
 sab = set(Ldictab.keys())
 diff1 = s.difference(sab)
 print('in L not in Lab',diff1)
 diff2 = sab.difference(s)
 print('in Lab not in L',diff2)

def check_metaline(entries,entriesab):
 nprob = 0
 for ientry,entry in enumerate(entries):
  entryab = entriesab[ientry]
  if entry.metaline != entryab.metaline:
   lnum = entry.linenum1
   print('%s old %s' %(lnum,entry.metaline))
   print('%s new %s' %(lnum,entryab.metaline))
   print(';')
   nprob = nprob + 1
   continue
   # rest of code not needed
   keys = list(entry.metad.keys())
   keysab = list(entryab.metad.keys())
   assert keys == keysab
   diffvals = []
   for key in keys:
    val = entry.metad[key]
    valab = entryab.metad[key]
    if val != valab:
     diffvals.append('%s: %s != %s' %(key,val,valab))
   print(diffvals)
   #print('%s != %s' %(entry.metaline ,entryab.metaline))
   nprob = nprob + 1
 print('check_metaline finds %s differences' % nprob)

def get_langlines(entry,langname):
 a = []
 regex = r'<lang n="%s">.*?</lang>' % langname
 for iline,line in enumerate(entry.datalines):
  b = re.findall(regex,line)
  if b != []:
   a.append(iline)
 return a
 
def mark_ab(entries,entriesab):
 nprob = 0
 for ientry,entry in enumerate(entries):
  entryab = entriesab[ientry]
  assert entry.metaline == entryab.metaline
  langs = langelts(entry)
  langsab = langelts(entryab)
  entryab.keep = False
  if langs != langsab:
   entryab.keep = True
   entryab.langs = langs
   entryab.langsab = langsab
   nprob = nprob + 1
 print(nprob,'entries marked with lang differences')

def get_outlangs(entryab):
 a = []
 langs = entryab.langs
 langsab = entryab.langsab
 nlangs = len(langs)
 nlangsab = len(langsab)
 m = max(nlangs,nlangsab)
 a.append('; %s %s %s' %('  ','AB'.ljust(20),'CSL'.ljust(20)))
 for i in range(m):
  if i < nlangsab:
   langab = langsab[i]
  else:
   langab = '(NONE)'
  if i < nlangs:
   lang = langs[i]
  else:
   lang = '(NONE)'
  if langab == lang:
   status = 'EQ'
  else:
   status = '??'
  a.append('; %s %s %s' %(status,langab.ljust(20),lang.ljust(20)))
 return a

d = {}
def update_d(n):
 if n not in d:
  d[n] = 0
 d[n] = d[n] + 1

def display_d():
 keys = sorted(d.keys())
 for key in keys:
  print('%s -> %s' %(key,d[key]))

def unused_write_helper(entry,langlines,langname):
 dbg = False
 outarr = []
 outarr.append('; %s' % entry.metaline)
 nlanglines = len(langlines)
 lines = entry.datalines
 nlines = len(lines)
 update_d(nlanglines)
 outarr.append('; %s lines with greek text (%s total lines)' %(nlanglines,nlines))
 temp = ['%s' %(iline+1,) for iline in langlines]
 outarr.append('; langlines = %s' % ','.join(temp))
 
 showlines = [0 for iline in range(nlines)]
 for iline in langlines:
  showlines[iline] = 1
 if dbg:print('dbg 1: ',showlines)
 for iline in langlines:
  iline1 = iline - 1
  if (0 <= iline1) and (showlines[iline1] != 1):
   showlines[iline1] = 2
  iline1 = iline + 1
  if (iline1 < nlines) and (showlines[iline1] != 1):
   showlines[iline1] = 2
 if dbg:print('dbg 2: ',showlines)
 if dbg:exit(1)
 for iline in range(nlines):
  line = lines[iline]
  iline1 = iline + 1
  if showlines[iline] == 0:
   #outarr.append('%s: %s %s' %('SKIP',iline1,line))
   pass
  elif showlines[iline] == 1:
   outarr.append('%s: %s %s' %(langname,iline1,line))
  else:
   outarr.append('%s: %s %s' %('context',iline1,line))
 return outarr

def write_helper(entry,langlines,langname):
 dbg = False
 outarr = []
 outarr.append('='*72)
 outarr.append('; %s' % entry.metaline)
 nlanglines = len(langlines)
 lines = entry.datalines
 nlines = len(lines)
 update_d(nlanglines)
 #outarr.append('; %s lines with greek text (%s total lines)' %(nlanglines,nlines))
 #temp = ['%s' %(iline+1,) for iline in langlines]
 #outarr.append('; langlines = %s' % ','.join(temp))
 outarr.append('')
 for iline in langlines:
  # previous context line
  iline1 = iline - 1
  if (iline1 not in langlines) and (0<=iline1):
   lnum = iline1 + 1
   line = lines[iline1]
   outarr.append('%s %s %s' %('context'.ljust(10),lnum,line))
  # lang line
  iline1 = iline
  lnum = iline1 + 1
  line = lines[iline1]
  outarr.append('%s %s %s' %(langname.ljust(10),lnum,line))
  # next context line
  iline1 = iline + 1
  if (iline1 not in langlines) and (iline1<nlines):
   lnum = iline1 + 1
   line = lines[iline1]
   outarr.append('%s %s %s' %('context'.ljust(10),lnum,line))
  # extra blank line
  outarr.append(' ')
 return outarr


def write(entries,fileout,langname):
 nout = 0
 with codecs.open(fileout,"w","utf-8") as f:
  for entry in entries:
   langlines = get_langlines(entry,langname)
   if langlines == []:
    continue
   nout = nout + 1
   outarr = write_helper(entry,langlines,langname)
   for out in outarr:
    f.write(out+'\n')
 print(nout,"entries written to",fileout)
 display_d()
 
if __name__=="__main__":
 langname = sys.argv[1]
 filein = sys.argv[2] # bop csl-orig
 fileout = sys.argv[3] #  

 entries = digentry.init(filein)
 write(entries,fileout,langname)

 
