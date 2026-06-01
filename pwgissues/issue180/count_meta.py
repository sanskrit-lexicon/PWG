""" count_meta.py
 counts number of lines that start with <L>
 
"""
import sys,re
import codecs

def read_lines(filein):
 lines = []
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  for line in f:
   #lines.append(line.strip()) # changed at ap_1
   lines.append(line.rstrip('\r\n'))
 #print(f'{len(lines)} read from {filein}')
 return lines

if __name__=="__main__":
 filein = sys.argv[1]
 lines = read_lines(filein)
 nlines = len(lines)
 n = 0
 for line in lines:
  if line.startswith('<L>'):
   n = n + 1
 print(f'{filein} {nlines} lines, {n} metalines')
 
 
