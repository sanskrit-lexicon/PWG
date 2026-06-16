""" mark_lang.py
 
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

def get_regex_split():
 tags3 = ['<div n=.*?>', '<info n=.*?/>']
 tags2 = ('F','VN','ab','fr','hom','is','lang','ls', 'lex','span','lang')
 tags2a = [f'<{x}.*?>.*?</{x}>' for x in tags2]
 # allow abbrevs in italic text '\{%.*?%\}', but not in Sanskrit text
 tags1 = ['\{#.*?#\}',  ] 
 tags = tags1 + tags2a + tags3
 a = '|'.join(tags)
 regex_raw = f'({a})'
 print('regex_raw=',regex_raw)
 regex = re.compile(regex_raw)
 return regex
regex_split= get_regex_split()

 
def mark_lang_one(line,abpattern,dbg):
 if dbg: print(f'old: {line}')
 parts = re.split(regex_split,line)
 newparts = []
 for part in parts:
  if part.startswith('<'):
   newpart = part
  elif part.startswith('{'):
   newpart = part
  else:
   newpart = re.sub(abpattern,r"<lang>\1</lang>", part)
  if dbg:
   print('  oldp=',part)
   print('  newp=',newpart)
  newparts.append(newpart)
 newline = ''.join(newparts)
 if dbg: print(f'new: {newline}')
 return newline

def test(abpattern):
 #line = 'Interj. '
 #newline = re.sub(abpattern,r"<lang>\1</lang>", line)
 line = '1. {#a#}¦ Interj. {#a apehi#} (die beiden Vocale fliessen nicht in einander)'
 newline = mark_lang_one(line,abpattern)
 print(line)
 print(newline)
 
 
def mark_lang(lines,abpattern):
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
  dbg = False
  newline = mark_lang_one(line,abpattern,dbg)
  newlines.append(newline)
  if newline != line:
   n = n + 1
 return newlines,n

class Abbrev:
 def __init__(self,line):
  parts = line.split('\t')
  self.abbrev = parts[0]
  self.count = 0

def init_abbrevs(lines):
 recs = [Abbrev(line) for line in lines]
 d = {}
 for rec in recs:
  ab = rec.abbrev
  if ab in d:
   print(f'DUPLICATE Abbrev: {ab}')
   exit(1)
  d[ab] = rec
 return recs,d

def build_abbrev_pattern(abbrevs0):
 # sort in decreasing length
 abbrevs = sorted(abbrevs0, key = lambda x: len(x.abbrev), reverse = True)
 
 # per copilot
 abbreviations = [x.abbrev for x in abbrevs]
 # Escape each abbreviation for regex safety
 escaped = [re.escape(abbrev) for abbrev in abbreviations]
 # 
 # pattern = r"\b(" + "|".join(escaped) + r")\b"
 pattern_raw = r"(?<!\w)(" + "|".join(escaped) + r")(?!\w)"
 pattern = re.compile(pattern_raw)
 if False:
  print('abbreviations =',abbreviations)
  print(pattern_raw)
  print('dbg exit')
  exit(1)
 return pattern

def update_count(lines,d):
 regex = re.compile(r'<lang>(.*?)</lang>')
 metaline = None
 for line in lines:
  if line.startswith('<L>'):
   metaline = True
   continue
  if line.startswith('<LEND>'):
   metaline = False
   continue
  if not metaline:
   continue
  for m in re.finditer(regex,line):
   e = m.group(1)  # abbreviation
   if e not in d:
    print('ERROR - abbrev not found',e)
    exit(1)
   rec = d[e] # Abbrev object
   rec.count = rec.count + 1

def get_count_outarr(keysd):
 # present results alphabetical order
 keys = sorted(keysd.keys(), key = lambda x: x.lower()) 
 outarr = []
 ntot = 0
 for tag in keys:
  abbrev = keysd[tag]
  n = abbrev.count
  out = '%s\t%s' %(tag,n)
  outarr.append(out)
  ntot = ntot + n
 return outarr,ntot
 
if __name__=="__main__":
 filein = sys.argv[1]
 filelang = sys.argv[2]
 fileout = sys.argv[3] # output path
 if len(sys.argv) == 5:
  fileout2 = sys.argv[4] # count summary
 else:
  fileout2 = None
 ablines = read_lines(filelang)
 abbrevs,dabbrevs = init_abbrevs(ablines)
 abpattern = build_abbrev_pattern(abbrevs)
 #
 lines = read_lines(filein)
 newlines,nchg = mark_lang(lines,abpattern)
 print(f'{nchg} lines changed')
 write_lines(fileout,newlines)
 if fileout2 != None:
  update_count(newlines,dabbrevs)
  outarr,ntot = get_count_outarr(dabbrevs)
  write_lines(fileout2,outarr)
  print(f'{ntot} = total number of <lang>X</lang>')
