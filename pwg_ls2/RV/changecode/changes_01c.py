#-*- coding:utf-8 -*-
"""changes_01a.py for ap57

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


def ls6parm(line,abbrev,tipd):
 abbrevregex = abbrev.replace('.','[.]')
 parmregex = r' ([0-9]+), ([0-9]+), ([0-9]+)[.] ([0-9]+), ([0-9]+), ([0-9]+)([.]?)'
 regex = r'<ls>%s%s</ls>'%(abbrevregex,parmregex)
 def f(m):
  a1,b1,c1 = m.group(1),m.group(2),m.group(3)
  a2,b2,c2 = m.group(4),m.group(5),m.group(6)
  d2 = m.group(7)  # optional period at end
  y1 = '<ls>%s %s, %s, %s.</ls>' %(abbrev,a1,b1,c1)
  y2 = '<ls n="%s">%s, %s, %s%s</ls>' %(abbrev,a2,b2,c2,d2)
  y = '%s %s' % (y1,y2)
  return y
 newline = re.sub(regex,f,line)
 return newline

def ls9parm(line,abbrev,tipd):
 abbrevregex = abbrev.replace('.','[.]')
 parmregex = r' ([0-9]+), ([0-9]+), ([0-9]+)[.] ([0-9]+), ([0-9]+), ([0-9]+)[.] ([0-9]+), ([0-9]+), ([0-9]+)([.]?)'
 regex = r'<ls>%s%s</ls>'%(abbrevregex,parmregex)
 def f(m):
  a1,b1,c1 = m.group(1),m.group(2),m.group(3)
  a2,b2,c2 = m.group(4),m.group(5),m.group(6)
  a3,b3,c3 = m.group(7),m.group(8),m.group(9)
  d3 = m.group(10)  # optional period at end
  y1 = '<ls>%s %s, %s, %s.</ls>' %(abbrev,a1,b1,c1)
  y2 = '<ls n="%s">%s, %s, %s.</ls>' %(abbrev,a2,b2,c2)
  y3 = '<ls n="%s">%s, %s, %s%s</ls>' %(abbrev,a3,b3,c3,d3)
  y = '%s %s %s' % (y1,y2,y3)
  return y
 newline = re.sub(regex,f,line)
 return newline

def init_changes(lines,tipd,abbrev):
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
  if metaline == None:
   continue
  newline = ls9parm(line,abbrev,tipd)
  if newline == line:
   continue
  # generate a change
  # ignore other lines line(s) for last '<ls>X</ls>' and derive source
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
 try:
  outarr.append('; ' + ident)
 except:
  print('ERROR: ident=',ident)
  exit(1)
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
 def __init__(self,ls,abbrev):
  self.ls = ls
  self.abbrev = abbrev
  self.parmstr = ls[len(abbrev):].strip()
  if self.parmstr == '':
   self.nparms = 0
   self.rawparms = []
  else:
   self.rawparms = self.parmstr.split(' ')
   self.nparms = len(self.rawparms)
  self.len = len(self.parmstr)
  
def unused_init_lscases(lines,tipd,abbrev):
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
   cases.append(LSCase(elt,abbrev))
 print(len(cases),'instances of %s'%abbrev)
 return cases

if __name__=="__main__":
 abbrev = sys.argv[1]  # used to filter abbreviation.
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx)
 filetip = sys.argv[3] # pwgbib_input.txt
 fileout = sys.argv[4] # possible change transactions
 tips0 = init_tooltip(filetip)
 tips = sorted(tips0,key = lambda tip: len(tip.abbrev),reverse=True)
 tipd = dfirstchar(tips)
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 changes= init_changes(lines,tipd,abbrev) 

 write_changes(fileout,changes)
 
