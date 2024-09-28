#-*- coding:utf-8 -*-
"""pwg_transcode.py
"""
from __future__ import print_function
import sys, re,codecs
import transcoder

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 print(len(lines),"lines read from",filein)
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"lines written to",fileout)

def print_unicode(u):
 """ Sample output:
x= a/MSa—BU/
0905 | अ | DEVANAGARI LETTER A
0951 | ॑ | DEVANAGARI STRESS SIGN UDATTA
0902 | ं | DEVANAGARI SIGN ANUSVARA
0936 | श | DEVANAGARI LETTER SHA
2014 | — | EM DASH
092D | भ | DEVANAGARI LETTER BHA
0942 | ू | DEVANAGARI VOWEL SIGN UU
0951 | ॑ | DEVANAGARI STRESS SIGN UDATTA
 """
 import unicodedata
 outarr = []
 for c in u:
  name = unicodedata.name(c)
  icode = ord(c)
  a = f"{icode:04X} | {c} | {name}"
  outarr.append(a)
 return outarr

def transcode(x,tranin,tranout):
 y = transcoder.transcoder_processString(x,tranin,tranout)
 return y

def convert_line(line,tranin,tranout,outarr):
 # convert text  in '{#X#}' -> {#Y#}
 #outarr = []
 def f(m):
  x = m.group(1)
  y = transcode(x,tranin,tranout)
  ans = '{#%s#}' % y
  #return ans # comment out this line to 
  # check invertibility 
  x1 = transcode(y,tranout,tranin)
  if x1 != x:
   y1 = transcode(x1,tranin,tranout)
   outarr.append(' x=%s,  y=%s' %(x,y))
   a = print_unicode(x)
   for a1 in a:
    outarr.append(a1)
   outarr.append('x1=%s, y1=%s' %(x1,y1))
   a = print_unicode(x1)
   for a1 in a:
    outarr.append(a1)
  return ans
 
 regex = '{#(.*?)#}'
 lineout = re.sub(regex,f,line)
 return lineout

def convert_lines(lines,tranin,tranout,outarr):
 newlines = []
 for line in lines:
  newline = convert_line(line,tranin,tranout,outarr)
  newlines.append(newline)
 return newlines

def test1():
 slp1s = ('aM/Sa', 'a/MSa', 'kAM/sya', 'kA/Msya')
 devas = []
 outarr=[]
 for slp1 in slp1s:
  deva = transcode(slp1,'slp1','deva1')
  devas.append(deva)
  outarr.append('test: %s: {#%s#}' % (slp1,deva))
  a = print_unicode(deva)
  for a1 in a:
   outarr.append(a1)
 fileout = 'temp_debug.txt'
 write_lines(fileout,outarr)
 exit(1)


def test():
 devas = ['अं꣫श']
 outarr=[]
 slp1s = []
 for deva in devas:
  slp1 = transcode(deva,'deva1','slp1')
  slp1s.append(slp1)
  outarr.append('test: %s: {#%s#}' % (deva,slp1))
  a = print_unicode(deva)
  for a1 in a:
   outarr.append(a1)
 slp1s = ['a
 fileout = 'temp_debug.txt'
 write_lines(fileout,outarr)
 exit(1)

if __name__=="__main__":
 transcoderdir = sys.argv[1]
 transcoder.transcoder_set_dir(transcoderdir)
 test()
