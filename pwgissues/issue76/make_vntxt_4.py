# coding=utf-8
""" make_vntxt_4.py
"""
import sys,re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,outarr,printFlag=False):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    if out == None:
     out = '?'
    f.write(out+'\n')
 if printFlag:
  print(len(outarr),"lines written to",fileout)

class VNRec:
 def __init__(self,line,L,vol,pc):
  self.line = line
  self.L0 = L
  self.vol = vol
  self.pc = pc
  self.newline = None
  self.k1k2harr = None
  self.Larr = None
  self.entries = None
  
def update_Lvpc(line,L,vol,pc):
 # line starting with []
 # L
 regex1 = r'\[L:([0-9]+)\]'
 # vol
 regex2 = r'\[Page:VN([1-6])-001\]'
 regex2a = r'\[Page:VN([1-6])-[0-9][0-9][0-9]\]'
 # pc
 regex3 = r'\[([1-6]-[0-9][0-9][0-9][0-9])\]'
 regexa = '^%s%s%s' % (regex1,regex2,regex3)
 m = re.search(regexa,line)
 if m != None:
  L = m.group(1)
  vol = m.group(2)
  pc = m.group(3)
  return (L,vol,pc)
 regexb = '^%s%s' %(regex2a,regex3)
 m = re.search(regexb,line)
 if m != None:
  vol = m.group(1)
  pc = m.group(2)
  return (L,vol,pc)  # uses old L
 print('update_Lvpc ERROR')
 print(line)
 print('regexa=%s' % regexa)
 print('regexb=%s' % regexb)
 for reg in (regex1,regex2,regex2aregex3):
  m = re.search(reg,line)
  if m == None:
   print('regex %s fails' % reg)
 exit(1)

def init_recs(lines):
 recs = []
 L = None
 vol = None
 pc = None

 for iline,line in enumerate(lines):
  if line.startswith(';'):
   # skip comment lines
   continue
  if line.strip() == '':
   # skip blank lines
   continue
  if line.startswith(('<F>','<H>')):
   # skip these lines also
   continue
  if line.startswith('['):
   L,vol,pc = update_Lvpc(line,L,vol,pc)
   # no output line
   continue
  if not '¦' in line:
   print('init_recs error 1 in line # ',iline+1)
   print(line)
   exit(1)
  if None in (L,vol,pc):
   print('init_recs error 2 in line # ',iline+1)
   print(line)
   exit(1)
  rec = VNRec(line,L,vol,pc)
  recs.append(rec)
 print('init_recs finds %s records' % len(recs))
 return recs

def write_dups(fileout,dups):
 outarr = []
 for idup,dup in enumerate(dups):
  line,iline1,iline2 = dup
  outarr.append('; %s. lines %s and %s are same' % (idup+1,iline1+1,iline2+1))
  outarr.append(line)
  outarr.append(';')
 print(len(dups),"dups written to",fileout)                
 write_lines(fileout,outarr)
 
def dupcheck(lines):
 known_dups = [
  '<hom>1.</hom> {#anurkAya#}	 ¦ [1.0199] Z. 23 lies: {#anukArya#}.',
  '{#aloha#}	 ¦ [1.0463] lies: <ls>P. 4,1,99.</ls>',
  ';; This is for the column name and has no role in the digitised text.'
  ]
 dups = []
 iline2dups = []
 for iline1,line1 in enumerate(lines):
  for iline2,line2 in enumerate(lines):
   if iline2 <= iline1:
    continue
   if line1 == line2:
    if line1 == '':
     # don't note empty line dups
     continue
    if line1 in known_dups:
     continue
    # add an erroneous dup
    dups.append((line1,iline1,iline2))
    iline2dups.append(iline2)
 print(len(dups),"unexpected duplicates found")
 if len(dups) != 0:
  fileout = 'vntxt_4_dup.txt'
  write_dups(fileout,dups)
  print('debug exit')
 else:
  print('No unknown duplicates found')
  # no dup problem found. return

def get_altk2s():
 d = {}
 d['{#aDiSrayaRa#} und {#aDiSrayitavE#}'] = ('aDiSrayaRa' , 'aDiSrayitavE')
  
 d['{#anAvraska#} und {#anASIrdA#}'] = ('anAvraska' , 'anASIrdA')
 
 d['{#kAmAkzI#} und {#kAmAKyA#}'] = ('kAmAkzI' , 'kAmAKyA')

 d['{#jaMh#} und {#jaMhas#}'] = ('jaMh' , 'jaMhas')

 d['{#wowaka#}, {#wotalA#} und {#wodalatantra#}'] = ('wowaka', 'wotalA' , 'wodalatantra')

 d['{#AgniveSi#}, {#AgniveSI#}'] = ('AgniveSi', 'AgniveSI')

 d['{#Alapana#} und {#Alapti#}'] = ('Alapana' , 'Alapti')

 d['{#gaganaromanTa#}, {#gaganaromantAyita#}'] = ('gaganaromanTa', 'gaganaromantAyita')

 return d

altk2s = get_altk2s()

def k2_to_k1(k2):
 k1 = k2
 for accent in ('\\','/','^'):
  k1 = k1.replace(accent,'')
 # check for unexpected characters in slp1.
 # This is an incomplete list, but suffices for current work.
 x = re.sub(r'[a-zA-Z]','',k1)
 if x != '':
  print('k2_to_k1 error:',k2)
  exit(1)
 return k1

def parse_head(head):
 m1 = re.search(r'^{#([^#]+)#}$',head)
 m2 = re.search(r'^<hom>([0-9]+)\.</hom> {#([^#]+)#}$',head)
 if m1 != None:
  k2 = m1.group(1)
  h = None
  k1 = k2_to_k1(k2)
  a = (k1,k2,h)
  b = [a]
 elif m2 != None:
  h = m2.group(1)
  k2 = m2.group(2)
  k1 = k2_to_k1(k2)
  a = (k1,k2,h)
  b = [a]
 elif head in altk2s:
  k2s = altk2s[head]
  b = []
  for k2 in k2s:
   k1 = k2_to_k1(k2)
   h = None
   a = (k1,k2,h)
   b.append(a)
 else:
  print('parse_head fails:',head)
  h = None
  k2 = None
  k1 = None
  a = (k1,k2,h)
  b = [a]
 return b

def update_k1k2h_rec(rec):
 m = re.search('^(.*?)\t ¦(.*)$',rec.line)
 head = m.group(1)
 body = m.group(2)
 # remove '\t '
 rec.newline = '%s¦%s' %(head,body)
 k1k2harr = parse_head(head)
 rec.k1k2harr = k1k2harr
 
def update_k1k2h(recs):
 for rec in recs:
  update_k1k2h_rec(rec)

def construct_recentries_helper(rec):
 entries = []
 pc = rec.pc
 LEND = '<LEND>'
 for idx,k1k2h in enumerate(rec.k1k2harr):
  k1,k2,h = k1k2h
  L = rec.Larr[idx]  # The L for this entry
  if h == None:
   metaline = '<L>%s<pc>%s<k1>%s<k2>%s' %(L,pc,k1,k2)
  else:
   metaline = '<L>%s<pc>%s<k1>%s<k2>%s<h>%s' %(L,pc,k1,k2,h)
  if idx == 0:
   body = rec.newline
   Lbody = L
  else:
   body = '{{Lbody=%s}}' % Lbody
  entry = [metaline,body,LEND]
  entries.append(entry)
 rec.entries = entries

def construct_entries(recs):
 for rec in recs:
  construct_recentries_helper(rec)
 # all entries
 entries = []
 for rec in recs:
  for entry in rec.entries:
   entries.append(entry)
 print(len(entries),"entries")
 return entries

def write_entries(fileout,entries):
 outarr = []
 for entry in entries:
  for line in entry:
   outarr.append(line)
 write_lines(fileout,outarr,printFlag=True)

def count_entries_by_volume(entries):
 d = {}
 for entry in entries:
  metaline = entry[0]
  m = re.search(r'<pc>(.)',metaline)
  v = m.group(1)
  if v not in d:
   d[v] = 0
  d[v] = d[v] + 1
 for v in d:
  n = d[v]
  print('%s entries in volume %s' % (n,v))

def check_pc_vol(recs):
 nprob = 0
 for rec in recs:
  pcv = rec.pc[0]  # pc = N-pppp
  vol = rec.vol
  if pcv != vol:
   nprob = nprob + 1
 print('check_pc_vol finds %s problems' % nprob)

def get_volincr():
 d = {}
 d['1'] = (0.004,3)
 d['2'] = (0.005,3)
 d['3'] = (0.005,3)
 d['4'] = (0.01,2)
 d['5'] = (0.01,2)
 d['6'] = (0.01,2)
 return d

volincr = get_volincr()

def update_Larr(recs):
 for vol in volincr:
  incr,incrplace = volincr[vol]
  
  recsv = [rec for rec in recs if rec.vol == vol]
  L0 = recsv[0].L0
  Lbase = float(L0)
  L = Lbase
  for irec,rec in enumerate(recsv):
   assert rec.L0 == L0
   Larr = []  
   for k1k2h in rec.k1k2harr:
    L = L + incr
    if incrplace == 2:
     Lstr = '%0.2f' % L
    elif incrplace == 3:
     Lstr = '%0.3f' % L
    else:
     print('update_Larr ERROR 1')
     exit(1)
    # Lstr = Lstr.rstrip('0')  # remove trailing '0' after the decimal
    Larr.append(Lstr)
   rec.Larr = Larr

def update_entries_ltnum(entries):
 n = 0
 for entry in entries:
  # entry = [metaline,body,LEND]
  # revise body
  old = entry[1]
  new = re.sub(r'<([0-9][0-9,. ]*)>', r'{\1}',old)
  if new != old:
   n = n + 1
  entry[1] = new
 print('update_entries_ltnum: %s lines changed' % n)

def update_entries_page(entries):
 # [V.pppp] -> [vgl. [Pagev-pppp]]
 n = 0
 for entry in entries:
  # entry = [metaline,body,LEND]
  # revise body
  old = entry[1]
  new = re.sub(r'\[([0-9])\.([0-9][0-9][0-9][0-9])\]',
               r'[vgl. [Page\1-\2]]',old)
  if new != old:
   n = n + 1
  entry[1] = new
 print('update_entries_page: %s lines changed' % n)

def update_entries_revsup(entries):
 # Append <info n="rev"/> or <info n="sup"/>
 nsup = 0
 nrev = 0
 for entry in entries:
  # entry = [metaline,body,LEND]
  # revise body
  old = entry[1]
  if 'Hinzuzufügen' in old:
   new = old + '<info n="sup"/>'
   nsup = nsup + 1
  else:
   new = old + '<info n="rev"/>'
   nrev = nrev + 1
  entry[1] = new
 print('update_entries_revsup: #rev = %s, # sup = %s' % (nrev,nsup))

if __name__=="__main__":
 filein = sys.argv[1]  # vntxt_3
 fileout = sys.argv[2] # vntxt_4
 lines = read_lines(filein)
 dupcheck(lines)
 recs = init_recs(lines)
 update_k1k2h(recs)
 update_Larr(recs)
 entries = construct_entries(recs)
 update_entries_ltnum(entries)
 update_entries_page(entries)
 update_entries_revsup(entries)
 count_entries_by_volume(entries)
 check_pc_vol(recs)
 write_entries(fileout,entries)
 
