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

def get_partitions(regexes,allrecs):
 matches = []
 imatches = []
 counts = {}
 for iregex,regex in enumerate(regexes):
  a,ia = match_recs(allrecs,regex)
  matches.append(a)
  imatches.append(ia)
  counts[iregex] = len(ia)
 return matches,imatches,counts

def print_regex_counts(title,regexraws,counts):
 outarr = []
 outarr.append(title)
 nregex = len(regexraws)
 ntot = 0
 for i in range(nregex):
  raw = regexraws[i]
  raw1 = raw.replace('\\','')
  n = counts[i]
  outarr.append('%5d %s' %(n,raw1))
  ntot = ntot + n
 outarr.append('%5d Total' %ntot)
 outarr.append('')
 #
 for out in outarr:
  print(out)
 
def findall_ls_entries(entries,regexes):
 nregex = len(regexes)
 recs = []
 counts = {}
 for i in range(nregex):
  counts[i] = 0
 for ientry,entry in enumerate(entries):
  text = ' '.join(entry.datalines)
  for iregex,regex in enumerate(regexes):
   a = re.findall(regex,text)
   for x in a:
    recs.append(x)
    counts[iregex] = counts[iregex] + 1
 return recs,counts

def get_standard_regexes(X):
 d1 = "([0-9]+)"
 d2 = "([0-9]+)"
 d3 = "([0-9]+)"
 # r"X (ABC|DEF)?"  syntax for optional matches
 # optional . OR optional fg. OR optional fgg.
 Y = "(\.| fg\.| fgg\.|\. fg\.|\. fgg\.)?"
 regexraws = [
  r'<ls>%s</ls>' % X,
  r'<ls>%s %s,%s,%s%s</ls>' %(X,d1,d2,d3,Y),
  r'<ls n="%s">%s,%s,%s%s</ls>' %(X,d1,d2,d3,Y),
  r'<ls n="%s %s,">%s,%s%s</ls>' %(X,d1,d2,d3,Y),
  r'<ls n="%s %s,%s,">%s%s</ls>' %(X,d1,d2,d3,Y),
 ]
 regexes = list(map(re.compile,regexraws))
 return regexes,regexraws

def get_partition_regexes(X):
 regexraws = [
  r'<ls>%s</ls>' % X,
  r'<ls>%s [0-9]' % X,
  r'<ls>%s [e]' % X,
  r'<ls>%s [^0-9e]' % X,
  
  r'<ls n="%s">' % X,
  r'<ls n="%s [0-9]' % X,
  r'<ls n="%s [e]' % X,
  r'<ls n="%s [^0-9e]' % X,
  r'<ls>%s\)' % X  # erroneous paren
 ]
 regexes = list(map(re.compile,regexraws))
 return regexes,regexraws

def match_recs(recs,regex):
 recs1 = []
 irecs1 = []
 for irec,rec in enumerate(recs):
  if re.search(regex,rec):
   irecs1.append(irec)
   recs1 = irecs1
 return recs1,irecs1
  
def check_disjoint(ab):
 # ab is a list of lists
 for i,a in enumerate(ab):
  for j,b in enumerate(ab):
   if j<=i:
    continue
   aset = set(a)
   bset = set(b)
   if not aset.isdisjoint(bset):
    cset = aset.intersection(bset)
    c = list(cset)
    print('%s is in group %s AND in group %s' %(c[0],i+1,j+1))
    exit(1)
 print('%s groups are pairwise disjoint' % len(ab))
 
def check_undetected(recs,matches,imatches):
 # matches and imatches are lists of lists.
 iall = set(range(0,len(recs)))
 union = set()
 for a in imatches: 
  for i in a:
   union.add(i)
 d = iall.difference(union)
 ans = []
 for i in d:
  rec = recs[i]
  ans.append(rec)

 #print('dbg:',ans[0:5])
 return ans

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
 def __init__(self,verse,pagerec):
  self.verse = verse
  self.pagerec = pagerec
  self.entry = None
  
def get_entry_for_examples(entries,examples):
 verses = [example.verse for example in examples]
 dexample = {}
 for example in examples:
  dexample[example.verse] = example
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
  verse = example.verse
  entry = example.entry
  if entry == None:
   print('No entry found for verse',v)
  else:
   print(example.verse, example.entry.metad['L'])
 exit(1)
 
def get_pagerec_from_verse(pagerecs,verse):
 for rec in pagerecs:
  if (rec.fromv <= verse) and (verse <= rec.tov):
   return rec
 print('get_pagerec_from_verse ERROR',verse)
 exit(1)

def main1():
 nrandom = int(sys.argv[1])
 filein = sys.argv[2]  # xxx.txt
 filevol = sys.argv[3] # volume number for Indisch index file
 filein1 = sys.argv[4] # name of Indisch index file
 fileout = sys.argv[5] # output file
 pagerecs = init_pagerecs(filein1,filevol)
 random_verses = randomize_pagerecs(pagerecs,nrandom)
 print(random_verses)
 examples = []
 for v in random_verses:
  pagerec = get_pagerec_from_verse(pagerecs,v)
  example = Example(v,pagerec)
  examples.append(example)
 print('ok so far')
 # now for dictionary  part
 entries = digentry.init(filein)
 get_entry_for_examples(entries,examples)
 print('2nd check point')

def init_verseentries(entries):
 regex_raw = r'<ls>Spr\. ([0-9]+)'
 regex = re.compile(regex_raw)
 d = {}
 for entry in entries:
  text = ' '.join(entry.datalines)
  for m in re.finditer(regex,text):
   verse = int(m.group(1))
   if verse not in d:
    d[verse] = []
   d[verse].append(entry)
 keys = list(d.keys())
 print('found %s distinct verses in kosha' % len(keys))
 return d

def get_pagerec(pagerecs,v):
 for rec in pagerecs:
  if (rec.fromv <= v) and (v <= rec.tov):
   return rec
 print('get_pagerec ERROR: cannot find verse',v)
 exit(1)
 
def get_examples(verseentries,nrandom,pagerecs):
 import random
 allkoshaverses = verseentries.keys()
 vmin = pagerecs[0].fromv
 vmax = pagerecs[-1].tov
 koshaverses = [v for v in allkoshaverses if ((vmin <= v) and (v <= vmax))]
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
  #assert (type(ventry1) == list) and (len(ventry1) == 1)
  #ventry = ventry1[0] # the element
  pagerec = get_pagerec(pagerecs,v)
  example = Example(v,pagerec)
  example.entry = ventry
  examples.append(example)
 return examples

def example_to_outrec(example):
 outarr = []
 verse  = example.verse
 pagerec = example.pagerec
 entry = example.entry
 line = pagerec.line
 outarr.append('verse %4d: %s' %(verse,line))
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
 
def main2():
 nrandom = int(sys.argv[1])
 filein = sys.argv[2]  # xxx.txt
 filevol = sys.argv[3] # volume number for Indisch index file
 filein1 = sys.argv[4] # name of Indisch index file
 fileout = sys.argv[5] # output file
 pagerecs = init_pagerecs(filein1,filevol)
 entries = digentry.init(filein)
 verseentries = init_verseentries(entries)
 examples = get_examples(verseentries,nrandom,pagerecs)
 print(len(examples),"examples found")
 write_examples(fileout,examples)
 

if __name__=="__main__":
 main2()
