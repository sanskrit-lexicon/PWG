# coding=utf-8
""" generate_random.py for ramayanabom
"""
from __future__ import print_function
import sys, re,codecs
import digentry
# from make_js_index import *

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

def parse_kand(x):
 if re.search(r'^[0-9]+$',x):
  return int(x)
 if re.search(r'^[ivxclm]+$',x): # lower-case agrees with 'mw'
  y = roman_to_integer(x)
  return y
 return None


def get_dict_key(m,dictcode):
 if '3' in dictcode:
  kand = parse_kand(m.group(1))
  sarga = int(m.group(2))
  verse = int(m.group(3))
  key = (kand,sarga,verse)
 elif '4' in dictcode:
  kand = parse_kand(m.group(1))
  sarga = int(m.group(2))
  sargap = int(m.group(3))
  verse = int(m.group(4))
  key = (kand,sarga,sargap,verse)
 else:
  print('get_dict_key error. dictcode=',dictcode)
  exit(1)
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
 vmin = pagerecs[0].v1
 vmax = pagerecs[-1].v2
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

def get_pagerec(pagerecs,key):
 for rec in pagerecs:
  if (rec.keymin <= key) and (key <= rec.keymax):
   return rec
 print('get_pagerec ERROR: cannot find key',key)
 return None

def set_pagerec_key(pagerecs,dictcode):
 # key is a 3-tuple of ints (kand, sarga, verse)
 # In python, n-tuples of ints have the <= relation
 for rec in pagerecs:
  if '3' in dictcode:
   rec.keymin = (rec.kand,rec.sarga,rec.v1)
   rec.keymax = (rec.kand,rec.sarga,rec.v2)
  elif '4' in dictcode:
   rec.keymin = (rec.kand,rec.sarga,rec.sargap,rec.v1)
   rec.keymax = (rec.kand,rec.sarga,rec.sargap,rec.v2)
  else:
   print('set_pagerec_key error. dictcode=',dictcode)
   exit(1)
   
def get_examples(verseentries,nrandom,pagerecs,dictcode):
 import random
 set_pagerec_key(pagerecs,dictcode)
 allkoshaverses = verseentries.keys()
 #print('dbg: len(allkoshaverses)=',len(allkoshaverses))
 #keyminall = pagerecs[0].keymin
 #keymaxall = pagerecs[-1].keymax
 koshaverses = list(allkoshaverses)
 #koshaverses = [key for key in allkoshaverses if
 #               ((keyminall <= key) and (key <= keymaxall))]
 #print('dbg: len(koshaverses)=',len(koshaverses))
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
  pagerec = get_pagerec(pagerecs,key) # can be None
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
  a = [str(x) for x in key]
  keya = ','.join(a)
  line = 'no index for (%s)' % keya
 else:
  line = pagerec.pseudoline
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
  'pwg3':r'<ls>R. ed. Bomb. ([0-9]+),([0-9]+),([0-9]+)[^,]',   
  'pw3':r'<ls>R. ed. Bomb. ([0-9]+),([0-9]+),([0-9]+)[^,]', 
  'pwkvn3':r'<ls>R. ed. Bomb. ([0-9]+),([0-9]+),([0-9]+)[^,]', 
  'sch3':r'<ls>R. ed. Bomb. ([0-9]+),([0-9]+),([0-9]+)[^,]', 
  'mw3':r'<ls>R. ed. Bomb. ([ivx]+), *([0-9]+), *([0-9]+)[^,]',
  # there are no 4-parameter "R. ed. Bomb." in pwg
  
  'pwg4':r'<ls>R. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)',   
  'pw4':r'<ls>R. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)', 
  'pwkvn4':r'<ls>R. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)', 
  'sch4':r'<ls>R. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)', 
  'mw4':r'<ls>R. (vii), *([0-9]+), *([0-9]+), *([0-9]+)',
  
  'pwg37':r'<ls>R. (7),([0-9]+),([0-9]+)[^,]',   
  'pw37':r'<ls>R. (7),([0-9]+),([0-9]+)[^,]', 
  'pwkvn37':r'<ls>R. (7),([0-9]+),([0-9]+)[^,]', 
  'sch37':r'<ls>R. (7),([0-9]+),([0-9]+)[^,]', 
  'mw37':r'<ls>R. (vii), *([0-9]+), *([0-9]+)[^,]',

  
   }
 if dictcode not in d:
  print('get_dict_regex Error',dictcode)
  exit(1)
 regex_raw = d[dictcode]
 print("regex_raw =",regex_raw)
 regex = re.compile(regex_raw)
 return regex 

class Pagerec(object):
 """
Format of index
VOL page	kand.	adhy.	brāhm.	from kaṇḍ.	to kaṇḍ.	ipage

III	578	7	23	52	53	37b	
III	578	7	23.1	1	15	37b	

""" 
 def __init__(self,obj,dictcode):
  self.kand = obj['kand']
  self.sarga = obj['sarga']
  self.sargap = obj['sargap']
  self.v1 = obj['v1']
  self.v2 = obj['v2']
  self.vp = obj['vp']
  k = str(self.kand)
  s = str(self.sarga)
  sp = str(self.sargap)
  v1 = str(self.v1)
  v2 = str(self.v2)
  vp = self.vp
  if '3' in dictcode:
   args = (k,s,v1,v2,vp)
  elif '4' in dictcode:
   args = (k,s,sp,v1,v2,vp)
  else:
   print('Pagerec: dictcode error',dictcode)
   exit(1)
  self.pseudoline = '\t'.join(args)
  
def pagerecs_from_js(filein,dictcode):
 lines = read_lines(filein)
 # drop first line and last line
 json_string = '\n' . join(lines[1:-1])
 import json
 data = json.loads(json_string)
 pagerecs = []
 for obj in data:
  pagerec = Pagerec(obj,dictcode)
  pagerecs.append(pagerec)
 return pagerecs

if __name__=="__main__":
 nrandom = int(sys.argv[1])
 dictcode = sys.argv[2]
 filein = sys.argv[3]  # xxx.txt
 filein1 = sys.argv[4] # name of index.js file
 fileout = sys.argv[5] # output file
 pagerecs = pagerecs_from_js(filein1,dictcode)
 entries = digentry.init(filein)

 verseentries = init_verseentries(entries, dictcode)
 print('begin get_examples')
 examples = get_examples(verseentries,nrandom,pagerecs,dictcode)
 print(len(examples),"examples found")
 write_examples(fileout,examples)

