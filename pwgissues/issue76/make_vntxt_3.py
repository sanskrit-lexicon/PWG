# coding=utf-8
""" make_vntxt_3.py
"""
import sys,re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 print('%s lines read from %s' % (len(lines),filein))
 return lines

def write_lines(fileout,outarr,printFlag=False):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    if out == None:
     out = '?'
    f.write(out+'\n')
 if printFlag:
  print(len(outarr),"lines written to",fileout)

class VNRec:
 def __init__(self,line,L,vol,pc):
  self.line = line
  self.L0 = L
  self.vol = vol
  self.pc = pc
  self.k1 = None
  self.k2 = None
  self.h = None

def update_Lvpc(line,L,vol,pc):
 # line starting with []
 # L
 regex1 = r'\[L:([0-9]+)\]'
 # vol
 regex2 = r'\[Page:VN([1-6])-001\]'
 regex2a = r'\[Page:VN([1-6])-[0-9][0-9][0-9]\]'
 # pc
 regex3 = r'\[([1-6]-[0-9][0-9][0-9][0-9])\]'
 regexa = '^%s%s%s' % (regex1,regex2,regex3)
 m = re.search(regexa,line)
 if m != None:
  L = m.group(1)
  vol = m.group(2)
  pc = m.group(3)
  return (L,vol,pc)
 regexb = '^%s%s' %(regex2a,regex3)
 m = re.search(regexb,line)
 if m != None:
  vol = m.group(1)
  pc = m.group(2)
  return (L,vol,pc)  # uses old L
 print('update_Lvpc ERROR')
 print(line)
 print('regexa=%s' % regexa)
 print('regexb=%s' % regexb)
 for reg in (regex1,regex2,regex2aregex3):
  m = re.search(reg,line)
  if m == None:
   print('regex %s fails' % reg)
 exit(1)

def init_recs(lines):
 recs = []
 L = None
 vol = None
 pc = None

 for iline,line in enumerate(lines):
  if line.startswith(';'):
   # skip comment lines
   continue
  if line.strip() == '':
   # skip blank lines
   continue
  if line.startswith(('<F>','<H>')):
   # skip these lines also
   continue
  if line.startswith('['):
   L,vol,pc = update_Lvpc(line,L,vol,pc)
   # no output line
   continue
  if not '¦' in line:
   print('init_recs error 1 in line # ',iline+1)
   print(line)
   exit(1)
  if None in (L,vol,pc):
   print('init_recs error 2 in line # ',iline+1)
   print(line)
   exit(1)
  rec = VNRec(line,L,vol,pc)
  recs.append(rec)
 print('init_recs finds %s records' % len(recs))
 return recs

def dupcheck(lines):
 known_dups = [
  '<hom>1.</hom> {#anurkAya#}	 ¦ [1.0199] Z. 23 lies: {#anukArya#}.',
  '{#aloha#}	 ¦ [1.0463] lies: <ls>P. 4,1,99.</ls>'
  ]
 dups = []
 iline2dups = []
 for iline1,line1 in enumerate(lines):
  for iline2,line2 in enumerate(lines):
   if iline2 <= iline1:
    continue
   if line1 == line2:
    if line1 == '':
     # don't note empty line dups
     continue
    #if line1 in known_dups:
    # continue
    # add an erroneous dup
    dups.append((line1,iline1,iline2))
    iline2dups.append(iline2)
 print(len(dups),"unexpected duplicates found")
 if len(dups) != 0:
  print('debug exit')
  exit(1)
 # no dup problem found. return

def adjust_semicolon(lines):
 newlines = []
 n = 0
 for iline,line in enumerate(lines):
  m = re.search(r'^(.*?) *(;;.*)$',line)
  if m == None:
   newlines.append(line)
  else:
   a,b = m.group(1),m.group(2)
   newlines.append(b)
   newlines.append(a)
   n = n + 1
 print('adjust_semicolon changes %s lines, resulting in %s lines' % (n,len(newlines)))
 return newlines

def adjust_extra(lines):
 newlines = []
 filein = 'vntxt_3_extra.txt'
 extras = read_lines(filein)
 for iline,line in enumerate(lines):
  if line.startswith('???	 ¦ [1.0956] — [1.1016] '):
   newlines.append(';' + line)
   for extra in extras:
    newlines.append(extra)
  else:
   newlines.append(line)
 print('adjust_extra inserts %s lines, resulting in %s lines' %(
  len(extras), len(newlines)))
 return newlines

def adjust_question(lines):
 newlines = []
 n = 0
 for iline,line in enumerate(lines):
  if line.startswith('?'):
   newlines.append(';' + line)
   n = n + 1
  else:
   newlines.append(line)
 print('adjust_question comments out %s lines, resulting in %s lines' %(
  n, len(newlines)))
 return newlines

def init_change(filein):
 lines0 = read_lines(filein)
 lines = [x for x in lines0 if not x.startswith(';')]
 changes = {}
 n = 0
 for iline,line in enumerate(lines):
  if line != 'old':
   continue
  old = lines[iline + 1]
  assert lines[iline + 2] == 'new'
  new = lines[iline + 3]
  n = n + 1
  changes[old] = new
 print('init_change: %s changes from %s' % (n,filein))
 return changes

def adjust_change(lines):
 newlines = []
 filein = 'vntxt_3_change.txt'
 changes = init_change(filein)
 n = 0
 for iline,line in enumerate(lines):
  if line not in changes:
   newlines.append(line)
  else:
   newline = changes[line]
   newlines.append(newline)
   n = n + 1
 print('adjust_change to %s lines, resulting in %s lines' %(
  n, len(newlines)))
 keys = changes.keys()
 assert len(keys) == n  # all changes made
 return newlines

if __name__=="__main__":
 filein = sys.argv[1]  # vntxt_2
 fileout = sys.argv[2] # vntxt_3
 lines = read_lines(filein)
 newlines = adjust_semicolon(lines)
 newlines = adjust_extra(newlines)
 newlines = adjust_question(newlines)
 newlines = adjust_change(newlines)
 
 write_lines(fileout,newlines,printFlag=True)
 exit(1)
 recs = init_recs(lines)
