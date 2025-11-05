# coding=utf-8
""" chkidx.py  adapted for taittiryas 
"""
from __future__ import print_function
import sys, re, codecs
#import json

def roman_to_int(roman):
 droman_int = {'I':1, 'II':2, 'III':3, 'IV':4,
                'V':5, 'VI':6, 'VII':7, 'VIII':8, 'IX':9,
                'X':10, 'XI':11, 'XII':12,'':0}
 if roman in droman_int:
  return droman_int[roman]
 else:
  # error condition
  return None

def read_lines(filein,commentFlag=False):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines1 = [x.rstrip('\r\n') for x in f]
 if commentFlag:
  # remove 'comments' - lines start with ';'
  lines = [x for x in lines1 if not x.startswith(';')]
  print(len(lines),"kept.")
  print(len(lines1),'lines read from',filein)
 else:
  lines = lines1
  print(len(lines1),'lines read from',filein)
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"lines written to",fileout)

class Pagerec:
 def __init__(self,line):
  parts = line.split('\t')
  # force each part to be an int field.
  fields = []
  # first field is volume
  vol = parts[0]
  ivol = roman_to_int(vol)
  assert type(ivol) == int
  assert 1<=ivol<=9 # 1 digit
  page = parts[1]
  ipage = int(page)
  vp = '%d%03d' %(ivol,ipage)
  ivp = int(vp)
  kanda = parts[2]
  ikanda = roman_to_int(kanda)
  parts1 = parts[1:]  # remove vol field
  parts1[0] = str(ivp)
  parts1[1] = str(ikanda)
  for part in parts1:
   # remove non-digits
   digits = re.sub(r'[^0-9]','',part)
   if digits == '': # no digits!
    field = -1
   else:
    field = int(digits)
   fields.append(field)
  self.fields = fields
  
  
def init_pagerecs(filein):
 """ filein is a tsv file, with first line as fieldnames
 """
 lines = read_lines(filein)
 recs = []
 for iline,line in enumerate(lines):
  if iline == 0:
   continue # skip first line
  else:
   rec = Pagerec(line)
   recs.append(rec)
 return recs

class Instance:
 def __init__(self,line):
  self.line = line
  parts = line.split('\t')
  self.lnum = int(parts[0])
  self.k1 = parts[1]
  self.matchstr = parts[2]
  parm_str = parts[3]
  parmarr = parm_str.split(',')
  self.parms = [int(p) for p in parmarr]
  self.ipage = None
  
def init_instances(filein):
 lines = read_lines(filein)
 recs = [Instance(line) for line in lines]
 return recs

def write_recs(fileout,data):
 with codecs.open(fileout,"w","utf-8") as f:
  f.write('indexdata = \n')
  jsonstring = json.dumps(data,indent=1)
  f.write( jsonstring +  '\n')
  f.write('; // end of indexdata\n')
  
 print('json data written to',fileout)

def check_index(instance,pagerecs):
 """
 example instace.parms is 3,2,7  
 Matching fields from a pagerec
  210  # page
    3  # first field  
    2  # second field
    5  # fromvalue for last field
    9  # tovalue for last field
  215  # ipage
  at least 3 + 3  fields expected
 This 
 """
 parms = instance.parms
 nparms = len(parms)
 # Example nparms == 2
 
 for rec in pagerecs:
  fields = rec.fields
  nfields = len(fields)
  if nfields < (nparms + 3):
   continue
  found = True
  for iparm in range(nparms - 1):
   parm = parms[iparm]
   ifield = 1 + iparm
   field = fields[ifield]
   if field != parm:
    found = False
    break
  if found == False:
   continue
  # last parm
  iparm = nparms - 1
  parm = parms[iparm]
  field1 = fields[iparm + 1]
  field2 = fields[iparm + 2]
  if field1 <= parm <= field2:
   instance.ipage = fields[iparm + 3]
   return

def make_outlines(instances):
 outlines = []
 for instance in instances:
  line = '%s\t%s' %(instance.ipage,instance.line)
  outlines.append(line)
 return outlines
if __name__ == "__main__":
 fileinstances = sys.argv[1]  # file created by lsfix3.py
 fileidx=sys.argv[2]  # tab-delimited index file for link target
 fileout = sys.argv[3]
 instances = init_instances(fileinstances)
 pagerecs = init_pagerecs(fileidx)
 n = 0
 for instance in instances:
  check_index(instance,pagerecs)
  if instance.ipage != None:
   n = n + 1
 print(f'{n} instances find ipage out of {len(instances)}')
 numinstance = len(instances)
 ntodo = numinstance - n
 print(f'{ntodo} references NOT FOUND in index')
 outlines = make_outlines(instances)
 write_lines(fileout,outlines)
