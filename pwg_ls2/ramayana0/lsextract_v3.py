#-*- coding:utf-8 -*-
"""lsextract_v3.py 
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

def write_changes(fileout,changes):
 with codecs.open(fileout,"w","utf-8") as f:
   for ichange,change in enumerate(changes):
    outarr = change_out(change,ichange)
    for out in outarr:
     f.write(out+'\n')
 print(len(changes),"possible changes written to",fileout)

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
 def __init__(self,ls,abbrev,metaline,iline,line,lsfull):
  self.ls = ls
  self.abbrev = abbrev
  self.metaline = metaline
  self.iline = iline
  self.line = line
  self.lsfull = lsfull
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
 lsentries = []  # list of 'entry' with ls of given abbrev
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
   entry = [] # list of LSCase appearing in this entry
   continue
  if line == '<LEND>':
   if len(entry)>0:
    lsentries.append(entry)
    # 
   metaline = None
   imetaline = None
   continue
  if line.startswith('[Page'):
   page = line
   continue
  for m in re.finditer(r'<ls([^>]*)>([^<]*)</ls>',line):
   lsfull = m.group(0)
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
   lscase = LSCase(elt,abbrev,metaline,iline,line,lsfull)
   entry.append(lscase)
 print(len(lsentries),'entries with ls for  %s'%abbrev)
 return lsentries

def write_lsentries(fileout,lsentries,abbrev):
 f = codecs.open(fileout,"w","utf-8")
 n0 = 0
 ntot = 0
 for lscases in lsentries:
  # lscases is a non-empty list of LSCase objects
  metaline = lscases[0].metaline
  n = len(lscases)
  ntot = ntot + n
  f.write(';-----------------------------------------------------------\n')
  x = re.sub(r'<k2>.*$','',metaline)
  f.write('; %s {%s %s}\n' %(x,abbrev,n))
  #f.write(';-----------------------------------------------------------\n')
  
  for lscase in lscases:
   #f.write(lscase.ls + '\n')
   f.write(lscase.lsfull + '\n')
  #f.write(';-----------------------------------------------------------\n')
 f.close()
 print(ntot,'= number of %s ls references'%abbrev)

def write_gorr_change_prelim(line,lsfull):
 lsnew = re.sub(r'<ls>R. GORR. ([0-9]), ([0-9]+), ([0-9]+)\. ([0-9]), ([0-9]+), ([0-9]+)(\.)?</ls>',
                r'<ls>R. GORR. \1, \2, \3.</ls> <ls n="R. GORR.">\4, \5, \6\7</ls>',lsfull)
 if lsnew != lsfull:
  newline = line.replace(lsfull,lsnew)
  return lsnew,newline

 lsnew = re.sub(r'<ls>R. GORR. ([0-9]), ([0-9]+), ([0-9]+)\. ([0-9]+), ([0-9]+)(\.)?</ls>',
                r'<ls>R. GORR. \1, \2, \3.</ls> <ls n="R. GORR. \1,">\4, \5\6</ls>',lsfull)
 if lsnew != lsfull:
  newline = line.replace(lsfull,lsnew)
  return lsnew,newline

 lsnew = re.sub(r'<ls>R. GORR. ([0-9]), ([0-9]+), ([0-9]+)\. ([0-9]+)(\.)?</ls>',
                r'<ls>R. GORR. \1, \2, \3.</ls> <ls n="R. XGORR. \1, \2,">\4\5</ls>',lsfull)
 if lsnew != lsfull:
  newline = line.replace(lsfull,lsnew)
  return lsnew,newline
 # ===========================
 lsnew = re.sub(r'<ls>R. GORR. ([0-9]), ([0-9]+), ([0-9]+)\. (.*)$',
                r'<ls>R. GORR. \1, \2, \3.</ls> <ls n="R. GORR.">\4',lsfull)
 if lsnew != lsfull:
  newline = line.replace(lsfull,lsnew)
  return lsnew,newline

 lsnew = re.sub(r'<ls n="R. GORR.">([0-9]), ([0-9]+), ([0-9]+)\. ([0-9]), ([0-9]+), ([0-9]+)(\.)?</ls>',
                r'<ls n="R. GORR.">\1, \2, \3.</ls> <ls n="R. GORR.">\4, \5, \6\7</ls>',lsfull)
 if lsnew != lsfull:
  newline = line.replace(lsfull,lsnew)
  return lsnew,newline

 lsnew = re.sub(r'<ls n="R. GORR.">([0-9]), ([0-9]+), ([0-9]+)\. (.*)$',
                r'<ls n="R. GORR.">\1, \2, \3.</ls> <ls n="R. GORR.">\4',lsfull)
 if lsnew != lsfull:
  newline = line.replace(lsfull,lsnew)
  return lsnew,newline

 return lsfull,line

def normal_gorr(lsfull):
 m = re.search(r'^<ls>R. GORR. [0-9]+, [0-9]+, [0-9]+\.?</ls>',lsfull)
 if m != None:
  return True

 m = re.search(r'^<ls>R. GORR. [0-9]+, [0-9]+, [0-9]+\.? fgg?\.</ls>',lsfull)
 if m != None:
  return True

 m = re.search(r'^<ls n="R. GORR.">[0-9]+, [0-9]+, [0-9]+\.?</ls>',lsfull)
 if m != None:
  return True

 m = re.search(r'^<ls n="R. GORR.">[0-9]+, [0-9]+, [0-9]+\.? fgg?\.</ls>',lsfull)
 if m != None:
  return True
 
 m = re.search(r'^<ls n="R. GORR. [0-9]+,">[0-9]+, [0-9]+\.?</ls>',lsfull)
 if m != None:
  return True

 m = re.search(r'^<ls n="R. GORR. [0-9]+, [0-9]+,">[0-9]+\.?</ls>',lsfull)
 if m != None:
  return True

 m = re.search(r'^<ls n="R. GORR. [0-9]+,">[0-9]+, [0-9]+\.? fgg?\.</ls>',lsfull)
 if m != None:
  return True

 m = re.search(r'^<ls n="R. GORR. [0-9]+, [0-9]+,">[0-9]+\.? fgg?\.</ls>',lsfull)
 if m != None:
  return True

 return False 
def write_gorr_changes(fileout,lsentries,abbrev):
 f = codecs.open(fileout,"w","utf-8")
 n0 = 0
 ntot = 0
 lnum_prev = None
 for lscases in lsentries:
  # lscases is a non-empty list of LSCase objects
  lscases_gorr = [lscase for lscase in lscases if not normal_gorr(lscase.lsfull)]
  
  n = len(lscases_gorr)
  if n == 0:
   continue  # skip
  metaline = lscases[0].metaline
  """
  if n > 1:
   pass
   #print('%s multi gorr at %s' % (n,metaline))
  f.write(';-----------------------------------------------------------\n')
  x = re.sub(r'<k2>.*$','',metaline)
  f.write('; %s\n' % x)
  """
  for ilscase,lscase in enumerate(lscases_gorr):
   lnum = lscase.iline + 1
   if lnum == lnum_prev:
    #print('duplicate lnum %s' % metaline)
    continue # don't repeat change for this line
   lnum_prev = lnum
   oldline = lscase.line
   lsfull = lscase.lsfull
   lsfullnew,newline = write_gorr_change_prelim(oldline,lsfull)
   if newline != oldline:
    continue #  skip the rest in this version
   # so this is unresolved. Generate output for change
   ntot = ntot + 1
   f.write(';-----------------------------------------------------------\n')
   x = re.sub(r'<k2>.*$','',metaline)
   f.write('; %s\n' % x)
   if ilscase != 0:
    f.write(';-------\n')
   f.write('; %s\n' %lsfull)
   #f.write('; %s\n' %lsfullnew)
   f.write('%s old %s\n' % (lnum,oldline))
   f.write('; \n')
   f.write('%s new %s\n' % (lnum,newline))
 f.close()
 print(ntot,'GORR change forms written to %s'%fileout)
 
if __name__=="__main__":
 abbrev = sys.argv[1]  # used to filter abbreviation.
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx)
 filetip = sys.argv[3] # pwgbib_input.txt
 fileout = sys.argv[4] # all the <ls> with 'abbrev'
 fileout1 = sys.argv[5] # manual change transactions for 'GORR'
 tips0 = init_tooltip(filetip)
 tips = sorted(tips0,key = lambda tip: len(tip.abbrev),reverse=True)
 tipd = dfirstchar(tips)
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 lsentries = init_lscases(lines,tipd,abbrev) # also, updates tip.changes
 write_lsentries(fileout,lsentries,abbrev)
 write_gorr_changes(fileout1,lsentries,abbrev)
 