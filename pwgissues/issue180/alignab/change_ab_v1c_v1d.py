""" change_ab_v1c_v1d.py
 
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
  ('<ab>adj.</ab>', '<lex>adj.</lex>'), # 2
  ('<ab>adj. Comp.</ab>', '<ab>adj. comp.</ab>'), # 7
  ('<lang>pers.</lang>', '<ab>pers.</ab>'), #16
  ('{%Fisch%} dies, und ', '{%Fisch%} <ab>dies.</ab> und '),
  ('<ls>SUŚR. 1,333, (323 <ab>gedr.</ab>) 19. 8</ls>',
   '<ls>SUŚR. 1,333, (323 gedr.) 19. 8</ls>'),
  ('die auch sonst weibl. personificirt werden',
   'die auch sonst <ab>weibl.</ab> personificirt werden'), #1
  ('<ab n="Süd">S.</ab> {#apyayadIkzita#}',
   '<ab>S.</ab> {#apyayadIkzita#}'),   # Sehen (?) = See
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
 print(f'{nchg} line(s) changed')
 return newlines

if __name__=="__main__":
 filein = sys.argv[1]  # base
 fileout = sys.argv[2] # adjusted base
 
 lines = read_lines(filein)

 lines1 = adjust_lines1(lines)
 #lines2 = adjust_lines2(lines1)
 write_lines(fileout,lines1)
