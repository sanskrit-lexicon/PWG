""" make_change_05.py
  Generate Python fragments to be used by change_0i_0j.py
 
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
 regex_raw = '<ls>Sp\. ([0-9]+), Z\. ([0-9]+)\. fgg\.</ls>'
 regex = re.compile(regex_raw)
 changes = []
 for iline,line in enumerate(lines):
  for m in re.finditer(regex,line):
   a = m.group(1)
   b = m.group(2)
   old = m.group(0)
   new = f'<ab>Sp.</ab> {a}, <ab>Z.</ab> {b}. <ab>fgg.</ab>'
   # ('X', 'Y'),
   change = f"  ('{old}',\n   '{new}'),"
   changes.append(change)
   #print(change)
   #exit(1)
 nchg = len(changes)
 print(f'{nchg} changes generated')
 return changes

if __name__=="__main__":
 filein = sys.argv[1]  # base
 fileout = sys.argv[2] # change records
 
 lines = read_lines(filein)

 lines1 = adjust_lines1(lines)
 write_lines(fileout,lines1)
