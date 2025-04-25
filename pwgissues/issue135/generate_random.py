# coding=utf-8
""" generate_random.py for raghuvamsacalc
"""
from __future__ import print_function
import sys, re,codecs
import digentry
from make_js_index import *

def roman_to_integer(roman):
 # courtest copilot
 roman_values = {
     'I': 1, 'V': 5, 'X': 10, 'L': 50,
     'C': 100, 'D': 500, 'M': 1000
 }
 integer_value = 0
 prev_value = 0
 romanup = roman.upper()  # upcase to agree with roman_values
 for char in reversed(romanup):
  current_value = roman_values[char]
  if current_value < prev_value:
      integer_value -= current_value
  else:
      integer_value += current_value
  prev_value = current_value

 return integer_value

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

def parse_taranga(x):
 if re.search(r'^[0-9]+$',x):
  return int(x)
 if re.search(r'^[ivxclm]+$',x): # lower-case agrees with 'mw'
  y = roman_to_integer(x)
  return y
 return None

def get_dict_key(m,dictcode):
 a = m.group(1)
 if dictcode == 'mw':
  taranga = roman_to_integer(a)
 else:
  taranga = int(a)
 verse = int(m.group(2))
 key = (taranga,verse)
 return key

def init_verseentries(entries,dictcode):
 # allow roman
 d = {}
 n = 0
 regex = get_dict_regex(dictcode)
 for entry in entries:
  text = ' '.join(entry.datalines)
  for m in re.finditer(regex,text):
   key = get_dict_key(m,dictcode)
   n = n + 1
   if key not in d:
    d[key] = []
   d[key].append(entry)
 keys = list(d.keys())
 print('found %s instances in kosha' % n)
 print('found %s distinct in kosha' % len(keys))
 return d

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
 
def unused_get_pagerec_from_verse(pagerecs,verse):
 for rec in pagerecs:
  if (rec.fromv <= verse) and (verse <= rec.tov):
   return rec
 print('get_pagerec_from_verse ERROR',verse)
 return None


def get_pagerec(pagerecs,key):
 for rec in pagerecs:
  if (rec.keymin <= key) and (key <= rec.keymax):
   return rec
 print('get_pagerec ERROR: cannot find key',key)

def set_pagerec_key(pagerecs,dictcode):
 # key is a 2-tuple of ints 
 # In python, n-tuples of ints have the <= relation
 for rec in pagerecs:
  a = rec.taranga
  fromv = rec.fromv
  tov = rec.tov
  rec.keymin = (a,fromv)
  rec.keymax = (a,tov)

def get_examples(verseentries,nrandom,pagerecs,dictcode):
 import random
 set_pagerec_key(pagerecs,dictcode)
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
 if pagerec == None:
  line = 'pagerec not found'
 else:
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

def get_dict_regex(dictcode):
 d = {
  'pwg':r'<ls>RĀJA-TAR. ([0-9]+),([0-9]+)',

  'pw':r'<ls>RĀJAT. ([0-9]+),([0-9]+)',
  'pwkvn':r'<ls>RĀJAT. ([0-9]+),([0-9]+)',

  'sch':r'<ls>Rājat. ([0-9]+),([0-9]+)',

  'mw':r'<ls>Rājat. ([vix]+), *([0-9]+)',   # 

   }
 if dictcode not in d:
  print('get_dict_regex Error',dictcode)
  exit(1)
 regex_raw = d[dictcode]
 print("regex_raw =",regex_raw)
 regex = re.compile(regex_raw)
 return regex 

if __name__=="__main__":
 nrandom = int(sys.argv[1])
 dictcode = sys.argv[2]
 filein = sys.argv[3]  # xxx.txt
 filein1 = sys.argv[4] # name of index file
 fileout = sys.argv[5] # output file
 pagerecs = init_pagerecs(filein1)
 entries = digentry.init(filein)

 #regex = get_dict_regex(dictcode)

 verseentries = init_verseentries(entries, dictcode)
 examples = get_examples(verseentries,nrandom,pagerecs,dictcode)
 print(len(examples),"examples found")
 write_examples(fileout,examples)

