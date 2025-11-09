# coding=utf-8
""" chkidx.py  adapted for VĀJASANEYISAM̃HITĀ
"""
from __future__ import print_function
import sys, re, codecs

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
 def __init__(self,line,parms):
  volfield = parms['volfield']
  nparm = parms['nparm']
  assert nparm >= 2
  parts0 = line.split('\t')
  dbg = False
  if volfield == True:
   # remove 1st field (volume)
   parts0 = parts0[1:]
  if dbg:
   print(f'Pagerec: nparm = {nparm}, len(parts0) = {len(parts0)}')
   print(f'parts0 = {parts0}')
  if len(parts0) < (nparm + 3):
   # no ipage
   # set ipage = epage (first field)
   parts0.append(parts0[0])
   if dbg:
    print(f'no ipage. using epage')
    print(f'revise parts0 = {parts0}')
  # convert to ints
  parts = []
  for part in parts0:
   digits = re.sub(r'[^0-9]','',part) # remove non-digits
   if digits == '': # no digits!
    newpart = -1
   else:
    newpart = int(digits)
   parts.append(newpart)
  self.parts0 = parts0
  self.parts = parts
  # parts[0] epage
  # parts[1] ... parts[nparm - 1] = fields[0] ... fields[nparm - 2]
  # parts[nparm] fromv for last field
  # parts[nparm + 1] tov for last field
  # parts[nparm + 2] ipage
  self.epage = parts[0]
  self.ipage = parts[nparm + 2]
  fromfields = [parts[i] for i in range(1,nparm)]
  tofields =   [parts[i] for i in range(1,nparm)]
  fromv = parts[nparm]
  tov = parts[nparm + 1]
  fromfields.append(fromv)
  tofields.append(tov)
  self.fromfields = fromfields
  self.tofields = tofields
  self.nparm = nparm
  if dbg: # dbg
   print(f'fromfields = {fromfields}')
   print(f'tofields = {tofields}')
   exit(1)
def init_pagerecs(filein,parms):
 """ filein is a tsv file, with first line as fieldnames
 """

 lines = read_lines(filein)
 recs = []
 for iline,line in enumerate(lines):
  if iline == 0:
   continue # skip first line
  else:
   rec = Pagerec(line,parms)
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
  self.ipage = None  # possibly re-set by check_index
  
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
 """
 parms = instance.parms
 nparms = len(parms)
 for rec in pagerecs:
  if rec.fromfields <= parms <= rec.tofields:
  # reset ipage 
   instance.ipage = rec.ipage
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
 parms = {'volfield': True,
          'nparm': 2,
  }
 instances = init_instances(fileinstances)
 pagerecs = init_pagerecs(fileidx,parms)
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
