""" combine1_extract.py
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

def get_outarr(recs):
 outarr = []
 ndone = 0
 ndonecount = 0
 ntodocount = 0
 for rec in recs:
  abbrev = rec.abbrev
  tip = rec.tip
  if rec.choiceflag == 'x': # skip
   print(f'skipping {rec.group[0]}')
   continue
  # add <N>N</N>,
  tip1 = f'{tip} <N>{rec.count}</N>'
  # add status
  if rec.status == 'DONE':
   stat = 'CHECKED'
  else:
   stat = 'UNCHECKED'
  tip1 = f'{tip1} {stat}'
  if rec.status == 'DONE':
   ndone = ndone + 1
   ndonecount = ndonecount + rec.count
  elif rec.status == 'TODO':
   ntodocount = ntodocount + rec.count
  a = (abbrev,tip1)
  out = '\t'.join(a)
  outarr.append(out)
 ntot = len(recs)
 ntotcount = ndonecount + ntodocount
 print(f'{ntot} tips, {ntotcount} instances')
 print(f'{ndone} tips checked, {ndonecount} instances')
 print(f'{ntot - ndone} questionable, {ntodocount} instances')
 return outarr

known_sources = ('PWG','PWK','GAS','JIM')
def parse_first(line):
 # returns status (TODO or DONE)
 # abbrev
 # count
 # choice  PWG|PWK|GAS|JIM
 # choiceflag  ["=", "x", ""]
 m = re.search(r'^[*] (TODO|DONE) (.*?) : ([0-9]+) : (.*)$',line)
 if m == None:
  print(f'ERROR1: {line}')
  exit(1)
 status = m.group(1)
 abbrev = m.group(2)
 try:
  count =  int(m.group(3))
 except:
  print(f'ERROR count: {line}')
  for i in range(1,5):
   print(f'group({i}) = "{m.group(i)}"')
  exit(1)
 datastr = m.group(4)
 data = re.split(r'[ :]+',datastr)
 data_parses = []
 flagvals = ["=", "x", ""]
 for ix,x in enumerate(data):
  m1 = re.search('^(PWG|PWK|GAS|JIM)([=x]?)$',x)
  if m1 == None:
   print(f'ERROR data = {data}')
   print(f'x: "{x}"')
   print(f'line: {line}')
   for i in range(1,5):
    print(f'group({i}) = "{m.group(i)}"')
   exit(1)
  source = m1.group(1)
  flag = m1.group(2)  # "=", "x", ""
  assert flag in flagvals
  data_parses.append((source,flag))
 # compute choice, choiceflag from data_parses
 choice = None
 choiceflag = None
 for source,flag in data_parses:
  if (flag != "") and (choiceflag != None):
   # error -- two choices!
   print(f'ERROR3: two choices: {data_parses}')
   exit(1)
  if flag != "":
   choice = source
   choiceflag = flag
 # There may be no choiceflag !
 #  in this case, choose choice = 'GAS', if present
 if choiceflag == None:
  for source,flag in data_parses:
   if source == 'GAS':
    choice = source
    choiceflag = flag
 # an error if choiceflag still None
 if choiceflag == None:
  print(f'ERROR4: No choices: {data_parses}')
  exit(1)
 return status,abbrev,count,choice,choiceflag
class Rec:
 def __init__(self,group):
  self.group = group
  a = parse_first(group[0])
  self.status,self.abbrev,self.count,self.choice,self.choiceflag = a
  assert len(group) > 1
  maybe_tips = group[1:]
  tip_found = None
  for x in maybe_tips:
   try:
    m = re.search(r'(PWG|PWK|GAS|JIM) : (.*)$',x)
   except:
    print(f'ERROR: x = {x}')
    exit(1)
   assert m != None
   src = m.group(1)
   tip = m.group(2)
   if self.choice == src:
    if tip_found != None: # duplicate src
     print(f'Rec ERROR: {line}')
     exit(1)
    tip_found = tip
  self.tip = tip_found
  # check consistency between status and choiceflag
  if (self.status == 'DONE') and (self.choiceflag == '='):
   pass
  elif (self.status == 'TODO') and (self.choiceflag in ('','x')):
   pass
  else:
   print(f'ERROR_status :{group[0]}')
   exit(1)
def init_groups(lines):
 group = None
 groups = []
 for iline,line in enumerate(lines):
  if line.startswith('* '):
   group = [line]
   groups.append(group)
  else:
   group.append(line)
 print(f'{len(groups)} groups found')
 return groups

def check_outarr_abbrev(recs):
 for rec in recs:
  abbrev = rec.abbrev
  tip = rec.tip
  m = re.search(r'<id>(.*?)</id>',tip)
  idtip = m.group(1)
  if (abbrev != idtip):
   print(f'abbrev check: {rec.group[0]}')
if __name__=="__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 lines = read_lines(filein)
 groups = init_groups(lines)
 recs = [Rec(group) for group in groups]
 outarr = get_outarr(recs)
 write_lines(fileout,outarr)
 check_outarr_abbrev(recs)
