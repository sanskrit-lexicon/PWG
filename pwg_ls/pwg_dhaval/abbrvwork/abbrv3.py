# coding=utf-8
#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
# abbrv3.py
import re
import codecs
import datetime
import sys
# use transcoder from another directory
sys.path.append('../../pwgbib/digitization')
import transcoder
# we must use a different as_roman transcoder here than was
# used in pwgbib/digitization
# Specifically, for 'C2'
#transcoder.transcoder_set_dir('../../pwgbib/digitization')
transcoder.transcoder_set_dir('')

from clean_proper import clean_one_properref  # Feb 16, 2016
def printtimestamp():
 return datetime.datetime.now()

def abbrv_transcode(p):
 tranin = 'as'
 tranout = 'roman1'
 proman = transcoder.transcoder_processString(p,tranin,tranout)
 # correct some errors:
 proman = proman.replace('Yourn','Journ')
 return proman

def occurrence(properrefs):
 # Replaces 'ur1' by a dictionary
 cleanrefs = []
 print "computing cleanrefs begins at",printtimestamp()
 for (a,b,d) in properrefs:
  clean=clean_one_properref(a,b,d)
  cleanrefs.append((clean,b,d)) 
 print "computing cleanrefs ends at",printtimestamp()

 cl1 = []
 ur1 = {}
 for (p,q,s) in cleanrefs:
  #if p not in ur1 and re.sub('[.]S$','',p) not in ur1:
  # Dec 31, 2015 (ejf). Removed the 'S' logic, as it
  # inhibits matching of 'KAP.S', for instance.
  if p not in ur1 :
   cl1.append((p,q,s))
   #ur1.append(p)
   ur1[p] = 0
  ur1[p] = ur1[p] + 1
 print "cl1 compute ends at",printtimestamp()
 occurlist = []
 for (p,q,s) in cl1:
  c = ur1[p]  # count
  occurlist.append((p,q,s,c))
 return occurlist


if __name__ == "__main__":
 filein = sys.argv[1]  # abbrvoutput/properrefs.txt
 fileoccur = sys.argv[2] # abbrvoutput/sortedcrefs.txt
 # read and parse filein
 with codecs.open(filein,"r","utf-8") as f:
  properrefs = [x.rstrip('\r\n').split('@') for x in f]
 print len(properrefs)

 print "Removing numbers from properrefs , and counting ", printtimestamp()
 print
 occurlist = occurrence(properrefs)
 #occurlist.sort(key=lambda x: (x[3],x[0]))
 occurlist.sort(key=lambda x: (x[0],x[3]))
 print "Completed storing occur references at ", printtimestamp()
 with codecs.open(fileoccur,"w","utf-8") as f:
  print len(occurlist),"records written to",fileoccur
  for (p,q,s,c) in occurlist:
   proman = abbrv_transcode(p)
   # construct array of fields for output
   y = (proman,p,str(c)) # c is an int
   out = '@'.join(y)
   f.write(out+'\n')
