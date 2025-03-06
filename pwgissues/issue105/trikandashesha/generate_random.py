# coding=utf-8
""" generate_random.py for IndischeSprueche
"""
from __future__ import print_function
import sys, re,codecs
import digentry
from make_js_index import *

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

def randomize_pagerecs(pagerecs,nrandom):
 import random
 vmin = pagerecs[0].fromv
 vmax = pagerecs[-1].tov
 ans = []
 for _ in range(nrandom):
  v = random.randint(vmin,vmax)
  ans.append(v)
 ans1 = sorted(ans)
 return ans1

class Example:
 def __init__(self,verse,pagerec,entry):
  self.verse = verse
  self.pagerec = pagerec
  self.entry = entry


def generate_pagerec_keys(pagerecs):
 # all known 4-tuple keys implied by pagerecs
 # 
 keys = []
 d = {}
 for rec in pagerecs:
  fromkey = rec.fromkey
  tokey = rec.tokey
  assert fromkey[:2] == tokey[:2]
  base = fromkey[:2]
  v1 = rec.fromkey[2]
  v2 = rec.tokey[2]
  for v in range(v1,v2+1):
   key = (base[0],base[1],v)
   keys.append(key)
   d[key] = rec # there can be duplicate keys
 print('generate_pagerec_keys: %s keys' % len(keys))
 return keys,d

def get_pagerec_from_verse(pagerecs,verse):
 for rec in pagerecs:
  if (rec.fromv <= verse) and (verse <= rec.tov):
   return rec
 print('get_pagerec_from_verse ERROR',verse)
 exit(1)

pwgregex_raw = r'<ls>TRIK[.] ([0-9]+),([0-9]+),([0-9]+)'
pwgregex = re.compile(pwgregex_raw)

def init_verseentries(entries):
 regex_raw = r'<ls>Spr\. ([0-9]+)'
 regex = re.compile(regex_raw)
 d = {}
 for entry in entries:
  text = ' '.join(entry.datalines)
  for m in re.finditer(pwgregex,text):
   versekey = (int(m.group(1)), int(m.group(2)), int(m.group(3)))
   if versekey not in d:
    d[versekey] = []
   d[versekey].append(entry)
 versekeys = list(d.keys())
 print('found %s distinct verse keys in kosha' % len(versekeys))
 return d

def get_pagerec(pagerecs,v):
 for rec in pagerecs:
  if (rec.fromv <= v) and (v <= rec.tov):
   return rec
 print('get_pagerec ERROR: cannot find verse',v)
 exit(1)
 

def get_examples(verseentries,nrandom,dpagerecs):
 import random
 koshaverses = list(verseentries.keys())
 nexamples = nrandom
 if nrandom > len(koshaverses):
  nexamples = len(koshaverses)
  print('WARNING Can only get %s examples' % len(koshaverses))
 # sample without duplicates
 exampleverses = random.sample(koshaverses,nexamples)
 examples = []
 for v in exampleverses:
  ventries = verseentries[v]
  ventry = random.choice(ventries)
  #pagerec = get_pagerec(pagerecs,v)
  if v not in dpagerecs:
   vstr = str(v)
   print('get_examples: verse %s not in pagerecs' % vstr)
   continue
  pagerec = dpagerecs[v]
  example = Example(v,pagerec,ventry)
  example.entry = ventry
  examples.append(example)
 return examples

def example_to_outrec(example):
 outarr = []
 verse  = example.verse
 pagerec = example.pagerec
 entry = example.entry
 line = pagerec.line
 outarr.append('verse %s: %s' %(verse,line))
 L = entry.metad['L']
 k1 = entry.metad['k1']
 pc = entry.metad['pc']
 outarr.append('L= %s, hw= %s, pc=%s' %(L,k1,pc))
 outarr.append('check: ?')
 outarr.append('----------------------------------------------')
 outarr.append('')
 return outarr

def write_examples(fileout,examples):
 outrecs = []
 # sort examples by verse
 examples1 = sorted(examples,key = lambda e: e.verse)
 for example in examples1:
  outrec = example_to_outrec(example)
  outrecs.append(outrec)
 #
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print(len(examples),"written to",fileout)
 
def main():
 nrandom = int(sys.argv[1])
 filein = sys.argv[2]  # xxx.txt
 filein1 = sys.argv[3] # name of index file
 fileout = sys.argv[4] # output file
 pagerecs = init_pagerecs(filein1)
 keys,dpagerecs = generate_pagerec_keys(pagerecs)
 entries = digentry.init(filein)
 verseentries = init_verseentries(entries)  # a dict
 examples = get_examples(verseentries,nrandom,dpagerecs)
 print(len(examples),"examples found")
 write_examples(fileout,examples)
 

if __name__=="__main__":
 main()
