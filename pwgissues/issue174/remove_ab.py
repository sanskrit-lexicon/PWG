""" remove_ab.py
 
"""
import sys,re
import codecs
# import os.path,time

def read_lines(filein):
 lines = []
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  for line in f:
   #lines.append(line.strip()) # changed at ap_1
   lines.append(line.rstrip('\r\n'))
 print(f'{len(lines)} read from {filein}')
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,'w','utf-8') as f:
  for out in outarr:
   f.write("%s\n" % out)
 print(f'{len(outarr)} lines written to {fileout}')

def remove_ab(lines):
 newlines = []
 regex = re.compile(r'<ab n="(.*?)">(.*?)</ab>')
 metaline = None
 n = 0 # number of lines changed
 for line in lines:
  if line.startswith('<L>'):
   metaline = True
   newlines.append(line)
   continue
  if line.startswith('<LEND>'):
   newlines.append(line)
   continue
  if not metaline:
   newlines.append(line)
   continue
  newline = line
  newline = newline.replace('<ab>','')
  newline = newline.replace('</ab>','')
  newline = re.sub('<ab.*?>','',newline)
  if newline != line:
   n = n + 1
  newlines.append(newline)
 return newlines,n

if __name__=="__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2] # output path
 lines = read_lines(filein)
 newlines,nchg = remove_ab(lines)
 print(f'{nchg} lines changed')
 write_lines(fileout,newlines)
