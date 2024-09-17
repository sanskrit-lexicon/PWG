# coding=utf-8
""" make_change_prosody.py
"""
from __future__ import print_function
import sys, re,codecs
#import digentry  

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_outrecs(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outrecs),"cases written to",fileout)

def write_changes(fileout,changes):
 outrecs = []
 for c in changes:
  outarr = []
  outarr.append('; -----------------------------------------------------')
  outarr.append('; %s' %c.metaline)
  # c.replacements is a Replacements object
  rep = c.replacements
  outarr.append('; replace %s' % rep.replace)
  outarr.append(';    with %s' % rep.withval)                
  check = rep.check
  if check:
   outarr.append('%s old %s' % (c.lnum,c.oldline))
   outarr.append(';')
   new = c.oldline.replace(rep.replace,rep.withval)
   outarr.append('%s new %s' % (c.lnum,new))
  else:
   outarr.append('%s old %s' % (c.lnum,c.oldline))
   outarr.append('; ?')
   new = rep.oldinit.replace(rep.replace,rep.withval)
   outarr.append('%s new %s' % (c.lnum,new))
   
  outrecs.append(outarr)
 write_outrecs(fileout,outrecs)

def write_outrecs(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outrecs),"cases written to",fileout)

def write_outarr(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

class Change:
 def __init__(self,oldline,newline,metaline,replacements,lnum):
  # a -> b
  self.oldline = oldline
  self.newline = newline
  self.lnum = lnum
  self.metaline = metaline
  self.replacements = replacements

def generate_groups(lines):
 group = None
 for iline,line in enumerate(lines):
  m = re.search(r'^[*] +(<ls.*?</ls>)$',line)
  if m != None:
   group = [m.group(1)]
   continue
  if line == '':
   yield group
   group = None
   continue
  m = re.search(r'(<ls.*?</ls>)',line)
  if m == None:
   print('generate_groups error at line %s: %s' %(iline+1,line))
   exit(1)
  group.append(m.group(1))

class Replacement:
 def __init__(self,line,iline,lines):
  self.status = False
  # (638898): xxxxxxx
  m = re.search(r'^\(([0-9]+)\): (.*)$',line)
  if m == None:
   return
  self.linenum = int(m.group(1))
  self.oldinit  = m.group(2)
  self.status = True
  self.check = None # filled in later
  self.old = None # old line from entries.see init_replacements
  #
  line1 = lines[iline + 1]
  m1 = re.search(r'^replace (.*)$',line1)
  if m1 == None:
   print('replacesments error 1',iline + 1)
   exit(1)
  self.replace = m1.group(1)
  line2 = lines[iline + 2]
  m2 = re.search(r'^with (.*)$',line2)
  if m2 == None:
   print('replacesments error 2',iline + 2)
   exit(1)
  self.withval = m2.group(1)
  return

def init_replacements(filein):
 lines = read_lines(filein)
 x = 0
 recs = []
 d = {}
 for iline,line in enumerate(lines):
  rec = Replacement(line,iline,lines)
  if not rec.status:
   continue
  recs.append(rec)
  key = rec.linenum
  if key in d:
   print('WARNING: duplicate',key)
   continue
   #exit(1)
  d[key] = rec
 print(len(recs),"records initialized")
 return recs,d

def get_prev_metaline(entrylines,ientry):
 ans = None
 while (ientry >= 0):
  line = entrylines[ientry]
  if line.startswith('<L>'):
   ans = line
   break
  else:
   ientry = ientry - 1
 return ans

def check_replacements(recs,entrylines):
 nok = 0
 nprob = 0
 for rec in recs:
  line  = rec.oldinit
  ientry = rec.linenum - 1
  entryline = entrylines[ientry]
  #if entryline == line:
  rec.old = entryline
  if entryline.strip() == line.strip():
   nok = nok + 1
   rec.check = True
  else:
   nprob = nprob + 1
   rec.check = False
  # get preceding metaline
  rec.metaline = get_prev_metaline(entrylines,ientry)
 print('nok=%s, nprob=%s' %(nok,nprob))
 
def get_newline(line,drec):
 dbg = False
 if dbg: print(line)
 lsarr = re.findall(r'<ls.*?</ls>',line)
 replacements = []
 for ls in lsarr:
  if ls not in drec:
   continue
  replacements.append(drec[ls])
  drec[ls].count = drec[ls].count + 1
 if replacements == []:
  return line,replacements
 # generate newline
 newline = line
 for rep in replacements:
  old = rep.old
  new = rep.new
  newline = newline.replace(old,new)
 return newline,replacements

def make_change_rep(rep):
 line = rep.old
 newline = line
 metaline = rep.metaline
 lnum = rep.linenum
 change = Change(line,newline,metaline,rep,lnum)
 return change
 
def make_changes(reps):
 changes = []
 for rep in reps:
  change = make_change_rep(rep)
  changes.append(change)
 return changes

def check_reps(reps):
 n = 0 # total count of rep.count
 for rep in reps:
  n = n + rep.count
  if rep.count == 0:
   print('not used:',rep.old)
 print(n,'count of replacements')


if __name__=="__main__":
 filein = sys.argv[1]  # xxx.txt
 filein1 = sys.argv[2] # C.lines.filled.or.corrected.-.wiki.style.txt
 fileout = sys.argv[3] # change transaction prototypes
 reps,repsd = init_replacements(filein1)
 entrylines = read_lines(filein)
 check_replacements(reps,entrylines)
 
 #exit(1)
 #entries = digentry.init(filein)

 changes = make_changes(reps)
 print(len(changes)," changes")
 #check_reps(reps)
 write_changes(fileout,changes)

