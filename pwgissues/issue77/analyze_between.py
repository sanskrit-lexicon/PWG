#-*- coding:utf-8 -*-
""" analyze_between.py
    analyze lines between <LEND> and <L>
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 print("%s lines read from %s" % (len(lines),filein))
 return lines

def remove_between(lines):
 # remove lines between <LEND> and <L>
 newlines = []  # returned
 metaline = None
 nchg = 0
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   metaline = line
   newlines.append(line)
   continue
  if line.startswith('<LEND>'):
   metaline = None
   newlines.append('<LEND>')
   continue
  if metaline == None:
   # drop this 'between' line
   nchg = nchg + 1
   continue
  # keep line in body.
  newlines.append(line)
 print('adjust: %s dropped between <LEND> and <L>' % nchg)
 return newlines

def insert_between(lines):
 # insert single blank line after <LEND>
 newlines = []  # returned
 metaline = None
 nchg = 0
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   metaline = line
   newlines.append(line)
   continue
  if line.startswith('<LEND>'):
   metaline = None
   newlines.append('<LEND>')
   newlines.append('')  # extra blank line
   nchg = nchg + 1
   continue
  if metaline == None:
   # drop this 'between' line
   # unexpected
   print('Unexpected line at line #',iline+1)
   exit(1)
  # keep line in body.
  newlines.append(line)
 print('adjust: %s blank lines inserted between <LEND> and <L>' % nchg)
 return newlines

def analyze_after_lend(iline,metaline,lines,nlines):
 ans = [] # lines after lend and before next <L>
 assert lines[iline] == '<LEND>'
 m = re.search(r'<L>(.*?)<',metaline)
 L = m.group(1)
 ans.append(L)
 if (iline + 1) == nlines:
  nextmeta = None
  ans.append(nextmeta)
  return ans

 b = []
 while True:
  iline = iline + 1
  nextline = lines[iline]
  if nextline.startswith('<L>'):
   ans.append(nextline)  # next meta line
   for c in b:
    ans.append(c)
   return ans
  else:
   b.append(nextline)

def check_afters_page(afters):
 nprob = 0
 for after in afters:
  L = after[0]
  nextmeta = after[1]
  b = after[2:]
  for c in b:
   m = re.search(r'^\[Page([0-9]-[0-9][0-9][0-9][0-9])\]$',c)
   if m == None:
    continue
   pc = m.group(1)
   m1 = re.search(r'<pc>(.*?)<',nextmeta)
   pc1 = m.group(1)
   if pc != pc1:
    out = '%s' % c
    print(out)
    nprob = nprob + 1
 print('check_afters_page finds %s problems' % nprob)
 
def summary_after(afters,fileout):
 n = 0
 for after in afters:
  L = after[0]
  nextmeta = after[1]
  lines = after[2:]
  if lines == ['']:
   n = n + 1
 print('%s entries with single blank line between <LEND> and <L>' % n)
 d = {}
 check_afters_page(afters)
 
 for after in afters:
  L = after[0]
  nextmeta = after[1]
  b = after[2:]
  n = len(b)
  if n not in d:
   d[n] = 0
  d[n] = d[n] + 1
 print(d)
 # fileout = 'temp.txt'
 outarr = []
 for after in afters:
  L = after[0]
  nextmeta = after[1]
  if nextmeta == None:
   continue # last entry
  b = after[2:]
  if b != ['']:
   x = [L] + b
   out = '%s' % x
   outarr.append(out)
 write(fileout,outarr)
 
def analyze_between(lines,fileout):
 # remove lines between <LEND> and <L>
 newlines = []  # returned
 metaline = None
 nchg = 0
 d = {}
 afters = []
 nmeta = 0
 nlines = len(lines)
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   metaline = line
   nmeta = nmeta + 1
   continue
  if line.startswith('<LEND>'):
   #metaline = None
   newlines.append('<LEND>')
   after = analyze_after_lend(iline,metaline,lines,nlines)
   afters.append(after)
 print('# of metalines = %s' % nmeta)
 print('# afters = %s' % len(afters))
 summary_after(afters,fileout)
 
def write(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line + '\n')
 print(len(lines),"written to",fileout)
 
if __name__=="__main__": 
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # revised xxx.txt
 lines = read_lines(filein)
 analyze_between(lines,fileout)
 
