# coding=utf-8
""" make_manudata.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 print(len(lines),"read from",filein)
 return lines

def write_lines(fileout,outarr,printFlag=False):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 if printFlag:
  print(len(outarr),"lines written to",fileout)

class Rec:
 def __init__(self,line):
  self.status = False  # True for 'normal' line
  self.line = line
  parts = line.split('\t')  # tab-delimited, 4 fields
  assert len(parts) == 4
  if parts[0] in ['page','1','2']:
   # not a normal page. skip
   print('skip line with page=%s' % parts[0])
   return
  
  self.ipage = int(parts[0])
  self.adhyaya = int(parts[1]) # 1-12, section
  self.shlokafirst = int(parts[2]) # first shloka that begins on this page
  self.shlokalast = int(parts[3]) # last  shloka that begins on this page
  # computed
  # epage (pdf page number) a linear translation from ipage
  self.epage = self.ipage + 21
  self.status = True
  self.shlokamap = []

def init_recs(lines):
 recs = []
 for line in lines:
  rec = Rec(line)
  if rec.status == True:
   recs.append(rec)
 print(len(recs),"records  from AB index file")
 return recs
    
def update_recs(recs):
 # construct rec.shlokamap
 # 40 2,79-83 -> {'2,79':'1040`, '2,80':'1040', ..., '2,83':'1040'}

 for irec,rec in enumerate(recs):
  epage3 = '%03d' % rec.epage
  page = epage3
  for s in range(rec.shlokafirst,rec.shlokalast + 1):
   a = "'%s,%s':'%s'" %(rec.adhyaya,s,page)
   rec.shlokamap.append(a)

def write_recs(fileout,recs):
 # make a javascript file
 outarr = []
 outarr.append('var manudata={') # begin the JS object literal
 for rec in recs:
  for smap in rec.shlokamap:
   outarr.append('%s,' % smap)
 outarr.append('}')  # end the JS object literal
 write_lines(fileout,outarr,printFlag=True)
 
if __name__=="__main__":
 filein = sys.argv[1]  # Manu.Deslongchamps.index.txt
 fileout = sys.argv[2] # javascript
 lines = read_lines(filein)
 recs = init_recs(lines)
 print(len(recs),"records from",filein)
 update_recs(recs)
 write_recs(fileout,recs)
 
