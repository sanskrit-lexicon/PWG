""" compare_lines.py
 
"""
import sys,re
import codecs
# import os.path,time
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

preface = ['<H>{#a#}',''] # lines before first entry

def get_entries(lines):
 entries = []
 entry = None # an array of lines
 n = 0 # number of lines changed
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   entry = []
   entry.append(line)
   continue
  if line.startswith('<LEND>'):
   entry.append(line)
   entries.append(entry)
   entry = None
   continue
  if entry == None:
   continue
  entry.append(line)
 # print(f'{len(entries)} entries')
 return entries

def get_entrylines(preface_lines,entries):
 a = []
 for x in preface_lines:
  a.append(x)
 ilast = len(entries) - 1
 for i,entry in enumerate(entries):
  for x in entry:
   a.append(x)
  if i != ilast:
   a.append('') # blank line after <LEND>
 return a

def unadjust_entry(entry):
 # entry consists of metaline, datalines, and LEND
 # the adjustments are made to datalines
 metaline = entry[0]
 lendline = entry[-1]
 datalines = entry[1:-1]
 newlines = []
 for line in datalines:
  parts = line.split(LBC)
  for x in parts:
   newlines.append(x)
 newentry = [metaline] + newlines + [lendline]
 return newentry

def parse_meta(meta):
 m = re.search('^<L>(.*?)<pc>(.*?)<k1>(.*?)(<k2>.*)$', meta)
 L = m.group(1)
 pc = m.group(2)
 k1 = m.group(3)
 rest = m.group(4)
 return (L,k1)

def get_difflines(entries1,entries2):
 ans = []
 for i,e1 in enumerate(entries1):
  e2 = entries2[i]
  n1 = len(e1)
  n2 = len(e2)
  if n1 == n2:
   continue
  L,k1 = parse_meta(e1[0])
  if n1 < n2:
   out = f'{L} {k1}: {n1} < {n2}'
  else:
   out = f'{L} {k1}: {n1} > {n2}'
  ans.append(out)
 return ans
if __name__=="__main__":
 filein1 = sys.argv[1]  # base c
 filein2 = sys.argv[2]
 fileout = sys.argv[3] # unadjusted base
 
 lines1 = read_lines(filein1)
 entries1 = get_entries(lines1)
 lines2 = read_lines(filein2)
 entries2 = get_entries(lines2)
 assert len(entries1) == len(entries2) # confirm same number of entries
 
 print(f'{len(entries1)} entries in both files')


 difflines = get_difflines(entries1,entries2)
 write_lines(fileout,difflines)
