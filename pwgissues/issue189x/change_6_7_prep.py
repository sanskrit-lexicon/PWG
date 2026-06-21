""" change_6_7_prep.py
 
"""
import sys,re
import codecs
# import os.path,time
LBC = ' 🞄'  # line-break replaces certain '\n'
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
 # print(f'{len(entries)} entries')
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

def gather_ab(entry):
 # entry is a sequence of strings
 # first entry is metaline
 # last entry is <LEND>
 entrydata = ' '.join(entry[1:-1])
 allparts = re.split('(<is[^>]*>[^<]*?</is>)',entrydata)
 return allparts

def gather_ab_1(entry):
 # entry is a sequence of strings
 # first entry is metaline
 # last entry is <LEND>
 entrydata = ' '.join(entry[1:-1])
 allparts = re.split('(<is[^>]*>[^<]*?</is>)',entrydata)
 alltags = [x for x in allparts if x.startswith('<is')]
 return alltags

def all_diffs(e1,e2):
 a1 = gather_ab(e1)
 a2 = gather_ab(e2)
 n1 = len(a1)
 n2 = len(a2)
 assert n1 == n2
 diffs = []
 for i in range(n1):
  x1 = a1[i]
  x2 = a2[i]
  flag1 = x1.startswith('<is')
  flag2 = x2.startswith('<is')
  # x1 and x2 both start with '<is' OR neither starts with '<is'
  assert (flag1 and flag2) or ((not flag1) and (not flag2))
  if (flag1 and flag2) and (x1 != x2):
   diffs.append((x1,x2))
 return diffs

def get_L(meta):
 m = re.search(r'<L>(.*?)<pc>',meta)
 L = m.group(1)
 return L

def get_tags(lines):
 regex_raw = '<is[^>]*>[^<]*?</is>'
 regex = re.compile(regex_raw)
 ans = []
 for iline,line in enumerate(lines):
  i = 0  
  for m in re.finditer(regex,line):
   tag = m.group(0)
   a = (iline,i,tag)
   ans.append(a)
 return ans

def tags_compare(tag1,tag2,regex):
 try:
  m1 = re.search(regex,tag1)
 except:
  print(f'ERROR in re.search')
  print(f'tag1={tag1}')
  print(f'regex={regex}')
  exit(1)
 attr1 = m1.group(1)
 ab1 = m1.group(2)
 #
 m2 = re.search(regex,tag2)
 attr2 = m2.group(1)
 ab2 = m2.group(2)
 #
 flag = ab1 == ab2
 return flag

def tags_comparable(tags1,tags2):
 regex_raw = r'^<is([^>]*)>([^<]*?)</is>$'
 regex = re.compile(regex_raw)
 diffs = []
 for itag1,tag1 in enumerate(tags1):
  tag2 = tags2[itag1]
  iline1,i1,t1 = tag1
  iline2,i2,t2 = tag2
  assert tags_compare(t1,t2,regex)
  if t1 != t2:
   diff = (iline1,t1,t2)
   diffs.append(diff)
 print(f'All tags are comparable')
 # generate details of differences
 print(f'Returning {len(diffs)} differences')
 return diffs
if __name__=="__main__":
 filein1 = sys.argv[1]  # base c
 filein2 = sys.argv[2]
 fileout = sys.argv[3] # unadjusted base
 
 lines1 = read_lines(filein1)
 tags1 = get_tags(lines1)
 print(f'{len(tags1)} tags in {filein1}')
 lines2 = read_lines(filein2)
 tags2 = get_tags(lines2)
 print(f'{len(tags2)} tags in {filein2}')

 ntags1 = len(tags1)
 ntags2 = len(tags2)
 assert ntags1 == ntags2
 diffs = tags_comparable(tags1,tags2)
 outlines = []
 for diff in diffs:
  (iline,oldtag,newtag) = diff
  lnum = str(iline+1)
  a = (lnum,oldtag,newtag)
  out = '\t' .join(a)
  outlines.append(out)
 write_lines(fileout,outlines)
