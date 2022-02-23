#-*- coding:utf-8 -*-
"""listls3_abnormal.py
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

class LSinstance(object):
 def __init__(self,entry,ls,iline,lstype=None):
  self.entry = entry
  self.ls = ls
  self.iline = iline
  self.type = lstype  # type of 

def regexdata_extra1(ls,tmp):
 if (ls == "MBH."):
  return [(r'<ls>%s[^<]*ed[.] Bomb[.].*?</ls>'%tmp , '1xa')]
 if (ls == 'ṚV.'):
  return [
   ('<ls>ṚV. ANUKRAMAṆIKĀ\.?</ls>','<ls>ṚV. ANUKRAMAṆIKĀ.</ls>'),
   ('<ls>ṚV. ANUKR\.</ls>','<ls>ṚV. ANUKR.</ls>'),
   ('<ls>ṚV. PRĀT\.</ls>','<ls>ṚV. PRĀT\.</ls>'),
   ('<ls>ṚV. PRĀT\. ([0-9]+), ([0-9]+[.]?)</ls>','<ls>ṚV. PRĀT\. #, #.</ls>'),
   ('<ls>ṚV. PRĀTIŚ\.</ls>','<ls>ṚV. PRĀTIŚ.</ls>'),
   ('<ls>ṚV. PRĀTIŚ\. ([0-9]+), ([0-9]+[.]?)</ls>','<ls>ṚV. PRĀTIŚ. #, #.</ls>'),
  ]
 return []

def regexdata_extra2(ls,tmp):
 if (ls == 'ṚV.'):
  return [
   ('<ls n="ṚV. PRĀT.">([0-9]+), ([0-9]+[.]?)</ls>',
    '<ls n="ṚV. PRĀT.">#, #.</ls>'),
   ('<ls n="ṚV. PRĀT. ([0-9]+),">([0-9]+[.]?)</ls>',
    '<ls n="ṚV. PRĀT. #, ">#.</ls>'),
   ('<ls n="ṚV. PRĀTIŚ.">([0-9]+), ([0-9]+[.]?)</ls>',
    '<ls n="ṚV. PRĀTIŚ.">#, #.</ls>'),
   ('<ls n="ṚV. PRĀTIŚ. ([0-9]+),">([0-9]+[.]?)</ls>',
    '<ls n="ṚV. PRĀTIŚ. #, ">#.</ls>'),
   ]
 return []

def get_regexdata(lspfx):
 replacements = (('.','[.]'), ('(','\('),  (')','\)'))
 tmp = lspfx
 for old,new in replacements:
  tmp = tmp.replace(old,new)
 regexdata = [
  [r'<ls>%s.*?</ls>'%tmp,
   [(r'<ls>%s ([0-9]+), ([0-9]+), ([0-9]+[.]?)</ls>'%tmp , 
     '<ls>%s #, #, #.</ls>' % tmp),
   (r'<ls>%s ([0-9]+), ([0-9]+), ([0-9]+[.]?) fgg?[.]</ls>' % tmp,
     '<ls>%s #, #, #. fgg.</ls>' % tmp),
   (r'<ls>%s ([0-9]+), ([0-9]+), ([0-9]+[.,]?) v[.] l[.]</ls>' % tmp,
     '<ls>%s #, #, #. v. l.</ls>' % tmp),
   (r'<ls>%s</ls>'%tmp ,
    '<ls>%s</ls>' % tmp),
   ] + regexdata_extra1(lspfx,tmp)
  ],
  [r'<ls n="%s[^"]*">.*?</ls>'%tmp,
   [(r'<ls n="%s">([0-9]+), ([0-9]+), ([0-9]+[.]?)</ls>'%tmp ,
     '<ls n="%s">#, #, #.</ls>' % tmp),

   (r'<ls n="%s">([0-9]+), ([0-9]+), ([0-9]+[.]?) fgg?[.]</ls>' % tmp,
     '<ls n="%s">#, #, #. fgg.</ls>' % tmp),
    
   (r'<ls n="%s">([0-9]+), ([0-9]+), ([0-9]+[.,]?) v[.] l[.]</ls>' % tmp,
     '<ls n="%s">#, #, #. v. l.</ls>' % tmp),

   (r'<ls n="%s ([0-9]+),">([0-9]+), ([0-9]+[.]?)</ls>'%tmp ,
     '<ls n="%s #,">#, #.</ls>' % tmp),

   (r'<ls n="%s ([0-9]+),">([0-9]+), ([0-9]+[.]?) fgg?[.]</ls>' % tmp,
     '<ls n="%s #,">#, #. fgg.</ls>' % tmp),

   (r'<ls n="%s ([0-9]+),">([0-9]+), ([0-9]+[.,]?) v[.] l[.]</ls>' % tmp,
     '<ls n="%s #,">#, #. v. l.</ls>' % tmp),

   (r'<ls n="%s ([0-9]+), ([0-9]+),">([0-9]+[.]?)</ls>'%tmp ,
     '<ls n="%s #, #,">#.</ls>' % tmp),

   (r'<ls n="%s ([0-9]+), ([0-9]+),">([0-9]+[.]?) fgg?[.]</ls>' % tmp,
     '<ls n="%s #, #,">#. fgg.</ls>' % tmp),

   (r'<ls n="%s ([0-9]+), ([0-9]+),">([0-9]+[.,]?) v[.] l[.]</ls>' % tmp,
     '<ls n="%s #, #,">#. v. l.</ls>' % tmp),

 
   ] + regexdata_extra2(lspfx,tmp)
  ]
 ]
 return regexdata

def find_abnormals3(lspfx,entries):
 regexdata = get_regexdata(lspfx)
 if False:
  regexnorms = regexdata[1][1]
  for regex1a,regextype in regexnorms:
   print('%s      %s' %(regextype,regex1a))
 abnormals = []
 normals = []
 for entry in entries:
  #text = '\n'.join(entry.datalines)
  for iline,line in enumerate(entry.datalines):
   text = line
   for regex1,regexnorms in regexdata:
    lsarr = re.findall(regex1,text,flags=re.DOTALL)
    for ls in lsarr:
     normal = None
     for regex1a,regextype in regexnorms:
      if re.search(regex1a,ls):
       normal = LSinstance(entry,ls,iline,regextype)
       normals.append(normal)
       break
     if normal == None:
      abnormal = LSinstance(entry,ls,iline)
      abnormals.append(abnormal)
 return abnormals,normals

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
  print('%6d' %d[t],t)
  tot = tot + d[t]
 print('totals=',tot)
 
def write_abnormals(fileout,abnormals):
 with codecs.open(fileout,"w","utf-8") as f:
  for x in abnormals:
   entry = x.entry
   ls = x.ls
   L = entry.metad['L']
   k1 = entry.metad['k1']
   out = '%s %s %s' %(ls,k1,L)
   f.write(out+'\n')
 print(len(abnormals),'abnormal ls written to',fileout)

def skip_abnormals(abnormals):
 regexes = [
    '<ls>ṚV\. [0-9]+, [0-9]+\.?</ls>',
    '<ls n="ṚV\.">[0-9]+, [0-9]+\.?</ls>',
    '<ls n="ṚV\. [0-9]+,">[0-9]+\.?</ls>',
 ]
 ans = [] # abnormals that are not skipped
 for x in abnormals:
  ls = x.ls # the abnormal ls
  skip = False
  for regex in regexes:
   if re.search(regex,ls):
    skip = True
    break
  if not skip:
   ans.append(x)
 return ans
 
def write_abnormals_change(fileout,abnormals):
 dbg = False
 if dbg:
  abnormals = skip_abnormals(abnormals)
 
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
 fileout = sys.argv[3] #
 fileoutchg = sys.argv[4]
 entries = init_entries(filein)
 abnormals,normals = find_abnormals3(lspfx,entries)
 write_abnormals(fileout,abnormals)
 write_abnormals_change(fileoutchg,abnormals)
 normals_summary(normals)
 
