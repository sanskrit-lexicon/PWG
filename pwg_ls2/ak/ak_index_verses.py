#-*- coding:utf-8 -*-
"""ak_index_verses.py for AK.
"""
import sys,re,codecs

class Index(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  line = line.rstrip()
  self.line = line
  m = re.search(r'^([0-9][0-9][0-9]) (.*)$',line)
  if m == None:
   print('Index parse error:',line)
   exit(1)
  self.page = int(m.group(1))
  data = m.group(2)
  m = re.search(r'^Book ([0-9]+)\. Chapter ([0-9]+)\. Sect\. ([0-9]+) (.*)$',data)
  m1 = re.search(r'^Book ([0-9]+)\. Chapter ([0-9]+)\. (.*)$',data)  
  if m:
   self.book = int(m.group(1))
   self.chapter = int(m.group(2))
   self.section = int(m.group(3))
   self.range = m.group(4)
  elif m1:
   self.book = int(m1.group(1))
   self.chapter = int(m1.group(2))
   self.section = None
   self.range = m1.group(3)
  else:
   print('Index. Parse Error 2',line)
   exit(1)
  # parse range. two forms
  # N1-N2
  # N1/X-N2
  x1,x2 = self.range.split('-') # strings
  self.v1 = int(x1.split('/')[0])
  self.v2 = int(x2)
                  
def init_indexes(filein):
 recs = []
 with codecs.open(filein,"r","utf-8") as f:
  for line in f:
   if line.startswith(';'):
    continue
   rec = Index(line)
   recs.append(rec)
 print(len(recs),"records read from",filein)
 return recs

def index_refs(index):
 ans = []
 p = index.page
 b = index.book
 c = index.chapter
 v1 = index.v1
 v2 = index.v2
 if index.section == None:
  for v in range(v1,v2+1):  # include v2
   ans.append(((b,c,v),p))
 else:
  s = index.section
  for v in range(v1,v2+1):  # include v2
   ans.append(((b,c,s,v),p))
 return ans

def generate_refs(indexes):
 refs = []  # list of tuples of integers
 for index in indexes:
  for ref in index_refs(index):
   refs.append(ref)
 return refs

def write_refs(fileout,refs):
 outarr = []
 outarr.append('#-*- coding:utf-8 -*-')
 outarr.append('ak_index_verses_set = { # a set')
 for ref,page in refs:
  outarr.append(' %s, # %s' % (str(ref), page))
 outarr.append('}')
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(refs),"refs written to",fileout)
 
if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # instances with parsed parms
 indexes = init_indexes(filein)
 refs = generate_refs(indexes)
 write_refs(fileout,refs)
 
