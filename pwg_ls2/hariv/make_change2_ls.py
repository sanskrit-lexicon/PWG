#-*- coding:utf-8 -*-
"""make_change2_ls.py
"""
from __future__ import print_function
import sys, re,codecs
from parseheadline import parseheadline

class Entry(object):
 Ldict = {}
 def __init__(self,lines,linenum1,linenum2):
  # linenum1,2 are int
  self.metaline = lines[0]
  self.lend = lines[-1]  # the <LEND> line
  self.datalines = lines[1:-1]  # the non-meta lines
  # parse the meta line into a dictionary
  #self.meta = Hwmeta(self.metaline)
  self.metad = parseheadline(self.metaline)
  self.linenum1 = linenum1
  self.linenum2 = linenum2
  #L = self.meta.L
  L = self.metad['L']
  if L in self.Ldict:
   print("Entry init error: duplicate L",L,linenum1)
   exit(1)
  self.Ldict[L] = self
  self.lsarr = []
  
def init_entries(filein):
 # slurp lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [line.rstrip('\r\n') for line in f]
 recs=[]  # list of Entry objects
 inentry = False  
 idx1 = None
 idx2 = None
 for idx,line in enumerate(lines):
  if inentry:
   if line.startswith('<LEND>'):
    idx2 = idx
    entrylines = lines[idx1:idx2+1]
    linenum1 = idx1 + 1
    linenum2 = idx2 + 1
    entry = Entry(entrylines,linenum1,linenum2)
    recs.append(entry)
    # prepare for next entry
    idx1 = None
    idx2 = None
    inentry = False
   elif line.startswith('<L>'):  # error
    print('init_entries Error 1. Not expecting <L>')
    print("line # ",idx+1)
    print(line.encode('utf-8'))
    exit(1)
   else: 
    # keep looking for <LEND>
    continue
  else:
   # inentry = False. Looking for '<L>'
   if line.startswith('<L>'):
    idx1 = idx
    inentry = True
   elif line.startswith('<LEND>'): # error
    print('init_entries Error 2. Not expecting <LEND>')
    print("line # ",idx+1)
    print(line.encode('utf-8'))
    exit(1)
   else: 
    # keep looking for <L>
    continue
 # when all lines are read, we should have inentry = False
 if inentry:
  print('init_entries Error 3. Last entry not closed')
  print('Open entry starts at line',idx1+1)
  exit(1)

 print(len(lines),"lines read from",filein)
 print(len(recs),"entries found")
 return recs

class Change(object):
 def __init__(self,metaline,lnum,old,new):
  self.metaline = metaline
  self.lnum = lnum
  self.old = old
  self.new = new

def init_strings(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  stringlist = [line.rstrip('\r\n') for line in f]
  stringset = set(stringlist) # handles duplicates, if any
 print(len(stringset),"strings read from",filein)
 return stringset

def change_ls_matching_given(line,stringset):
 def f(m):
  ans = m.group(0)
  ls = m.group(1)
  if ans in stringset:
   ans = '<ls>[%s]</ls>'%ls
  return ans
 newline = re.sub(r'<ls>(.*?)</ls>',f,line)
 return newline

def write_changes(fileout,changes):
 outrecs = []
 for change in changes:
  outarr = []
  outarr.append('; -------------------------------------')
  outarr.append('; ' + change.metaline)
  outarr.append('%s old %s' %(change.lnum,change.old))
  outarr.append('; ')
  outarr.append('%s new %s' %(change.lnum,change.new))
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(outrecs),"records written to",fileout)

def change_ls_matching_given_1(line,lnum):
 def f(m):
  lsname = m.group(1)
  versedata = m.group(2)
  verseparts = versedata.split(' ')
  orig = m.group(0)
  if len(verseparts) in [1]:
   return orig
  vparts = []
  versetypes = []
  malformed = False
  remainder = versedata.lstrip(' ')
  lsarr = []
  p = None
  while remainder != '':
   m1 = re.search(r'^([0-9]+[.])(.*)$',remainder)
   if m1:
    v = m1.group(1)
    rest = m1.group(2)
    if len(lsarr) == 0:
     ls = '<ls>%s %s</ls>' % (lsname,v)
    else:
     ls = '<ls n="%s">%s</ls>' % (lsname,v)
    lsarr.append(ls)
    remainder = rest.lstrip(' ')
    continue
   # try same m1 but with no period and at end
   m1 = re.search(r'^([0-9]+)$',remainder)
   if m1:
    v = m1.group(1)
    rest = '' # m1.group(2)
    if len(lsarr) == 0:
     print('_6 data error b',orig)
     return orig
    else:
     ls = '<ls n="%s">%s</ls>' % (lsname,v)
    lsarr.append(ls)
    remainder = rest.lstrip(' ')
    continue
   # handle fg. and fgg.
   m1 = re.search(r'^(fgg?[.])(.*)$',remainder)
   if m1:
    if len(lsarr) == 0:
     # error:
     print('_6 data error a',orig)
     return orig
    x = m1.group(1)
    prev_ls = lsarr[-1]
    ls = prev_ls.replace('</ls>',' %s</ls>' % x)
    lsarr[-1] = ls
    rest = m1.group(2)
    remainder = rest.lstrip(' ')
    continue
   # error
   print('_6 data error c',orig)
   #print('remainder="%s"' % remainder)
   fdbg.write(';--------------------------\n')
   fdbg.write('%s old %s\n' %(lnum,line))
   fdbg.write(';\n')
   fdbg.write('%s new %s\n' %(lnum,line))
   #exit(1)
   return orig
  lsnew = ' '.join(lsarr)
  return lsnew
 # <ls>HARIV n.  m.  </ls>
 newline = re.sub(r'<ls>(HARIV[.]) ([0-9. fg]+)</ls>',f,line)
 flag = not (newline == line)
 return flag,newline

def old_change_ls_matching_given_1(line,iline):
 def f(m):
  lsname = m.group(1)
  p1 = m.group(2)
  v1 = m.group(3)
  p2 = m.group(4)
  v2 = m.group(5)
  lsnew1 = "<ls>%s %s, %s</ls>" %(lsname,p1,v1)
  lsnew2 = '<ls n="%s">%s, %s</ls>' %(lsname,p2,v2)
  lsnew = '%s %s' %(lsnew1,lsnew2)
  return lsnew
 newline = re.sub(r'<ls>(MBH[.]) ([0-9]+), ([0-9]+[.]) ([0-9]+), ([0-9]+[.]?)</ls>',f,line)
 flag = not (newline == line)
 return flag,newline

def change_ls_matching_given_2(line,iline):
 def f(m):
  lsname = m.group(1)
  p1 = m.group(2)
  v1 = m.group(3)
  versedata = m.group(4)
  if False:
   print(m.group(0))
   print(lsname)
   print('p1=',p1,'v1=',v1)
   print('"%s"'%versedata)
   exit(1)
  versedata1 = versedata.lstrip()  # remove leading ' '
  versenums = versedata1.split(' ')
  lsarr = []
  lsnew1 = "<ls>%s %s, %s</ls>" %(lsname,p1,v1)
  lsarr.append(lsnew1)
  for iverse,verse in enumerate(versenums):
   ls = '<ls n="%s %s,">%s</ls>' % (lsname,p1,verse)
   lsarr.append(ls)
  lsnew = ' '.join(lsarr)
  return lsnew
 newline = re.sub(r'<ls>(MBH[.]) ([0-9]+), ([0-9]+[.])(( [0-9]+[.]?){1,})</ls>',f,line)
 flag = not (newline == line)
 return flag,newline

def change_ls_matching_given_3(line,iline):
 def f(m):
  lsname = m.group(1)
  versedata = m.group(2)
  if False:
   print(m.group(0))
   print(lsname)
   print('"%s"'%versedata)
   exit(1)
  
  #versedata1 = versedata.lstrip()  # remove leading ' '
  #versenums = versedata1.split(' ')
  lsarr = []
  iverse = 0
  for m in re.finditer(r' [0-9]+, [0-9]+[.]',versedata):
   versedatum = m.group(0).lstrip(' ')
   if iverse == 0:
    ls = '<ls>%s %s</ls>' %(lsname,versedatum)
   else:
    ls = '<ls n="%s">%s</ls>' %(lsname,versedatum)
   lsarr.append(ls)
   iverse = iverse + 1
  lsnew = ' '.join(lsarr)
  return lsnew
 # <ls>MBH. n, m. n, m. ETC </ls>
 newline = re.sub(r'<ls>(MBH[.])(( [0-9]+, [0-9]+[.]){2,})</ls>',f,line)
 flag = not (newline == line)
 return flag,newline

def change_ls_matching_given_4(line,iline):
 def f(m):
  lsname = m.group(1)
  versedata = m.group(2)
  verseparts = versedata.split(' ')
  orig = m.group(0)
  if len(verseparts) in [1,2]:
   return orig
  versetypes = []
  malformed = False
  for ipart,part in enumerate(verseparts):
   if re.search(r'^[0-9]+[.]$',part):
    versetypes.append('v')
   elif re.search(r'^[0-9]+[,]$',part):
    versetypes.append('p') # parvan
   elif re.search(r'^[0-9]+$',part) and (ipart+1 == len(verseparts)):
    versetypes.append('v')
   else:
    malformed = True
    break
  if malformed:
   ans = orig.replace('<ls>','<lsx>')
  else:
   ans = orig
  return ans
 newline = re.sub(r'<ls>(MBH[.]) ([0-9,. ]+)</ls>',f,line)
 flag = not (newline == line)
 return flag,newline

def change_ls_matching_given_5(line,lnum):
 def f(m):
  lsname = m.group(1)
  versedata = m.group(2)
  verseparts = versedata.split(' ')
  orig = m.group(0)
  if len(verseparts) in [1,2]:
   return orig
  vparts = []
  versetypes = []
  malformed = False
  remainder = versedata.lstrip(' ')
  lsarr = []
  p = None
  while remainder != '':
   m1 = re.search(r'^([0-9]+,) ([0-9]+[.])(.*)$',remainder)
   if m1:
    p = m1.group(1)
    v = m1.group(2)
    pv = '%s %s' %(p,v)
    rest = m1.group(3)
    if len(lsarr) == 0:
     ls = '<ls>%s %s</ls>' % (lsname,pv)
    else:
     ls = '<ls n="%s">%s</ls>' % (lsname,pv)
    lsarr.append(ls)
    remainder = rest.lstrip(' ')
    continue
   m1 = re.search(r'^([0-9]+[.])(.*)$',remainder)
   if m1:
    if p == None:
     # error:
     fdbg.write('; _5 data error a',orig)
     fdbg.write(';--------------------------\n')
     fdbg.write('%s old %s\n' %(lnum,line))
     fdbg.write(';\n')
     fdbg.write('%s new %s\n' %(lnum,line))
     return orig
    v = m1.group(1)
    rest = m1.group(2)
    if len(lsarr) == 0:
     print('_5 data error b',orig)
     return orig
    else:
     ls = '<ls n="%s %s">%s</ls>' % (lsname,p,v)
    lsarr.append(ls)
    remainder = rest.lstrip(' ')
    continue
   # try same m1 but with no period and at end
   m1 = re.search(r'^([0-9]+,) ([0-9]+)$',remainder)
   if m1:
    p = m1.group(1)
    v = m1.group(2)
    pv = '%s %s' %(p,v)
    rest = '' #m1.group(3)
    if len(lsarr) == 0:
     ls = '<ls>%s %s</ls>' % (lsname,pv)
    else:
     ls = '<ls n="%s">%s</ls>' % (lsname,pv)
    lsarr.append(ls)
    remainder = rest.lstrip(' ')
    continue
   m1 = re.search(r'^([0-9]+)$',remainder)
   if m1:
    if p == None:
     # error:
     print('_5 data error a',orig)
     return orig
    v = m1.group(1)
    rest = '' # m1.group(2)
    if len(lsarr) == 0:
     print('_5 data error b',orig)
     return orig
    else:
     ls = '<ls n="%s %s">%s</ls>' % (lsname,p,v)
    lsarr.append(ls)
    remainder = rest.lstrip(' ')
    continue
   # error
   print('_5 data error c',orig)
   #print('remainder="%s"' % remainder)
   fdbg.write(';--------------------------\n')
   fdbg.write('%s old %s\n' %(lnum,line))
   fdbg.write(';\n')
   fdbg.write('%s new %s\n' %(lnum,line))
   #exit(1)
   return orig
  lsnew = ' '.join(lsarr)
  return lsnew
 # <ls>MBH. n, m. n, m. ETC </ls>
 newline = re.sub(r'<ls>(MBH[.]) ([0-9,. ]+)</ls>',f,line)
 flag = not (newline == line)
 return flag,newline

def change_ls_matching_given_6(line,lnum):
 def f(m):
  lsname = m.group(1)
  versedata = m.group(2)
  verseparts = versedata.split(' ')
  orig = m.group(0)
  if len(verseparts) in [1,2]:
   return orig
  vparts = []
  versetypes = []
  malformed = False
  remainder = versedata.lstrip(' ')
  lsarr = []
  p = None
  while remainder != '':
   m1 = re.search(r'^([0-9]+,) ([0-9]+[.])(.*)$',remainder)
   if m1:
    p = m1.group(1)
    v = m1.group(2)
    pv = '%s %s' %(p,v)
    rest = m1.group(3)
    if len(lsarr) == 0:
     ls = '<ls>%s %s</ls>' % (lsname,pv)
    else:
     ls = '<ls n="%s">%s</ls>' % (lsname,pv)
    lsarr.append(ls)
    remainder = rest.lstrip(' ')
    continue
   m1 = re.search(r'^([0-9]+[.])(.*)$',remainder)
   if m1:
    if p == None:
     # error:
     print('; _6 data error a',orig)
     fdbg.write(';--------------------------\n')
     fdbg.write('%s old %s\n' %(lnum,line))
     fdbg.write(';\n')
     fdbg.write('%s new %s\n' %(lnum,line))
     return orig
    v = m1.group(1)
    rest = m1.group(2)
    if len(lsarr) == 0:
     print('_6 data error b',orig)
     return orig
    else:
     ls = '<ls n="%s %s">%s</ls>' % (lsname,p,v)
    lsarr.append(ls)
    remainder = rest.lstrip(' ')
    continue
   # try same m1 but with no period and at end
   m1 = re.search(r'^([0-9]+,) ([0-9]+)$',remainder)
   if m1:
    p = m1.group(1)
    v = m1.group(2)
    pv = '%s %s' %(p,v)
    rest = '' #m1.group(3)
    if len(lsarr) == 0:
     ls = '<ls>%s %s</ls>' % (lsname,pv)
    else:
     ls = '<ls n="%s">%s</ls>' % (lsname,pv)
    lsarr.append(ls)
    remainder = rest.lstrip(' ')
    continue
   m1 = re.search(r'^([0-9]+)$',remainder)
   if m1:
    if p == None:
     # error:
     print('_6 data error a',orig)
     return orig
    v = m1.group(1)
    rest = '' # m1.group(2)
    if len(lsarr) == 0:
     print('_6 data error b',orig)
     return orig
    else:
     ls = '<ls n="%s %s">%s</ls>' % (lsname,p,v)
    lsarr.append(ls)
    remainder = rest.lstrip(' ')
    continue
   # handle fg. and fgg.
   m1 = re.search(r'^(fgg?[.])(.*)$',remainder)
   if m1:
    if len(lsarr) == 0:
     # error:
     print('_6 data error a',orig)
     return orig
    x = m1.group(1)
    prev_ls = lsarr[-1]
    ls = prev_ls.replace('</ls>',' %s</ls>' % x)
    lsarr[-1] = ls
    rest = m1.group(2)
    remainder = rest.lstrip(' ')
    continue
   # error
   print('_6 data error c',orig)
   #print('remainder="%s"' % remainder)
   fdbg.write(';--------------------------\n')
   fdbg.write('%s old %s\n' %(lnum,line))
   fdbg.write(';\n')
   fdbg.write('%s new %s\n' %(lnum,line))
   #exit(1)
   return orig
  lsnew = ' '.join(lsarr)
  return lsnew
 # <ls>MBH. n, m. n, m. ETC </ls>
 newline = re.sub(r'<ls>(MBH[.]) ([0-9,. fg]+)</ls>',f,line)
 flag = not (newline == line)
 return flag,newline

def change_ls_matching_given_7(line,lnum):
 def f(m):
  orig = m.group(0)
  if orig == '<ls>MBH.</ls>':
   return orig
  lsname = m.group(1)
  versedata = m.group(2)
  # some preliminary adjustments  
  versedata1 = re.sub(r'^([^ ])',r' \1',versedata)
  versedata1 = re.sub(r'([.,])([0-9])',r'\1 \2',versedata)
  #if len(verseparts) in [1,2]:
  # return orig
  remainder = versedata1.lstrip(' ')
  lsarr = []
  p = None
  while remainder != '':
   m1 = re.search(r'^([0-9]+,) ([0-9]+[.])(.*)$',remainder)
   if m1:
    p = m1.group(1)
    v = m1.group(2)
    pv = '%s %s' %(p,v)
    rest = m1.group(3)
    if len(lsarr) == 0:
     ls = '<ls>%s %s</ls>' % (lsname,pv)
    else:
     ls = '<ls n="%s">%s</ls>' % (lsname,pv)
    lsarr.append(ls)
    remainder = rest.lstrip(' ')
    continue
   m1 = re.search(r'^([0-9]+[.])(.*)$',remainder)
   if m1:
    if p == None:
     # error:
     print('; _7 data error a',orig)
     fdbg.write(';--------------------------\n')
     fdbg.write('%s old %s\n' %(lnum,line))
     fdbg.write(';\n')
     fdbg.write('%s new %s\n' %(lnum,line))
     return orig
    v = m1.group(1)
    rest = m1.group(2)
    if len(lsarr) == 0:
     print('_7 data error b',orig)
     return orig
    else:
     ls = '<ls n="%s %s">%s</ls>' % (lsname,p,v)
    lsarr.append(ls)
    remainder = rest.lstrip(' ')
    continue
   # try same m1 but with no period and at end
   m1 = re.search(r'^([0-9]+,) ([0-9]+)$',remainder)
   if m1:
    p = m1.group(1)
    v = m1.group(2)
    pv = '%s %s' %(p,v)
    rest = '' #m1.group(3)
    if len(lsarr) == 0:
     ls = '<ls>%s %s</ls>' % (lsname,pv)
    else:
     ls = '<ls n="%s">%s</ls>' % (lsname,pv)
    lsarr.append(ls)
    remainder = rest.lstrip(' ')
    continue
   m1 = re.search(r'^([0-9]+)$',remainder)
   if m1:
    if p == None:
     # error:
     print('_7 data error a1',orig)
     fdbg.write(';--------------------------\n')
     fdbg.write('%s old %s\n' %(lnum,line))
     fdbg.write(';\n')
     fdbg.write('%s new %s\n' %(lnum,line))
     return orig
    v = m1.group(1)
    rest = '' # m1.group(2)
    if len(lsarr) == 0:
     print('_7 data error b',orig)
     return orig
    else:
     ls = '<ls n="%s %s">%s</ls>' % (lsname,p,v)
    lsarr.append(ls)
    remainder = rest.lstrip(' ')
    continue
   # handle fg. and fgg.
   m1 = re.search(r'^(fgg?[.])(.*)$',remainder)
   if m1:
    if len(lsarr) == 0:
     # error:
     print('_7 data error a',orig)
     return orig
    x = m1.group(1)
    prev_ls = lsarr[-1]
    ls = prev_ls.replace('</ls>',' %s</ls>' % x)
    lsarr[-1] = ls
    rest = m1.group(2)
    remainder = rest.lstrip(' ')
    continue
   # error
   print('_7 data error c',orig)
   #print('remainder="%s"' % remainder)
   fdbg.write(';--------------------------\n')
   fdbg.write('%s old %s\n' %(lnum,line))
   fdbg.write(';\n')
   fdbg.write('%s new %s\n' %(lnum,line))
   #exit(1)
   return orig
  lsnew = ' '.join(lsarr)
  return lsnew
 # <ls>MBH. n, m. n, m. ETC </ls>
 newline = re.sub(r'<ls>MBH[.]([^ <])',r'<ls>MBH. \1',line)
 newline = re.sub(r'<ls>(MBH[.])([0-9,. fg]+)</ls>',f,newline)
 flag = not (newline == line)
 return flag,newline

dataxraw = """
<ls>Spr. (II) 1091)</ls> viDA 91865


"""
def get_datax():
 lines1 = dataxraw.splitlines()
 lines = []
 for line in lines1:
  line = line.strip()
  if line == '':
   continue
  line = re.sub('</ls>.*$','</ls>',line)
  lines.append(line)
 return lines

data4list = get_datax()
 
def change_ls_matching_given_x(line):
 for ls in data4list:
  if ls in line:
   return True,line
 return False,line

def generate_changes(entries,option):
 for entry in entries:
  metaline = entry.metaline
  # works for LS whose citations take just 1 parameter
  prevlsname = None
  for iline,line in enumerate(entry.datalines):
   lnum = entry.linenum1+iline+1
   for m in re.finditer(r'<ls>(.*?)</ls>',line):
    lsold = m.group(0)
    data = m.group(1)
    if lsold.startswith('<ls n="%s">' % option):
     continue
    if data.startswith(option):
     prevlsname = option
    elif re.search(r'^[0-9]',data):  # <ls>N...</ls>
     if prevlsname == None:
      pass
     else:
      oldline = line
      lsnew = lsold.replace('<ls>','<ls n="%s">' % option)
      newline = line.replace(lsold,lsnew)
      change = Change(metaline,lnum,oldline,newline)
      yield change
      #prevlsname = None
    else:
     prevlsname = None
if __name__=="__main__":
 option = sys.argv[1]
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx
 fileout = sys.argv[3] # change_X
 filedbg = 'tempdbg.txt'
 fdbg = codecs.open(filedbg,"w","utf-8")
 entries = init_entries(filein)
 #fname = 'change_ls_matching_given_%s' % option
 #changef = locals()[fname]
 changes = generate_changes(entries,option)
 write_changes(fileout,changes)
 exit(1)
                      
 for entry in entries:
  for iline,line in enumerate(entry.datalines):
   lnum = entry.linenum1+iline+1
   flag,newline = changef(line,lnum)
   if flag: #
    lnum = entry.linenum1+iline+1
    metaline = re.sub(r'<k2>.*$','',entry.metaline)
    change = Change(metaline,lnum,line,newline)
    changes.append(change)

 write_changes(fileout,changes)
 fdbg.close()
