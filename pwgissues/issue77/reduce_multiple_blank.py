#-*- coding:utf-8 -*-
"""reduce_multiple_blank.py

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


def reduce_multiple_blank(lines):
 # remove [Pagev-xxxx] lines between <LEND> and <L>
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
  if metaline != None:
   # keep line in body.
   newlines.append(line)
   continue
  # metaline == None
  nextline = lines[iline + 1]
  if (line == '') and (nextline == ''):
   nchg = nchg + 1
   continue
  else:
   # keep the line
   newlines.append(line)
 print('drop %s extra blank lines' % nchg)
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
 
 newlines = reduce_multiple_blank(lines) 
 # insert blank line between <LEND> and <L>
 write(fileout,newlines)
 
