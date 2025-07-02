# coding=utf-8
""" cmp_bcs0.py
"""
from __future__ import print_function
import sys, re, codecs
import json

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
 print(len(outarr),"cases written to",fileout)

def make_js(recs):
 outarr = []
 outarr.append('indexdata = [')
 arr = [] # array of Python dicts
 for rec in recs:
  d = rec.todict()  # a Python dictionary
  arr.append(d)
 return arr

def write_recs(fileout,data):
 with codecs.open(fileout,"w","utf-8") as f:
  f.write('indexdata = \n')
  jsonstring = json.dumps(data,indent=1)
  f.write( jsonstring +  '\n')
  f.write('; // end of indexdata\n')
  
 print('json data written to',fileout)

class BCS:
 def __init__(self,k1,k2,k3,v1,v2,code):
  self.k1 = k1
  self.k2 = k2
  self.k3 = k3
  self.v1 = v1
  self.v2 = v2
  self.code = code
  self.data = (k1,k2,k3,v1,v2)
  self.key = (k1,k2,k3)
  
def write_cmp1(fileout,recs1,recs2):
 outarr = []
 # assume same keys
 code1 = recs1[0].code
 code2 = recs2[0].code
 for irec,rec1 in enumerate(recs1):
  rec2 = recs2[irec]
  if rec1.data == rec2.data:
   out = '%s %s = %s' % (rec1.data,code1,code2)
  else:
   out = '%s %s' %(rec1.data,rec2.data)
  outarr.append(out)
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print('%s records written to %s' %(len(recs1),fileout))
 
def init_bcs(filein,code):
 lines = read_lines(filein)
 recs = []
 for line in lines:
  line = line.lstrip() # remove space at beginning of line
  parts = re.split(r'[ :-]+',line)
  if len(parts) != 5:
   print('parts=',parts)
   exit(1)
  assert len(parts) == 5
  k1,k2,k3,v1,v2 = [int(part) for part in parts]
  key1 = k1,k2,k3
  rec = BCS(k1,k2,k3,v1,v2,code)
  recs.append(rec)
 print(len(recs),"from",filein)
 return recs

def compare_keys(recs1,recs2):
 keys1 = [rec.key for rec in recs1]
 keys2 = [rec.key for rec in recs2]
 code1 = recs1[0].code
 code2 = recs2[0].code
 for key in keys1:
  if key not in keys2:
   print('key %s unique to %s' %(key,code1))
 for key in keys2:
  if key not in keys1:
   print('key %s unique to %s' %(key,code2))

def key_uniqueness(recs):
 # uniqueness of key in recs1
 d = {}
 n = 0 # number of records with dup keys
 code = recs[0].code
 for rec in recs:
  if rec.key in d:
   print('%s duplicate key %s' %(code,rec.key))
   n = n + 1
  else:
   d[rec.key] = True
 print('%s has %s duplicate keys' %(code,n))

def artificial_col():
 ans = []
 for s in range(29,33):
  rec = BCS(3,4,s,0,0,'col')
  ans.append(rec)
 return ans

def count_verses(recs):
 code = recs[0].code
 n = 0
 for rec in recs:
  v1 = rec.v1
  v2 = rec.v2
  nv = v2 - v1 + 1 # number of verses for this key
  n = n + nv
 print('%s verses for %s' %(n,code))

def check_intersect_helper(recs):
 code = recs[0].code
 n = 0
 for irec,rec in enumerate(recs):
  if irec == 0:
   prev = rec
   continue
  u1 = prev.v1
  u2 = prev.v2
  v1 = rec.v1
  v2 = rec.v2
  assert v1 <= v2
  assert u1 <= u2
  #assert u2 <= v1
  # do intervals [u1,u2] and [v1,v2] intersect
  urange = range(u1,u2+1)
  vrange = range(v1,v2+1)
  uset = set(urange)
  vset = set(vrange)
  iset = uset.intersection(vset)
  if len(iset) != 0:
   n = n + 1
   print('%s %s %s intersect %s' %(code,irec,prev.data, rec.data))
  prev = rec
  
 print('%s non-disjoint sets in %s' % (n,code))

def check_intersect(recs):
 recs_3_4 = [rec for rec in recs if (rec.k1,rec.k2) == (3,4)]
 check_intersect_helper(recs_3_4)
 recs_3_6 = [rec for rec in recs if (rec.k1,rec.k2) == (3,6)]
 check_intersect_helper(recs_3_6)

def verse_to_section(v,recs):
 # first rec containing verse v
 for r in recs:
  if r.v1 <= v <= r.v2:
   return r
 print('verse_to_section fails for v = %s, code = %s' % (v,recs[0].code))
 exit(1)
 
def mapping(recsa,recsb,key1,key2,nverse):
 recsa1 = [r for r in recsa if (key1,key2) == (r.k1,r.k2)]
 recsb1 = [r for r in recsb if (key1,key2) == (r.k1,r.k2)]

 ans = []
 for v in range(1,nverse+1):
  reca = verse_to_section(v,recsa1)
  recb = verse_to_section(v,recsb1)
  # dlc is recsa, col is recsb
  ansa = [reca.k1,reca.k2,reca.k3,v]
  ansb = [recb.k1,recb.k2,recb.k3,v]
  ans.append([ansa,ansb])
 return ans

def write_map_crude(fileout,data):
 with codecs.open(fileout,"w","utf-8") as f:
  f.write('dlc_col = \n')
  jsonstring = json.dumps(data,indent=1)
  f.write( jsonstring +  '\n')
  f.write('; // end of indexdata\n')
 print('write_map data to',fileout)

def unused_intarr_to_str(x):
 # x = [1,2,3]   array of ints
 y = []
 for val in x:
  valstr = str(val)
  y.append(valstr)
 

def write_map_helper(data):
 # data is an array, each element being a
 # example element: [[1,2,3,4],[5,6,7,8]]
 outarr = []
 outarr.append('dlc_col = [')
 for x in data:
  out = '%s,' % x
  outarr.append(out)
 outarr.append('];')
 return outarr
def write_map(fileout,data):
 outarr = write_map_helper(data)
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out + '\n')
 print('write_map sends %s lines to %s' %(len(outarr),fileout))

if __name__ == "__main__":
 filein1 = sys.argv[1]  # bcs_dlc
 filein2 = sys.argv[2]  # bcs_col
 fileout = sys.argv[3]
 fileout1 = sys.argv[4] # mapping for (3,4,x,v)
 recs1 = init_bcs(filein1,'dlc')
 recs2 = init_bcs(filein2,'col')
 count_verses(recs1)
 count_verses(recs2)
 
 key_uniqueness(recs1)
 key_uniqueness(recs2)
 
 compare_keys(recs1,recs2)
 # keys (3,4,29-32) are unique to dlc.
 # Add these as artificial keys to col.
 recs2x = artificial_col()
 recs2a = recs2 + recs2x
 recs2b = sorted(recs2a, key = lambda rec: rec.key)
 keys1 = [rec.key for rec in recs1]
 keys2 = [rec.key for rec in recs2b]
 assert keys1 == keys2
 # write_cmp1(fileout,recs1,recs2b)
 check_intersect(recs1)
 check_intersect(recs2)

 map1 = mapping(recs1,recs2,3,4,241)
 # also identity map
 # dlc 3,4,32,v  <-> 3,4,28,v  for v = 1-18
 map2 = []
 for v in range(1,18+1):
  a = [3,4,32,v]
  b = [3,4,28,v]
  c = [a,b]
  map2.append(c)
 mapall = map1 + map2
 write_map(fileout1,mapall)
  
