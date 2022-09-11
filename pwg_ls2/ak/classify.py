#-*- coding:utf-8 -*-
"""classify.py for AK.
"""
import sys,re,codecs

sys.stdout.reconfigure(encoding='utf-8') 


class LSChange(object):
 def __init__(self,metaline,iline,line,newline):
  self.metaline = metaline
  self.iline = iline
  self.line = line
  self.newline = newline

def replace_line_0(line):
 # sort of irregular. Will be changed later.
 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  if parmstr == '':
   return all
  m1 = re.search(r'^ [0-9,. ]*(v\. l\.)?[.,]?$',parmstr)
  if m1 == None:
   return '**'+all
  return all
 
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

rnum = '[0-9]+'
rnum4 = '%s, %s, %s, %s\.' %(rnum,rnum,rnum,rnum)
def replace_line_1a(line):
 # sort of irregular. Will be changed later.
 regex = '^ (%s) (%s)$' % (rnum4,rnum4)
 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1)
  p2 = m1.group(2)
  new = '<ls>AK. %s</ls> <ls n="AK.">%s</ls>' % (p1,p2)
  return new

 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

replacements = {
 '0': replace_line_0,
 '1a': replace_line_1a,
 }

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
 return lstype

def classify_2(ls):
 m = re.search(r'^<ls n="AK\.(.*?)">(.*)</ls>$',ls)
 if m == None:
  print('classify_2 error: ',ls)
  exit(1)
 parmstr1 = m.group(1)
 parmstr2 = m.group(2)
 if parmstr1 == '':
  parmstr = parmstr2
 else:
  parmstr = parmstr1 + ' ' + parmstr2
 words = parm_words(parmstr)
 wordtypes = [word_type(w) for w in words]
 lstype = ' '.join(wordtypes)
 return lstype

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
   rec = (instance,metaline)
   c = classify_1(instance)
   if c not in d:
    d[c] = []
   d[c].append(rec)
  #
  instances = re.findall(r'<ls n="AK\..*?</ls>',line)
  for instance in instances:
   rec = (instance,metaline)
   c = classify_2(instance)
   if c not in d:
    d[c] = []
   d[c].append(rec)
   
 parmtypes = d.keys()
 print(len(parmtypes),'parameter types found')
 return d

def write_lschanges(fileout,d):
 keys = d.keys()
 keys1 = sorted(keys,key = lambda c: len(d[c]),reverse = True)
 ntot = 0
 outrecs = []
 outarr = []
 outarr.append('; =======================================================' )
 outarr.append('; %s (%s)' %(fileout,len(keys)))
 outarr.append('; =======================================================' )
 outrecs.append(outarr)
 for c in keys1:
  outarr = []
  outarr.append('; -------------------------------------------------------' )
  instances = d[c]
  n = len(instances)
  ntot = ntot + n
  outarr.append('; %s (%s)' % (c,n))
  for rec in instances:
   # rec = (ls-instance, metaline)
   instance,metaline = rec
   meta = re.sub(r'<k2>.*$','',metaline)
   i = instance.ljust(40)
   outarr.append('%s   %s' % (i,meta))
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print('%s instances in %s categories written to %s' %
       (ntot,len(keys),fileout))
 
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
 fileout1 = sys.argv[2] # instances with parsed parms
 fileout2 = sys.argv[3] # instances with unparsed parms
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 d = classification(lines) # also, updates tip.changes
 d1,d2 = done_notdone(d) # separate 
 write_lschanges(fileout1,d1)
 write_lschanges(fileout2,d2)
 
