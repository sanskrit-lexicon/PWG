""" div_split.py
 
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

if __name__=="__main__":
 filein = sys.argv[1]  # base
 fileout1 = sys.argv[2] # unadjusted base
 
 lines = read_lines(filein)
 entries = get_entries(lines)
 print(f'{len(entries):6} original entries')

 entries1 = [unadjust_entry(e) for e in entries]
 print(f'{len(entries1):6} unadjusted entries')

 lines1 = get_entrylines(preface,entries1)
 write_lines(fileout1,lines1)
