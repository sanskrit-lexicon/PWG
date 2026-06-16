""" compare_lang.py
 
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

def gather_ab॒_version1(entry):
 # entry is a sequence of strings
 a = []
 iabs = []
 allparts = []
 for i,line in enumerate(entry):
  parts = re.split('(<lang>.*?</lang>)',line)
  allparts = allparts + parts
 for ipart,part in enumerate(allparts):
  a.append(part)
  if part.startswith('<lang'):
   iabs.append(ipart)
 if False:
  for x in a:
   print(x)
  exit(1)
 return a,iabs

def gather_ab(entry):
 # entry is a sequence of strings
 # first entry is metaline
 # last entry is <LEND>
 entrydata = ' '.join(entry[1:-1])
 allparts = re.split('(<lang>[^<]*?</lang>)',entrydata)
 return allparts,[]

def first_diff(e1,e2):
 a1,iabs1 = gather_ab(e1)  # iabs not used
 a2,iabs2 = gather_ab(e2)
 n1 = len(a1)
 n2 = len(a2)
 n = max(n1,n2)
 ifirst = None
 for i in range(n):
  if (i < n1) and (i < n2):
   x1 = a1[i]
   x2 = a2[i]
   if x1.startswith('<lang') and x2.startswith('<lang') and x1 != x2:
    ifirst = i
    break
   elif (x1.startswith('<lang')) and (not x2.startswith('<lang')):
    ifirst = i
    break
   elif (not x1.startswith('<lang')) and (x2.startswith('<lang')):
    ifirst = i
    break
  elif (i < n1) and a1[i].startswith('<lang'):
   ifirst = i
   break
  elif (i < n2) and a2[i].startswith('<lang'):
   ifirst = i
   break
 if ifirst == None:
  return []
 # generate output for first difference
 # print(f'e1[0] = "{e1[0]}"')
 difflines = []
 difflines.append(e1[0]) # metalines
 for i in range(ifirst + 5):
  if i < n1:
   d1 = f'{a1[i]}'
  else:
   d1 = 'NA'
  if i < n2:
   d2 = f'{a2[i]}'
  else:
   d2 = 'NA'

  if i == ifirst:
   pfx = '*** '
  else:
   pfx=''
  d1a = f'CDSL: {d1}'
  d2a = f'  AB: {d2}'
  difflines.append(f'{pfx}{d1a}')
  difflines.append(f'{pfx}{d2a}')
  difflines.append('SPACE')
  #if i == ifirst:
  # break
 return difflines
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
 ifirst = None
 for i,e1 in enumerate(entries1):
  e2 = entries2[i]
  diff = first_diff(e1,e2)
  if diff != []:
   ifirst = i
   break
 if ifirst != None:
  print(f'First problem: {entries1[ifirst][0]}')
 write_lines(fileout,diff)
