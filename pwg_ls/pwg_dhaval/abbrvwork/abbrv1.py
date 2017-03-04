# coding=utf-8
#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
import re
import codecs
import datetime
import sys
def printtimestamp():
 return datetime.datetime.now()

def segregatepurenumbers(wholeabbrvlist):
 properrefs = []
 numrefs=[]
 roman_numeral_starts=(
  'LV','LX',
  'II','IL','IV','IX',
  'VI,','VII',
  'X'
 )
 for (a,b,d) in wholeabbrvlist:
  # flag is True when improperref, else it is properref
  if a.startswith('an.'):
   # this i
   flag=False  
  elif not re.match(r'^[A-Z]',a): 
   #  require first character of LS  be a capital letter
   # This adds about 2000 cases to 
   flag=True
  elif a.startswith(roman_numeral_starts):
   # exclude roman-numerals
   flag=True
  else:
   flag=False
  if flag:
   numrefs.append((a,b,d))
  else:
   properrefs.append((a,b,d)) # Append to the list
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
