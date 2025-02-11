#-*- coding:utf-8 -*-
"""lsexamine2.py  
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

class Tooltip(object):
 def __init__(self,count,abbrev,tooltip):
  self.count = int(count)
  self.abbrev = abbrev
  self.tooltip = tooltip
  self.line = '%s\t%s\t%s' % (count,abbrev,tooltip)
  self.total = 0
  self.eltparms = []
  self.lstexts = [] # parallel to eltparms
  # self.case_counts = []
  self.nparms = [] # parallel to eltparms
  
 def appendelt(self,line):
  # assume
  m = re.search(r'^(.*?) (<ls.*?</ls>)$',line)
  elt = m.group(1)
  lstext = m.group(2)
  assert elt.startswith(self.abbrev)
  eltparm = elt.replace(self.abbrev,'',1)
  #eltparm = eltparm.lstrip()  
  self.eltparms.append(eltparm)
  self.lstexts.append(lstext)
  self.total = self.total + 1
  #self.elts.append(elt)

def tipgroups(lines):
 # a generator
 tip = None
 for iline,line in enumerate(lines):
  if '\t' in line:
   if tip != None:
    yield tip
   tip = []
   parts = line.split('\t')
   count = parts[0]
   abbrev = parts[1]
   tooltip = parts[2]
   tip = Tooltip(count,abbrev,tooltip)
  else:
   # an element
   tip.appendelt(line)
 yield tip # last one
def init_tipinfo(lines):
 tips = list(tipgroups(lines))
 print(len(tips),"read by init_tipinfo")
 return tips
def findtip(ls,tiplist):
 for tip in tiplist:
  if ls.startswith(tip.abbrev):
   return tip
 return None

def write_tips(fileout,tips0):
 outrecs = []
 outrecs.append('')  # for totals
 tips = sorted(tips0,key = lambda tip: tip.total,reverse=True)
 def tipformat(tip):
  text = tip.tooltip
  text = re.sub(r'^.*? = ','',text)
  text = text.replace('[Cologne Addition]','')
  text = text[0:40]
  return '%05d\t%s\t%s' %(tip.total,tip.abbrev,text)
 tot = 0
 for tip in tips:
  outarr = []
  outarr.append(tipformat(tip))
  tot = tot + tip.total
  for eltparm in tip.eltparms:
   tipelt = tip.abbrev + eltparm
   outarr.append(tipelt)
  outrecs.append(outarr)
 #
 import datetime
 x = datetime.datetime.now()
 date = x.strftime("%Y-%m-%d")
 #outrecs[0] = '%05d\t%s\tAs of %s' %(tot,'ALL',date)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print("write_tips Output in ",fileout)

def analyze2_helper(parm,lstext):
 nparm_other = 5
 dbg = (lstext == '<ls>Spr. 109, v. l.</ls>')
 if dbg: print('parm="%s"' % parm)
 if parm == '':
  return 0 # no parameters
 parm1 = parm.lstrip()
 parm1a = re.sub(r'\. fgg?\.$','',parm1)
 parm1b = re.sub(r'[.,] v\. l\.$','',parm1a)
 if dbg:
  print('parm1="%s"' % parm1)
  print('parm1a="%s"' % parm1a)
  print('parm1b="%s"' % parm1b)
 if '. ' in parm1b:
  return nparm_other
 parm2 = re.sub(r'[.].*$','',parm1b)
 m = re.search(r'^[0-9,]+$',parm2)
 if m == None:
  return nparm_other
 parts = parm2.split(',')
 nparm = len(parts)
 if nparm > nparm_other:
  return nparm_other
 return nparm

def analyze2(tip):
 for i,eltparm in enumerate(tip.eltparms):
  lstext = tip.lstexts[i]
  nparm = analyze2_helper(eltparm,lstext)
  tip.nparms.append(nparm)
  
def tipformat(tip):
  text = tip.tooltip
  text = re.sub(r'^.*? = ','',text)
  #text = text.replace('[Cologne Addition]','')
  #text = text[0:40]
  return '* %05d\t%s\t%s' %(tip.total,tip.abbrev,text)
 
def write_tips2_helper(tip,nparm0,nparm_other):
 eltparms1 = []
 lstexts1 = []
 for i,eltparm in enumerate(tip.eltparms):
  nparm = tip.nparms[i]
  lstext = tip.lstexts[i]
  if nparm == nparm0:
   eltparms1.append(eltparm)
   lstexts1.append(lstext)
 abbrev = tip.abbrev
 ncase = len(eltparms1)
 outarr = []  # return value
 #if ncase == 0:
 # return outarr
 if nparm0 < nparm_other:
  casetitle = ('** (%s) %s with %s numeric parameters ' %
               (ncase,abbrev,nparm0))
 else:
  casetitle = ('** (%s) %s with OTHER parameters ' % (ncase,abbrev))
 outarr.append(casetitle)
 #if nparm0 == 0:
 # return outarr
 for i,eltparm in enumerate(eltparms1):
  if nparm0 == nparm_other:
   lstext = ' ' + lstexts1[i]
   nparmtext = '?'
  else:
   lstext = ''
   nparmtext = str(nparm0)

  tipelt = '%s%s %s%s' %(abbrev,eltparm,nparmtext,lstext)
  outarr.append(tipelt)
 return outarr

def write_tips2(fileout,tips0):
 nparm_other = 5
 outrecs = []
 tips = sorted(tips0,key = lambda tip: tip.total,reverse=True)
 tot = 0
 nparmvals = range(nparm_other + 1)  # [0,1,...5]
 for tip in tips:
  arr = []  #
  for nparm in nparmvals:
   temparr = write_tips2_helper(tip,nparm,nparm_other)
   n = len(temparr)
   ncase = n - 1 # discount the 'title' line of temparr
   arrval = (ncase,nparm,temparr)
   arr.append(arrval)
  # sort arr descending
  arr1 = sorted(arr,key=lambda arrval: arrval[0], reverse = True)
  first = tipformat(tip)
  outarr = [first]
  for iarrval,arrval in enumerate(arr1):
   ncase,nparm,temparr = arrval
   for ix,x in enumerate(temparr):
    if (iarrval == 0) and (ix == 0):
     x = x.replace('** (', '** !(')
    outarr.append(x)
    if nparm == 0:
     break;
  outrecs.append(outarr)
  tot = tot + tip.total
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print("write_tips Output in ",fileout)

if __name__=="__main__": 
 filein = sys.argv[1] #  lsexamine1.txt
 fileout = sys.argv[2] # output summary
 lines = read_lines(filein)
 
 tips = init_tipinfo(lines)
 for tip in tips:
  analyze2(tip)
 write_tips2(fileout,tips)

