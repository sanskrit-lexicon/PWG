# coding=utf-8
""" make_renum.py
  then new1.txt is same as new.txt.
"""
from __future__ import print_function
import sys, re,codecs

from make_renum_parms import parms
def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(outarr),"lines written to",fileout)

def get_outarr(vol):
 indir = parms['indir']
 outdir = parms['outdir']
 dictcode = parms['dictcode']
 volparms = parms[vol]
 n1 = volparms['n1']
 n2 = volparms['n2']
 nskip = volparms['nskip']
 outarr = []
 def f(n):
  return (2 * (n-1)) + 1

 for n in range(n1,n2 + 1):
  if n == nskip:
   print(f'skipping n = {nskip}')
   continue
  if n < nskip:
   m = f(n)
  else:
   m = f(n-1)
  infile = f'{indir}/"{dictcode}{vol} {n}.pdf"'
  outfile = f'{outdir}/{dictcode}{vol}-{m:04d}.pdf'
  out = f'cp {infile} {outfile}'
  outarr.append(out)
 return outarr
if __name__=="__main__":
 vol = int(sys.argv[1])
 fileout = sys.argv[2]
 outarr = get_outarr(vol)
 write_lines(fileout,outarr)
 
 
 
