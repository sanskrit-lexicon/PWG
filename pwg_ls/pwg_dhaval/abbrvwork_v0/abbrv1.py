# coding=utf-8
#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
import re
import codecs
import datetime
import sys
from clean_proper import clean_one_properref  # Feb 16, 2016
def printtimestamp():
 return datetime.datetime.now()


def segregatepurenumbers(wholeabbrvlist):
 properrefs = []
 numrefs=[]
 for (a,b,c,d) in wholeabbrvlist:
  #if a is None:
  # a = ""
  flag=False
  if re.match(r'^([^a-zA-Z]*)$',a): # Removing improper reference tags.
   flag=True
  elif re.match(r'^([0-9a-z()&.,]+)$',a): # Same
   flag=True
  elif re.match(r'^[0-9]',a): # Jan 19, 2016. ejf. Start with digit
   flag=True
  if flag:
   numrefs.append((a,b,c,d))
  else:
   properrefs.append((a,b,c,d)) # Append to the list
 return (numrefs,properrefs) # Return both lists


if __name__ == "__main__":
 filein = sys.argv[1]  # abbrvoutput/abbrvlist.txt
 filenum = sys.argv[2] # abbrvoutput/purenumberabbrvlist.txt
 fileprop = sys.argv[3] # abbrvoutput/properrefs.txt
 # read and parse filein
 with codecs.open(filein,"r","utf-8") as f:
  abbrvlist = [x.rstrip('\r\n').split('@') for x in f]
 print len(abbrvlist)
 print "Segregating references with only numbers to abbrvoutput/purenumberabbrvlist.txt and "
 print "proper references to abbrvoutput/properrefs.txt at", printtimestamp()
 print
 (numrefs,properrefs) = segregatepurenumbers(abbrvlist)
 with codecs.open(filenum,"w","utf-8") as f:
  print len(numrefs),"records written to",filenum
  for x in numrefs:
   out = '@'.join(x)
   f.write(out+'\n')
 with codecs.open(fileprop,"w","utf-8") as f:
  print len(properrefs),"records written to",fileprop
  for x in properrefs:
   out = '@'.join(x)
   f.write(out+'\n')

 print "Completed segregating references at ", printtimestamp()
 print
