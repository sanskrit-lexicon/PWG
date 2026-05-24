""" combine1.py
"""
import sys,re
import codecs

def read_lines(filein):
 lines = []
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  for line in f:
   #lines.append(line.strip()) # changed at ap_1
   lines.append(line.rstrip('\r\n'))
 print(f'{len(lines):03d} lines read from {filein}')
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,'w','utf-8') as f:
  for out in outarr:
   f.write("%s\n" % out)
 print(f'{len(outarr)} lines written to {fileout}')

class Abbrev:
 def __init__(self,line,code):
  parts = line.split('\t')
  self.abbrev = parts[0]
  self.count = 0
  if code == 'count':
   self.count = int(parts[1])
  self.tips = {}
  
def init_abbrev_counts(file_count_ab, file_count_lex):
 lines_ab =  read_lines(file_count_ab)
 recs_ab =   [Abbrev(line,'count') for line in lines_ab]
 lines_lex = read_lines(file_count_lex)
 recs_lex =  [Abbrev(line,'count') for line in lines_lex]
 recs = recs_ab + recs_lex
 d = {}
 for rec in recs:
  ab = rec.abbrev
  if ab in d:
   print(f'DUPLICATE Abbrev: {ab}')
   exit(1)
  d[ab] = rec
 return d

def update_abbrevs(filename,src,d):
 unused = []
 lines = read_lines(filename)
 for line in lines:
  abbrev,tip = line.split('\t')
  if abbrev in d:
   d[abbrev].tips[src] = tip
  else:
   # print(f'new {abbrev} from {src}')
   # make a new abbrev
   #line = f'{abbrev}\t0'
   #abrec = Abbrev(line,'count')
   #d[abbrev] = abrec
   #d[abbrev].tips[src] = tip
   unused.append(f'{src} {line}')
 return unused
def get_outarr(d):
 # present results alphabetical order
 keys = sorted(d.keys(), key = lambda x: x.lower()) 
 outarr = []
 for ab in keys:
  rec = d[ab]  # Abbrev
  count = rec.count
  tips = rec.tips
  sources = sorted(tips.keys()) # list
  a = [f'* TODO {ab}',  f'{count}']
  a = a + sources
  out = ' : '.join(a)
  outarr.append(f'{out}')
  for src in sources:
   tip = tips[src]
   out = f'{src} : {tip}'
   outarr.append(out)
 return outarr

def get_outarr1(d):
 outarr = []
 for src in d:
  unusedlines = d[src]
  for x in unusedlines:
   outarr.append(x)
 outarr1 = sorted(outarr, key = lambda x: x.lower())
 return outarr1
if __name__=="__main__":
 fileout = sys.argv[1]
 fileout1 = sys.argv[2]
 file_count_ab  = '../count_ab_8.txt'
 file_count_lex = '../count_lex_5.txt'
 file_tips = {
  'PWG': '../pwgab_input_1c.txt',
  'PWK': 'pwab_input.txt',
  'GAS': 'pwgab_input_draft.txt'
  }
 abbrevs_d = init_abbrev_counts(file_count_ab, file_count_lex)
 source_codes = ['PWG','PWK','GAS']
 unused = {}
 for src in file_tips:
  filename = file_tips[src]
  unused[src] = update_abbrevs(file_tips[src],src,abbrevs_d)
 outarr = get_outarr(abbrevs_d)
 write_lines(fileout,outarr)
 
 outarr1 = get_outarr1(unused)
 write_lines(fileout1,outarr1)
