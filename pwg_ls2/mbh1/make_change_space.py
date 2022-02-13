#-*- coding:utf-8 -*-
"""make_change_space.py
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

exceptions = ('ŚR.', 'GṚHY.', 'BR.', 'UP.', 'ŚAT.', 'ANUKR.', 'PARIŚ.', 'PRĀT.', 'Chr.', 'P.', 'DEV.', 'CH.', 'PADDH.', 'Alg.', 'COLEBR.', 'DAŚAK.', 'MĪM.', 'an.', 'ś.', 'KANDYUR', 'Ind.', 'LAGHUJ.', 'Lebensb.', 'Kār.', 'YOGAŚ.', 'PRĀTIŚ.', 'D.', 'SĀṂKHYAK.', 'SV.', 'PR.', 'UPAL.', 'BṚH.', 'JĀT.', 'B.', 'H.', 'M.', 'Spr.', 'KĀTY.', 'R.', 'UPAK.', 'MĀN.', 'ST.', 'NAL.', 'NALA', 'AV.', 'JYOT.', 'Nakṣ.', 'NAKṢ.', 'NĪTIS.', 'Cow.', 'RĀMAT.', 'NĀṬYAŚ.', 'KERN', 'RATNAM.', 'WEBER', 'BÜHLER', 'GRIMM', 'MUIR', 'N.', 'POTT', 'AUFRECHT', 'DHARMAŚ.', 'HIOUEN-THSANG', 'PERTSCH', 'KṚṢṆAJ.', 'SPAṢṬĀDH.', 'WILLIAMS', 'BURNELL', 'SIDDH.', 'NIR.', 'TRIPR.', 'TRIPRAŚNAV.', 'KUHN', 'GRAHAṆAV.', 'WINDISCH', 'GOLAB.', 'ŚIKṢĀ', 'BHUVANAK.', 'BRUCE', 'BHĀR.', 'BÖHTL.', 'ŚKDR.', 'HALL', 'MÜLLER\'S', 'KENOP.', 'J.', 'HALĀY.', 'GORR.', 'PRATIJÑĀS.',
              'd. d. m. G.','d. Oxf. H.','d. Cambr. H.','d. Tüb. H.',
              'Anh.','v. l.','ved.','Śl.','No.','B. H.',
              'Sch.','Schol.','ANUKR.','Misc. Ess.')
# </ls><ls>  (MBH dem im vgl oxyt noch Im voc. v. u. 10te ebend zu des ein
# imperf. potent aor praes perf mit imper neutr masc fem m. f. n.
# nur auch wohl Bed. st
def init_lschanges(lines,tips):
 replacements = []
 for a in tips:
  if a.abbrev not in exceptions:
   replacement = (' '+a.abbrev,'</ls> <ls>'+a.abbrev)
   replacements.append(replacement)
 #replacements = [(' '+a.abbrev,'</ls> <ls>'+a.abbrev) for a in tips]
 print('# replacements=',len(replacements))
 def fspace(m):
  ls = m.group(1)
  for old,new in replacements:
   ls = ls.replace(old,new)
  lsnew = '<ls>%s</ls>' %ls
  return lsnew
 lschanges = []
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
  newline = re.sub(r'<ls>(.*?)</ls>',fspace,line)
  if newline == line:
   continue
  lschange = LSChange(metaline,iline,line,newline)
  lschanges.append(lschange)
 print(len(lschanges),'lines changed')
 return lschanges

def write_lschanges(fileout,lschanges):
 outrecs = []
 for lschange in lschanges:
  lnum = lschange.iline+1
  old = lschange.line
  new = lschange.newline
  metaline = re.sub(r'<k2>.*$','',lschange.metaline)
  outarr = []
  outarr.append('; -------- %s' % metaline)
  outarr.append('%s old %s' %(lnum,old))
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,new))
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')

def test_tips(tips):
 n = 0
 x = []
 d = {}
 for tip in tips:
  a = tip.abbrev.split(' ')
  if len(a) == 1:
   d[a[0]] = tip
   continue
  n = n + 1
  x.append(tip)
 print(len(x))
 y = []
 for tip in x:
  flag = False
  a = tip.abbrev.split(' ')
  for w in a[1:]:
   if w in d:
    if d[w] not in y:
     y.append(d[w])
 print(len(y), "one-word tips appearing in other tips")
 fileout = 'temptips.txt'
 outarr = []
 for tip in y:
  outarr.append( "'%s'" %tip.abbrev)
 out1 = ', '.join(outarr)
 out2 = ' exceptions = (%s)' % out1
 with codecs.open(fileout,"w","utf-8") as f:
  f.write(out2+'\n')
  for tip in y:
   f.write(tip.abbrev + '\n')
 print('see',fileout)
 exit(1)
if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 filetip = sys.argv[2] # pwgbib_input.txt
 fileout = sys.argv[3] # possible change transactions
 tips0 = init_tooltip(filetip)
 #test_tips(tips0)
 tips = sorted(tips0,key = lambda tip: len(tip.abbrev),reverse=True)
 tipd = dfirstchar(tips)
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 lschanges = init_lschanges(lines,tips) # also, updates tip.changes
 write_lschanges(fileout,lschanges)
 
