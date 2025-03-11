# coding=utf-8
""" ref_byvol.py
"""
from __future__ import print_function
import sys, re,codecs
sys.path.append('../') # location of digentry
import digentry

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

def get_all_regexes(X):
 regexraws = [
  r'<ls>%s.*?</ls>' % X,
  r'<ls n="%s.*?</ls>' % X
 ]
 regexes = list(map(re.compile,regexraws))
 return regexes,regexraws

def arec_to_outrec(arec):
 outarr = []
 adhy = arec.adhy
 maxv = arec.maxv
 datas = arec.data_prob
 nprob = len(datas)
 out = '* (%s) adhy=%s, verse > %s' %(nprob,adhy,maxv)
 outarr.append(out)
 datas1 = sorted(datas,key = lambda t: t[2]) # verse in ls
 for idata,data in enumerate(datas):
  entry,adhy1,v1,ls = data
  meta = entry.metaline
  outarr.append('%d,%d %s %s' %(adhy1,v1,ls,meta))
 return outarr

def write_vols(fileout,refvols):
 outrecs = []
 tot = 0
 for refvol in refvols:
  (vol,count) = refvol
  tot = tot + count
 pctot = 0
 for refvol in refvols:
  (vol,count) = refvol
  percent = (100*count // tot)
  pctot = pctot + percent
  out = '%s %5d %3d pct' % (vol,count,percent)
  outrecs.append(out)
 #
 write_lines(fileout,outrecs)
 print(len(outrecs),"lines written to",fileout)

class AdhyRange(object):
 def __init__(self,line):
  parts = re.split(r' +',line)
  assert len(parts) == 2
  self.adhy = int(parts[0])
  self.maxv = int(parts[1])
  self.data_ok = []   # tuples of entry,adhy,verse
  self.data_prob = [] # tuples of entry,adhy,verse

def init_AdhyRange(filein):
 lines = read_lines(filein)
 recs = [AdhyRange(line) for line in lines]
 d = {}
 for rec in recs:
  d[rec.adhy] = rec
 return recs,d

def get_entry_vol(entry):
 # for pwg
 # pc v-nnnn
 pc = entry.metad['pc']
 m = re.search(r'^([1-7])-([0-9][0-9][0-9][0-9])$',pc)
 if m == None:
  print('ERROR get_entry_vol')
  exit(1)
 vol = int(m.group(1))
 return vol

def byvols(entries):
 regex_raw = r'<ls>VARĀH. BṚH. S. ([0-9]+),([0-9]+)'
 print("regex_raw =",regex_raw)

 regex = re.compile(regex_raw)
 # initialize counter
 d = {}
 for i in range(7):
  vol = i + 1
  d[vol] = 0
 
 n = 0
 for entry in entries:
  text = ' '.join(entry.datalines)
  vol = get_entry_vol(entry)
  for m in re.finditer(regex,text):
   n = n + 1
   d[vol] = d[vol] + 1
 print('found %s entries matching %s' % (n,regex_raw))
 x = [(vol,d[vol]) for vol in d.keys()]
 return x

if __name__=="__main__":
 filein = sys.argv[1]  # xxx.txt
 fileout = sys.argv[2] # output file
 
 entries = digentry.init(filein)
 # set entries attribute of AdhyRange objects
 refvols = byvols(entries)
 print(refvols)
 write_vols(fileout,refvols)
 
 
