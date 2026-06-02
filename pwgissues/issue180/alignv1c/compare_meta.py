""" compare_meta.py  
 
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

preface = ['<H>{#a#}',''] # lines before first entry

def get_entries(lines):
 entries = []
 entry = None # an array of lines
 n = 0 # number of lines changed
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   entry = []
   entry.append(line)
   continue
  if line.startswith('<LEND>'):
   entry.append(line)
   entries.append(entry)
   entry = None
   continue
  if entry == None:
   continue
  entry.append(line)
 print(f'{len(entries)} entries')
 return entries
 
def get_entrylines(preface_lines,entries):
 a = []
 for x in preface_lines:
  a.append(x)
 ilast = len(entries) - 1
 for i,entry in enumerate(entries):
  for x in entry:
   a.append(x)
  if i != ilast:
   a.append('') # blank line after <LEND>
 return a

def get_metas(entries):
 ans = []
 for entry in entries:
  ans.append(entry[0])  
 return ans
def get_entries_dict(entries):
 d = {}
 for entry in entries:
  meta = entry[0]
  m = re.search('<L>(.*?)<pc>',meta)
  L = m.group(1)
  L0 = float(L)
  assert L0 not in d
  d[L0] = entry
 return d

def parse_meta(meta):
 m = re.search('^<L>(.*?)<pc>(.*?)<k1>(.*?)(<k2>.*)$', meta)
 L = m.group(1)
 pc = m.group(2)
 k1 = m.group(3)
 rest = m.group(4)
 return (L,pc,k1,rest)


def compare_metas(metas1, metas2):
 ans = []
 nmetas1 = len(metas1)
 nmetas2 = len(metas2)
 print(f'# metas1 = {nmetas1}')
 print(f'# metas2 = {nmetas2}')
 assert nmetas1 == nmetas2
 nmetaeq = 0
 for imeta,meta1 in enumerate(metas1):
  meta2 = metas2[imeta]
  if meta1 == meta2:
   nmetaeq = nmetaeq + 1
  ans.append((meta1,meta2))
 print(f'{nmetaeq} metalines are identical, {nmetas1-nmetaeq} differ')
 return ans

def get_diffmetas_outlines(diffmetas):
 outarr = []
 n = 0  # number of metas with same (L,k1)
 for i,diffmeta  in enumerate(diffmetas):
  case = i+1
  meta1,meta2 = diffmeta
  L_1,pc_1,k1_1,rest_1 = parse_meta(meta1)
  L_2,pc_2,k1_2,rest_2 = parse_meta(meta2)
  if (L_1,k1_1) == (L_2,k1_2):
   outarr.append(f'+ {case}')
   n = n + 1
  else: 
   outarr.append(f'- {case}')
  #outarr.append(f'meta1: {meta1}')
  #outarr.append(f'meta2: {meta2}')
  outarr.append(f'<L>{L_1}<k1>{k1_1}')
  outarr.append(f'<L>{L_2}<k1>{k1_2}')
  outarr.append('')
 print(f'{n} metalines with same L-k1, {len(diffmetas) - n } with different L-k1' )
 return outarr

if __name__=="__main__":
 filein1 = sys.argv[1]  # xxx.txt
 filein2 = sys.argv[2] # xxx_base
 fileout = sys.argv[3] # vn_base
 
 lines1 = read_lines(filein1)
 lines2 = read_lines(filein2)
 
 entries1 = get_entries(lines1)
 entries2 = get_entries(lines2)

 metas1 = get_metas(entries1)
 metas2 = get_metas(entries2)

 diffmetas = compare_metas(metas1,metas2)
 outlines = get_diffmetas_outlines(diffmetas)

 write_lines(fileout,outlines)

