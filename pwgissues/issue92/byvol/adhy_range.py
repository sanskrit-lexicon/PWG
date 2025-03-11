# coding=utf-8
""" adhy_range.py for brihat-samhitA
"""
from __future__ import print_function
import sys, re, codecs
sys.path.append('../') # location of make_js_index.py
from make_js_index import *

def adhy_range(pagerecs):
 prev = None
 a1 = pagerecs[0].adhy
 a2 = pagerecs[-1].adhy
 adhys = range(a1,a2+1)
 ans = []
 for adhy in adhys:
  x = [(rec.fromv,rec.tov) for rec in pagerecs if rec.adhy == adhy]
  fromv,tov = x[0]  # first instance
  assert fromv == 1
  fromv,tov = x[-1]  # last
  atov = (adhy,tov)
  ans.append(atov)

 print('adhy_range returns %s 2-tuples' % len(ans))
 return ans

def write_recs(fileout,data):
 with codecs.open(fileout,"w","utf-8") as f:
  for datum in data:
   adhy,tovmax = datum
   out = '%s %s' %(adhy,tovmax)
   f.write(out + '\n')
  
 print('adhyAya ranges written to',fileout)

if __name__ == "__main__":
 filein=sys.argv[1]  # tab-delimited index file
 fileout = sys.argv[2]
 pagerecs = init_pagerecs(filein)
 outrecs = adhy_range(pagerecs)
 write_recs(fileout,outrecs)
 check1(pagerecs)
 
 
