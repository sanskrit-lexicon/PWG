#-*- coding:utf-8 -*-
"""make_change.py
"""
import sys,re,codecs

sys.stdout.reconfigure(encoding='utf-8') 
class Change(object):
 def __init__(self,metaline,page,iline,old,new,reason,iline1,line1,new1):
  self.metaline = metaline1
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
  #self.changes = []
  #self.abbrevwords = self.abbrev.split(' ')
  
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

class LSChange(object):
 def __init__(self,metaline,iline,line,newline):
  self.metaline = metaline
  self.iline = iline
  self.line = line
  self.newline = newline

def replace_line_0(line):
 # sort of irregular. Will be changed later.
 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  if parmstr == '':
   return all
  m1 = re.search(r'^ [0-9,. ]*(v\. l\.)?[.,]?$',parmstr)
  if m1 == None:
   return '**'+all
  return all
 
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_1a(line):
 newline = re.sub(r'(<ls>AK\.[^ <])', r'**\1',line)
 return newline

def replace_line_1b(line):
 newline = re.sub(r'(<ls>AK\. [^0-9])', r'**\1',line)
 return newline

def replace_line_1c(line):
 #
 def f(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  while True:
   parmstr1 = re.sub(r'([0-9]),([0-9])',r'\1, \2',parmstr)
   if parmstr1 == parmstr:
    break
   parmstr = parmstr1
  new = '<ls>%s%s</ls>' % (abbrev,parmstr1)  
  return new

 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f,line)
 return newline

def replace_line_1d(line):
 newline = re.sub(r'(\bady\.)', r'<lex>**adj.</lex>',line)
 return newline

def replace_line_1e(line):
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s\.' %(rnum,rnum,rnum,rnum)
 
 regex = '^ (%s) (%s)$' % (rnum4,rnum4)
 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1)
  p2 = m1.group(2)
  new = '<ls>AK. %s</ls> <ls n="AK.">%s</ls>' % (p1,p2)
  return new

 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_1f(line):
 rnum = '[0-9]+'
 rnum3 = '%s, %s, %s\.' %(rnum,rnum,rnum)
 rnum4 = '%s, %s, %s, %s\.' %(rnum,rnum,rnum,rnum)
 
 regex = '^ (%s) (%s)$' % (rnum3,rnum4)
 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1)
  p2 = m1.group(2)
  new = '<ls>AK. %s</ls> <ls n="AK.">%s</ls>' % (p1,p2)
  return new

 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_1g(line):
 rnum = '[0-9]+'
 rnum3 = '%s, %s, %s\.' %(rnum,rnum,rnum)
 #rnum4 = '%s, %s, %s, %s\.' %(rnum,rnum,rnum,rnum)
 
 regex = '^ (%s) (%s)$' % (rnum3,rnum3)
 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1)
  p2 = m1.group(2)
  new = '<ls>AK. %s</ls> <ls n="AK.">%s</ls>' % (p1,p2)
  return new

 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_1h(line):
 rnum = '[0-9]+'
 rnum3 = '%s, %s, %s\.' %(rnum,rnum,rnum)
 rnum4 = '%s, %s, %s, %s\.' %(rnum,rnum,rnum,rnum)
 
 regex = '^ (%s) (%s)$' % (rnum4,rnum3)
 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1)
  p2 = m1.group(2)
  new = '<ls>AK. %s</ls> <ls n="AK.">%s</ls>' % (p1,p2)
  return new

 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_1i(line):
 rnum = '[0-9]+'
 rnum3 = '%s, %s, %s\.' %(rnum,rnum,rnum)
 rnum4 = '%s, %s, %s, %s\.' %(rnum,rnum,rnum,rnum)
 rnum2 = '%s, %s' % (rnum,rnum)
 
 regex = '^ (%s), (%s)\. (%s)\.$' % (rnum2,rnum2,rnum2)
 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1)
  p2 = m1.group(2)
  p3 = m1.group(3)
  new = '<ls>AK. %s, %s</ls> <ls n="AK. %s,">%s</ls>' % (p1,p2,p1,p3)
  return new

 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_1j(line):
 rnum = '[0-9]+'
 rnum3 = '%s, %s, %s\.' %(rnum,rnum,rnum)
 rnum4 = '%s, %s, %s, %s\.' %(rnum,rnum,rnum,rnum)
 rnum2 = '%s, %s' % (rnum,rnum)
 
 regex = '^ (%s), (%s), (%s)\. (%s)\.$' % (rnum,rnum,rnum,rnum)
 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1)
  p2 = m1.group(2)
  p3 = m1.group(3)
  p4 = m1.group(4)
  new = '<ls>AK. %s, %s, %s.</ls> <ls n="AK. %s, %s,">%s.</ls>' % (p1,p2,p3,p1,p2,p4)
  return new

 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_1k(line):
 rnum = '[0-9]+'
 rnum3 = '%s, %s, %s\.' %(rnum,rnum,rnum)
 rnum4 = '%s, %s, %s, %s\.' %(rnum,rnum,rnum,rnum)
 rnum2 = '%s, %s' % (rnum,rnum)
 
 regex = '^ (%s), (%s), (%s), (%s)\. (%s)\.$' % (rnum,rnum,rnum,rnum,rnum)
 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1)
  p2 = m1.group(2)
  p3 = m1.group(3)
  p4 = m1.group(4)
  p5 = m1.group(5)
  new = '<ls>AK. %s, %s, %s, %s.</ls> <ls n="AK. %s, %s, %s,">%s.</ls>' % (
          p1,p2,p3,p4,p1,p2,p3,p5)
  return new

def replace_line_1l(line):
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum2 = '%s, %s' % (rnum,rnum)

 regex = '^ (%s)\. (%s), (%s)\. (%s)\.$' %(rnum4,rnum2,rnum2,rnum2)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1) # 4
  p2 = m1.group(2) # 2
  p3 = m1.group(3) # 2
  p4 = m1.group(4) # 2
  new = '<ls>AK. %s.</ls> <ls n="AK.">%s, %s.</ls> <ls n="AK. %s,">%s.</ls>' %(
       p1,p2,p3,p2,p4)
  return new

 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_1m(line):
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum2 = '%s, %s' % (rnum,rnum)

 regex = '^ (%s), (%s)\. (%s)\.$' %(rnum,rnum2,rnum2)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1) # 4
  p2 = m1.group(2) # 2
  p3 = m1.group(3) # 2
  new = '<ls>AK. %s, %s.</ls> <ls n="AK. %s,">%s.</ls> ' %(p1,p2,p1,p3)
  return new

 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_1n(line):
 rnum = '[0-9]+'

 regex = '^ (%s), (%s), (%s),$' %(rnum,rnum,rnum)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  new = '**' + all  # to be corrected manually
  return new

 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_1o(line):
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 rnum2 = '%s, %s' % (rnum,rnum)

 regex = '^ (%s)\. (%s), (%s)\. (%s)\.$' %(rnum3,rnum2,rnum2,rnum2)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1) # 3
  p2 = m1.group(2) # 2
  p3 = m1.group(3) # 2
  p4 = m1.group(4) # 2
  new = '<ls>AK. %s.</ls> <ls n="AK.">%s, %s.</ls> <ls n="AK. %s,">%s.</ls> ' %(p1,p2,p3,p2,p4)
  return new

 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_1p(line):
 rnum = '[0-9]+'

 regex = '^ (%s)\. (%s), (%s), (%s)\.$' %(rnum,rnum,rnum,rnum)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1) # 3
  p2 = m1.group(2) # 2
  p3 = m1.group(3) # 2
  p4 = m1.group(4) # 2
  new = '<ls>AK. %s, %s, %s, %s.</ls> ' %(p1,p2,p3,p4)
  return new

 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_1q(line):
 rnum = '[0-9]+'
 regex = '^ (%s), (%s)\. (%s), (%s)\.$' %(rnum,rnum,rnum,rnum)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1) # 3
  p2 = m1.group(2) # 2
  p3 = m1.group(3) # 2
  p4 = m1.group(4) # 2
  new = '<ls>AK. %s, %s, %s, %s.</ls> ' %(p1,p2,p3,p4)
  return new

 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_1r(line):
 rnum = '[0-9]+'
 regex = '^ (%s), (%s)\. (%s)\.$' %(rnum,rnum,rnum)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1) # 3
  p2 = m1.group(2) # 2
  p3 = m1.group(3) # 2
  new = '<ls>AK. %s, %s, %s.</ls> ' %(p1,p2,p3)
  return new

 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_1s(line):
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)

 regex = '^ (%s), (%s)\. (%s)\. (%s)\.$' %(rnum,rnum3,rnum3,rnum4)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1) # 1
  p2 = m1.group(2) # 3
  p3 = m1.group(3) # 3
  p4 = m1.group(4) # 4
  new = '<ls>AK. %s, %s.</ls> <ls n="AK.">%s.</ls> <ls n="AK.">%s.</ls> ' %(p1,p2,p3,p4)
  return new

 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_1t(line):
 # ; N, N, N. N. N, N, N, N.
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 regex = '^ (%s). (%s)\. (%s)\.$' %(rnum3,rnum,rnum4)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  return '**' + all
  
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_1u(line):
 # N, N, N, N. N, N. N, N. (7)
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 rnum2 = '%s, %s' %(rnum,rnum)
 regex = '^ (%s)\. (%s)\. (%s)\.$' %(rnum4,rnum2,rnum2)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  return '**' + all
  
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_1v(line):
 #  N, N, N. N, N, N. N. (6)
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 rnum2 = '%s, %s' %(rnum,rnum)
 regex = '^ (%s)\. (%s)\. (%s)\.$' %(rnum3,rnum3,rnum)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  return '**' + all
  
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_1w(line):
 #  N, N, N, N. N, N, N. N. (6)
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 rnum2 = '%s, %s' %(rnum,rnum)
 regex = '^ (%s)\. (%s)\. (%s)\.$' %(rnum4,rnum3,rnum)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  return '**' + all
  
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_1x(line):
 # N, N, N, N. N, N, N, N. N, N, N. (6)
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 rnum2 = '%s, %s' %(rnum,rnum)
 regex = '^ (%s)\. (%s)\. (%s)\.$' %(rnum4,rnum4,rnum3)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  return '**' + all
  
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_1y(line):
 # N, N, N, N.  N, N, N.  N, N, N, N.  N, N. 7
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 rnum2 = '%s, %s' %(rnum,rnum)
 regex = '^ (%s)\. (%s)\. (%s)\. (%s)\.$' %(rnum4,rnum3,rnum4, rnum2)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1)
  p2 = m1.group(2)
  p3 = m1.group(3)
  p4 = m1.group(4)
  new = '<ls>AK. %s.</ls> <ls n="AK.">%s.</ls> <ls n="AK.">%s.</ls> <ls n="AK.">%s.</ls>' % (p1,p2,p3,p4)
  return new
  # return '**' + all
 
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_1z(line):
 # N, N, N, N.  N, N, N, N.  N, N.  N, N. (6)
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 rnum2 = '%s, %s' %(rnum,rnum)
 regex = '^ (%s)\. (%s)\. (%s)\. (%s)\.$' %(rnum4,rnum4,rnum2,rnum2)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1)
  p2 = m1.group(2)
  p3 = m1.group(3)
  p4 = m1.group(4)
  new = '<ls>AK. %s.</ls> <ls n="AK.">%s.</ls> <ls n="AK. 3, 4,">%s.</ls> <ls n="AK. 3, 4,">%s.</ls>' % (p1,p2,p3,p4)
  return new
 
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_2a(line):
 # N, N, N ? N. N, N, N. (6)  ? = (28),
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 rnum2 = '%s, %s' %(rnum,rnum)
 regex = '^ (%s) \(28\), (%s)\. (%s)\.$' %(rnum3,rnum,rnum3)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1)
  p2 = m1.group(2)
  p3 = m1.group(3)
  new = '<ls>AK. %s (28), %s.</ls> <ls n="AK.">%s.</ls>' % (p1,p2,p3)
  return new
 
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_2b(line):
 # N. N, N. -
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 rnum2 = '%s, %s' %(rnum,rnum)
 regex = '^ (%s)\. (%s), (%s)\.$' %(rnum,rnum,rnum)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1)
  p2 = m1.group(2)
  p3 = m1.group(3)
  new = '<ls>AK. %s, %s, %s.</ls>' % (p1,p2,p3)
  return new
 
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_2c(line):
 # N. N, N. -
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 rnum2 = '%s, %s' %(rnum,rnum)
 regex = '^ (%s)\. (%s)\. (%s)\.$' %(rnum3,rnum2,rnum)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1)
  p2 = m1.group(2)
  p3 = m1.group(3)
  new = '<ls>AK. %s.</ls> <ls n="AK. 3,">%s.</ls> <ls n="AK. 3, 4,">%s.</ls>' % (p1,p2,p3)
  return new
 
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_2d(line):
 # N, N, N. N
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 rnum2 = '%s, %s' %(rnum,rnum)
 regex = '^ (%s), (%s)\. (%s)$' %(rnum2,rnum,rnum)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1)
  p2 = m1.group(2)
  p3 = m1.group(3)
  # add the period
  new = '<ls>AK. %s, %s.</ls> <ls n="AK. %s,">%s.</ls>' % (p1,p2,p1,p3)
  return new
 
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_2e(line):
 # N, N, N, N. ?
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 rnum2 = '%s, %s' %(rnum,rnum)
 regex = '^ (%s)\. ([^0-9f].*)$' %(rnum4,)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1)
  p2 = m1.group(2)
  # add the period
  new = '<ls>AK. %s.</ls> %s' % (p1,p2)
  return new
 
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_2f(line):
 #  N, N, N, N.  N, N, N (4)
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 rnum2 = '%s, %s' %(rnum,rnum)
 regex = '^ (%s)\. (%s)$' %(rnum4,rnum3)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1)
  p2 = m1.group(2)
  # add period to 2nd group
  new = '<ls>AK. %s.</ls> <ls n="AK.">%s.</ls>' % (p1,p2)
  return new
 
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_2g(line):
 
 newline = re.sub(r'<ls>28 COLEBR.</ls>','*<ls>28 COLEBR.</ls>',line)
 return newline

def replace_line_2h(line):
 #  N, N, N, N.  N, N, N (4)
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 rnum2 = '%s, %s' %(rnum,rnum)
 regex = '^ (%s), (%s)\. (%s)\. (%s)\.$' %(rnum2,rnum2,rnum2,rnum3)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1)
  p2 = m1.group(2)
  p3 = m1.group(3)
  p4 = m1.group(4)
  # add period to 2nd group
  new = '<ls>AK. %s, %s.</ls> <ls n="AK. %s,">%s.</ls> <ls n="AK.">%s.</ls>' % (p1,p2,p1,p3,p4)
  return new
 
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_2i(line):
 #  N, N, N, N. N (4)
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 rnum2 = '%s, %s' %(rnum,rnum)
 regex = '^ (%s), (%s)\. (%s)$' %(rnum3,rnum,rnum)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1)
  p2 = m1.group(2)
  p3 = m1.group(3)
  # add period to 2nd group
  new = '<ls>AK. %s, %s.</ls> <ls n="AK. %s,">%s.</ls>' % (p1,p2,p1,p3)
  return new
 
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_2j(line):
 #  N, N. N. N. (4)
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 rnum2 = '%s, %s' %(rnum,rnum)
 regex = '^ (%s), (%s)\. (%s)\. (%s)\.$' %(rnum,rnum,rnum,rnum)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1)
  p2 = m1.group(2)
  p3 = m1.group(3)
  p4 = m1.group(4)
  new = '<ls>AK. %s, %s, %s, %s.</ls>' % (p1,p2,p3,p4)
  return new
 
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_2k(line):
 # contains (COLEBR
 regex = '\(COLEBR\.' 

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  
  return '**'+all
 
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_2l(line):
 # N, N, N.  N, N, N, N.  N, N.  N, N. (4)
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 rnum2 = '%s, %s' %(rnum,rnum)
 regex = '^ (%s)\. (%s), (%s)\. (%s). (%s)\.$' %(rnum3,rnum2,rnum2,rnum2,rnum2)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1)
  p2 = m1.group(2)
  p3 = m1.group(3)
  p4 = m1.group(4)
  p5 = m1.group(5)
  new = '<ls>AK. %s.</ls> <ls n="AK.">%s, %s.</ls> <ls n="AK. %s,">%s.</ls> <ls n="AK. %s,">%s.</ls>' % (p1,p2,p3,p2,p4,p2,p5)
  return new
 
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_2m(line):
 # N, N, N, N.  N.  N, N, N, N. (3) 
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 rnum2 = '%s, %s' %(rnum,rnum)
 regex = '^ (%s), (%s)\. (%s). (%s)\.$' %(rnum3,rnum,rnum,rnum4)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1)
  p2 = m1.group(2)
  p3 = m1.group(3)
  p4 = m1.group(4)
  new = '<ls>AK. %s, %s.</ls> <ls n="AK. %s,">%s.</ls> <ls n="AK.">%s.</ls> ' % (p1,p2,p1,p3,p4)
  return new
 
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_2n(line):
 # N, N, N. N, N, N, N (3)  add period
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 rnum2 = '%s, %s' %(rnum,rnum)
 regex = '^ (%s)\. (%s)$' %(rnum3,rnum4)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1)
  p2 = m1.group(2)
  new = '<ls>AK. %s.</ls> <ls n="AK.">%s.</ls>' % (p1,p2,)
  return new
 
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_2o(line):
 # N, N, N, N.  N, N.  N, N, N, N. (3)
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 rnum2 = '%s, %s' %(rnum,rnum)
 regex = '^ (%s), (%s)\. (%s)\. (%s)\.$' %(rnum2,rnum2,rnum2,rnum4)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1)
  p2 = m1.group(2)
  p3 = m1.group(3)
  p4 = m1.group(4)
  new = '<ls>AK. %s, %s.</ls> <ls n="AK. %s,">%s.</ls> <ls n="AK.">%s.</ls>' % (p1,p2,p1,p3,p4)
  return new
 
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_2p(line):
 # N, N, N, N.  N, N, N, N.  N, N, N, N. 
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 rnum2 = '%s, %s' %(rnum,rnum)
 regex = '^ (%s)\. (%s)\. (%s)\.$' %(rnum4,rnum4,rnum4)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1)
  p2 = m1.group(2)
  p3 = m1.group(3)
  #p4 = m1.group(4)
  new = '<ls>AK. %s.</ls> <ls n="AK.">%s.</ls> <ls n="AK.">%s.</ls>' % (p1,p2,p3)
  return new
 
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_2q(line):
 # N, N, N.  N, N, N.  N, N, N, N. (3)
 # various markup
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 rnum2 = '%s, %s' %(rnum,rnum)
 regex = '^ (%s)\. (%s)\. (%s)\.$' %(rnum3,rnum3,rnum4)
 
 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  
  return '**'+all
 
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_2r(line):
 # (
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 rnum2 = '%s, %s' %(rnum,rnum)
 regex = '^ \('
 
 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  
  return '**'+all
 
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_2s(line):
 # (
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 rnum2 = '%s, %s' %(rnum,rnum)
 regex = '^ (%s), (%s)\. (%s)\. (%s)\.$' %(rnum,rnum2,rnum2,rnum2)
 
 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  
  return '**'+all
 
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_2t(line):
 #  N, N, N N. (2)
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 rnum2 = '%s, %s' %(rnum,rnum)
 regex = '^ (%s), (%s), (%s) (%s)\.$' %(rnum,rnum,rnum,rnum)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1)
  p2 = m1.group(2)
  p3 = m1.group(3)
  p4 = m1.group(4)
  new = '<ls>AK. %s, %s, %s, %s.</ls>' % (p1,p2,p3,p4)
  return new
 
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_2u(line):
 #  N, N, N N. (2)
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 rnum2 = '%s, %s' %(rnum,rnum)
 regex = '^ (%s)\. (%s), (%s)\. (%s)\. (%s)\.$' %(rnum4,rnum2,rnum,rnum,rnum)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1)
  p2 = m1.group(2)
  p3 = m1.group(3)
  p4 = m1.group(4)
  p5 = m1.group(5)
  new = '<ls>AK. %s.</ls> <ls n="AK.">%s, %s.</ls> <ls n="AK. %s,">%s.</ls> <ls n="AK. %s,">%s.</ls>' % (p1,p2,p3,p2,p4,p2,p5)
  return new
 
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_2v(line):
 #  N, N, N, N.  N, N, N.  N, N. (2)
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 rnum2 = '%s, %s' %(rnum,rnum)
 regex = '^ (%s)\. (%s), (%s)\. (%s)\.$' %(rnum4,rnum,rnum2,rnum2)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1)
  p2 = m1.group(2)
  p3 = m1.group(3)
  p4 = m1.group(4)
  new = '<ls>AK. %s.</ls> <ls n="AK.">%s, %s.</ls> <ls n="AK. %s,">%s.</ls>' % (p1,p2,p3,p2,p4)
  return new
 
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

data_2w_raw="""
<ls>AK. 2, 9, 51. 52. 7, 23.</ls>          <L>8154<pc>1-0611<k1>Ajya
<ls>AK. 3, 4, 80. 81. 5, 17.</ls>          <L>9940<pc>1-0753<k1>i
<ls>AK. 2, 5, 13. 2, 6, 3, 12. 3, 1, 51.</ls>   <L>18757<pc>2-0407<k1>kfmi
<ls>AK. 2, 7, 57. 2, 8, 1, 12. 3, 1, 14.</ls>   <L>114279<pc>7-1349<k1>snigDa
<ls>AK. 3, 1, 47. 3, 4, 25, 193. 179.</ls>   <L>19915<pc>2-0507<k1>krUra
<ls>AK. 3, 4, 1. 3, 6, 2, 11. 16.</ls>     <L>43539<pc>4-0579<k1>paryAya
<ls>AK. 3. 1. 3, 1.</ls>                   <L>20142<pc>2-0530<k1>kzantar
<ls>AK. 1. 1. 7, 20.</ls>                  <L>54121<pc>5-0202<k1>BayaMkara
<ls>AK. 1, 1, 1, 24. 3. 4, 14, 60.</ls>    <L>21888<pc>2-0695<k1>garutmant
<ls>AK. 2, 4, 5, 1. 23. 2, 9, 34.</ls>     <L>98522<pc>7-0125<k1>SAka
<ls>AK. 2, 9, 60. 66. 3, 4, 3, 26. 25, 167.</ls>   <L>23011<pc>2-0789<k1>go
<ls>AK. 3, 1, 28. 47. 3, 4, 18, 112. 25, 190.</ls>   <L>24064<pc>2-0886<k1>GAtuka
<ls>AK. 1, 1, 2, 10. 2, 8, 2, 20. 77. 9, 85.</ls>   <L>30777<pc>3-0415<k1>traya
<ls>AK. 2, 8, 1, 24. 3, 4, 14, 80. 83. 23, 144.</ls>   <L>82186<pc>6-0149<k1>yuj
<ls>AK. 1, 1, 3, 1,</ls>                   <L>33063<pc>3-0627<k1>diS
<ls>AK. 2, 4, 1, 5,</ls>                   <L>43701<pc>4-0592<k1>palASin
<ls>AK. 2, 7, 24. 9, 33. 3, 4, 25, 181.</ls>   <L>44264<pc>4-0644<k1>pAtra
<ls>AK. 2, 7, 26. 10, 37. 3, 4, 9, 42.</ls>   <L>89485<pc>6-0893<k1>vAcyaliNga
<ls>AK. 1, 1, 5, 10. 3, 4, 32 (28), 9.</ls>   <L>46960<pc>4-0856<k1>pfcCA
<ls>AK. 1, 1, 1, 1. 3, 4, 32 (28), 16.</ls>   <L>115161<pc>7-1441<k1>svar
<ls>AK. 3, 4, 32, 13. 17. 5, 12.</ls>      <L>50343<pc>4-1116<k1>prAkASya
<ls>AK. 3, 4, 25, 173. 175. 30, 237.</ls>   <L>88106<pc>6-0710<k1>vara
<ls>AK. 1, 1, 4, 10. 3, 4, 18, 112. 125.</ls>   <L>52900<pc>5-0099<k1>budDi
<ls>AK. 2, 6, 2, 21. 3, 4, 18, 112. 126.</ls>   <L>88693<pc>6-0804<k1>varzman
<ls>AK. 1, 1, 1, 63, v. l. 1, 2, 2, 4.</ls>   <L>55731<pc>5-0375<k1>Bedya
<ls>AK. 1, 1, 7, 13, v. l. 2, 6, 1, 5.</ls>   <L>55841<pc>5-0385<k1>Bogin
<ls>AK. 2, 4, 2, 26)</ls>                  <L>84262<pc>6-0327<k1>rAjAdana
<ls>AK. 3, 6, 1, 4).</ls>                  <L>95906<pc>6-1408<k1>vEra
<ls>AK. 2, 4, 1, 9. 3, 14, 69. 6, 1, 3.</ls>   <L>88813<pc>6-0815<k1>valli
<ls>AK. 2, 6, 1, 32. 8, 1, 17. 3, 1, 10.</ls>   <L>115691<pc>7-1472<k1>svAmin
<ls>AK. 3, 5, 7. 3, 4, 32, (COL. 28,) 7.</ls>   <L>535<pc>1-0040<k1>agratas
<ls>AK. 2, 1, 1. 2, 8, 2, 48. 3, 4, 25. 39. 224.</ls>   <L>670<pc>1-0050<k1>aNga
<ls>AK. 1, 1, 1, 6. 3, 20. 2, 4, 2, 51. 8, 2, 17.</ls>   <L>1694<pc>1-0123<k1>adas
<ls>AK. 1, 1, 7, 18. 3, 4, 32, (COL. 28,) 5. 6.</ls>   <L>2705<pc>1-0198<k1>anukampA
<ls>AK. 3, 4, 32, (COL. 28), 10. 16.</ls>   <L>2818<pc>1-0206<k1>anunaya
<ls>AK. 1, 1, 2, 14. 3, 4, 32, (COL. 28,) 18. 25, 189.</ls>   <L>3334<pc>1-0249<k1>antarDi
<ls>AK. 3, 2, 17. 4, 32,</ls>              <L>3404<pc>1-0253<k1>antika
<ls>AK. 2, 2, 1. 9, 92. 3, 6, 24.</ls>     <L>3523<pc>1-0261<k1>anya
<ls>AK. 3, 4, 32, [COL. 28,] 17.</ls>      <L>4534<pc>1-0334<k1>aBitas
<ls>AK. 2, 7, 32. 3, 3, 6. 4, 226.</ls>    <L>5896<pc>1-0435<k1>arTanA
<ls>AK. 3, 6, 33 (3, 6, 19</ls>            <L>6015<pc>1-0446<k1>arbuda
<ls>AK. 3, 3, 39, (COL. 38</ls>            <L>6408<pc>1-0478<k1>avana
<ls>AK. 1, 1, 1, 31. 2, 5, 8. 9, 24. 2, 6, 3, 21. 3, 4, 171.</ls>   <L>8482<pc>1-0636<k1>Adya
<ls>AK. 3, 4, 3. 3, 3, 31, v. l.</ls>      <L>9418<pc>1-0705<k1>Aloka
<ls>AK. 2, 6, 3, 40. 7, 45. 3, 4, 171. 187.</ls>   <L>9740<pc>1-0736<k1>Asana
<ls>AK. 1, 2, 1, 9, 3, 6, 37.</ls>         <L>12413<pc>1-0997<k1>uraga
<ls>AK. 3, 6, 3, 28). 4, 2, 118.</ls>      <L>12595<pc>1-1009<k1>uSInara
<ls>AK. 3, 4, 32, (COLEBR. 28,) 2</ls>     <L>17404<pc>2-0303<k1>ku
<ls>AK. 1, 1, 7, 32. 33. 3, 4, 18, 120. 6, 1, 5.</ls>   <L>19867<pc>2-0502<k1>krIqa
<ls>AK. 3, 4, 27, 215. 26, 203. 1, 1, 2, 36. 2, 6, 2, 5.</ls>   <L>20033<pc>2-0518<k1>klIba
<ls>AK. 2, 6, 1, 39 3, 4, 13, 48. 22, 138.</ls>   <L>21945<pc>2-0701<k1>garBa
<ls>AK. 3, 3, 39 (38). 3, 4, 18, 118.</ls>   <L>27108<pc>3-0068<k1>javana
<ls>AK. 1, 1, 2. 20. 36. 4, 18. 3, 4, 25, 174.</ls>   <L>28547<pc>3-0214<k1>tadvant
<ls>AK. 3, 4, 32 (28), 18. 5, 6.</ls>      <L>29670<pc>3-0331<k1>tiras
<ls>AK. 2, 2, 13. 14. 2, 8, 2, 25. 2, 9, 15.</ls>   <L>32612<pc>3-0595<k1>dAru
<ls>AK. 32</ls>                            <L>33119<pc>3-0645<k1>dInAra
<ls>AK. 2. 9. 98.</ls>                     <L>35977<pc>3-0849<k1>dvyazwa
<ls>AK. S. IX.</ls>                        <L>37749<pc>4-0053<k1>nayanAnanda
<ls>AK. 3, 2, 31. 4, 32</ls>               <L>39184<pc>4-0175<k1>nirarTaka
<ls>AK. 1, 1, 4, 12. 3, 4, 3, 23. 32 (COLEBR. 28), 14. 5, 16</ls>   <L>39944<pc>4-0232<k1>niScaya
<ls>AK. 2. 7, 5. 3, 4, 18, 103.</ls>       <L>41753<pc>4-0390<k1>paRqita
<ls>AK. 2, 16.</ls>                        <L>42207<pc>4-0463<k1>padya
<ls>AK. 3, 4, 1, 2. 14, 81. 30, 234. 6, 3, 31.</ls>   <L>42207<pc>4-0463<k1>padya
<ls>AK. 3, 4, 19, 132. 25, 171. 179. 187. 31, 241.</ls>   <L>42756<pc>4-0521<k1>paricCada
<ls>AK. 3, 4, 14, 79. 32 (COLEBR. 28), 13.</ls>   <L>43537<pc>4-0579<k1>paryApti
<ls>AK. 3, 4, 25, 185. 32 (COLEBR. 28), 7. 3, 5, 7.</ls>   <L>46007<pc>4-0779<k1>puras
<ls>AK. 2, 6, 3, 1. 22. v. l.</ls>         <L>48130<pc>4-0946<k1>pratikarman
<ls>AK. 1, 1, 5, 6. 3, 4, 32 (28), 15</ls>   <L>49334<pc>4-1034<k1>prabanDa
<ls>AK. 1, 1, 7, 8. 2, 3, 2. 2, 2, 10. 3, 4, 26, 195.</ls>   <L>49452<pc>4-1044<k1>praBeda
<ls>AK. 1, 1, 4, 8. 3, 4, 13, 57. 14, 62. 80.</ls>   <L>50641<pc>4-1136<k1>prARin
<ls>AK. 2. 10, 17</ls>                     <L>51239<pc>4-1178<k1>prEzya
<ls>AK. 2, 4, 1, 15. 19. 2, 47. 5, 35. 3, 4, 26, 203.</ls>   <L>51456<pc>4-1200<k1>Pala
<ls>AK. 2. 2, 16. 12.</ls>                 <L>52078<pc>5-0044<k1>bahirdvAra
<ls>AK. 2, 8, 1. 20. fg.</ls>              <L>55716<pc>5-0372<k1>Beda
<ls>AK. 1, 1, 1, 67. 5, 18. 7, 5. 1, 2, 1, 11. 2, 5, 41. 3, 4, 13, 51. 3, 4, 14, 63.</ls>   <L>55716<pc>5-0372<k1>Beda
<ls>AK. 2, 7. 50. 2, 8, 2, 5.</ls>         <L>57120<pc>5-0498<k1>maDya
<ls>AK. 1, 1 7, 34.</ls>                   <L>57308<pc>5-0524<k1>manAk
<ls>AK. 3, 2, 11. 3, 4, 25, 179. fg.</ls>   <L>59685<pc>5-0707<k1>mAtra
<ls>AK. 2, 7, 4. 9. 13. 47. 3, 4, 9, 41. 6, 2, 11.</ls>   <L>81822<pc>6-0112<k1>yAga
<ls>AK. 3, 6, 2, 19 (3, 6, 4, 35</ls>      <L>82339<pc>6-0179<k1>yUpa
<ls>AK. 2, 8, 2, 45. 64. 71.</ls>          <L>83099<pc>6-0242<k1>raRa
<ls>AK. 2, 8, 2, 1. 19. 21. fg.</ls>       <L>83340<pc>6-0254<k1>raTa
<ls>AK. 1, 1, 4, 16. 3, 4, 30, 229</ls>    <L>83706<pc>6-0290<k1>rasa
<ls>AK. 1, 1. 2, 35. 3, 4, 5, 30.</ls>     <L>84878<pc>6-0379<k1>ruci
<ls>AK. 2, 6, 2, 50, 3, 12.</ls>           <L>85422<pc>6-0447<k1>roman
<ls>AK. 2, 10, 24).</ls>                   <L>86522<pc>6-0563<k1>lubDa
<ls>AK. ed. COLEBR. 2, 7, 3.</ls>          <L>89624<pc>6-0904<k1>vARaprasTa
<ls>AK. 2, 6. 2, 36. 3, 2, 34.</ls>        <L>89972<pc>6-0924<k1>vAma
<ls>AK. 1, 1, 5, 8. 3, 4, 14, 66. 78. 32 (28), 16.</ls>   <L>90346<pc>6-0947<k1>vArtta
<ls>AK. 3, 4, 32 (28), 4. 9. 3, 5, 5.</ls>   <L>90825<pc>6-0985<k1>vikalpa
<ls>AK. ed. COLEBR. 3, 2, 58</ls>          <L>91581<pc>6-1041<k1>vid
<ls>AK. 3, 3, 22. 3, 4, 14, 69. 18, 116. 32 (28), 15.</ls>   <L>94193<pc>6-1276<k1>vistAra
<ls>AK. 3, 4, 32, (28), 9. 3, 5, 4.</ls>   <L>94837<pc>6-1325<k1>vfTA
<ls>AK. 2, 4, 1, 19. 9, 15. 21.</ls>       <L>96960<pc>6-1504<k1>vrIhi
<ls>AK. 2, 6, 2, 48. 3, 37. fg.</ls>       <L>99255<pc>7-0179<k1>SiKA
<ls>AK. 2 ,5, 5. 3, 4, 27, 214.</ls>       <L>99612<pc>7-0200<k1>Siva
<ls>AK. 2, 2, 5. 7, 14. 3, 4, 14, 73. 22, 140.</ls>   <L>105174<pc>7-0671<k1>saBA
<ls>AK. ed. COLEBR. 3, 4, 13, 89.</ls>     <L>106193<pc>7-0749<k1>saMbanDa
<ls>AK. 3, 3, 2. 3, 4, 24, 150. 32 (28), 8. 3, 5, 3.</ls>   <L>107929<pc>7-0890<k1>sAkalya
<ls>AK. 2, 8, 2, 28. 3, 4, 18, 109. fg.</ls>   <L>108167<pc>7-0905<k1>sAdin
<ls>AK. 1, 1, 7, 38. 3, 4, 3, 23. 18, 112. 26, 203. 27, 209.</ls>   <L>115043<pc>7-1433<k1>svaBAva
<ls>AK. 2, 6, 3, 4. 6. 3, 4, 6, 31. 14, 82.</ls>   <L>116761<pc>7-1597<k1>hAra
"""
class DATA_2w:
 def __init__(self,line):
  self.line = line
  m = re.search(r'^(<ls>.*?</ls>) +<L>(.*?)<pc>(.*?)<k1>(.*)$',line)
  if m == None:
   self.lstxt = None
   return
  self.lstxt = m.group(1)
  self.L = m.group(2)
  self.pc = m.group(3)
  self.k1 = m.group(4)
  self.count = 0 #updated later
  
def get_data_2w():
 lines = data_2w_raw.split('\n')
 print(len(lines),'data_2w')
 ans = []
 for line in lines:
  rec = DATA_2w(line)
  if rec.lstxt != None:
   ans.append(rec)
 d = {}
 for rec in ans:
  key = rec.lstxt
  if key in d:
   print('get_data_2w duplicate',key)
  d[key] = rec
 return ans,d

data_2w_recs,data_2w_d = get_data_2w()
print(len(data_2w_recs),'records in data_2w_recs')

def replace_line_2w(line):
 
 def f_1(m):
  lstxt = m.group(0) # no change
  if lstxt not in data_2w_d:
   return lstxt  # so no change
  else:
   rec = data_2w_d[lstxt]
   rec.count = rec.count + 1
   return '**' + lstxt
 
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_2o(line):
 # N, N, N, N.  N, N.  N, N, N, N. (3)
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 rnum2 = '%s, %s' %(rnum,rnum)
 regex = '^ (%s), (%s)\. (%s)\. (%s)\.$' %(rnum2,rnum2,rnum2,rnum4)

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  p1 = m1.group(1)
  p2 = m1.group(2)
  p3 = m1.group(3)
  p4 = m1.group(4)
  new = '<ls>AK. %s, %s.</ls> <ls n="AK. %s,">%s.</ls> <ls n="AK.">%s.</ls>' % (p1,p2,p1,p3,p4)
  return new
 
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

def replace_line_2x(line):
 # 32, (COL. 28,) -> 32 (COL. 28),  and also COLEBR.
 rnum = '[0-9]+'
 rnum4 = '%s, %s, %s, %s' %(rnum,rnum,rnum,rnum)
 rnum3 = '%s, %s, %s' %(rnum,rnum,rnum)
 rnum2 = '%s, %s' %(rnum,rnum)
 regex = '32, \(COL(EBR)?. 28,\)'

 def f_1(m):
  all = m.group(0) # no change
  abbrev = m.group(1)
  parmstr = m.group(2)
  m1 = re.search(regex,parmstr)
  if m1 == None:
   return all
  new = all.replace('32, (COL. 28,)','32 (COL. 28),')
  new = new.replace('32, (COLEBR. 28,)','32 (COLEBR. 28),')
  return new
 
 newline = re.sub(r'<ls>(AK\.)(.*?)</ls>',f_1,line)
 return newline

replacements = {
 '0': replace_line_0, '1a':replace_line_1a, '1b':replace_line_1b,
 '1c':replace_line_1c, '1d':replace_line_1d, '1e':replace_line_1e,
 '1f':replace_line_1f, '1g':replace_line_1g, '1h':replace_line_1h,
 '1i':replace_line_1i, '1j':replace_line_1j, '1k':replace_line_1k,
 '1l':replace_line_1l, '1m':replace_line_1m, '1n':replace_line_1n,
 '1o':replace_line_1o, '1p':replace_line_1p, '1q':replace_line_1q,
 '1r':replace_line_1r, '1s':replace_line_1s, '1t':replace_line_1t,
 '1u':replace_line_1u, '1v':replace_line_1v, '1w':replace_line_1w,
 '1x':replace_line_1x, '1y':replace_line_1y, '1z':replace_line_1z,
 '2a':replace_line_2a,
 '2b':replace_line_2b, '2c':replace_line_2c, '2d':replace_line_2d,
 '2e':replace_line_2e, '2f':replace_line_2f, '2g':replace_line_2g,
 '2h':replace_line_2h, '2i':replace_line_2i, '2j':replace_line_2j,
 '2k':replace_line_2k, '2l':replace_line_2l, '2m':replace_line_2m,
 '2n':replace_line_2n, '2o':replace_line_2o, '2p':replace_line_2p,
 '2q':replace_line_2q, '2r':replace_line_2r, '2s':replace_line_2s,
 '2t':replace_line_2t, '2u':replace_line_2u, '2v':replace_line_2v,
 '2w':replace_line_2w, '2x':replace_line_2x, #'2y':replace_line_2y,
 #'2z':replace_line_2z, '3a':replace_line_3a, '3b':replace_line_3b,
 }

def init_lschanges(lines,tips,option):
 if option not in replacements:
  print('init_lschanges: unknown option:"%s"' %option)
  exit(1)
 replaceF = replacements[option]
 lschanges = []
 metaline = None
 imetaline1 = None
 page = None
 for iline,line in enumerate(lines):
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

  newline = replaceF(line)
  if newline == line:
   continue
  lschange = LSChange(metaline,iline,line,newline)
  lschanges.append(lschange)
 print(len(lschanges),'lines changed')
 return lschanges

def write_lschanges(fileout,lschanges):
 outrecs = []
 outarr = []
 outarr.append('; =======================================================' )
 outarr.append('; %s (%s)' %(fileout,len(lschanges)))
 outarr.append('; =======================================================' )
 outrecs.append(outarr)
 for lschange in lschanges:
  lnum = lschange.iline+1
  old = lschange.line
  new = lschange.newline
  metaline = re.sub(r'<k2>.*$','',lschange.metaline)
  outarr = []
  outarr.append('; -------------------------------------------------------' )
  outarr.append(';%s' % metaline)
  outarr.append('%s old %s' %(lnum,old))
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,new))
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')


if __name__=="__main__":
 option = sys.argv[1]
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx)
 filetip = sys.argv[3] # pwgbib_input.txt
 fileout = sys.argv[4] # possible change transactions
 tips0 = init_tooltip(filetip)

 tips = sorted(tips0,key = lambda tip: len(tip.abbrev),reverse=True)
 tipd = dfirstchar(tips)
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 lschanges = init_lschanges(lines,tips,option) # also, updates tip.changes
 write_lschanges(fileout,lschanges)
 if option == '2w':
  # print unexpected counts
  for rec in data_2w_recs:
   if rec.count != 1:
    print('unexpected count=%s for %s' %(rec.count,rec.line))
    
