# coding=utf-8
""" generate_random.py for malavikagni
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

def unused_parse_anka(x):
 if re.search(r'^[0-9]+$',x):
  return int(x)
 if re.search(r'^[ivxclm]+$',x): # lower-case agrees with 'mw'
  y = roman_to_integer(x)
  return y
 return None

def get_dict_key1(m,dictcode):
 verse = int(m.group(1)) 
 key = (verse,)
 return key

def get_dict_key2(m,dictcode):
 if dictcode in ('pwg2','pw2','pwkvn2','sch2'):
  anka = int(m.group(1))
  verse = int(m.group(2))
  key = (anka,verse)
  return key
 elif dictcode == 'mw2':
  anka_raw = m.group(1)
  anka = roman_to_integer(anka_raw)
  verse = int(m.group(2))
  key = (anka,verse)
  return key
 else:
  print('get_dict_key2 NOT AVALIABLE for',dictcode)
  exit(1)
 
def get_dict_key(m,dictcode):
 if dictcode.endswith('1'):
  return get_dict_key1(m,dictcode)
 if dictcode.endswith('2'):
  return get_dict_key2(m,dictcode)

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

def dbg_write_pagerecs(pagerecs):
 fileout = 'temp_dbg_pagerecs_mw.txt'
 outarr = []
 for r in pagerecs:
  a = (r.page, r.anka,r.fromv,r.tov,r.fromv_orig,r.tov_orig,r.ipage)
  a1 = map(str,a)
  out = '\t'.join(a1)
  outarr.append(out)
 write_lines(fileout,outarr)
 
def get_pagerec(pagerecs,key):
 for rec in pagerecs:
  if (rec.keymin <= key) and (key <= rec.keymax):
   return rec
 print('get_pagerec ERROR: cannot find key',key)
 dbg_write_pagerecs(pagerecs)

def set_pagerec_key1(rec,dictcode):
 a = rec.anka
 fromv = rec.fromv
 tov = rec.tov
 rec.keymin = (fromv,)
 rec.keymax = (tov,)

def set_pagerec_key2(rec,dictcode):
 if dictcode in ('pwg2','pw2','pwkvn2','sch2'):
  ipage = rec.ipage
  rec.keymin = (ipage,1)
  rec.keymax = (ipage,100) # 100 arbitrary big
 elif dictcode == 'mw2':
  rec.keymin = (rec.anka,rec.fromv)
  rec.keymax = (rec.anka,rec.tov)
 else:
  print('set_pagerec_key2 NOT AVAILABLE for ',dictcode)
  exit(1)
 
def set_pagerec_key(pagerecs,dictcode):
 # key is a 1-tuple or 2-tuple
 # In python, n-tuples of ints have the <= relation
 for rec in pagerecs:
  if dictcode.endswith('1'):
   set_pagerec_key1(rec,dictcode)
  elif dictcode.endswith('2'):
   set_pagerec_key2(rec,dictcode)
  else:
   print('set_pagerec_key: invalid dictcode',dictcode)
   exit(1)

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
 # get all examples
 
 for key in exampleverses:
  ventries = verseentries[key]
  ventry = random.choice(ventries)
  pagerec = get_pagerec(pagerecs,key)
  example = Example(key,pagerec)
  example.entry = ventry
  examples.append(example)
 return examples

def get_examples_all(verseentries,nrandom,pagerecs,dictcode):
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
 # get all examples
 
 for key in exampleverses:
  ventries = verseentries[key]
  #ventry = random.choice(ventries)
  for ventry in ventries:
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
  # line = pagerec.line
  line = '%s [%s - %s]' %(pagerec.line,pagerec.fromv, pagerec.tov)
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
  'mw2':r'<ls>Mālav. ([vix]+), *([0-9]+)',   # 
   }
 if dictcode not in d:
  print('get_dict_regex Error',dictcode)
  exit(1)
 regex_raw = d[dictcode]
 print("regex_raw =",regex_raw)
 regex = re.compile(regex_raw)
 return regex 

def adjust_mw_rec(rec):
  offsets = (0,21,35,58,75)
  anka = rec.anka
  if anka == 0:
   anka = 1
   rec.anka = anka
  offset = offsets[anka - 1]
  fromv = rec.fromv  # continuous verses (per pdf)
  tov = rec.tov
  v1a = fromv
  v2a = tov
  # verses for anka start at 1  (MW convention for Malav. R,N
  v1 = v1a - offset
  v2 = v2a - offset
  rec.fromv = v1
  rec.tov = v2
  rec.fromv_orig = v1a
  rec.tov_orig = v2a
       
def adjust_mw_pagerecs(pagerecs):
 for rec in pagerecs:
  adjust_mw_rec(rec)
  
if __name__=="__main__":
 parm = sys.argv[1]
 if parm == 'ALL':
  nrandom = 1000
 else:
  nrandom = int(sys.argv[1])
  
 dictcode = sys.argv[2]
 filein = sys.argv[3]  # xxx.txt
 filein1 = sys.argv[4] # name of index file
 fileout = sys.argv[5] # output file
 pagerecs = init_pagerecs(filein1)
 adjust_mw_pagerecs(pagerecs)
 entries = digentry.init(filein)

 #regex = get_dict_regex(dictcode)

 verseentries = init_verseentries(entries, dictcode)
 if parm == 'ALL':
  examples = get_examples_all(verseentries,nrandom,pagerecs,dictcode)
 else:
  examples = get_examples(verseentries,nrandom,pagerecs,dictcode)
  
 print(len(examples),"examples found")
 write_examples(fileout,examples)

