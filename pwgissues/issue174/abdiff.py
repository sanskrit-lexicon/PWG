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

class AbbrevCount:
 def __init__(self,line):
  parts = line.split('\t')
  self.abbrev = parts[0]
  self.count = int(parts[1])
  
def init_abbrev(lines):
 recs = [] # array of AbbrevCount objects
 d = {} # check for duplicates
 for line in lines:
  rec = AbbrevCount(line)
  if rec.abbrev in d:
   print(f'Duplicate abbrev: {line}')
  else:
   d[rec.abbrev] = rec
   recs.append(rec)
 return recs,d

def get_outarr(abbrevs0,d1,d2):
 abbrevs = sorted(abbrevs0,key = lambda x: x.lower())
 outarr = []
 for a in abbrevs:
  v1 = -1
  v2 = -1
  if a in d1:
   v1 = d1[a].count
  if a in s2:
   v2 = d2[a].count
  outarr.append(f'{a}\t{v1}\t{v2}')
 return outarr
if __name__=="__main__":
 filein1 = sys.argv[1] # first abbreviation-count file
 filein2 = sys.argv[2] # 2nd abbreviation-count file
 fileout = sys.argv[3] # output path
 lines1 = read_lines(filein1)
 recs1,d1 = init_abbrev(lines1)
 lines2 = read_lines(filein2)
 recs2,d2 = init_abbrev(lines2)
 # union of keys
 s1 = set(d1.keys())
 s2 = set(d2.keys())
 s = s1.union(s2)
 abbrevs = list(s)
 print(f'{len(s)} total distinct abbreviations')
 outarr = get_outarr(abbrevs,d1,d2)

 write_lines(fileout,outarr)
