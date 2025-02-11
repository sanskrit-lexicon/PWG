#-*- coding:utf-8 -*-
"""lsexamine1.py
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

class Tooltip(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  # pwg has code, abbrevUpper, abbrevLower,tip
  try:
   self.code,self.abbrev,self.abbrevlo,self.tip = line.split('\t')
  except:
   print('Tooltip error:\n%s' %line)
   parts=line.split('\t')
   exit(1)
  self.total = 0
  self.eltparms = []
  self.lstexts = []
 def appendelt(self,elt):
  assert elt.startswith(self.abbrev)
  eltparm = elt.replace(self.abbrev,'',1)
  #eltparm = eltparm.lstrip()  
  self.eltparms.append(eltparm)
  #self.elts.append(elt)
  
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


def count_tips(lines,tipd,numbertip,unknowntip):
 lsunknowns = []
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
   lstext = m.group(0)
   attrib = m.group(1)
   elt = m.group(2)
   m1 = re.search(r' +n="(.*?)"',attrib)
   if m1 != None:
    nval = m1.group(1)
    if nval.endswith(','):
     elt = nval + elt
    else:
     elt = nval + ' ' + elt
   if re.search(r'^[0-9]',elt): # number
    tip = numbertip
    continue
   elif elt[0] not in tipd:
    tip = unknowntip
    lsunknowns.append((metaline,m.group(0)))
    continue 
   else:
    tiplist = tipd[elt[0]]
    tip  = findtip(elt,tiplist)
    if tip == None:
     tip = unknowntip
     lsunknowns.append((metaline,m.group(0)))
     continue
   # found a match
   tip.total = tip.total + 1
   tip.appendelt(elt)
   tip.lstexts.append(lstext)
   
def write_lsunknowns(lsunknowns):
 fileout = "lsunknowns.txt"
 with codecs.open(fileout,"w","utf-8") as f:
  for temp in lsunknowns:
   metaline,lsunknown = temp
   meta = re.sub(r'<k2>.*$','',metaline)
   meta1 = meta.ljust(30)
   out = '%s : %s' %(meta1,lsunknown)
   f.write(out+'\n')
 print(len(lsunknowns),"unknown ls written to",fileout)

 
def write_tips(fileout,tips0,numbertip,unknowntip):
 outrecs = []
 outrecs.append('')  # for totals
 tips = sorted(tips0,key = lambda tip: tip.total,reverse=True)
 def tipformat(tip):
  text = tip.tip
  text = re.sub(r'^.*? = ','',text)
  text = text.replace('[Cologne Addition]','')
  text = text[0:40]
  return '%05d\t%s\t%s' %(tip.total,tip.abbrev,text)
 #outrecs.append(tipformat(numbertip))
 #outrecs.append(tipformat(unknowntip))
 tot = 0
 tot = tot + numbertip.total
 tot = tot + unknowntip.total
 for tip in tips:
  outarr = []
  outarr.append(tipformat(tip))
  tot = tot + tip.total
  for ieltparm,eltparm in enumerate(tip.eltparms):
   tipelt = tip.abbrev + eltparm
   lstext = tip.lstexts[ieltparm]
   out = '%s %s' %(tipelt,lstext)
   outarr.append(out)
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
   f.write(lscase.ls + '\n')
  #f.write(';-----------------------------------------------------------\n')
 f.close()
 print(ntot,'= number of %s ls references'%abbrev)
if __name__=="__main__":
 
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 filetip = sys.argv[2] # pwgbib_input.txt
 fileout = sys.argv[3] # output summary
 tips0 = init_tooltip(filetip)
 tips = sorted(tips0,key = lambda tip: len(tip.abbrev),reverse=True)
 tipd = dfirstchar(tips)
 # dummy for number
 numbertip = Tooltip("9.1\tNUMBER\tnumber\tls starts with number")
 # dummy for unknown
 unknowntip = Tooltip("9.2\tUNKNOWN\tunknown\tls is unknown")
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 count_tips(lines,tipd,numbertip,unknowntip) # also, updates tip.changes
 write_tips(fileout,tips0,numbertip,unknowntip)
 exit(1)
 write_lsentries(fileout,lsentries,abbrev)
 
