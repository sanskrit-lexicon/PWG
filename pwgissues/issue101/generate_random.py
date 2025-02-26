# coding=utf-8
""" generate_random.py for SĀHITYADARPAṆA
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

class Example:
 def __init__(self,key,pagerec,linenum):
  self.key = key
  self.pagerec = pagerec
  self.linenum = linenum
  self.entry = None

def init_verseentries(entries,nparm):
 X = 'SĀH. D.'
 if nparm == 1:
  regex_raw = r'<ls>%s ([0-9]+)([.])' % X
 elif nparm == 2:
  regex_raw = r'<ls>%s ([0-9]+),([0-9]+)[.]' % X
 else:
  print('init_verseentries bad nparm',nparm)
  exit(1)
 print("nparm=%s, regex_raw = %s" % (nparm,regex_raw))
 regex = re.compile(regex_raw)
 d = {}
 n = 0
 for entry in entries:
  text = ' '.join(entry.datalines)
  for m in re.finditer(regex,text):
   n = n + 1
   if nparm == 1:
    verse = int(m.group(1))
    linenum = -1
    key = verse
   elif nparm == 2:
    linenum = int(m.group(2))
    ipage   = int(m.group(1))
    key = ipage
   else:
    assert True == False
   if key not in d:
    d[key] = []
   d[key].append((entry,linenum))
 keys = list(d.keys())
 print('found %s instances in kosha' % n)
 print('found %s distinct instances in kosha' % len(keys))
 return d

def get_pagerec(pagerecs,key,nparm):
 for rec in pagerecs:
  if (rec.keymin <= key) and (key <= rec.keymax):
   return rec
 print('get_pagerec ERROR: cannot find key',key)
 
def set_pagerec_key(pagerecs,nparm):
 # key depends on nparm
 # key is a 2-tuple of ints (adhy,verse)
 # In python, n-tuples of ints have the <= relation
 for rec in pagerecs:
  if nparm == 1:
   #rec.keys = list(range(rec.fromv, rec.tov + 1)
   rec.keymin = rec.fromv
   rec.keymax = rec.tov
  elif nparm == 2:
   rec.keymin = rec.ipage
   rec.keymax = rec.ipage
   
def get_examples(verseentries,nrandom,pagerecs,nparm):
 import random
 set_pagerec_key(pagerecs,nparm)
 allkoshaverses = verseentries.keys()
 keyminall = pagerecs[0].keymin
 keymaxall = pagerecs[-1].keymax

 koshaverses = [key for key in allkoshaverses if
                ((keyminall <= key) and (key <= keymaxall))]
 nexamples = nrandom
 if nrandom > len(koshaverses):
  nexamples = len(koshaverses)
  print('WARNING Can only get %s examples' % len(koshaverses))
 # sample without duplicates
 exampleverses = random.sample(koshaverses,nexamples)
 examples = []
 for ikey,key in enumerate(exampleverses):
  ventries = verseentries[key]
  ventry = random.choice(ventries)
  entry,linenum = ventry
  pagerec = get_pagerec(pagerecs,key,nparm)
  if False:
   print('get_examples %s: key=%s, pagerec=%s' %(ikey+1,key,pagerec.line))
  example = Example(key,pagerec,linenum)
  example.entry = entry
  examples.append(example)
 return examples

def example_to_outrec(example,nparm):
 outarr = []
 key  = example.key
 pagerec = example.pagerec
 linenum = example.linenum  # used when nparm=2
 entry = example.entry
 line = pagerec.line
 if nparm == 1:
  keyout = key
 elif nparm == 2:
  keyout = (key,linenum)  # k == ipage
 else:
  assert True == False
 outarr.append('key %s: %s' %(keyout,line))
 L = entry.metad['L']
 k1 = entry.metad['k1']
 pc = entry.metad['pc']
 outarr.append('L= %s, hw= %s, pc=%s' %(L,k1,pc))
 outarr.append('check: ?')
 outarr.append('----------------------------------------------')
 outarr.append('')
 return outarr

def write_examples(fileout,examples,nparm):
 outrecs = []
 # sort examples by verse
 examples1 = sorted(examples,key = lambda e: e.key)
 for example in examples1:
  if False:
   print('write_examples: key=%s, pagerec=%s' %(example.key,example.pagerec.line))
  outrec = example_to_outrec(example,nparm)
  outrecs.append(outrec)
 #
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print(len(examples),"written to",fileout)

  
def main1(entries,pagerecs,nparm):
 verseentries = init_verseentries(entries,nparm)
 examples = get_examples(verseentries,nrandom,pagerecs,nparm)
 print(len(examples),"examples found")
 write_examples(fileout,examples,nparm)
 
if __name__=="__main__":
 nrandom = int(sys.argv[1])
 nparm = int(sys.argv[2])
 filein = sys.argv[3]  # xxx.txt
 filein1 = sys.argv[4] # name of index file
 fileout = sys.argv[5] # output file
 pagerecs = init_pagerecs(filein1)
 entries = digentry.init(filein)
 # pwg uses 2 ways to refer to this literary source:
 # 1 parm:  the 'verse'
 # 2 parm:  linenum,ipage
 main1(entries,pagerecs,nparm)
 

