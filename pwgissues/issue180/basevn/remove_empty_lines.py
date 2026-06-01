""" remove_empty_lines.py
 # removes empty lines WITHIN an entry
 
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

def adjust_lines(lines):
 newlines = []
 inentry = False
 n = 0 # number of empty lines removied from entries
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   inentry = True
   newlines.append(line) 
   #continue
  elif inentry == False:
   newlines.append(line)
   #continue
  elif line.startswith('<LEND>'):
   newlines.append(line)
   inentry = False
   #continue
  else:
   if line == '':
    n = n + 1
   else:
    newlines.append(line)
   
 print(f'{n} empty lines removed from entries')
 return newlines

if __name__=="__main__":
 filein = sys.argv[1]  # base
 fileout = sys.argv[2] # adjusted base
 
 lines = read_lines(filein)

 lines1 = adjust_lines(lines)
 write_lines(fileout,lines1)
