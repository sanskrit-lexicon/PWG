#-*- coding:utf-8 -*-
"""make_change3_abnormal.py
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

def make_number_change(lsold,lsabbr,n1,n2):
 # 1)
 m = re.search(r'^<ls>([0-9]+,) ([0-9]+,) ([0-9]+[.]?)</ls>$',lsold)
 if m:
  a1 = m.group(1)
  a2 = m.group(2)
  a3 = m.group(3)
  lsnew = '<ls n="%s">%s %s %s</ls>' %(lsabbr,a1,a2,a3)
  return lsnew
 # 2)
 m = re.search(r'^<ls>([0-9]+,) ([0-9]+,) ([0-9]+[.]) ((fgg?\.)|(v\. l\.))</ls>$',lsold)
 if m:
  a1 = m.group(1)
  a2 = m.group(2)
  a3 = m.group(3)
  a4 = m.group(4)
  lsnew = '<ls n="%s">%s %s %s %s</ls>' %(lsabbr,a1,a2,a3,a4)
  return lsnew
 # 3)
 m = re.search(r'^<ls>([0-9]+,) ([0-9]+[.]?)</ls>$',lsold)
 if m:
  a1 = n1 
  a2 = m.group(1)
  a3 = m.group(2)
  lsnew = '<ls n="%s %s,">%s %s</ls>' %(lsabbr,a1,a2,a3)
  return lsnew
 # 3a)
 m = re.search(r'^<ls>([0-9]+[.]?)</ls>$',lsold)
 if m:
  a1 = n1
  a2 = n2
  assert (n1 != None) and (n2 != None)
  a3 = m.group(1)
  lsnew = '<ls n="%s %s, %s,">%s</ls>' %(lsabbr,a1,a2,a3)
  return lsnew
 # 4)
 m = re.search(r'^<ls>([0-9]+,) ([0-9]+[.]) ((fgg?\.)|(v\. l\.))</ls>$',lsold)
 if m:
  a1 = n1
  a2 = m.group(1)
  a3 = m.group(2)
  a4 = m.group(3)
  lsnew = '<ls n="%s n=%s,">%s %s %s</ls>' %(lsabbr,a1,a2,a3,a4)
  return lsnew
 # 5)
 m = re.search(r'^<ls>([0-9]+,) ([0-9]+,) ([0-9]+[.]) ([0-9].*$)',lsold)
 if m:
  a1 = m.group(1)
  a2 = m.group(2)
  a3 = m.group(3)
  a4 = m.group(4)
  lsnew = '<ls n="%s">%s %s %s</ls> <ls>%s' %(lsabbr,a1,a2,a3,a4)
  return lsnew
 # 6)
 m = re.search(r'^<ls>([0-9]+,) ([0-9]+[.]) ([0-9].*$)',lsold)
 if m:
  a1 = n1
  assert n1 != None
  a2 = m.group(1)
  a3 = m.group(2)
  a4 = m.group(3)
  lsnew = '<ls n="%s %s,">%s %s</ls> <ls>%s' %(lsabbr,a1,a2,a3,a4)
  return lsnew
 # 7)
 m = re.search(r'^<ls>([0-9]+[.]) ([0-9].*$)',lsold)
 if m:
  a1 = n1
  a2 = n2
  assert (n1 != None) and (n2 != None)
  a3 = m.group(1)
  a4 = m.group(2)
  lsnew = '<ls n="%s %s, %s,">%s</ls> <ls>%s' %(lsabbr,a1,a2,a3,a4)
  return lsnew
 return None

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
  
def generate_changes(entries,lsabbr):
 # works for LS whose citations take 3 parameters
 regex = r'<ls>(%s) ([0-9]+), ([0-9]+), ([0-9]+)[.]([^<]*)</ls>' %lsabbr
 def fnew3(m):
  lsold = m.group(0)
  lsab = m.group(1)
  n1 = m.group(2)
  n2 = m.group(3)
  n3 = m.group(4)
  rest = m.group(5)
  if rest == '':
   return lsold # no change
  m1 = re.search(r'^ [0-9]',rest)
  if m1 == None:
   # abnormal. cannot handle
   return lsold
  rest1 = rest[1:]
  lsnew = '<ls>%s %s, %s, %s.</ls> <ls>%s</ls>' %(lsab,n1,n2,n3,rest1)
  return lsnew
 
 changes = []
 for entry in entries:
  metaline = entry.metaline
  for iline,line in enumerate(entry.datalines):
   lnum = entry.linenum1+iline+1
   newline = re.sub(regex,fnew3,line)
   if newline != line:
    changes.append(Change(metaline,lnum,line,newline))
 print(len(changes),'lines changed')
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
 lsabbr = sys.argv[1]
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx
 fileout = sys.argv[3] # change_X
 filedbg = 'tempdbg.txt'
 fdbg = codecs.open(filedbg,"w","utf-8")
 entries = init_entries(filein)
 changes = generate_changes(entries,lsabbr)
 write_changes(fileout,changes)
