#-*- coding:utf-8 -*-
"""make_change_ls.py
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

def change_ls_matching_given_1(line):
 def f(m):
  # <ls>(Spr. (II) ...) ((I)...)</ls>
  partII = m.group(1)
  partI = m.group(2)
  ls1 = '<ls>%s</ls>' % partII
  ls2 = '<ls n="Spr.">%s</ls>' % partI
  lsnew = '%s %s' %(ls1,ls2)
  return lsnew
 newline = re.sub(r'<ls>(Spr. \(II\)[^<]*?) (\(I\).*?)</ls>',f,line)
 flag = not (newline == line)
 return flag,newline

def change_ls_matching_given_2(line):
 def f(m):
  # <ls>Spr. (II) 2375. 2886. 3104. 7424.</ls>
  #  2375. 2886. 3104. 7424.

  #print(m.group(0))
  #print(m.group(1))
  #print()
  versedata = m.group(1)
  versedata1 = versedata.lstrip()  # remove leading ' '
  versenums = versedata1.split(' ')
  lsarr = []
  pfx = 'Spr. (II)'
  for iverse,verse in enumerate(versenums):
   if iverse == 0:
    ls = '<ls>%s %s</ls>' % (pfx,verse)
   else:
    ls = '<ls n="%s">%s</ls>' % (pfx,verse)
   lsarr.append(ls)
  lsnew = ' '.join(lsarr)
  return lsnew
 newline = re.sub(r'<ls>Spr. \(II\)(( [0-9]+[.]?){2,})</ls>',f,line)
 flag = not (newline == line)
 return flag,newline

def change_ls_matching_given_2a(line):
 replacements = [
  ('</ls> <ls>v. l.',' v. l.'),
  ('</ls> <ls>fgg.',' fgg.'),
  ('</ls> <ls>fg.',' fg.'),
  ]
 newline = line
 for old,new in replacements:
  newline = newline.replace(old,new)
 flag = not (newline == line)
 return flag,newline

def change_ls_matching_given_3(line):
 def f(m):
  # <ls>Spr. (II) 2375. 7424, v. l.</ls>
  versedata = m.group(1)
  extra = m.group(3) # v. l., or fgg?. Why is this not m.group(2) ?
  #versedata = m.group('verses')
  #extra = m.group('extra')
  versedata1 = versedata.lstrip()  # remove leading ' '
  versenums = versedata1.split(' ')
  lsarr = []
  pfx = 'Spr. (II)'
  iverselast  = len(versenums) - 1
  for iverse,verse in enumerate(versenums):
   if iverse == 0:
    ls = '<ls>%s %s</ls>' % (pfx,verse)
   elif iverse == iverselast:
    ls = '<ls n="%s">%s %s</ls>' % (pfx,verse,extra)
   else:
    ls = '<ls n="%s">%s</ls>' % (pfx,verse)
   lsarr.append(ls)
  lsnew = ' '.join(lsarr)
  return lsnew
 newline = re.sub(r'<ls>Spr. \(II\)(( [0-9]+[.,]?){2,}) ((v\. l\.)|(fg\.)|(fgg\.))</ls>',f,line)
 #newline = re.sub(r'<ls>Spr. \(II\)(?P<verses>( [0-9]+[.]?){2,}) (?P<extra>(v\. l\.)|(fg\.)|(fgg\.))</ls>',f,line)
 flag = not (newline == line)
 return flag,newline

def change_ls_matching_given_4(line):
 def f(m):
  # <ls>Spr. (II) 2375. 7424, v. l.</ls>
  versedata = m.group(1)
  #extra = m.group(3) # v. l., or fgg?. Why is this not m.group(2) ?
  #versedata = m.group('verses')
  #extra = m.group('extra')
  versedata1 = versedata.lstrip()  # remove leading ' '
  versedata2 = versedata1.replace(' v. l.','__1')
  versenums = versedata2.split(' ')
  lsarr = []
  pfx = 'Spr. (II)'
  iverselast  = len(versenums) - 1
  for iverse,verse in enumerate(versenums):
   if iverse == 0:
    ls = '<ls>%s %s</ls>' % (pfx,verse)
   else:
    ls = '<ls n="%s">%s</ls>' % (pfx,verse)
   lsarr.append(ls)
  lsnew = ' '.join(lsarr)
  lsnew = lsnew.replace('__1',' v. l.')
  return lsnew
 newline = re.sub(r'<ls>Spr. \(II\)(( [0-9]+[.,]?( (v\. l\.))?){2,})</ls>',f,line)
 flag = not (newline == line)
 return flag,newline

def change_ls_matching_given_5(line):
 def f(m):
  # <ls>Spr. (II) 2375. 7424, v. l.</ls>
  versedata = m.group(1)
  #extra = m.group(3) # v. l., or fgg?. Why is this not m.group(2) ?
  #versedata = m.group('verses')
  #extra = m.group('extra')
  versedata1 = versedata.lstrip()  # remove leading ' '
  versedata2 = versedata1.replace(' fgg.','__1')
  versedata3 = versedata2.replace(' fg.','__2')
  versenums = versedata3.split(' ')
  lsarr = []
  pfx = 'Spr. (II)'
  iverselast  = len(versenums) - 1
  for iverse,verse in enumerate(versenums):
   if iverse == 0:
    ls = '<ls>%s %s</ls>' % (pfx,verse)
   else:
    ls = '<ls n="%s">%s</ls>' % (pfx,verse)
   lsarr.append(ls)
  lsnew = ' '.join(lsarr)
  lsnew = lsnew.replace('__1',' fgg.')
  lsnew = lsnew.replace('__2',' fg.')
  return lsnew
 newline = re.sub(r'<ls>Spr. \(II\)(( [0-9]+[.,]?( (fgg?\.))?){2,})</ls>',f,line)
 flag = not (newline == line)
 return flag,newline


dataxraw = """
<ls>Spr. (II) 1091)</ls> viDA 91865
<ls>Spr. (II) 268).</ls> viDAtar 91866
<ls>Spr. (II) 1652)</ls> vftta 94757
<ls>Spr. (II) 701.fg.</ls> vftti 94793
<ls>Spr. (II) Vorwort S. XVI.</ls> vfdDacARakya 94861
<ls>Spr. (II)</ls> Satruka 97703
<ls>Spr. (II) 1009. 3482, v. l. 4029. (I) 2794.</ls> Silpa 99590
<ls>Spr. (II) 1073).</ls> Socis 101047
<ls>Spr. (II) 328)</ls> SOca 101170
<ls>Spr. (II) 3963 </ls> Sram 101446
<ls>Spr. (II) 2457,</ls> SrezWa 101916
<ls>Spr. (II) 5705)</ls> zaRqa 102570
<ls>Spr. (II) 6802).</ls> saktimant 103336
<ls>Spr. (II) 1650)</ls> saMkalpa 103442
<ls>Spr. (II) 751)</ls> saMkalpa 103442
<ls>Spr. (II) 5873)</ls> saMkzaya 103522
<ls>Spr. (II) 4111,</ls> satyavAcaka 104150
<ls n="Spr. (II)">4977,</ls> satyavAdin 104153
<ls>Spr. (II) 4600,</ls> sad 104247
<ls>Spr. (II) 6100. 6750. 6752 u.s.w.</ls> sadA 104294
<ls>Spr. (II) 4111,</ls> sadAkArin 104296
<ls>Spr. (II) 1929. 2071. 4287, v. l. 6206, v. l. 6767. fg. 7299.</ls> sadBAva 104380
<ls>Spr. (II) 2327. 2586. 5483. 6869. fgg. 6918, v. l.</ls> saMpatti 106026
<ls>Spr. (II) 881).</ls> saMpAdin 106069
<ls>Spr. (II) 1110. 5582. <is>Śiva</is></ls> sarvaBakza 106901
<ls>Spr. (II) 5264,</ls> sallApa 107288
<ls>Spr. (II) 6973)</ls> sahasra 107620
<ls>Spr. (II) 3669.7565.</ls> sAhasin 108968
<ls>Spr. (II)</ls> suBAzita 110848
<ls>Spr. (II) 2875. - 5606</ls> sumantrin 110951
<ls>Spr. (II) 639. 790. fg. 5860, v. l. 7187. 7581.</ls> staB 113579
<ls>Spr. (II)</ls> sparSa 114358
<ls>Spr. (II) 4781.7259.</ls> smartavya 114602
<ls>Spr. (II) 3274)</ls> svaBAva 115043
<ls>Spr. (II) 6781 </ls> svAti 115581
<ls>Spr. (II) 1584. -</ls> svAdu 115602
<ls>Spr. (II) 4736)</ls> svecCA 115801
<ls>Spr. (II)</ls> han 115989
<ls>Spr. (II) 6841,</ls> hayaSAstra 116065
<ls>Spr. (II) 5656 - 5678.</ls> hi 116887
<ls>Spr. (II) 6128)</ls> hita 116942
<ls>Spr. (II) 6629, v. l. -</ls> hInatas 117216
<ls>Spr. (II)</ls> utpAdaka 118984
<ls>Spr. (II)</ls> kfpAlutA 119576
<ls>Spr. (II) 2533,</ls> bAhya 121285
<ls>Spr. (II) 5249,</ls> rUpasanAtana 121798

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

if __name__=="__main__":
 option = sys.argv[1]
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx
 fileout = sys.argv[3] # change_X
 
 entries = init_entries(filein)
 fname = 'change_ls_matching_given_%s' % option
 changef = locals()[fname]
 changes = []  # list of change records
 for entry in entries:
  for iline,line in enumerate(entry.datalines):
   flag,newline = changef(line)
   if flag: #
    lnum = entry.linenum1+iline+1
    metaline = re.sub(r'<k2>.*$','',entry.metaline)
    change = Change(metaline,lnum,line,newline)
    changes.append(change)

 write_changes(fileout,changes)
 
