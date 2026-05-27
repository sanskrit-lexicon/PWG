""" change1
 
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
 newline = re.sub('([0-9]),<ab>c\.</ab>',  r'\1,c.',line)
 newline = re.sub('([0-9]),<ab>d\.</ab>',  r'\1,d.',newline)
 newline = newline.replace(' Cit.</ls>', '</ls> Cit.')
 newline = newline.replace('(s. auch <ab>d.</ab>)', '(s. auch d.)')
 newline = newline.replace(' a. a. O.</ls>', '</ls> <ab>a. a. O.</ab>')
 newline = newline.replace('(acc.)', '(<ab>acc.</ab>)') # 12
 newline = newline.replace(' acc.', ' <ab>acc.</ab>')  # 7
 newline = newline.replace(' pl.', ' <ab>pl.</ab>')
 newline = newline.replace(' act.:', ' <ab>act.</ab>:')
 newline = newline.replace(', Anf.</ls>', '</ls>, <ab>Anf.</ab>') # 15
 newline = newline.replace(', Anm.</ls>', '</ls>, <ab>Anm.</ab>') # 16
 newline = newline.replace('<ab>d.</ab> <lex>f.</lex> <ab>W.</ab>',
                           '<ab>d. f. W.</ab>')
 newline = newline.replace('</ls> <ab>fg.</ab>', ' fg.</ls>')
 newline = newline.replace('</ls> <ab>fgg.</ab>', ' fgg.</ls>')
 newline = newline.replace('</ls> <ab>Eibl.</ab>', ' Einl.</ls>')
 newline = re.sub('{%([A-Za-z]+ [A-Za-z]+) <ab>Dec\.</ab>%}',
                  r'{%\1 Dec.%}', newline) # 47
 newline = re.sub('{%([A-Za-z]+ [A-Za-z]+) <ab>Corr\.</ab>%}',
                  r'{%\1 Corr.%}', newline) # 
 newline = re.sub('{%([A-Za-z]+ [A-Za-z]+) <ab>Pers\.</ab>%}',
                  r'{%\1 Pers.%}', newline) # 
 newline = newline.replace('{%Croton polyandrum <ab>Spr.</ab>%}',
                           '{%Croton polyandrum Spr.%}') # 4

 return newline
def change(lines):
 newlines = []
 metaline = None
 n = 0 # number of lines changed
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   metaline = True
   newlines.append(line)
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
 return newlines,n


if __name__=="__main__":
 filein = sys.argv[1]  # xxx.txt
 fileout = sys.argv[2] # new xxx.txt
 lines = read_lines(filein)
 newlines,nchg = change(lines)
 print(f'{nchg} lines changed')
 write_lines(fileout,newlines)
