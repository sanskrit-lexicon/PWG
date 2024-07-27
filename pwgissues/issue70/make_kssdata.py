# coding=utf-8
""" make_kssdata.py
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
  self.line = line
  m = re.search(r'^([0-9]+) (.+)$',line)
  assert m != None

  self.epage = int(m.group(1))
  self.data = m.group(2)
  self.taranga = None
  self.shlokafirst = None
  self.shlokalast = None
  self.comment = None
  self.shlokamap = []
  if not re.search(r'^[1-9]',self.data):
   # a 'comment'
   self.comment = self.data
   return
  m = re.search(r'^([0-9]+),([0-9]+)-([0-9]+)$',self.data)
  if m !=None:
   self.taranga = m.group(1)
   self.shlokafirst = int(m.group(2))
   self.shlokalast = int(m.group(3))
   return                         
  print('Rec: Cannot parse line\n%s' % line)
  exit(1)

def init_recs(lines):
 recs = []
 for line in lines:
  rec = Rec(line)
  if rec.comment == None:
   recs.append(rec)
 return recs
    
def update_recs(recs,V):
 # construct rec.shlokamap
 # V=1 example
 # 40 2,79-83 -> {'2,79':'1040`, '2,80':'1040', ..., '2,83':'1040'}

 for irec,rec in enumerate(recs):
  if rec.comment != None:
   print('update_recs: unexpected comment',rec.line)
   exit(1)
  epage3 = '%03d' % rec.epage
  page = V + epage3  # 1026, for instance
  for s in range(rec.shlokafirst,rec.shlokalast + 1):
   a = "'%s,%s':'%s'" %(rec.taranga,s,page)
   rec.shlokamap.append(a)

def write_recs(fileout,recs,V):
 # make a javascript file
 outarr = []
 outarr.append('var kssdata%s={' %V)
 for rec in recs:
  for smap in rec.shlokamap:
   outarr.append('%s,' % smap)
 outarr.append('}')  # close the object
 write_lines(fileout,outarr,printFlag=True)
 
if __name__=="__main__":
 V = sys.argv[1] # 1 or 2
 filein = sys.argv[2]  # begin_map_Vb.txt
 fileout = sys.argv[3] # javascript
 lines = read_lines(filein)
 recs = init_recs(lines)
 print(len(recs),"records from",filein)
 update_recs(recs,V)
 write_recs(fileout,recs,V)
 
