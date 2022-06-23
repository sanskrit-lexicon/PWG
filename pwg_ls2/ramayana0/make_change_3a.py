#-*- coding:utf-8 -*-
"""make_change3a.py  
"""
from __future__ import print_function
import sys, re,codecs
from parseheadline import parseheadline

class Entry(object):
 Ldict = {}
 def __init__(self,lines,linenum1,linenum2):
  # linenum1,2 are int
  self.metaline = lines[0]
  self.lend = lines[-1]  # the <LEND> line
  self.datalines = lines[1:-1]  # the non-meta lines
  # parse the meta line into a dictionary
  #self.meta = Hwmeta(self.metaline)
  self.metad = parseheadline(self.metaline)
  self.linenum1 = linenum1
  self.linenum2 = linenum2
  #L = self.meta.L
  L = self.metad['L']
  if L in self.Ldict:
   print("Entry init error: duplicate L",L,linenum1)
   exit(1)
  self.Ldict[L] = self
  self.lsarr = []
  
def init_entries(filein):
 # slurp lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [line.rstrip('\r\n') for line in f]
 recs=[]  # list of Entry objects
 inentry = False  
 idx1 = None
 idx2 = None
 for idx,line in enumerate(lines):
  if inentry:
   if line.startswith('<LEND>'):
    idx2 = idx
    entrylines = lines[idx1:idx2+1]
    linenum1 = idx1 + 1
    linenum2 = idx2 + 1
    entry = Entry(entrylines,linenum1,linenum2)
    recs.append(entry)
    # prepare for next entry
    idx1 = None
    idx2 = None
    inentry = False
   elif line.startswith('<L>'):  # error
    print('init_entries Error 1. Not expecting <L>')
    print("line # ",idx+1)
    print(line.encode('utf-8'))
    exit(1)
   else: 
    # keep looking for <LEND>
    continue
  else:
   # inentry = False. Looking for '<L>'
   if line.startswith('<L>'):
    idx1 = idx
    inentry = True
   elif line.startswith('<LEND>'): # error
    print('init_entries Error 2. Not expecting <LEND>')
    print("line # ",idx+1)
    print(line.encode('utf-8'))
    exit(1)
   else: 
    # keep looking for <L>
    continue
 # when all lines are read, we should have inentry = False
 if inentry:
  print('init_entries Error 3. Last entry not closed')
  print('Open entry starts at line',idx1+1)
  exit(1)

 print(len(lines),"lines read from",filein)
 print(len(recs),"entries found")
 return recs

class Change(object):
 def __init__(self,metaline,lnum,old,new):
  self.metaline = metaline
  self.lnum = lnum
  self.old = old
  self.new = new


def write_debug(lnum,metaline,prevls,lsold,line):
 # generate message to fdbg output
 metaline1 = re.sub(r'<k2>.*$','',metaline)
 #metaline1 = '%s   %s' %(prevls,metaline1)
 outarr = []
 outarr.append('; ---------------------------')
 outarr.append('; %s' %metaline1)
 outarr.append('; prev = %s' % prevls)
 outarr.append('; todo = %s' % lsold)
 outarr.append('%s old %s' %(lnum,line))
 outarr.append(';')
 outarr.append('%s new %s' %(lnum,line))
 for out in outarr:
  fdbg.write(out+'\n')

regexesold = {}
regexesnew = {}
# option = 1
regexoldraw = r'<ls>R\. ([12]), ([0-9]+), ([0-9]+) \(([0-9]+), ([0-9]+) GORR\.\)\.</ls>'
regexesold['1'] = re.compile(regexoldraw)
regexesnew['1'] = r'<ls>R. \1, \2, \3</ls> (<ls n="GORR. \1,">\4, \5</ls> <ls>GORR.</ls>).'

# option = 1a
regexoldraw = r'<ls>R\. ([12]), ([0-9]+), ([0-9]+) \(([0-9]+), ([0-9]+) GORR\.\)</ls>'
regexesold['1a'] = re.compile(regexoldraw)
regexesnew['1a'] = r'<ls>R. \1, \2, \3</ls> (<ls n="GORR. \1,">\4, \5</ls> <ls>GORR.</ls>)'

# option = 2
regexoldraw = r'<ls>R\. ([12]), ([0-9]+), ([0-9]+) \(([0-9]+) GORR\.\)\.</ls>'
regexesold['2'] = re.compile(regexoldraw)
regexesnew['2'] = r'<ls>R. \1, \2, \3</ls> (<ls n="GORR. \1, \2,">\4</ls> <ls>GORR.</ls>).'

# option = 2a  no period after GORR.)
regexoldraw = r'<ls>R\. ([12]), ([0-9]+), ([0-9]+) \(([0-9]+) GORR\.\)</ls>'
regexesold['2a'] = re.compile(regexoldraw)
regexesnew['2a'] = r'<ls>R. \1, \2, \3</ls> (<ls n="GORR. \1, \2,">\4</ls> <ls>GORR.</ls>)'

# option = 2b  
regexoldraw = r'<ls n="R\. ([12]),">([0-9]+), ([0-9]+) \(([0-9]+) GORR\.\)\.</ls>'
regexesold['2b'] = re.compile(regexoldraw)
regexesnew['2b'] = r'<ls n="R. \1,">\2, \3</ls> (<ls n="GORR. \1, \2,">\4</ls> <ls>GORR.</ls>).'

# option = 3
regexoldraw = r'<ls>R\. ([12]), ([0-9]+), ([0-9]+) \(([0-9]+), ([0-9]+) GORR\.\)\. ([0-9].*?)</ls>'
regexesold['3'] = re.compile(regexoldraw)
regexesnew['3'] = r'<ls>R. \1, \2, \3</ls> (<ls n="GORR. \1,">\4, \5</ls> <ls>GORR.</ls>). <ls n="R.">\6</ls>'

# option = 4
regexoldraw = r'<ls>R\. ([1-7])\.'  # correct error
regexesold['4'] = re.compile(regexoldraw)
regexesnew['4'] = r'<ls>R. \1,'

def generate_changes(entries,option):
 regexold = regexesold[option]
 regexnew = regexesnew[option]
 changes = []
 for entry in entries:
  metaline = entry.metaline
  prevlsname = None
  n1 = None
  n2 = None
  prevls = None
  for iline,line in enumerate(entry.datalines):
   newline = re.sub(regexold,regexnew,line)
   if newline == line:
    continue
   lnum = entry.linenum1+iline+1
   change = Change(metaline,lnum,line,newline)
   changes.append(change)
 print(len(changes),'changes constructed')
 return changes
def write_changes(fileout,changes):
 outrecs = []
 for change in changes:
  outarr = []
  outarr.append('; -------------------------------------')
  outarr.append('; ' + change.metaline)
  outarr.append('%s old %s' %(change.lnum,change.old))
  outarr.append('; ')
  outarr.append('%s new %s' %(change.lnum,change.new))
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(outrecs),"records written to",fileout)

if __name__=="__main__":
 option = sys.argv[1]
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx
 fileout = sys.argv[3] # change_X
 filedbg = 'tempdbg.txt'
 fdbg = codecs.open(filedbg,"w","utf-8")
 entries = init_entries(filein)
 changes = generate_changes(entries,option)
 write_changes(fileout,changes)
