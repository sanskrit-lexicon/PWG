# coding=utf-8
""" make_renum.py
  then new1.txt is same as new.txt.
"""
from __future__ import print_function
import sys, re,codecs

parms = {
    'indir': 'extracts',
    'outdir': 'replacements',
    'dictcode':'pwg',
    'vol': 6,
    'n1': 1,
    'n2': 55,
 }

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(outarr),"lines written to",fileout)

def get_outarr():
 indir = parms['indir']
 outdir = parms['outdir']
 dictcode = parms['dictcode']
 n1 = parms['n1']
 n2 = parms['n2']
 vol = parms['vol']
 outarr = []
 def f(n):
  # f(1) = 301  300 + 2*(1-1) + 1
  # f(2) = 303  300 + 2*(2-1) + 1
  # ...
  # f(55) =   300 + 2*(55-1) + 1 = 300 + 2*54 + 1 = 300 + 108 + 1 = 409
  return  300 + (2 * (n-1)) + 1

 for n in range(n1,n2 + 1):
  m = f(n)
  infile = f'{indir}/"{dictcode}{vol} {n}.pdf"'
  outfile = f'{outdir}/{dictcode}{vol}-{m:04d}.pdf'
  out = f'cp {infile} {outfile}'
  outarr.append(out)
 return outarr
if __name__=="__main__":
 fileout = sys.argv[1]
 outarr = get_outarr()
 write_lines(fileout,outarr)
 
 
 
