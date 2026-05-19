""" abdiff.py
 abbreviation differences in two files
 
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

def init_col(lines,icol):
 ans = set()  # set
 for line in lines:
  parts = line.split('\t')
  part = parts[icol]
  if part in ans:
   print('duplicate',part)
  ans.add(part)
 return ans

if __name__=="__main__":
 filein1 = sys.argv[1] # first abbreviation file
 filein2 = sys.argv[2] # 2nd abbreviation file
 fileout = sys.argv[3] # output path
 icol = 0
 lines1 = read_lines(filein1)
 s1 = init_col(lines1,icol)
 lines2 = read_lines(filein2)
 s2 = init_col(lines2,icol)
 s = s1.union(s2)
 outarr = []
 outarr.append(f'col1: abbreviation')
 outarr.append(f'col2: {filein1}')
 outarr.append(f'col3: {filein2}')
 print(len(s1),len(s2),len(s))
 for a in s:
  v1 = 'NO'
  v2 = 'NO'
  if a in s1:
   v1 = 'YES'
  if a in s2:
   v2 = 'YES'
  outarr.append(f'{a}\t{v1}\t{v2}')
 write_lines(fileout,outarr)
