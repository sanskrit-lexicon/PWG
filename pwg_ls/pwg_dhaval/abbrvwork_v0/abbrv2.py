# coding=utf-8
#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
# abbrv2.py
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
   ur1[p] = True
 print "cl1 compute ends at",printtimestamp()
 uniquerefs = ur1 # Return only the unique references.
 #uniquerefs.sort() # Sort alphabetically.
 #for i in xrange(len(cl1)):
 # cleanfile.write(cl1[i][0]+"@"+cl1[i][1]+"@"+cl1[i][2]+"@"+cl1[i][3]+"\n") # Write to cleanrefs.txt
 #cleanfile.close()
 #return (uniquerefs, cleanrefs) # Return a tuple with uniquerefs and cleanrefs as members. Both have their utility.
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
