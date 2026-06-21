""" change_6_7.py
 
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


def adjust_lines1(lines):
 replacements = [
  # Begin 06-21-2026 
  ('{%<is>Br.</is> beschützt die Vollbringer von Werken%}',
   '{%<is n="Brahma">Br.</is> beschützt die Vollbringer von Werken%}'),
  #('', ''),
  #('', ''),
  #('', ''),
  #('', ''),
  #('', ''),
 ]
 newlines = []
 nchg = 0
 for iline,line in enumerate(lines):
  newline = line
  for old,new in replacements:
   newline = newline.replace(old,new)
  if newline != line:
   nchg = nchg + 1
  newlines.append(newline)
 print(f'{nchg} line(s) changed by adjust_lines1')
 return newlines

def init_changes(fileprep):
 lines = read_lines(fileprep)
 d = {}
 for line in lines:
  lnumstr,oldtag,newtag = line.split('\t')
  lnum = int(lnumstr)
  iline = lnum - 1
  if iline not in d:
   d[iline] = []
  d[iline].append((oldtag,newtag))
 return d
def adjust_lines0(lines,fileprep):
 dchanges = init_changes(fileprep)
 ans = lines
 nchg = 0  # number of lines changed
 for iline in dchanges:
  oldline = ans[iline]
  replacements  = dchanges[iline]
  newline = lines[iline]
  for oldtag,newtag in replacements:
   newline = newline.replace(oldtag,newtag)
  ans[iline] = newline
  assert oldline != newline
  nchg = nchg + 1
 print(f'{nchg} lines changed by adjust_lines0')
 return ans
if __name__=="__main__":
 fileprep = sys.argv[1]
 filein = sys.argv[2]  # base
 fileout = sys.argv[3] # adjusted base

 lines = read_lines(filein)
 lines0 = adjust_lines0(lines,fileprep)
 #lines0 = lines
 lines1 = adjust_lines1(lines0)
 write_lines(fileout,lines1)
