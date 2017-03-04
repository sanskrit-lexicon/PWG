# coding=utf-8
#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
# abbrv2.py
# 02-28-2017. This version also keeps the original LS field,
# as well as the cleaned LS field.
import re
import codecs
import datetime
import sys
from clean_proper import clean_one_properref  # Feb 16, 2016

def printtimestamp():
# Function to return timestamp
 return datetime.datetime.now()

def removenumbers(properrefs):
 # Replaces 'ur1' by a dictionary
 cleanrefs = []
 print "computing cleanrefs begins at",printtimestamp()
 for (a,b,d) in properrefs:
  clean=clean_one_properref(a,b,d)
  cleanrefs.append((clean,a,b,d))  # keep 'a' as well as 'clean'
 print "computing cleanrefs ends at",printtimestamp()

 cl1 = []
 ur1 = {}
 for x in cleanrefs:
  #if p not in ur1 and re.sub('[.]S$','',p) not in ur1:
  # Dec 31, 2015 (ejf). Removed the 'S' logic, as it
  # inhibits matching of 'KAP.S', for instance.
  p = x[0] # cleaned abbreviation
  if p not in ur1 :
   cl1.append(x)
   #ur1.append(p)
   ur1[p] = True
 print "cl1 compute ends at",printtimestamp()
 uniquerefs = ur1 # Return only the unique references.

 return cl1  # 
if __name__ == "__main__":
 filein = sys.argv[1]  # abbrvoutput/properrefs.txt
 fileclean = sys.argv[2] # abbrvoutput/cleanrefs.txt
 # read and parse filein
 with codecs.open(filein,"r","utf-8") as f:
  properrefs = [x.rstrip('\r\n').split('@') for x in f]
 print len(properrefs)

 print "Removing numbers from properrefs and storing only names of works to",fileclean," at ", printtimestamp()
 print
 #(uniquerefs, cleanrefs) = removenumbers(properrefs)
 cl1 = removenumbers(properrefs)
 print "Completed storing clean references at ", printtimestamp()
 with codecs.open(fileclean,"w","utf-8") as f:
  print len(cl1),"records written to",fileclean
  for x in cl1:
   out = '@'.join(x)
   f.write(out+'\n')
