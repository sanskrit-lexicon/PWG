""" dropdouble_LBC.py
 
"""
import sys,re
import codecs
LBC = ' 🞄'  # line-break replaces certain '\n'

def read_lines(filein):
 lines = []
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  for line in f:
   lines.append(line.rstrip('\r\n'))
 print(f'{len(lines)} lines read from {filein}')
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,'w','utf-8') as f:
  for out in outarr:
   f.write("%s\n" % out)
 print(f'{len(outarr)} lines written to {fileout}')

def adjust_lines(lines):
 newlines = []
 inentry = False
 replace_old = f'{LBC}{LBC}'
 replace_new = f'{LBC}'
 n = 0 # of lines changed
 for line in lines:
  newline = line
  if not line.startswith('<LEND>'):
   newline = line.replace(replace_old,replace_new)
  elif not ('VERBESSERUNGEN' in line):
    newline = line.replace(replace_old,replace_new)
  if newline != line:
   n = n + 1
  newlines.append(newline)
 print(f'{n} lines changed')
 return newlines

if __name__=="__main__":
 filein = sys.argv[1]  # base
 fileout = sys.argv[2] # adjusted base
 
 lines = read_lines(filein)

 lines1 = adjust_lines(lines)
 write_lines(fileout,lines1)
