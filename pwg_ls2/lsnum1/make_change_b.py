#-*- coding:utf-8 -*-
"""make_change_b.py
"""
import sys,re,codecs


def get_lsnames_approved(option):
 lsnames = [
  "PAÑCAT.","MBH.","ṚV.","M.","N.","TS.","SUŚR.","VOP.","KATHĀS.","HIT.",
  "ŚAT. BR.","KĀTY. ŚR.","BHĀG. P.","ŚĀK.","R.","NIR.",
  "RAGH.", "BHAṬṬ.","VS.","MEGH.","YĀJÑ.","HIḌ.",
"SĀH. D.", "LĀṬY.", 
"VP.", "VYUTP.", "ṚV. PRĀT.", "BHAG.", "RĀJA-TAR.", 
"AIT. BR.", "Ind. St.", "ĀŚV. ŚR.", "DHĀTUP.", "BHARTṚ.", 
"TRIK.", "MṚCCH.", "ĀŚV. GṚHY.", "KAUŚ.", "GĪT.", 
"VIKR.", "ŚIŚ.", "ŚĀṄKH. ŚR.", "CHĀND. UP.", 
"AK.", "ṚT.", "KUMĀRAS.", "VET.", "GOBH.", 
"COLEBR. Alg.", "VĀLAKH.", 
"MĀRK. P.", "MĀLAV.", "DAŚAK.", "NAIGH.", "TBR.", "VARĀH. BṚH.", 
"VARĀH. BṚH. S.", "PRAB.", "PAÑCAV. BR.", "SŪRYAS.", "KĀṬH.", 
"KĀM. NĪTIS.", "R. SCHL.", "HALĀY.", "PRATĀPAR.", "LALIT. ed. Calc.", 
"PAÑCAR.", "WEBER, RĀMAT. UP.", "SARVADARŚANAS.", "RĀJAN.", "YOGAŚ.",
 ]
 d = {}
 for lsname in lsnames:
  d[lsname] = []  # list of Change objects
 return d

class Change(object):
 def __init__(self,ilineprev,lineprev,iline,old,new):
  self.ilineprev = ilineprev
  self.lineprev = lineprev
  self.iline = iline
  self.old = old
  self.new = new
  
def change_1(lines,d_approved):
 d_not_approved = {}
 newlines = []
 for line in lines:
  newlines.append(line)
 #
 changes = []
 nchg = 0
 for iline,old in enumerate(newlines):
  lscount = len(re.findall(r'<ls',old))
  if lscount != 1:  # can only handle 1
   continue
  # prev line
  ilineprev = iline - 1
  oldprev = newlines[ilineprev] # preceding line
  ls_all_prev = re.findall(r'<ls',oldprev)
  if len(ls_all_prev) != 1:  # cannot handle more than 1 in prev line
   continue
  if re.search(r'[()]',oldprev):
   # exclude cases where the ls in previous line is parenthetical
   continue
  m = re.search(r'<ls([^>]*)>([^<]*)</ls>',oldprev)
  if m == None:
   # Can happen if there is '<is>' or other markup in lsprev
   continue
  # further restrictions
  mprev = re.search(r'^<ls([^>]*)>([^<]*)</ls>',oldprev)
  if mprev == None:
   continue
  mold = re.search(r'^<ls>[0-9]',old)
  if mold == None:
   continue
  # further require prev line starts with <ls>X. [0-9]
  # where X is string of non-digit characters
  mprev1 = re.search(r'^<ls>([^0-9]+\.) [0-9]',oldprev)
  if mprev1 == None:
   continue
  lsname = mprev1.group(1)
  if lsname not in d_approved:
   if lsname not in d_not_approved:
    d_not_approved[lsname] = 0
   d_not_approved[lsname] = d_not_approved[lsname] + 1
   continue
  lsnew = '<ls n="%s">' %lsname 
  new = old.replace('<ls>',lsnew)
  newlines[iline] = new
  nchg = nchg + 1
  change = Change(ilineprev,oldprev,iline,old,new)
  changes = d_approved[lsname]  # previous changes for this lsname
  changes.append(change)
  
  if False: # dbg
   print('iline=%s, ls=%s' % (iline,ls))
   print('old:%s' % old)
   print()
   print('new:%s' % new)
   exit(1)
 print("make_change_a changes %s lines" %nchg)
 print("add to approved?")
 for lsname in d_not_approved:
  n = d_not_approved[lsname]
  if 10<=n:
   print(lsname,n)

def write_changes(fileout,d):
 outrecs = []
 # file title
 outarr = []
 outarr.append('; ********************************************************')
 outarr.append('; %s' % fileout)
 outarr.append('; ********************************************************')
 outrecs.append(outarr)
 #
 ntot = 0 # total number of changes
 for lsname in d:
  changes = d[lsname]
  nchg = len(changes)
  ntot = ntot + nchg
  outarr = []
  outarr.append('; ========================================================')
  outarr.append('; %s: %s (%s)' %(fileout,lsname,nchg))
  outarr.append('; ========================================================')
  for c in changes:
   lnumprev = c.ilineprev + 1
   lnum = c.iline + 1
   lineprev = c.lineprev
   old = c.old
   new = c.new
   outarr.append('; --------------------------------------')
   outarr.append('; %s %s' %(lnumprev,lineprev))
   outarr.append(';')
   outarr.append('%s old %s' %(lnum,old))
   outarr.append(';')
   outarr.append('%s new %s' %(lnum,new))
   #outarr.append('; --------------------------------------')
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(ntot,"change transactions written to",fileout)

if __name__=="__main__":
 option = sys.argv[1]
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[3] # marked revision of xxx.txt
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 if option == '1':
  lsnames_d = get_lsnames_approved(option)
  change_1(lines, lsnames_d) # update lsnames_d
 else:
  print('ERROR: unknown option',option)
  exit(1)
 write_changes(fileout,lsnames_d)


 
