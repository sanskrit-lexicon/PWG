""" lend.py 
   for pwg. 
"""
import sys,re
import codecs
# import os.path,time
LBC = ' 🞄'  # line-break replaces certain '\n'
def read_lines(filein):
 lines = []
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  for line in f:
   #lines.append(line.strip()) # changed at ap_1
   lines.append(line.rstrip('\r\n'))
 print(f'{len(lines)} lines read from {filein}')
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,'w','utf-8') as f:
  for out in outarr:
   f.write("%s\n" % out)
 print(f'{len(outarr)} lines written to {fileout}')

def lend_merge(lines):
 newlines = []
 nlines = len(lines)
 iline_last = nlines - 1
 iline = 0
 while iline < nlines:
  line = lines[iline]
  if line != '<LEND>':
   newlines.append(line)
   iline = iline + 1
   continue
  if iline == iline_last:
   newlines.append(line) # <LEND> for last line of file
   iline = iline + 1
   continue
  # collect lines up to next <L>
  a = [line]  # <LEND>
  iline = iline + 1
  while not lines[iline].startswith('<L>'):
   a.append(lines[iline])
   iline = iline + 1
  assert lines[iline].startswith('<L>')
  assert lines[iline-1] == ''
  assert a[-1] == ''
  b = a[0:-1] 
  newline = LBC.join(b)
  newlines.append(newline)
  iline = iline - 1 # blank line preceding next <L>
 return newlines

def lend_restore(lines):
 newlines = []
 for line in lines:
  a = line.split(LBC)
  for x in a:
   newlines.append(x)
 return newlines
if __name__=="__main__":
 option = sys.argv[1]
 filein = sys.argv[2]  # xxx.txt
 fileout = sys.argv[3] # xxx_
 
 lines = read_lines(filein)
 if option == 'MERGE':
  newlines = lend_merge(lines)
 elif option == 'RESTORE':
  newlines = lend_restore(lines)
 else:
  print(f'OPTION ERROR: {option}')
  exit(1)
 write_lines(fileout,newlines)
