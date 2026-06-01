""" basevn_split.py  
 
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
 print(f'{len(entries)} entries')
 return entries
 
def split_entries(entries):
 entries1 = []
 entries2 = []
 n_3 = 0
 n_2 = 0
 for entry in entries:
  meta = entry[0]
  if re.search('<L>(.*?)\.[0-9]{3}<pc>',meta):
   n_3 = n_3 + 1
   entries2.append(entry)
  elif re.search('<L>(.*?)\.[0-9]{2}<pc>',meta):
   n_2 = n_2 + 1
   entries2.append(entry)
  else:
   entries1.append(entry)
 return entries1,entries2

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

if __name__=="__main__":
 filein = sys.argv[1]  # xxx.txt
 fileout1 = sys.argv[2] # xxx_base
 fileout2 = sys.argv[3] # vn_base
 
 lines = read_lines(filein)
 entries = get_entries(lines)
 entries1,entries2 = split_entries(entries)
 print(f'{len(entries1):6} base entries')
 print(f'{len(entries2):6} vn entries')

 
 lines1 = get_entrylines(preface,entries1)
 lines2 = get_entrylines([],entries2)

 write_lines(fileout1,lines1)
 write_lines(fileout2,lines2)
