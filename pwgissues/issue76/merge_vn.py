# coding=utf-8
""" merge_vn.py
"""
import sys,re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 print(len(lines),"read from",filein)
 return lines

def write_lines(fileout,outarr,printFlag=False):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    if out == None:
     out = '?'
    f.write(out+'\n')
 if printFlag:
  print(len(outarr),"lines written to",fileout)

def get_vnentries(lines):
 entries = []
 for iline, line in enumerate(lines):
  if not line.startswith('<L>'):
   continue
  metaline = line
  body = lines[iline+1]
  lend = lines[iline+2]
  entry = [metaline,body,lend]
  entries.append(entry)
 return entries

vnvols = ('1','2','3','4','5','6')

def get_vnd(entries):
 d = {}
 for vol in vnvols:
  d[vol] = []
 # 
 for entry in entries:
  metaline,body,lend = entry
  m = re.search(r'<L>(.*?)<pc>(.*?)<',metaline)
  L = m.group(1)
  pc = m.group(2)
  m1 = re.search(r'^([1-6])-([0-9][0-9][0-9][0-9])$',pc)
  vol = m1.group(1)
  assert vol in vnvols
  d[vol].append(entry)
 for vol in vnvols:
  print('%3s entries for vn volume %s' %(len(d[vol]),vol))
 return d

def metaline_to_Lbase(metaline):
 m = re.search(r'<L>(.*?)<pc>(.*?)<',metaline)
 L = m.group(1)
 Lbase = re.sub(r'[.].*$', '',L)
 return Lbase

def get_vnLbase(vnd):
 d = {}
 for vol in vnvols:
  entries = vnd[vol] # list of entries with given volume
  entry = entries[0]
  metaline = entry[0]
  Lbase0 = metaline_to_Lbase(metaline)
  d[vol] = Lbase0
  # check rest of entries have same L
  for entry in entries:
   Lbase = metaline_to_Lbase(entry[0])
   assert Lbase == Lbase0
 if True:
  for vol in vnvols:
   print('%3s Lbase = %s' %(vol,d[vol]))
 return d

def get_Lbase_lend():
 pass

def get_lend_iline(vnLbase_inverse,lines):
 # lines is array of pwg lines
 d = {}
 for iline,line in enumerate(lines):
  if not line.startswith('<L>'):
   continue
  metaline = line
  m = re.search(r'<L>(.*?)<pc>(.*?)<',metaline)
  L = m.group(1)
  if L not in vnLbase_inverse:
   continue
  Lbase = L
  vol = vnLbase_inverse[Lbase]
  iline1 = iline
  while True:
   iline1 = iline1 + 1
   line1 = lines[iline1]
   if line1 == '<LEND>':
    break
  d[iline1] = vol
 if True:
  for iline1 in d:
   vol = d[iline1]
   print('vol %s: iline1=%s' %(vol,iline1))
 return d

def get_vnLbase_inverse(vnLbase):
 d = {} # inverse vnLbase 
 for vol in vnLbase:
  Lbase = vnLbase[vol]
  assert Lbase not in d
  d[Lbase] = vol
 return d

def merge(lines,vnLbase,vnd):
 vnLbase_inverse  = get_vnLbase_inverse(vnLbase)
 lend_ilined = get_lend_iline(vnLbase_inverse,lines)
 print(lend_ilined)
 newlines = []
 for iline,line in enumerate(lines):
  newlines.append(line)
  if iline in lend_ilined:
   vol = lend_ilined[iline]
   vnentries = vnd[vol]
   for vnentry in vnentries:
    # extra blank line
    newlines.append('')
    # the vnlines to insert
    for vnline in vnentry:
     newlines.append(vnline)
 return newlines

if __name__=="__main__":
 filein = sys.argv[1]  # temp_pwg_1
 filein1 = sys.argv[2] # vntxt_4.txt
 fileout = sys.argv[3] # temp_pwg_2
 vnlines = read_lines(filein1)
 vnentries = get_vnentries(vnlines)
 vnd = get_vnd(vnentries)
 vnLbase = get_vnLbase(vnd)
 lines = read_lines(filein)  # pwg
 print(len(lines),"lines from",filein)
 newlines = merge(lines,vnLbase,vnd)
 write_lines(fileout,newlines,printFlag=True)
 
 
