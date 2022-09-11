#-*- coding:utf-8 -*-
"""ak_verse_change.py
"""
import sys,re,codecs
from ak_index_verses_set import ak_index_verses_set
#print(len(ak_index_verses_set))

sys.stdout.reconfigure(encoding='utf-8') 

def parm_words(parmstr):
 parmstr1 = parmstr.replace('v. l.','v._l.')
 # parenthesized expressions
 def f(m):
  old = m.group(0)
  new = old.replace(' ','_')
  return new
 parmstr1a = re.sub(r'\(.*?\)',f,parmstr1)
 if parmstr1a != parmstr1:
  #print('parm_words chk: "%s" -> "%s"' %(parmstr1,parmstr1a))
  parmstr1 = parmstr1a
  #exit(1)
 if parmstr1.startswith(' '):
  parmstr1 = parmstr1[1:] # drop initial space
 words = parmstr1.split(' ')
 return words

word_type_regexes = [
  # regex: name
  (r'^[0-9]+\.$',  'N.'),
  (r'^[0-9]+\,$',  'N,'),
  (r'^[0-9]+$',  'N'),
  (r'^v\._l\.$',  'vl'), # varia-licta
  (r'^$',  'NP'), # no parms
  (r'^fg\.$',  'fg'),
  (r'^\(.*\)$','pe'),
  (r'^.*$',  '?'), # not elsewhere classified 
 ]
def word_type(word):
 ans = None
 for regex,w_type in word_type_regexes:
  if re.search(regex,word):
   ans = w_type
   break
 #if word.startswith('('):
 # print('word_type %s = %s' %(word, ans))
 # exit(1)
 return ans

def classify_1(ls):
 m = re.search(r'^<ls>AK\.(.*)</ls>$',ls)
 parmstr = m.group(1)
 words = parm_words(parmstr)
 wordtypes = [word_type(w) for w in words]
 lstype = ' '.join(wordtypes)
 if False:
  print('words=',words)
  print('parmstr=',parmstr)
  exit(1)
 return lstype,parmstr

def classify_2(ls):
 m = re.search(r'^<ls n="AK\.(.*?)">(.*)</ls>$',ls)
 parmstr1 = m.group(1)
 parmstr2 = m.group(2)
 if parmstr1 == '':
  parmstr = parmstr2
 else:
  parmstr = parmstr1 + ' ' + parmstr2
 words = parm_words(parmstr)
 wordtypes = [word_type(w) for w in words]
 lstype = ' '.join(wordtypes)
 return lstype,parmstr

def classification(lines):
 d = {} # 
 lschanges = []
 metaline = None
 imetaline1 = None
 page = None
 for iline,line in enumerate(lines):
  line = line.rstrip('\r\n')
  if line == '':
   continue
  if line.startswith('<L>'):
   metaline = line
   imetaline1 = iline+1
   continue
  if line == '<LEND>':
   metaline = None
   imetaline = None
   continue
  if line.startswith('[Page'):
   page = line
   continue
  instances = re.findall(r'<ls>AK\..*?</ls>',line)
  for instance in instances:
   c,parmstr = classify_1(instance)
   rec = (instance,metaline,parmstr,iline+1,line)
   if c not in d:
    d[c] = []
   d[c].append(rec)
  #
  instances = re.findall(r'<ls n="AK\..*?</ls>',line)
  for instance in instances:
   c,parmstr = classify_2(instance)
   rec = (instance,metaline,parmstr,iline+1,line)
   if c not in d:
    d[c] = []
   d[c].append(rec)
   
 parmtypes = d.keys()
 print(len(parmtypes),'parameter types found')
 return d

def get_parm_tuple(parmstr):
 # " 3, 5, 1."  -> (3,5,1)
 x = parmstr.replace('fg.','')
 x = x.replace(r'vl.','')
 x = re.sub(r' +','',x)
 x = x.replace('.','')
 words = []
 for w in x.split(','):
  if w != 'vl':
   words.append(w)
 try:
  parmtuple = tuple([int(w) for w in words])
 except:
  print('parmstr=',parmstr,words)
  exit(1)
 return parmtuple

def convert_dparmstr(d):
 e = {}
 for c in d.keys():
  for rec in d[c]:
   (instance,metaline,parmstr,lnum,line) = rec
   if parmstr == '': # exclude <ls>AK.</ls>
    continue
   #print('parmstr="%s"' %parmstr)
   parmtuple = get_parm_tuple(parmstr)
   #print('parmtuple=',parmtuple)
   #exit(1)
   if parmtuple not in e:
    e[parmtuple] = []
   e[parmtuple].append(rec)
 return e

def write_doneparms(fileout,d):
 #keys = d.keys()
 #keys1 = sorted(keys,key = lambda c: len(d[c]),reverse = True)
 dparms = convert_dparmstr(d)
 # add empty records for keys 'not used'
 for parmtuple in ak_index_verses_set:
  if parmtuple not in dparms:
   dparms[parmtuple] = []
 keys = dparms.keys()  # integer tuples
 print(len(keys),"keys found")
 keys1 = sorted(keys)
 ntot = 0
 outrecs = []
 outarr = []
 lnumsd = {} # lnum used. To avoid dupliclates
 outarr.append('; =======================================================' )
 outarr.append('; %s (%s)' %(fileout,len(keys)))
 outarr.append('; =======================================================' )

 for parmtuple in keys1:
  parmknown = '-'
  if parmtuple in ak_index_verses_set:
   parmknown = '+'
  
  rec = dparms[parmtuple]
  numinstance = len(rec)
  outarr.append('%s %s %s' %(parmknown,parmtuple,numinstance))
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')
 print(len(keys1),"records written to",fileout)
 
# parameter patterns that are 'done'
donec = {'NP',
         'N, N, N, N.',
         'N, N, N.',
         'N, N, N, N',
         'N, N, N',
         'N, N, N, N, vl',
         'N, N, N, vl',
         'N, N, N, N. fg',
         }
def done_notdone(d):
 d1 = {}
 d2 = {}
 for c in d:
  if c in donec:
   d1[c] = d[c]
  else:
   d2[c] = d[c]
 return d1,d2

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # instances with parsed parms
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 d = classification(lines) # also, updates tip.changes
 d1,d2 = done_notdone(d) # separate 
 write_doneparms(fileout,d1)
 
