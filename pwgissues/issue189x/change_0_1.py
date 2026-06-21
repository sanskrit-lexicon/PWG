""" change_0_1.py
 
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
 newlines = []
 nchg = 0
 for iline,line in enumerate(lines):
  newline = line
  newline = newline.replace('<is>Vārtt</is>.','<is n="Vārttika">Vārtt.</is>')
  newline = re.sub(r"<is>([^<]+)'s</is>",r"<is>\1</is>ʼs",newline)
  if newline != line:
   nchg = nchg + 1
  newlines.append(newline)
 print(f'{nchg} line(s) changed')
 return newlines

def unused_adjust_lines0(lines):
 ans = lines
 lnum = 1078685
 iline = lnum - 1
 assert ans[iline] == 'im <lang>Prākrit</lang>'
 ans[iline] = 'im Prākrit'
 return ans
if __name__=="__main__":
 filein = sys.argv[1]  # base
 fileout = sys.argv[2] # adjusted base
 
 lines = read_lines(filein)
 lines1 = adjust_lines1(lines)
 write_lines(fileout,lines1)
