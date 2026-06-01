""" change_0a_0b.py
 
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
 skiplines = [
  '<div n="1"> 1) {#keSarahita#} {%haarlos%},' ,
  '<div n="1"> 2) {#alpakeSayukta#} {%mit wenig Haar versehen%},' ,
  '<div n="1"> 3) {#apraSastakeSaviSizwa#} {%nicht durch schönes Haar ausgezeichnet.%}'
  ]
 oldline = '<ls>ŚKDR.</ls> {#akeSa#} durch'
 newline = '<ls>ŚKDR.</ls> {#akeSa#} durch 1) {#keSarahita#} {%haarlos%},  2) {#alpakeSayukta#} {%mit wenig Haar versehen%}, 3) {#apraSastakeSaviSizwa#} {%nicht durch schönes Haar ausgezeichnet.%}'
 
 newlines = []
 nskip = 0
 nchg = 0
 for iline,line in enumerate(lines):
  if line in skiplines:
   nskip = nskip + 1
   pass
  elif line == oldline:
   newlines.append(newline)
   nchg = nchg + 1
  else:
   newlines.append(line)
 print(f'{nskip} lines skipped,  {nchg} line(s) changed')
 return newlines

def adjust_lines2(lines):
 L_insert = {
  '14148' : '<H>{#ka#}',
  '26305' : '<H>{#ja#}',
  '37259' : '<H>{#na#}',
  '51684' : '<H>{#ba#}',
  '80800' : '<H>{#ya#}',
  '96987' : '<H>{#Sa#}',
 }
 newlines = []
 L = None
 n = 0 
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   m = re.search(r'^<L>(.*?)<pc>',line)
   L = m.group(1)
   newlines.append(line)
   continue
  if line.startswith('<LEND>'):
   newlines.append(line)
   if L in L_insert:
    newline = L_insert[L]
    newlines.append(newline)
    n = n + 1
   L = None                    
   continue
  newlines.append(line)
 print(f'adjust_lines2 inserts {n} lines ')
 return newlines

if __name__=="__main__":
 filein = sys.argv[1]  # base
 fileout1 = sys.argv[2] # adjusted base
 
 lines = read_lines(filein)

 lines1 = adjust_lines1(lines)
 lines2 = adjust_lines2(lines1)
 write_lines(fileout1,lines2)
