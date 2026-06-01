""" change_1.py
 
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
 # changes to cdsl version
 x = line
 x = x.replace('<ab>d.</ab> <lex>folg.</lex>', '<ab>d. f.</ab>')
 x = x.replace('<ab>ind.</ab>' , '<lex>ind.</lex>')
 x = x.replace('<ab>indecl.</ab>' , '<lex>indecl.</lex>')
 x = x.replace('<ab>neutr.</ab>' , '<lex>neutr.</lex>')
 x = x.replace('(femin.)' , '<lex>femin.</lex>')
 x = x.replace(' fem.' , ' <lex>fem.</lex>')
 x = x.replace('(fem.' , '(<lex>fem.</lex>')
 x = re.sub('^fem\.',  '<lex>fem.</lex>', x)
 x = x.replace(' ff.' , ' <lex>ff.</lex>')
 x = x.replace(' mm.' , ' <lex>mm.</lex>')
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
