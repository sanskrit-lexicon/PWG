#-*- coding:utf-8 -*-
"""lsfilter_irreg.py -- summary stats
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 
class Change(object):
 def __init__(self,metaline,page,iline,old,new,reason,iline1,line1,new1):
  self.metaline = metaline
  self.page = page
  self.iline = iline
  self.old = old
  self.new = new
  self.reason = reason
  self.iline1 = iline1
  self.line1 = line1
  self.new1 = new1

def ls_questionmark(line,tipd):
 def f(m):
  x = m.group(0)   # <lsX</ls>
  y = re.sub(r'[?]','',x)  # remove questionmark character(s)
  return y
 # handle question mark in <ls>X</ls> and <ls n="A">X</ls>
 newline = re.sub(r'<ls(.*?)</ls>',f,line) 
 return newline
  
def init_changes(lines,tipd):
 changes = [] # array of Change objects
 metaline = None
 imetaline1 = None
 page = None
 for iline,line in enumerate(lines):
  if iline == 0: # %***This File is E:\\APTE.ALL, Last update 11.09.06 
   continue  # 
  line = line.rstrip('\r\n')
  if line == '':
   continue
  if line.startswith('<L>'):
   metaline = line
   imetaline1 = iline+1
   continue
  if line == '<LEND>':
   metaline = None
   imetaline = None
   continue
  if line.startswith('[Page'):
   page = line
   continue
  reason=''
  newline = ls_questionmark(line,tipd)
  if newline == line:
   continue
  # generate a change
  # look at previous line(s) for last '<ls>X</ls>' and derive source
  found = None
  if found == None:
   iline1 = None
   line1 = None
   newline1 = None
   reason = ''
   #print('manual check:',iline+1,line)
  else:
   newline1 = line1 # re.sub(r'#} *$',' …#}',line1)
  change = Change(metaline,page,iline,line,newline,reason,iline1,line1,newline1)
  changes.append(change)
 print(len(changes),'potential changes found')
 return changes

class Tooltip(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.abbrev,self.tip = line.split('\t')

def change_out(change,ichange):
 outarr = []
 case = ichange + 1
 #outarr.append('; TODO Case %s: (reason = %s)' % (case,change.reason))
 try:
  ident = change.metaline
 except:
  print('ERROR:',change.iline,change.old)
  exit(1)
 if ident == None:
  ident = change.page
 outarr.append('; ' + ident)
 # possible change for iline1
 if change.iline1 != None:
  lnum = change.iline1 + 1
  line = change.line1
  new = change.new1
  outarr.append('%s old %s' % (lnum,line))
  outarr.append('%s new %s' % (lnum,new))
  outarr.append(';')
 
 # change for iline
 lnum = change.iline + 1
 line = change.old
 new = change.new
 outarr.append('%s old %s' % (lnum,line))
 outarr.append('%s new %s' % (lnum,new))
 outarr.append(';')

 # dummy next line
 return outarr

class Tooltip(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  # pwg has code, abbrevUpper, abbrevLower,tip
  self.code,self.abbrev,self.abbrevlo,self.tip = line.split('\t')
  self.changes = []
  self.abbrevwords = self.abbrev.split(' ')
  
def init_tooltip(filein):
 with codecs.open(filein,"r","utf-8") as f:
  ans = [Tooltip(x) for x in f]
 print(len(ans),'tooltips from',filein)
 return ans

def dfirstchar(tooltips_sorted):
 d = {}
 for tip in tooltips_sorted:
  c = tip.abbrev[0]
  if c not in d:
   d[c] = []
  d[c].append(tip)
 return d

def findtip(ls,tiplist):
 for tip in tiplist:
  if ls.startswith(tip.abbrev):
   return tip
 return None

class LSCase(object):
 def __init__(self,ls,abbrev,metaline,iline,line):
  self.ls = ls
  self.abbrev = abbrev
  self.metaline = metaline
  self.iline = iline
  self.line = line
  self.parmstr = ls[len(abbrev):].strip()
  if self.parmstr == '':
   self.nparms = 0
  else:
   self.nparms = len(self.parmstr.split(' '))
  self.len = len(self.parmstr)
  #if ls == abbrev:
  # print(ls,"'%s'" %self.parmstr,self.nparms)
  # exit(1)
  
def init_lscases(lines,tipd,abbrev):
 cases = []
 metaline = None
 imetaline1 = None
 page = None
 for iline,line in enumerate(lines):
  if iline == 0: # %***This File is E:\\APTE.ALL, Last update 11.09.06 
   continue  # 
  line = line.rstrip('\r\n')
  if line == '':
   continue
  if line.startswith('<L>'):
   metaline = line
   imetaline1 = iline+1
   continue
  if line == '<LEND>':
   metaline = None
   imetaline = None
   continue
  if line.startswith('[Page'):
   page = line
   continue
  for m in re.finditer(r'<ls([^>]*)>([^<]*)</ls>',line):
   attrib = m.group(1)
   elt = m.group(2)
   m1 = re.search(r' +n="(.*?)"',attrib)
   if m1 != None:
    nval = m1.group(1)
    elt = nval + ' ' + elt
   if elt[0] not in tipd:
    continue
   tiplist = tipd[elt[0]]
   tip  = findtip(elt,tiplist)
   if tip == None:
    #print('tooltip abbreviation not found:',elt)
    continue
   if tip.abbrev != abbrev:
    continue
   # found a match
   cases.append(LSCase(elt,abbrev,metaline,iline,line))
 print(len(cases),'instances of %s'%abbrev)
 return cases

def write_lscases(fileout,cases,abbrev):
 parmsd = {}  # 
 #parmscount = {}
 mparm = 0
 nparms = []
 for ls in cases:
  n = ls.nparms
  if n not in parmsd:
   parmsd[n] = []
  parmsd[n].append(ls)
  if n > mparm:
   mparm = n
  if n not in nparms:
   nparms.append(n)
   
 nparms.sort()
 print(nparms)
 for n in nparms:
  casesn = parmsd[n]
  print("%s cases with %s parms" %(len(casesn),n))
 print('ok so far')
 f = codecs.open(fileout,"w","utf-8")
 n0 = 4
 for n in nparms:
  casesn = parmsd[n]
  if n != n0:
   continue 
  f.write(';-----------------------------------------------------------\n')
  f.write(';  %s %s instances with %s parameters\n' %(len(casesn),abbrev,n))
  f.write(';-----------------------------------------------------------\n')
  
  for lscase in casesn:
   outarr = []
   if n == n0:
    outarr.append('; %s' %lscase.metaline)
    outarr.append('; %s' %lscase.ls)
    newls = re.sub(r'(%s [0-9]+, [0-9]+, [0-9]+[.]) ' % abbrev,
                   r'\1</ls> <ls n="%s">' % abbrev,lscase.ls)
    if newls != lscase.ls:
     outarr.append('%s old %s' %(lscase.iline+1,lscase.line))
     newline = lscase.line.replace(lscase.ls,newls)
     outarr.append('%s new %s' %(lscase.iline+1,newline))
    else:
     outarr.append('; %s old %s' %(lscase.iline+1,lscase.line))
    outarr.append(';')
   else:
    outarr.append('; %s' %lscase.ls)
   for out in outarr:
     f.write(out+'\n')
 f.close()

def write_lscases_1(fileout,cases,abbrev):
 parmsd = {}  # 
 mparm = 0
 nparms = []
 for ls in cases:
  n = ls.nparms
  if n not in parmsd:
   parmsd[n] = []
  parmsd[n].append(ls)
  if n > mparm:
   mparm = n
  if n not in nparms:
   nparms.append(n)
   
 nparms.sort()
 print(nparms)
 for n in nparms:
  casesn = parmsd[n]
  print("%s cases with %s parms" %(len(casesn),n))
 print('ok so far')
 f = codecs.open(fileout,"w","utf-8")
 n0 = 0
 for n in nparms:
  casesn = parmsd[n]
  if n <= 3:
   continue 
  f.write(';-----------------------------------------------------------\n')
  f.write(';  %s %s instances with %s parameters\n' %(len(casesn),abbrev,n))
  f.write(';-----------------------------------------------------------\n')
  
  for lscase in casesn:
   outarr = []
   outarr.append('; %s' %lscase.metaline)
   outarr.append('; %s' %lscase.ls)
   outarr.append('%s old %s' %(lscase.iline+1,lscase.line))
   outarr.append('%s new %s' %(lscase.iline+1,lscase.line))
   #newline = lscase.line.replace(lscase.ls,newls)
   #outarr.append('%s new %s' %(lscase.iline+1,newline))
   outarr.append(';')
   for out in outarr:
    f.write(out+'\n')
 f.close()

def write_lscases_0(fileout,cases,abbrev):
 parmsd = {}  # 
 mparm = 0
 nparms = []
 for ls in cases:
  n = ls.nparms
  if n not in parmsd:
   parmsd[n] = []
  parmsd[n].append(ls)
  if n > mparm:
   mparm = n
  if n not in nparms:
   nparms.append(n)
   
 nparms.sort()
 print(nparms)
 for n in nparms:
  casesn = parmsd[n]
  print("%s cases with %s parms" %(len(casesn),n))
 print('ok so far')
 f = codecs.open(fileout,"w","utf-8")
 n0 = 0
 for n in nparms:
  casesn = parmsd[n]
  if n != n0:
   continue 
  f.write(';-----------------------------------------------------------\n')
  f.write(';  %s %s instances with %s parameters\n' %(len(casesn),abbrev,n))
  f.write(';-----------------------------------------------------------\n')
  
  for lscase in casesn:
   outarr = []
   outarr.append('; %s' %lscase.metaline)
   #outarr.append('; %s' %lscase.ls)
   outarr.append('%s old %s' %(lscase.iline+1,lscase.line))
   #outarr.append('%s new %s' %(lscase.iline+1,lscase.line))
   #newline = lscase.line.replace(lscase.ls,newls)
   #outarr.append('%s new %s' %(lscase.iline+1,newline))
   outarr.append(';')
   for out in outarr:
    f.write(out+'\n')
 f.close()

def regular_ls(ls,abbrev):
 if re.search(r'^%s$'%abbrev,ls):
  return True
 if re.search(r'^%s [0-9]+, [0-9]+, [0-9]+[.]?$'%abbrev,ls):
  return True
 if re.search(r'^%s [0-9]+, [0-9]+[.]?$'%abbrev,ls):
  return True
 if re.search(r'^%s [0-9]+, [0-9]+-[0-9]+[.]?$'%abbrev,ls):
  return True
 if re.search(r'^%s [0-9]+, [0-9]+, [0-9]+-[0-9]+[.]?$'%abbrev,ls):
  return True
 return False

def write_lscases_irreg(fileout,cases,abbrev):
 f = codecs.open(fileout,"w","utf-8")
 n = 0
 for lscase in cases:
  outarr = []
  if regular_ls(lscase.ls,abbrev):
   continue
  n = n + 1
  outarr.append('; %s' %lscase.metaline)
  outarr.append('; %s' %lscase.ls)
  outarr.append('%s old %s' %(lscase.iline+1,lscase.line))
  outarr.append('%s new %s' %(lscase.iline+1,lscase.line))
  #newline = lscase.line.replace(lscase.ls,newls)
  #outarr.append('%s new %s' %(lscase.iline+1,newline))
  outarr.append(';')
  for out in outarr:
   f.write(out+'\n')
 print(n,'irregular cases written to',fileout)
 f.close()

def test(tipd,tips):
 ls = 'ṚV.'
 tiplist = tipd[ls[0]]
 print(len(tiplist))
 tip = findtip(ls,tiplist)
 print(tip.tip)
 exit(1)
 
if __name__=="__main__":
 abbrev = sys.argv[1]  # used to filter abbreviation.
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx)
 filetip = sys.argv[3] # pwgbib_input.txt
 fileout = sys.argv[4] # possible change transactions
 tips0 = init_tooltip(filetip)
 tips = sorted(tips0,key = lambda tip: len(tip.abbrev),reverse=True)
 tipd = dfirstchar(tips)
 #test(tipd,tips)
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 lscases = init_lscases(lines,tipd,abbrev) # also, updates tip.changes

 #write_lscases(fileout,lscases,abbrev)
 #write_lscases_1(fileout,lscases,abbrev)
 #write_lscases_0(fileout,lscases,abbrev)
 write_lscases_irreg(fileout,lscases,abbrev)
  
