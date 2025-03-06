""" generate_random.py for Yajnavalkya
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
 def __init__(self,key,pagerec):
  self.key = key
  self.pagerec = pagerec
  self.entry = None
  
def get_entry_for_examples(entries,examples):
 verses = [example.key for example in examples]
 dexample = {}
 for example in examples:
  dexample[example.key] = example
 regex_raw = r'<ls>Spr\. ([0-9]+)'
 regex = re.compile(regex_raw)
 for entry in entries:
  text = ' '.join(entry.datalines)
  for m in re.finditer(regex,text):
   versekosha = int(m.group(1))
   if versekosha in dexample:
    example = dexample[versekosha]
    example.entry = entry
    break
 for example in examples:
  verse = example.key
  entry = example.entry
  if entry == None:
   print('No entry found for verse',v)
  else:
   print(example.key, example.entry.metad['L'])
 exit(1)
 
def get_pagerec_from_verse(pagerecs,verse):
 adhy = verse[0]
 v = verse[1]
 for rec in pagerecs:
  if (rec.fromv <= v) and (v <= rec.tov):
   return rec
 print('get_pagerec_from_verse ERROR',verse)
 exit(1)

def main1():
 nrandom = int(sys.argv[1])
 filein = sys.argv[2]  # xxx.txt
 filein1 = sys.argv[3] # name of Indisch index file
 fileout = sys.argv[4] # output file
 pagerecs = init_pagerecs(filein1)
 random_verses = randomize_pagerecs(pagerecs,nrandom)
 print(random_verses)
 examples = []
 for key in random_verses:
  pagerec = get_pagerec_from_verse(pagerecs,key)
  example = Example(key,pagerec)
  examples.append(example)
 print('ok so far')
 # now for dictionary  part
 entries = digentry.init(filein)
 get_entry_for_examples(entries,examples)
 print('2nd check point')

def init_verseentries(entries):
 # VID. [0-9]+
 regex_raw = r'<ls>HĀR. ([0-9]+)'
 print("regex_raw =",regex_raw)

 regex = re.compile(regex_raw)
 d = {}
 n = 0
 for entry in entries:
  text = ' '.join(entry.datalines)
  for m in re.finditer(regex,text):
   n = n + 1
   verse = int(m.group(1))
   key = (verse,)  # 1-tuple
   if key not in d:
    d[key] = []
   d[key].append(entry)
 keys = list(d.keys())
 print('found %s instances verse in kosha' % n)
 print('found %s distinct verse in kosha' % len(keys))
 return d


def get_pagerec(pagerecs,key):
 for rec in pagerecs:
  if (rec.keymin <= key) and (key <= rec.keymax):
   return rec
 print('get_pagerec ERROR: cannot find key',key)
 
def set_pagerec_key(pagerecs):
 # key is a verse
 # In python, n-tuples of ints have the <= relation
 for rec in pagerecs:
  rec.keymin = (rec.fromv,)
  rec.keymax = (rec.tov,)
 
def get_examples(verseentries,nrandom,pagerecs):
 import random
 set_pagerec_key(pagerecs)
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
 for key in exampleverses:
  ventries = verseentries[key]
  ventry = random.choice(ventries)
  pagerec = get_pagerec(pagerecs,key)
  example = Example(key,pagerec)
  example.entry = ventry
  examples.append(example)
 return examples

def example_to_outrec(example):
 outarr = []
 key  = example.key
 pagerec = example.pagerec
 entry = example.entry
 line = pagerec.line
 outarr.append('key %s: %s' %(key,line))
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
 examples1 = sorted(examples,key = lambda e: e.key)
 for example in examples1:
  outrec = example_to_outrec(example)
  outrecs.append(outrec)
 #
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print(len(examples),"written to",fileout)

  
def main2():
 nrandom = int(sys.argv[1])
 filein = sys.argv[2]  # xxx.txt
 filein1 = sys.argv[3] # name of index file
 fileout = sys.argv[4] # output file
 pagerecs = init_pagerecs(filein1)
 entries = digentry.init(filein)
 verseentries = init_verseentries(entries)
 examples = get_examples(verseentries,nrandom,pagerecs)
 print(len(examples),"examples found")
 write_examples(fileout,examples)
 

if __name__=="__main__":
 main2()
