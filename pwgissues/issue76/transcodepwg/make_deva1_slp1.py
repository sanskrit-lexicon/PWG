#-*- coding:utf-8 -*-
"""make_deva1_slp1.py

"""
from __future__ import print_function
import sys, re,codecs

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

class Replace:
 def __init__(self,old,new):
  self.old = old
  self.new = new
  self.count = 0

replacements_data = [
  ('u0951' , 'ua8eb'),
  ('u1ce0' , 'u0951'),
 ]

def init_Replacements():
 recs = []
 for old,new in replacements_data:
  rec = Replace(old,new)
  recs.append(rec)
 return recs

# res = [i for i in range(len(test_str)) if test_str.startswith(test_sub, i)]
def convert_line(line,recs):
 newline = line
 for rec in recs:
  #a = re.findall(rec.old,newline)  # complication when '(' is in rec.old
  nline = len(newline)
  a = res = [i for i in range(nline) if newline.startswith(rec.old, i)]
  n = len(a)
  if n == 0:
   continue
  rec.count = rec.count + n
  newline = newline.replace(rec.old,rec.new)
 return newline

def convert_lines(lines,recs):
 newlines = []
 for line in lines:
  newline = convert_line(line,recs)
  newlines.append(newline)
 return newlines

def test():
 slp1 = 'rAARa/'
 deva = transcode(slp1,'slp1','deva')
 print('test: {#%s#}' % deva)
 exit(1)

def write_counts(fileout,recs):
 outarr = []
 for rec in recs:
  out = '%02d: "%s" -> "%s"' %(rec.count,rec.old,rec.new)
  outarr.append(out)
 write_lines(fileout1,outarr)

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx
 fileout = sys.argv[2] # 
 lines = read_lines(filein)
 recs = init_Replacements()
 newlines = convert_lines(lines,recs)
 write_lines(fileout,newlines)
 fileout1 = 'temp_debug.txt'
 write_counts(fileout1,recs)
 #write_lines(fileout1,outarr)
