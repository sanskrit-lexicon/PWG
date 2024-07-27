# coding=utf-8
""" begin_mapa.py
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
  m = re.search(r'^([0-9]+),([0-9]+)$',self.data)
  if m == None:
   print('Rec: Cannot parse line\n%s' % line)
   exit(1)
  self.taranga = int(m.group(1))
  self.shlokafirst = int(m.group(2))

def init_recs(lines):
 recs = [Rec(line) for line in lines]
 # last line should be a comment
 assert recs[-1].comment != None
 return recs
    
def update_recs(recs):
 # fill in shlokalast
 for irec,rec in enumerate(recs[:-1]):
  if rec.comment != None:
   continue
  if rec.shlokalast != None:
   # already filled in
   continue
  # infer shlokalast as 1 less than shlokafirst of next rec
  rec1 = recs[irec+1] # next rec
  rec.shlokalast = rec1.shlokafirst - 1

def write_recs(fileout,recs):
 outarr = []
 for rec in recs:
  if rec.comment != None:
   out = rec.line # no change to these
  else:
   out = '%s %s,%s-%s' %(rec.epage,rec.taranga,rec.shlokafirst,rec.shlokalast)
  outarr.append(out)
 write_lines(fileout,outarr,printFlag=True)
 
if __name__=="__main__":
 filein = sys.argv[1]  # 
 fileout = sys.argv[2] # 
 lines = read_lines(filein)
 recs = init_recs(lines)
 print(len(recs),"records from",filein)
 update_recs(recs)
 write_recs(fileout,recs)
 
