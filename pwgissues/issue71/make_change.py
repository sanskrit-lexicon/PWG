# coding=utf-8
""" make_change.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry  

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
  for rep in c.replacements:
   outarr.append('; oldls:%s' % rep.old)
   outarr.append('; newls:%s' % rep.new)
  outarr.append('%s old %s' % (c.lnum,c.oldline))
  outarr.append(';')
  outarr.append('%s new %s' % (c.lnum,c.newline))
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
 def __init__(self,old,new):
  self.old = old
  self.new = new
  self.count = 0
  
def init_replacements(filein):
 lines = read_lines(filein)
 groups = list(generate_groups(lines))
 print("init_replacements: %s groups" % len(groups))
 reps = []
 d = {}
 for group in groups:
  old = group[0]
  new = ' '.join(group[1:])
  rep = Replacement(old,new)
  if old in d:
   print('init_replacements skipping duplicate',old)
   continue
  reps.append(rep)
  d[old] = rep
 return reps,d

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

def make_changes(entries,repsd):
 changes = []
 for ientry,e in enumerate(entries):
  for iline,line in enumerate(e.datalines):
   newline,replacements = get_newline(line,repsd)
   if newline == line:
    continue
   metaline = e.metaline
   lnum = e.linenum1 + iline + 1
   change = Change(line,newline,metaline,replacements,lnum)
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
 filein1 = sys.argv[2] # link_change_X_ok.txt
 fileout = sys.argv[3] # change transactions
 reps,repsd = init_replacements(filein1)
 entries = digentry.init(filein)

 changes = make_changes(entries,repsd)
 print(len(changes),"lines changes")
 check_reps(reps)
 write_changes(fileout,changes)

