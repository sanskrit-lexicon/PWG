#-*- coding:utf-8 -*-
"""change_abnormal.py
   generate change transactions for lines in entries which
   are considered abnormal.  The
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


class LSchange(object):
 def __init__(self,entry,iline,ls):
  self.entry = entry
  self.iline = iline
  self.ls = ls
  
def find_abnormals_hariv(lspfx,entries):
 replacements = (('.','[.]'), ('(','\('),  (')','\)'))
 tmp = lspfx
 for old,new in replacements:
  tmp = tmp.replace(old,new)
 #regexnorm = re.compile(r'^<ls>%s ([0-9]+), ( fg+[.])?</ls>$'%tmp)
 """
 regexdata = [
  [r'<ls>%s.*?</ls>'%tmp,
   [ (r'<ls>%s ([0-9]+), ([0-9]+[.]?)</ls>'%tmp , '1a'),
   (r'<ls>%s ([0-9]+), ([0-9]+[.]?) fgg?[.]</ls>' % tmp, '1b'),
   (r'<ls>%s ([0-9]+), ([0-9]+[.,]?) v[.] l[.]</ls>' % tmp, '1c'),
   (r'<ls>%s</ls>'%tmp , '1d'),
   (r'<ls>%s[^<]*ed[.] Bomb[.].*?</ls>'%tmp , '1e'),
   ]
  ],
  [r'<ls n="%s[^"]*">.*?</ls>'%tmp,
   [(r'<ls n="%s">([0-9]+), ([0-9]+[.]?)</ls>'%tmp , '2a'),
   (r'<ls n="%s">([0-9]+), ([0-9]+[.]?) fgg?[.]</ls>' % tmp, '2b'),
   (r'<ls n="%s">([0-9]+), ([0-9]+[.,]?) v[.] l[.]</ls>' % tmp, '2c'),
   (r'<ls n="%s ([0-9]+),">([0-9]+[.]?)</ls>'%tmp , '2d'),
   (r'<ls n="%s ([0-9]+),">([0-9]+[.]?) fgg?[.]</ls>' % tmp, '2e'),
   (r'<ls n="%s ([0-9]+),">([0-9]+[.,]?) v[.] l[.]</ls>' % tmp, '2f'),
 
   ]
  ]
 ]
 """
 regexdata = [
  [r'<ls>%s.*?</ls>'%tmp,
   [ (r'<ls>%s ([0-9]+[.]?)</ls>'%tmp , '1a'),
   (r'<ls>%s ([0-9]+[.]?) fgg?[.]</ls>' % tmp, '1b'),
   (r'<ls>%s ([0-9]+[.,]?) v[.] l[.]</ls>' % tmp, '1c'),
   (r'<ls>%s</ls>'%tmp , '1d'),
   (r'<ls>%s[^<]*ed[.] Bomb[.].*?</ls>'%tmp , '1e'),
   ]
  ],
  [r'<ls n="%s[^"]*">.*?</ls>'%tmp,
   [(r'<ls n="%s">([0-9]+[.]?)</ls>'%tmp , '2a'),
   (r'<ls n="%s">([0-9]+[.]?) fgg?[.]</ls>' % tmp, '2b'),
   (r'<ls n="%s">([0-9]+[.,]?) v[.] l[.]</ls>' % tmp, '2c'),
   #(r'<ls n="%s ([0-9]+),">([0-9]+[.]?)</ls>'%tmp , '2d'),
   #(r'<ls n="%s ([0-9]+),">([0-9]+[.]?) fgg?[.]</ls>' % tmp, '2e'),
   #(r'<ls n="%s ([0-9]+),">([0-9]+[.,]?) v[.] l[.]</ls>' % tmp, '2f'),
 
   ]
  ]
 ]
 abnormals = []
 normals = []
 for entry in entries:
  #text = '\n'.join(entry.datalines)
  for iline,line in enumerate(entry.datalines):
   abnormal = False
   for regex1,regexnorms in regexdata:
    lsarr = re.findall(regex1,line)
    #abnormal = 
    for ls in lsarr:
     normal = False
     for regex1a,regextype in regexnorms:
      if re.search(regex1a,ls):
       #normal = LSinstance(entry,ls,regextype)
       #normals.append(normal)
       normal = True
       break
     if normal == False:
      abnormal = True
      break # for ls in lsarr
    if abnormal:
     break # for regex1a
   #
   if abnormal:
    # generate change transaction for this line
    instance = LSchange(entry,iline,ls)
    abnormals.append(instance)
 print(len(abnormals),'abnormal lines found')
 return abnormals

def normals_summary(normals):
 d = {} 
 for lsinstance in normals:
  t = lsinstance.type
  if t not in d:
   d[t] = 0
  d[t] = d[t] + 1
 types = sorted(d.keys())
 tot = 0
 for t in types:
  print(d[t],"ls instances of type",t)
  tot = tot + d[t]
 print('totals=',tot)
 
def write_abnormals(fileout,abnormals):
 with codecs.open(fileout,"w","utf-8") as f:
  for x in abnormals:
   entry = x.entry
   iline = x.iline
   ls = x.ls # the abnormal ls
   lnum = entry.linenum1+iline+1
   metaline = re.sub(r'<k2>.*$','',entry.metaline)
   line = entry.datalines[iline]
   outarr = []
   outarr.append('; --------------------------------')
   outarr.append('; %s' % metaline)
   outarr.append('; Abnormal ls: %s' %ls)
   outarr.append('%s old %s' %(lnum,line))
   outarr.append(';')
   outarr.append('%s new %s' %(lnum,line))
   for out in outarr:
    f.write(out+'\n')
 print(len(abnormals),'change transactions',fileout)

if __name__=="__main__":
 lspfx = sys.argv[1]
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx)
 #filebib = sys.argv[2]  # pwbib_input.txt
 fileout = sys.argv[3] #
 entries = init_entries(filein)
 if lspfx == 'HARIV.':
  abnormals = find_abnormals_hariv(lspfx,entries)
  write_abnormals(fileout,abnormals)
 else:
  print('Not implemented for lspfx = %s' %lspfx)
