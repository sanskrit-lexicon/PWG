""" update_tips.py
"""
import sys,re
import codecs

def read_lines(filein):
 lines = []
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  for line in f:
   lines.append(line.rstrip('\r\n'))
 print(f'{len(lines):03d} lines read from {filein}')
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,'w','utf-8') as f:
  for out in outarr:
   f.write("%s\n" % out)
 print(f'{len(outarr)} lines written to {fileout}')

class AbbrevCount:
 def __init__(self,line):
  parts = line.split('\t')
  self.abbrev = parts[0]
  self.count = int(parts[1])

def init_counts(lines):
 recs = [AbbrevCount(line) for line in lines]
 d = {}
 for rec in recs:
  ab = rec.abbrev
  if ab in d:
   print(f'DUPLICATE Abbrev: {ab}')
   exit(1)
  d[ab] = rec
 return d

class Tip:
 def __init__(self,line):
  parts = line.split('\t')
  self.abbrev = parts[0]
  self.tip = parts[1]
  self.count = 0
  
def init_tips(lines):
 recs = [Tip(line) for line in lines]
 d = {}
 for rec in recs:
  ab = rec.abbrev
  if ab in d:
   print(f'DUPLICATE Tip: {ab}')
   exit(1)
  d[ab] = rec
 return d

def modify_tip(ab,tip,count):
 lexes = ('adj.','adv.','f.','ind.', 'indecl.', 'interj.','m.', 'n.', 'neutr.')
 # lexes consistent with count_lex
 m = re.search(r'<id>(.*?)</id> *<disp>(.*?)</disp> *(<INFER/>)? *<N>(.*?)</N> *(CHECKED|UNCHECKED)?',tip)
 if m == None:
  print(f'tip error: {tip}')
  exit(1)
 assert ab == m.group(1)
 disp = m.group(2)
 infer = m.group(3)
 if infer == None:
  infer = ''
 n = m.group(4)
 checked = m.group(5)
 if checked == None:
  checked = 'UNCHECKED'
 newtip = f'<id>{ab}</id> <disp>{disp}</disp> {infer} <N>{count}</N> {checked}'
 return newtip

def get_outarr(d):
 # present results alphabetical order
 keys = sorted(d.keys(), key = lambda x: x.lower())
 lexes = ('adj.','adv.','f.', 'ind.', 'indecl.', 'interj.','m.', 'n.', 'neutr.')
 outarr = []
 warnings = []
 for ab in keys:
  rec = d[ab]  # Tip record
  count = rec.count
  tip = rec.tip
  # modify tip
  newtip = modify_tip(ab,tip,count)
  out = f'{ab}\t{newtip}'
  if (count == 0):
   if ab in lexes:
    warnings.append(f'LEX : {newtip}')
   else:
    warnings.append(f'WARN: {newtip}')
  outarr.append(out)
 return outarr,warnings

def all_abbrevs(dtips,dcounts):
 d = {}
 for ab in dtips:
  d[ab] = True
 for ab in dcounts:
  d[ab] = True
 abs = list(d.keys())
 return abs
     
def update_tips(dtips,dcounts):
 abbrevs = all_abbrevs(dtips,dcounts)
 for ab in abbrevs:
  if ab not in dcounts:
   # make new AbbrevCount record
   val = 0
   line = f'{ab}\t{val}'
   rec = AbbrevCount(line)
   dcounts[ab] = rec
  if ab not in dtips:
   # make new Tip record
   val = f'<id>{ab}</id> <disp>?</disp> <N>0</N>'
   line = f'{ab}\t{val}'
   rec = Tip(line)
   dtips[ab] = rec
 # now dtips and dcounts have same keys, namely abbrevs
 assert set(dcounts.keys()) == set(dtips.keys())
 assert set(abbrevs) == set(dcounts.keys())
 # update count field in tips
 for ab in abbrevs:
  dtips[ab].count = dcounts[ab].count

if __name__=="__main__":
 filein = sys.argv[1]  # pwgab_input.txt format
 filein1 = sys.argv[2] # count format
 fileout = sys.argv[3] # revised pwgab_input
 fileout1 = sys.argv[4] # warnings  count=0 and lex
 lines = read_lines(filein)
 dtips = init_tips(lines)
 lines1 = read_lines(filein1)
 dcounts = init_counts(lines1)
 # update dtips and dcounts
 update_tips(dtips,dcounts)
 outarr,warnings = get_outarr(dtips)
 write_lines(fileout,outarr)
 warnings = sorted(warnings, key = lambda x: x.lower())
 write_lines(fileout1,warnings)
 
