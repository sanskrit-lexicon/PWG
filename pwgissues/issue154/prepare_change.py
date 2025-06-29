# coding=utf-8
""" prepare_change.py
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
 print(len(outarr),"cases written to",fileout)

def get_unique_strings(lines):
 ans = []  # list of strings returned
 n = 0
 d = {} # for unique
 ndup = 0 # number of duplicate lines
 for line in lines:
  n = n + 1
  if line in d:
   ndup = ndup + 1
  else:
   d[line] = True
   ans.append(line)
 print(len(ans),"unique strings found")
 print(ndup,"duplicates noticed")
 return ans

def mark_strings(lines,strings):
 newlines = []
 markc = '@'  # this character
 print('marking strings with "%s"' % markc)
 n = 0 # number of lines with at least one string marked
 for line in lines:
  newline = line
  for s in strings:
   if s in newline:
    # '@' does not occur in
    newline = newline.replace(s,markc+s)
  newlines.append(newline)
  if newline != line:
   n = n + 1
 print(n,'lines marked')
 return newlines

def get_manual_data():
 dataraw="""
<ls n="AK. 3,">4,32 (28 COLEBR.),9.</ls>	<ls n="AK. 3,">4,32,9.</ls> (<ls>COLEBR. 3,4,28,9.</ls>)
<ls n="AK.">3,4,32 (28 COLEBR.),18.</ls>	<ls n="AK.">3,4,32,18.</ls> (<ls>COLEBR. 3,4,28,18.</ls>)
<ls>AK. 3,3,43 (COLEBR. 42).</ls>	<ls>AK. 3,3,43.</ls> (<ls>COLEBR. 3,3,42.</ls>)
<ls>AK. 3,4,32 (28 COLEBR.),5.</ls>	<ls>AK. 3,4,32,5.</ls> (<ls>COLEBR. 3,4,28,5.</ls>)
<ls>AK. 3,4,32, [COL. 28,] 10.</ls>	<ls>AK. 3,4,32,10.</ls> [<ls>COL. 3,4,28,10.</ls>]
<ls>AK. 3,4,32,18 (28).</ls>	<ls>AK. 3,4,32,18.</ls> (<ls>COL. 3,4,28,18.</ls>)
<ls n="AK.">II. 167.</ls>	<ls>H. 167.</ls>
<ls n="AK.">3,5,2 5.</ls>	<ls n="AK.">3,5,2</ls> <ls n="AK. 3,5,">5.</ls>
<ls>AK. 2,8,2</ls>, <ls n="AK.">67.H. 366.</ls>	       <ls>AK. 2,8,2,67.</ls> <ls>H. 366.</ls>
<ls>AK. 3,3,42.</ls> [<ls>COL. 41.</ls>])	<ls>AK. 3,3,42.</ls> [<ls>COL. 3,3,41.</ls>])
<ls>AK. 3,3,39.</ls>, (<ls>COL. 38</ls>,) <ls>Sch.</ls>	<ls>AK. 3,3,39</ls>, (<ls>COL. 3,3,38</ls>,) <ls>Sch.</ls>
<ls>AK. 3,3,40.</ls> (<ls>COLEBR. 39.</ls>)	<ls>AK. 3,3,40.</ls> (<ls>COLEBR. 3,3,39.</ls>)
<ls>AK. 3,3,39</ls> (<ls>COLEBR. 38).</ls>	<ls>AK. 3,3,39.</ls> (<ls>COLEBR. 3,3,38.</ls>)
<ls>AK. 3,4,32</ls> (<ls>COLEBR. 28),12.</ls>	<ls>AK. 3,4,32,12.</ls> (<ls>COLEBR. 3,4,28,12.</ls>)
<ls>AK. 3,4,32</ls> (<ls>COLEBR. 28),2.</ls>	<ls>AK. 3,4,32,2.</ls> (<ls>COLEBR. 3,4,28,2.</ls>)
<ls>AK. 3,4,32</ls> (<ls>COLEBR. 28),9.</ls>	<ls>AK. 3,4,32,9.</ls> (<ls>COLEBR. 3,4,28,9.</ls>)
"""
 datarr = dataraw.splitlines()
 print(len(datarr),"manual lines")
 recs = []
 for data in datarr:
  if data == "":
   continue
  try:
   old,new = data.split('\t')
  except:
   print('data error:\n"%s"' % data)
   exit(1)
  recs.append( (old,new) )
 return recs

 
def make_change_manual(rec):
 manualrecs = get_manual_data()
 x = rec.old
 for old,new in manualrecs:
  if x == old:
   rec.new = new
   rec.method = 'man'
   return
 
def make_change(rec):
 # 1. (COL. N)
 regex = r'^<ls>AK. ([0-9]+),([0-9]+),([0-9]+) \((COL.) ([0-9]+)\),([0-9]+)\.</ls>$'
 x = rec.old
 m = re.search(regex,x)
 if m != None:
  b = m.group(1)
  c = m.group(2)
  s = m.group(3)
  colname = m.group(4)
  sc = m.group(5) # colebrooke section
  v = m.group(6)
  newd = '<ls>AK. %s,%s,%s,%s.</ls>' %(b,c,s,v)
  newc = '<ls>%s %s,%s,%s,%s.</ls>' %(colname,b,c,sc,v)
  newc1 = '(%s)' % newc
  new = '%s %s' % (newd, newc1)
  rec.new = new
  rec.method = '1'
  return 
 # 2. (COLEBR. N)
 regex = r'^<ls>AK. ([0-9]+),([0-9]+),([0-9]+) \((COLEBR.) ([0-9]+)\),([0-9]+)\.</ls>$'
 m = re.search(regex,x)
 if m != None:
  b = m.group(1)
  c = m.group(2)
  s = m.group(3)
  colname =  m.group(4)
  sc = m.group(5) # colebrooke section
  v = m.group(6)
  newd = '<ls>AK. %s,%s,%s,%s.</ls>' %(b,c,s,v)
  newc = '<ls>%s %s,%s,%s,%s.</ls>' %(colname,b,c,sc,v)
  newc1 = '(%s)' % newc
  new = '%s %s' % (newd, newc1)
  rec.new = new
  rec.method = '2'
  return
 # 3. (N)    Use 'COL.' for ls abbrev
 regex = r'^<ls>AK. ([0-9]+),([0-9]+),([0-9]+) \(()([0-9]+)\),([0-9]+)\.</ls>$'
 m = re.search(regex,x)
 if m != None:
  b = m.group(1)
  c = m.group(2)
  s = m.group(3)
  assert m.group(4) == ''
  colname = 'COL.' # why no space required?
  sc = m.group(5) # colebrooke section
  v = m.group(6)
  newd = '<ls>AK. %s,%s,%s,%s.</ls>' %(b,c,s,v)
  newc = '<ls>%s %s,%s,%s,%s.</ls>' %(colname,b,c,sc,v)
  newc1 = '(%s)' % newc
  new = '%s %s' % (newd, newc1)
  rec.new = new
  rec.method = '3'
  return
 # 3a. (N)    Use 'COL.' for ls abbrev
 regex = r'^<ls n="AK.">([0-9]+),([0-9]+),([0-9]+) \(()([0-9]+)\),([0-9]+)\.</ls>$'
 m = re.search(regex,x)
 if m != None:
  b = m.group(1)
  c = m.group(2)
  s = m.group(3)
  assert m.group(4) == ''
  colname = 'COL.' # why no space required?
  sc = m.group(5) # colebrooke section
  v = m.group(6)
  newd = '<ls n="AK.">%s,%s,%s,%s.</ls>' %(b,c,s,v)
  newc = '<ls>%s %s,%s,%s,%s.</ls>' %(colname,b,c,sc,v)
  newc1 = '(%s)' % newc
  new = '%s %s' % (newd, newc1)
  rec.new = new
  rec.method = '3a'
  return
 # 3c. (N)    Use 'COL.' for ls abbrev
 regex = r'^<ls n="AK. ([0-9]+),([0-9]+),">([0-9]+) \(()([0-9]+)\),([0-9]+)\.</ls>$'
 m = re.search(regex,x)
 if m != None:
  b = m.group(1)
  c = m.group(2)
  s = m.group(3)
  assert m.group(4) == ''
  colname = 'COL.' # why no space required?
  sc = m.group(5) # colebrooke section
  v = m.group(6)
  newd = '<ls n="AK. %s,%s,">%s,%s.</ls>' %(b,c,s,v)
  newc = '<ls>%s %s,%s,%s,%s.</ls>' %(colname,b,c,sc,v)
  newc1 = '(%s)' % newc
  new = '%s %s' % (newd, newc1)
  rec.new = new
  rec.method = '3c'
  return
 # 3d. (N)    Use 'COL.' for ls abbrev
 regex = r'^<ls n="AK. ([0-9]+),([0-9]+),([0-9]+) \(()([0-9]+)\),">([0-9]+)\.</ls>$'
 m = re.search(regex,x)
 if m != None:
  b = m.group(1)
  c = m.group(2)
  s = m.group(3)
  assert m.group(4) == ''
  colname = 'COL.' # why no space required?
  sc = m.group(5) # colebrooke section
  v = m.group(6)
  newd = '<ls n="AK. %s,%s,%s,">%s.</ls>' %(b,c,s,v)
  newc = '<ls>%s %s,%s,%s,%s.</ls>' %(colname,b,c,sc,v)
  newc1 = '(%s)' % newc
  new = '%s %s' % (newd, newc1)
  rec.new = new
  rec.method = '3d'
  return
 # 1a. (COL. N)
 regex = r'^<ls n="AK.">([0-9]+),([0-9]+),([0-9]+) \((COL.) ([0-9]+)\),([0-9]+)\.</ls>$'
 m = re.search(regex,x)
 if m != None:
  b = m.group(1)
  c = m.group(2)
  s = m.group(3)
  colname = m.group(4)
  sc = m.group(5) # colebrooke section
  v = m.group(6)
  newd = '<ls n="AK.">%s,%s,%s,%s.</ls>' %(b,c,s,v)
  newc = '<ls>%s %s,%s,%s,%s.</ls>' %(colname,b,c,sc,v)
  newc1 = '(%s)' % newc
  new = '%s %s' % (newd, newc1)
  rec.new = new
  rec.method = '1a'
  return
 # 1b. (COL. N)
 regex = r'^<ls n="AK. ([0-9]+),">([0-9]+),([0-9]+) \((COL.) ([0-9]+)\),([0-9]+)\.</ls>$'
 m = re.search(regex,x)
 if m != None:
  b = m.group(1)
  c = m.group(2)
  s = m.group(3)
  colname = m.group(4)
  sc = m.group(5) # colebrooke section
  v = m.group(6)
  newd = '<ls n="AK. %s,">%s,%s,%s.</ls>' %(b,c,s,v)
  newc = '<ls>%s %s,%s,%s,%s.</ls>' %(colname,b,c,sc,v)
  newc1 = '(%s)' % newc
  new = '%s %s' % (newd, newc1)
  rec.new = new
  rec.method = '1b'
  return
 # 1d. (N)    Use 'COL.' for ls abbrev
 regex = r'^<ls n="AK. ([0-9]+),([0-9]+),([0-9]+) \((COL.) ([0-9]+)\),">([0-9]+)\.</ls>$'
 m = re.search(regex,x)
 if m != None:
  b = m.group(1)
  c = m.group(2)
  s = m.group(3)
  assert m.group(4) == 'COL.'
  colname = 'COL.' # why no space required?
  sc = m.group(5) # colebrooke section
  v = m.group(6)
  newd = '<ls n="AK. %s,%s,%s,">%s.</ls>' %(b,c,s,v)
  newc = '<ls>%s %s,%s,%s,%s.</ls>' %(colname,b,c,sc,v)
  newc1 = '(%s)' % newc
  new = '%s %s' % (newd, newc1)
  rec.new = new
  rec.method = '1d'
  return
 # 2a. (COL. N)
 regex = r'^<ls n="AK.">([0-9]+),([0-9]+),([0-9]+) \((COLEBR.) ([0-9]+)\),([0-9]+)\.</ls>$'
 m = re.search(regex,x)
 if m != None:
  b = m.group(1)
  c = m.group(2)
  s = m.group(3)
  colname = m.group(4)
  sc = m.group(5) # colebrooke section
  v = m.group(6)
  newd = '<ls n="AK.">%s,%s,%s,%s.</ls>' %(b,c,s,v)
  newc = '<ls>%s %s,%s,%s,%s.</ls>' %(colname,b,c,sc,v)
  newc1 = '(%s)' % newc
  new = '%s %s' % (newd, newc1)
  rec.new = new
  rec.method = '2a'
  return
 # 2c. (COL. N)
 regex = r'^<ls n="AK. ([0-9]+),([0-9]+),">([0-9]+) \((COLEBR.) ([0-9]+)\),([0-9]+)\.</ls>$'
 m = re.search(regex,x)
 if m != None:
  b = m.group(1)
  c = m.group(2)
  s = m.group(3)
  colname = m.group(4)
  sc = m.group(5) # colebrooke section
  v = m.group(6)
  newd = '<ls n="AK. %s,%s,">%s,%s.</ls>' %(b,c,s,v)
  newc = '<ls>%s %s,%s,%s,%s.</ls>' %(colname,b,c,sc,v)
  newc1 = '(%s)' % newc
  new = '%s %s' % (newd, newc1)
  rec.new = new
  rec.method = '2c'
  return
 # 2d. (N)    Use 'COL.' for ls abbrev
 regex = r'^<ls n="AK. ([0-9]+),([0-9]+),([0-9]+) \((COLEBR.) ([0-9]+)\),">([0-9]+)\.</ls>$'
 m = re.search(regex,x)
 if m != None:
  b = m.group(1)
  c = m.group(2)
  s = m.group(3)
  assert m.group(4) == 'COLEBR.'
  colname = 'COLEBR.' # why no space required?
  sc = m.group(5) # colebrooke section
  v = m.group(6)
  newd = '<ls n="AK. %s,%s,%s,">%s.</ls>' %(b,c,s,v)
  newc = '<ls>%s %s,%s,%s,%s.</ls>' %(colname,b,c,sc,v)
  newc1 = '(%s)' % newc
  new = '%s %s' % (newd, newc1)
  rec.new = new
  rec.method = '2d'
  return
 # 4. (N)    Use 'COL.' for ls abbrev -- no section
 regex = r'^<ls>AK. ([0-9]+),([0-9]+),([0-9]+) \(()([0-9]+)\)\.</ls>$'
 m = re.search(regex,x)
 if m != None:
  b = m.group(1)
  c = m.group(2)
  v = m.group(3)
  assert m.group(4) == ''
  colname = 'COL.' # why no space required?
  vc = m.group(5) # colebrooke verse
  newd = '<ls>AK. %s,%s,%s.</ls>' %(b,c,v)
  newc = '<ls>%s %s,%s,%s.</ls>' %(colname,b,c,vc)
  newc1 = '(%s)' % newc
  new = '%s %s' % (newd, newc1)
  rec.new = new
  rec.method = '4'
  return
 # revert to manual

 make_change_manual(rec)
 return
 
class Change:
 def __init__(self,string):
  self.old = string
  self.new = None
  self.method = None
  make_change(self)

def write_changes(fileout,changes):
 outarr = []
 # sort output by method
 changes1 = sorted(changes, key = lambda x: str(x.method) + str(x.old))
 n = 0 # number not changed
 for change in changes1:
  new = change.new
  if new == None:
   new = '?'
   n = n + 1
  method = change.method
  out = '%s\t%s\tmethod=%s' %(change.old,change.new,change.method)
  outarr.append(out)
 write_lines(fileout,outarr)
 print(n,"changes not yet done")
 
if __name__=="__main__":
 #filein = sys.argv[1]  # kosha
 filein1 = sys.argv[1] # source of strings used to modify kosha
 fileout = sys.argv[2] # revised filein1
 #lines = read_lines(filein)
 lines1 = read_lines(filein1,commentFlag=True)
 
 strings = get_unique_strings(lines1)
 changes = [Change(s) for s in strings]
 write_changes(fileout,changes)
 
 exit(1)              
 newlines = mark_strings(lines,strings)
 write_lines(fileout,newlines)
 
