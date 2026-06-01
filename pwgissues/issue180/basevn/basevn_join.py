""" basevn.py  
 
"""
import sys,re
import codecs

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
 print(f'{len(entries)} entries')
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

def get_entries_dict(entries):
 d = {}
 for entry in entries:
  meta = entry[0]
  m = re.search('<L>(.*?)<pc>',meta)
  L = m.group(1)
  L0 = float(L)
  assert L0 not in d
  d[L0] = entry
 return d

if __name__=="__main__":
 filein1 = sys.argv[1]  # xxx.txt
 filein2 = sys.argv[2] # xxx_base
 fileout = sys.argv[3] # vn_base
 
 lines1 = read_lines(filein1)
 lines2 = read_lines(filein2)
 
 entries1 = get_entries(lines1)
 entries2 = get_entries(lines2)
 
 print(f'{len(entries1):6} base entries')
 print(f'{len(entries2):6} vn entries')

 entries = entries1 + entries2
 d = get_entries_dict(entries)
 keys = sorted(d.keys())
 newentries = [d[key] for key in keys]
 newlines = get_entrylines(preface,newentries)

 write_lines(fileout,newlines)

