# coding=utf-8
""" prepare_3b.py  revised. so oldparms (parts[4]) present in input/output
Also, a 'pc: ' partial print-change line
"""
from __future__ import print_function
import sys, re, codecs

def read_lines(filein,commentFlag=False):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines1 = [x.rstrip('\r\n') for x in f]
 if commentFlag:
  # remove 'comments' - lines start with ';'
  lines = [x for x in lines1 if not x.startswith(';')]
  print(len(lines),"kept.")
  print(len(lines1),'lines read from',filein)
 else:
  lines = lines1
  print(len(lines1),'lines read from',filein)
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"lines written to",fileout)

def write_changes(fileout,changes):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in changes:
   for out in outarr:
    f.write(out+'\n')  
 print(len(changes),"change templates written to",fileout)
 
class REPL:
 def __init__(self,line):
  self.line = line
  parts = line.split('\t')
  assert len(parts) == 6
  self.status = parts[0]  # None
  assert self.status == 'None'
  self.lnum = int(parts[1])  # line-number in kosha
  self.k1 = parts[2]
  self.lsref = parts[3]  # ls element to change
  self.oldparms = parts[4]
  self.newparms = parts[5]  # correction to oldparms
  self.koshaline = None  # filled in later
  self.meta = None # filled in later
  
def repls_d(repls):
 d = {}
 for repl in repls:
  lnum = repl.lnum
  if lnum not in d:
   d[lnum] = []
  d[lnum].append(repl)
 lnums = d.keys()
 print(len(lnums),'lines to change')
 return d

def apply_repls_v0(lines,replsd):
 # lines of dictionary.
 newlines = []
 nchg = 0 # number of lines changed
 for iline,line in enumerate(lines):
  lnum = iline + 1
  if lnum not in replsd:
   continue
  repls = replsd[lnum]
  for repl in repls:
   repl.koshaline = line
  nchg = nchg + 1
 print('apply_repls: %s lines to change' % nchg)
 return newlines

def apply_repls(lines,replsd):
 # lines of dictionary.
 # also get metaline
 newlines = []
 nchg = 0 # number of lines changed
 meta = None
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   meta = line
  if line.startswith('<LEND>'):
   meta = None
  lnum = iline + 1
  if lnum not in replsd:
   continue
  repls = replsd[lnum]
  for repl in repls:
   repl.koshaline = line
   repl.meta = meta
  nchg = nchg + 1
 print('apply_repls: %s lines to change' % nchg)
 return newlines

def get_pcline_lsref(lsref):
 m = re.search('^<ls(.*?)>(.*?)</ls>$',lsref)
 attr = m.group(1)
 body = m.group(2)
 if attr == '': # no attributes
  return body
 # change representation of attributes
 m1 = re.search(r'^ n="(.*)"$',attr)
 attr1 = m1.group(1)
 new = f'({attr1}){body}'
 return new

def make_change(repls,ncase):
 # repls with same lnum
 # return a 'change' transaction
 outarr = []
 repl0 = repls[0] # first REPL
 lnum = repl0.lnum
 k1 = repl0.k1
 koshaline = repl0.koshaline
 meta = repl0.meta
 # extract 'L' from meta
 m = re.search(r'<L>(.*?)<pc>.*?<k1>(.*?)<k2',meta)
 L = m.group(1)
 metak1 = m.group(2)
 assert k1 == metak1
 assert koshaline != None
 outarr.append(f'; case {ncase:03d} {k1} ---')
 outarr.append(f'; {meta}')
 outarr.append('%s old %s' % (lnum,koshaline))
 pclines = []
 for irepl,repl in enumerate(repls):
  assert repl.lnum == lnum
  assert repl.k1 == k1
  assert repl.koshaline == koshaline
  # comments  on this repl
  try:
   assert repl.lsref in koshaline
  except:
   print(f'{repl.lsref} not in koshaline')
   outarr.append(f'; WARNING: lsref not in koshaline')
  outarr.append(f'; ({irepl + 1:02d})  {repl.lsref}')
  outarr.append(f';       {repl.oldparms}')
  newparms = re.sub(r'^[ :]+','',repl.newparms)
  outarr.append(f';       {newparms}')
  # partial print-change line
  pclsref = get_pcline_lsref(repl.lsref)
  #pcline = f'; pc: {L} : {k1} : {repl.lsref} : {repl.lsref} : t'
  pcline = f'; pc: {L} : {k1} : {pclsref} : {pclsref} : t'
  pclines.append(pcline)
  #outarr.append(pcline)
 outarr.append('%s new %s' % (lnum,koshaline))
 for pcline in pclines:
  outarr.append(pcline)
 outarr.append(';')
 return outarr

def make_changes(d):
 changes = []
 for ncase,lnum in enumerate(d):
  change = make_change(d[lnum],ncase + 1)
  changes.append(change)
 return changes

if __name__=="__main__":
 filein = sys.argv[1]  # kosha
 filein1 = sys.argv[2] # line string replacements
 fileout = sys.argv[3] # revised kosha
 lines = read_lines(filein)
 lines1 = read_lines(filein1,commentFlag=True)
 
 repls = [REPL(line) for line in lines1]
 d = repls_d(repls)
 apply_repls(lines,d)
 changes = make_changes(d)
 write_changes(fileout,changes) # template for changes
 
