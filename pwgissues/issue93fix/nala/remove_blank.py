#-*- coding:utf-8 -*-
"""remove_blank.py
  remove blank lines within body 
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 print("%s lines read from %s" % (len(lines),filein))
 return lines

def adjust(lines):
 # remove blank lines in body
 newlines = []  # returned
 metaline = None
 nchg = 0
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   metaline = line
   newlines.append(line)
   continue
  if line.startswith('<LEND>'):
   metaline = None
   newlines.append('<LEND>')
   continue
  if metaline == None:
   newlines.append(line)
   continue
  # line in body.
  if line.strip() == '':
   # skip this line
   nchg = nchg + 1
   continue
  # non-empty line in entry body
  newlines.append(line)
 print('adjust: %s empty body lines dropped' % nchg)
 return newlines

def write(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line + '\n')
 print(len(lines),"written to",fileout)
 
if __name__=="__main__": 
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # revised xxx.txt
 lines = read_lines(filein)
 newlines = adjust(lines)
 write(fileout,newlines)

 
