# coding=utf-8
#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
# abbrv3.py
import re
import codecs
import datetime
import sys
from clean_proper import clean_one_properref  # Feb 16, 2016
def printtimestamp():
 return datetime.datetime.now()

def unused_occurrence():
 global cleanrefs, uniquerefs # Fetched from global
 abbstats = codecs.open('abbrvoutput/sortedcrefs.txt','w','utf-8') # Sorted according to occurrences first and alphabetically second.
 occurlist = []
 onlyls = [a for (a,b,c,d) in cleanrefs]
 uniquerefs.sort()
 ur1 = uniquerefs[:]
 for (a,b,c,d) in cleanrefs:
  if a in ur1:
   count = onlyls.count(a)
   occurlist.append((a,b,c,d,count))
   ur1.remove(a)
 occurlist.sort(key=lambda x: (x[4],x[0]))
 for (a,b,c,d,e) in occurlist:
  abbstats.write(a+"@"+b+"@"+c+"@"+d+"@"+str(e)+"\n")
 abbstats.close()
 

def occurrence(properrefs):
 # Replaces 'ur1' by a dictionary
 cleanrefs = []
 print "computing cleanrefs begins at",printtimestamp()
 for (a,b,c,d) in properrefs:
  clean=clean_one_properref(a,b,c,d)
  cleanrefs.append((clean,b,c,d))
 print "computing cleanrefs ends at",printtimestamp()

 cl1 = []
 ur1 = {}
 for (p,q,r,s) in cleanrefs:
  #if p not in ur1 and re.sub('[.]S$','',p) not in ur1:
  # Dec 31, 2015 (ejf). Removed the 'S' logic, as it
  # inhibits matching of 'KAP.S', for instance.
  if p not in ur1 :
   cl1.append((p,q,r,s))
   #ur1.append(p)
   ur1[p] = 0
  ur1[p] = ur1[p] + 1
 print "cl1 compute ends at",printtimestamp()
 occurlist = []
 for (p,q,r,s) in cl1:
  c = ur1[p]  # count
  occurlist.append((p,q,r,s,c))
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
 occurlist.sort(key=lambda x: (x[4],x[0]))
 print "Completed storing occur references at ", printtimestamp()
 with codecs.open(fileoccur,"w","utf-8") as f:
  print len(occurlist),"records written to",fileoccur
  for (p,q,r,s,c) in occurlist:
   y = (p,q,r,s,str(c)) # c is an int
   out = '@'.join(y)
   f.write(out+'\n')
