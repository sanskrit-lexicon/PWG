""" count_ab.py
 Find occurrence of all instances of <ab>X</ab>
 
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

def gather(lines):
 d = {}
 regex = re.compile(r'<ab n="(.*?)">(.*?)</ab>')
 metaline = None
 for line in lines:
  if line.startswith('<L>'):
   metaline = True
   continue
  if line.startswith('<LEND>'):
   metaline = False
   continue
  if not metaline:
   continue
  for m in re.finditer(regex,line):
   e1 = m.group(1)
   e2 = m.group(2)
   e = (e2,e1)
   if e not in d:
    d[e] = 0
   d[e] = d[e] + 1
 return d

def get_outarr(keysd):
 # present results alphabetical order
 keys = sorted(keysd.keys(), key = lambda x: x[1].lower())
 outarr = []
 for tag in keys:
  (e2,e1) = tag
  out = '(%s:%s)\t%s' %(e2,e1,keysd[tag])
  outarr.append(out)
 return outarr

if __name__=="__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2] # output path
 lines = read_lines(filein)
 keysd = gather(lines)  # dictionary with counts
 outarr = get_outarr(keysd)
 write_lines(fileout,outarr)
