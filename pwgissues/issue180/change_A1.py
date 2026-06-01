""" change_A1.py  
   change AB version
"""
import sys,re
import codecs
# import os.path,time

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

def change_one(line):
 # changes to Andhrabharati version
 x = line
 x = x.replace('<lex>m.f.n.</lex>' ,
               '<lex>m.</lex> <lex>f.</lex> <lex>n.</lex>')
 x = x.replace('<lex>m.f.</lex>' ,
               '<lex>m.</lex> <lex>f.</lex>')
 x = x.replace('<lex>m.n.</lex>' ,
               '<lex>m.</lex> <lex>n.</lex>')
 x = x.replace('<lex>f.n.</lex>' ,
               '<lex>f.</lex> <lex>n.</lex>')
 # x = x.replace('<lex>ff.</lex>' , '<ab>ff.</ab>')
 # x = x.replace('' , '')
 # x = x.replace('' , '')
 # x = x.replace('' , '')
 # x = x.replace('' , '')
 # x = x.replace('' , '')
 # x = x.replace('' , '')

 return x
def change(lines):
 newlines = []
 metaline = None
 nmeta = 0 
 n = 0 # number of lines changed
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   metaline = True
   newlines.append(line)
   nmeta = nmeta + 1
   continue
  if line.startswith('<LEND>'):
   newlines.append(line)
   continue
  if not metaline:
   newlines.append(line)
   continue
  #dbg = iline == 48544
  #dbg = False
  newline = change_one(line)
  newlines.append(newline)
  if newline != line:
   n = n + 1
 print(f'{nmeta} metalines')
 return newlines,n


if __name__=="__main__":
 filein = sys.argv[1]  # xxx.txt
 fileout = sys.argv[2] # new xxx.txt
 lines = read_lines(filein)
 newlines,nchg = change(lines)
 print(f'{nchg} lines changed')
 write_lines(fileout,newlines)
