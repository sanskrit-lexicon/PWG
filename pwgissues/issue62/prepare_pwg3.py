# coding=utf-8
""" prepare_pwg3.py
"""
from __future__ import print_function
import sys, re, codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

def get_unique_strings(lines):
 ans = []  # list of strings returned
 n = 0
 regex = r'<ls.*?</ls>'
 for line in lines:
  n = n + 1
  m = re.search(regex,line)
  if m != None:
   s = m.group(0)
   # exclude duplicates
   if s not in ans:
    ans.append(s)
 print(len(ans),"unique strings found")
 return ans

def mark_strings(lines,strings):
 newlines = []
 markc = '@'  # this character
 print('marking strings with "%s"' % markc)
 n = 0 # number of lines with at least one string marked
 for line in lines:
  newline = line
  for s in strings:
   if s in newline:
    # '@' does not occur in
    newline = newline.replace(s,markc+s)
  newlines.append(newline)
  if newline != line:
   n = n + 1
 print(n,'lines marked')
 return newlines

if __name__=="__main__":
 filein = sys.argv[1]  # old kosha
 filein1 = sys.argv[2] # source of strings used to modify kosha
 fileout = sys.argv[3] # revised kosha
 lines = read_lines(filein)
 lines1 = read_lines(filein1)
 strings = get_unique_strings(lines1)
 newlines = mark_strings(lines,strings)
 write_lines(fileout,newlines)
 
