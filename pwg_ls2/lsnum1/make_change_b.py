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

def change_3a(lines,d_approved):
 d_not_approved = {}
 newlines = []
 for line in lines:
  newlines.append(line)
 #
 changes = []
 nchg = 0
 for iline,old in enumerate(newlines):
  # require old start with a numeric orphan
  m = re.search(r'^<ls>[0-9].*?</ls>',old)
  if m == None:
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
  new = old.replace('<ls>',lsnew,1)  # first ls is replaced
  newlines[iline] = new
  nchg = nchg + 1
  change = Change(ilineprev,oldprev,iline,old,new)
  changes = d_approved[lsname]  # previous changes for this lsname
  changes.append(change)
 print("change_3a changes %s lines" %nchg)

def change_3b(lines,d_approved):
 d_not_approved = {}
 newlines = []
 for line in lines:
  newlines.append(line)
 #
 changes = []
 nchg = 0
 for iline,old in enumerate(newlines):
  # require old start with a numeric orphan
  m = re.search(r'^<ls>[0-9].*?</ls>',old)
  if m == None:
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
  a = mprev.group(1)
  b = mprev.group(2)
  # get lsname
  m1 = re.search(r' n="(.*?)"',a)
  if m1 != None:
   a1 = m1.group(1)
   m2 = re.search(r'^[^0-9]+\.$',a1)
   if m2 != None:
    lsname = a1
   else:
    m3 = re.search(r'^([^0-9]+\.) [0-9,. ]+$',a1)
    if m3 != None:
     lsname = m3.group(1)
    else:
     # cannot get lsname from <ls n="X">
     continue
  else:
   # m1 == None
   m3 = re.search(r'^([^0-9]+\.) [0-9,. ]+$',b)
   if m3 != None:
    lsname = m3.group(1)
   else:
    # cannot get lsname from <ls>X</ls>
    continue
  # now we have lsname.
  if lsname not in d_approved:
   if lsname not in d_not_approved:
    d_not_approved[lsname] = 0
   d_not_approved[lsname] = d_not_approved[lsname] + 1
   continue
  lsnew = '<ls n="%s">' %lsname 
  new = old.replace('<ls>',lsnew,1)  # first ls is replaced
  newlines[iline] = new
  nchg = nchg + 1
  change = Change(ilineprev,oldprev,iline,old,new)
  changes = d_approved[lsname]  # previous changes for this lsname
  changes.append(change)
 print("change_3b changes %s lines" %nchg)

def change_4b(lines,d_approved):
 d_not_approved = {}
 newlines = []
 for line in lines:
  newlines.append(line)
 #
 changes = []
 nchg = 0
 for iline,old in enumerate(newlines):
  # require old start with a numeric orphan
  m = re.search(r'^<ls>[0-9].*?</ls>',old)
  if m == None:
   continue
  # prev line
  ilineprev = iline - 1
  oldprev = newlines[ilineprev] # preceding line
  ls_all_prev = re.findall(r'<ls.*?</ls>',oldprev)
  if len(ls_all_prev) == 0:  # 
   continue
  lastls = ls_all_prev[-1] # last ls in previous line
  if re.search(r'[()]',oldprev):
   # exclude cases where the ls in previous line is parenthetical
   continue
  m = re.search(r'<ls([^>]*)>([^<]*)</ls>',lastls)
  if m == None:
   # Can happen if there is '<is>' or other markup in lsprev
   continue
  # further restrictions
  mprev = re.search(r'^<ls([^>]*)>([^<]*)</ls>',lastls)
  if mprev == None:
   continue
  a = mprev.group(1)
  b = mprev.group(2)
  # get lsname
  m1 = re.search(r' n="(.*?)"',a)
  if m1 != None:
   a1 = m1.group(1)
   m2 = re.search(r'^[^0-9]+\.$',a1)
   if m2 != None:
    lsname = a1
   else:
    m3 = re.search(r'^([^0-9]+\.) [0-9,. ]+$',a1)
    if m3 != None:
     lsname = m3.group(1)
    else:
     # cannot get lsname from <ls n="X">
     continue
  else:
   # m1 == None
   m3 = re.search(r'^([^0-9]+\.) [0-9,. ]+$',b)
   if m3 != None:
    lsname = m3.group(1)
   else:
    # cannot get lsname from <ls>X</ls>
    continue
  # now we have lsname.
  if lsname not in d_approved:
   if lsname not in d_not_approved:
    d_not_approved[lsname] = 0
   d_not_approved[lsname] = d_not_approved[lsname] + 1
   continue
  lsnew = '<ls n="%s">' %lsname 
  new = old.replace('<ls>',lsnew,1)  # first ls is replaced
  newlines[iline] = new
  nchg = nchg + 1
  change = Change(ilineprev,oldprev,iline,old,new)
  changes = d_approved[lsname]  # previous changes for this lsname
  changes.append(change)
 print("change_4b changes %s lines" %nchg)

def change_4c(lines,d_approved):
 d_not_approved = {}
 newlines = []
 for line in lines:
  newlines.append(line)
 #
 changes = []
 nchg = 0
 for iline,old in enumerate(newlines):
  # require old start with a numeric orphan
  m = re.search(r'^<ls>[0-9].*?</ls>',old)
  if m == None:
   continue
  # prev line
  ilineprev = iline - 1
  oldprev = newlines[ilineprev] # preceding line
  # remove parenthetical expressions
  oldprev1 = re.sub(r'\(.*?\)','',oldprev)
  ls_all_prev = re.findall(r'<ls.*?</ls>',oldprev1)
  if len(ls_all_prev) == 0:  # 
   continue
  lastls = ls_all_prev[-1] # last ls in previous line
  if re.search(r'[()]',oldprev1):
   # exclude cases where the ls in previous line is parenthetical
   continue
  m = re.search(r'<ls([^>]*)>([^<]*)</ls>',lastls)
  if m == None:
   # Can happen if there is '<is>' or other markup in lsprev
   continue
  # further restrictions
  mprev = re.search(r'^<ls([^>]*)>([^<]*)</ls>',lastls)
  if mprev == None:
   continue
  a = mprev.group(1)
  b = mprev.group(2)
  # get lsname
  m1 = re.search(r' n="(.*?)"',a)
  if m1 != None:
   a1 = m1.group(1)
   m2 = re.search(r'^[^0-9]+\.$',a1)
   if m2 != None:
    lsname = a1
   else:
    m3 = re.search(r'^([^0-9]+\.) [0-9,. ]+$',a1)
    if m3 != None:
     lsname = m3.group(1)
    else:
     # cannot get lsname from <ls n="X">
     continue
  else:
   # m1 == None
   m3 = re.search(r'^([^0-9]+\.) [0-9,. ]+$',b)
   if m3 != None:
    lsname = m3.group(1)
   else:
    # cannot get lsname from <ls>X</ls>
    continue
  # now we have lsname.
  if lsname not in d_approved:
   if lsname not in d_not_approved:
    d_not_approved[lsname] = 0
   d_not_approved[lsname] = d_not_approved[lsname] + 1
   continue
  lsnew = '<ls n="%s">' %lsname 
  new = old.replace('<ls>',lsnew,1)  # first ls is replaced
  newlines[iline] = new
  nchg = nchg + 1
  change = Change(ilineprev,oldprev,iline,old,new)
  changes = d_approved[lsname]  # previous changes for this lsname
  changes.append(change)
 print("change_4c changes %s lines" %nchg)

def change_5a(lines,d_approved):
 d_not_approved = {}
 newlines = []
 for line in lines:
  newlines.append(line)
 #
 changes = []
 nchg = 0
 for iline,old in enumerate(newlines):
  # require old start with a numeric orphan
  m = re.search(r'^<ls>[0-9].*?</ls>',old)
  if m == None:
   continue
  # prev line and lastls
  lastls = None
  for i in [1,2,3]:
   ilineprev = iline - i
   oldprev = newlines[ilineprev] # preceding line
   if oldprev.startswith('<div'):
    # fail
    break
   # remove parenthetical expressions
   oldprev1 = re.sub(r'\(.*?\)','',oldprev)
   ls_all_prev = re.findall(r'<ls.*?</ls>',oldprev1)
   if len(ls_all_prev) == 0:  # 
    continue
   lastls = ls_all_prev[-1] # last ls in previous line
   break  # for i
  if lastls == None:
   continue
  m = re.search(r'<ls([^>]*)>([^<]*)</ls>',lastls)
  if m == None:
   # Can happen if there is '<is>' or other markup in lsprev
   continue
  # further restrictions
  mprev = re.search(r'^<ls([^>]*)>([^<]*)</ls>',lastls)
  if mprev == None:
   continue
  a = mprev.group(1)
  b = mprev.group(2)
  # get lsname
  m1 = re.search(r' n="(.*?)"',a)
  if m1 != None:
   a1 = m1.group(1)
   m2 = re.search(r'^[^0-9]+\.$',a1)
   if m2 != None:
    lsname = a1
   else:
    m3 = re.search(r'^([^0-9]+\.) [0-9,. ]+$',a1)
    if m3 != None:
     lsname = m3.group(1)
    else:
     # cannot get lsname from <ls n="X">
     continue
  else:
   # m1 == None
   m3 = re.search(r'^([^0-9]+\.) [0-9,. ]+$',b)
   if m3 != None:
    lsname = m3.group(1)
   else:
    # cannot get lsname from <ls>X</ls>
    continue
  # now we have lsname.
  if lsname not in d_approved:
   if lsname not in d_not_approved:
    d_not_approved[lsname] = 0
   d_not_approved[lsname] = d_not_approved[lsname] + 1
   continue
  lsnew = '<ls n="%s">' %lsname 
  new = old.replace('<ls>',lsnew,1)  # first ls is replaced
  newlines[iline] = new
  nchg = nchg + 1
  change = Change(ilineprev,oldprev,iline,old,new)
  changes = d_approved[lsname]  # previous changes for this lsname
  changes.append(change)
 print("change_5a changes %s lines" %nchg)

def change_5b(lines,d_approved):
 d_not_approved = {}
 newlines = []
 for line in lines:
  newlines.append(line)
 #
 changes = []
 nchg = 0
 for iline,old in enumerate(newlines):
  # require old start with a numeric orphan
  m = re.search(r'^<ls>[0-9].*?</ls>',old)
  if m == None:
   continue
  # prev line and lastls
  lastls = None
  for i in [1,2,3]:
   ilineprev = iline - i
   oldprev = newlines[ilineprev] # preceding line
   if oldprev.startswith('<div'):
    # fail
    break
   # remove parenthetical expressions
   # special handling for Spr. (II)
   oldprev1a = oldprev.replace('Spr. (II)','Spr. _II_')
   oldprev1 = re.sub(r'\(.*?\)','',oldprev1a)
   ls_all_prev = re.findall(r'<ls.*?</ls>',oldprev1)
   if len(ls_all_prev) == 0:  # 
    continue
   lastls1 = ls_all_prev[-1] # last ls in previous line
   lastls = lastls1.replace('Spr. _II_','Spr. (II)')
   break  # for i
  if lastls == None:
   continue
  # ----------------------------------------------
  # get lsname from lastls
  m = re.search(r'<ls([^>]*)>([^<]*)</ls>',lastls)
  if m == None:
   # Can happen if there is '<is>' or other markup in lsprev
   continue
  # further restrictions
  mprev = re.search(r'^<ls([^>]*)>([^<]*)</ls>',lastls)
  if mprev == None:
   continue
  a = mprev.group(1)
  b = mprev.group(2)
  # get lsname
  m1 = re.search(r' n="(.*?)"',a)
  if m1 != None:
   a1 = m1.group(1)
   # next misses when "Spr. (II)"
   m2 = re.search(r'^[^0-9]+\.$',a1)
   if m2 != None:
    lsname = a1
   elif a1.startswith('Spr. (II)'):
    lsname = 'Spr. (II)'
   else:
    m3 = re.search(r'^([^0-9]+\.) [0-9,. ]+$',a1)
    if m3 != None:
     lsname = m3.group(1)
    else:
     # cannot get lsname from <ls n="X">
     continue
  else:
   # m1 == None
   m3 = re.search(r'^([^0-9]+\.) [0-9,. ]+$',b)
   if m3 != None:
    lsname = m3.group(1)
   elif b.startswith('Spr. (II)'):
    lsname = 'Spr. (II)'
   else:
    # cannot get lsname from <ls>X</ls>
    continue
  # now we have lsname.
  if False:
   print("%s -> %s" %(lastls,lsname))
  if lsname not in d_approved:
   if lsname not in d_not_approved:
    d_not_approved[lsname] = 0
   d_not_approved[lsname] = d_not_approved[lsname] + 1
   continue
  lsnew = '<ls n="%s">' %lsname 
  new = old.replace('<ls>',lsnew,1)  # first ls is replaced
  newlines[iline] = new
  nchg = nchg + 1
  change = Change(ilineprev,oldprev,iline,old,new)
  changes = d_approved[lsname]  # previous changes for this lsname
  changes.append(change)
 print("change_5b changes %s lines" %nchg)

def change_5b3(lines,d_approved):
 d_not_approved = {}
 newlines = []
 for line in lines:
  newlines.append(line)
 #
 changes = []
 nchg = 0
 for iline,old in enumerate(newlines):
  # require old start with a numeric orphan
  m = re.search(r'^<ls>[0-9].*?</ls>',old)
  if m == None:
   continue
  # prev line and lastls
  lastls = None
  for i in [1,2,3]:
   ilineprev = iline - i
   oldprev = newlines[ilineprev] # preceding line
   if oldprev.startswith('<div'):
    # fail
    break
   # remove parenthetical expressions
   # special handling for HALL  (which does not end in period_
   #oldprev1a = oldprev.replace('Spr. (II)','Spr. _II_')
   oldprev1 = re.sub(r'\(.*?\)','',oldprev)
   ls_all_prev = re.findall(r'<ls.*?</ls>',oldprev1)
   if len(ls_all_prev) == 0:  # 
    continue
   lastls = ls_all_prev[-1] # last ls in previous line
   break  # for i
  if lastls == None:
   continue
  # ----------------------------------------------
  # get lsname from lastls
  m = re.search(r'<ls([^>]*)>([^<]*)</ls>',lastls)
  if m == None:
   # Can happen if there is '<is>' or other markup in lsprev
   continue
  # further restrictions
  mprev = re.search(r'^<ls([^>]*)>([^<]*)</ls>',lastls)
  if mprev == None:
   continue
  a = mprev.group(1)
  b = mprev.group(2)
  # get lsname
  m1 = re.search(r' n="(.*?)"',a)
  if m1 != None:
   a1 = m1.group(1)
   # next misses when "HALL"
   m2 = re.search(r'^[^0-9]+\.?$',a1)
   if m2 != None:
    lsname = a1
   else:
    m3 = re.search(r'^([^0-9]+\.) [0-9,. ]+$',a1)
    if m3 != None:
     lsname = m3.group(1)
    else:
     # cannot get lsname from <ls n="X">
     continue
  else:
   # m1 == None
   m3 = re.search(r'^([^0-9]+\.?) [0-9,. ]+$',b)
   if m3 != None:
    lsname = m3.group(1)
   #elif b.startswith('Spr. (II)'):
   # lsname = 'Spr. (II)'
   else:
    # cannot get lsname from <ls>X</ls>
    continue
  # now we have lsname.
  if False:
   print("%s -> %s" %(lastls,lsname))
  if lsname not in d_approved:
   if lsname not in d_not_approved:
    d_not_approved[lsname] = 0
   d_not_approved[lsname] = d_not_approved[lsname] + 1
   continue
  lsnew = '<ls n="%s">' %lsname 
  new = old.replace('<ls>',lsnew,1)  # first ls is replaced
  newlines[iline] = new
  nchg = nchg + 1
  change = Change(ilineprev,oldprev,iline,old,new)
  changes = d_approved[lsname]  # previous changes for this lsname
  changes.append(change)
 print("change_5b3 changes %s lines" %nchg)

def change_5b4(lines,d_approved):
 d_not_approved = {}
 newlines = []
 for line in lines:
  newlines.append(line)
 #
 changes = []
 nchg = 0
 for iline,old in enumerate(newlines):
  # require old start with a numeric orphan
  m = re.search(r'^<ls>[0-9].*?</ls>',old)
  if m == None:
   continue
  # prev line and lastls
  lastls = None
  for i in [1,2,3]:
   ilineprev = iline - i
   oldprev = newlines[ilineprev] # preceding line
   if oldprev.startswith('<div'):
    # fail
    break
   # remove parenthetical expressions
   oldprev1 = re.sub(r'\(.*?\)','',oldprev)
   ls_all_prev = re.findall(r'<ls.*?</ls>',oldprev1)
   if len(ls_all_prev) == 0:  # 
    continue
   lastls = ls_all_prev[-1] # last ls in previous line
   break  # for i
  if lastls == None:
   continue
  m = re.search(r'<ls([^>]*)>([^<]*)</ls>',lastls)
  if m == None:
   # Can happen if there is '<is>' or other markup in lsprev
   continue
  # further restrictions
  mprev = re.search(r'^<ls([^>]*)>([^<]*)</ls>',lastls)
  if mprev == None:
   continue
  a = mprev.group(1)
  b = mprev.group(2)
  # get lsname
  m1 = re.search(r' n="(.*?)"',a)
  if m1 != None:
   a1 = m1.group(1)
   m2 = re.search(r'^[^0-9]+\.$',a1)
   if m2 != None:
    lsname = a1
   else:
    m3 = re.search(r'^([^0-9]+\.) *$',a1)  # no numbers
    if m3 != None:
     lsname = m3.group(1)
    else:
     # cannot get lsname from <ls n="X">
     continue
  else:
   # m1 == None
   m3 = re.search(r'^([^0-9]+\.) *$',b) # no numbers
   if m3 != None:
    lsname = m3.group(1)
   else:
    # cannot get lsname from <ls>X</ls>
    continue
  # now we have lsname.
  if lsname not in d_approved:
   if lsname not in d_not_approved:
    d_not_approved[lsname] = 0
   d_not_approved[lsname] = d_not_approved[lsname] + 1
   continue
  lsnew = '<ls n="%s">' %lsname 
  new = old.replace('<ls>',lsnew,1)  # first ls is replaced
  newlines[iline] = new
  nchg = nchg + 1
  change = Change(ilineprev,oldprev,iline,old,new)
  changes = d_approved[lsname]  # previous changes for this lsname
  changes.append(change)
 print("change_5a changes %s lines" %nchg)

def change_6a(lines,d_approved):
 d_not_approved = {}
 newlines = []
 for line in lines:
  newlines.append(line)
 #
 changes = []
 nchg = 0
 for iline,old in enumerate(newlines):
  # require exactly 2 ls, 2nd numeric
  ls_all = re.findall(r'<ls.*?</ls>',old)
  if len(ls_all) != 2:
   continue
  lsfirst = ls_all[0]
  lslast = ls_all[1]
  # require lslast start with a numeric orphan
  m = re.search(r'^<ls>[0-9]',lslast)
  if m == None:
   continue
  # ----------------------------------------------
  # get lsname from lsfirst
  m = re.search(r'<ls([^>]*)>([^<]*)</ls>',lsfirst)
  if m == None:
   # Can happen if there is '<is>' or other markup in lsprev
   continue
  # further restrictions
  mprev = re.search(r'^<ls([^>]*)>([^<]*)</ls>',lsfirst)
  if mprev == None:
   continue
  a = mprev.group(1)
  b = mprev.group(2)
  # get lsname
  m1 = re.search(r' n="(.*?)"',a)
  if m1 != None:
   a1 = m1.group(1)
   # next misses when "HALL"
   m2 = re.search(r'^[^0-9]+\.?$',a1)
   if m2 != None:
    lsname = a1
   else:
    m3 = re.search(r'^([^0-9]+\.) [0-9,. ]+$',a1)
    if m3 != None:
     lsname = m3.group(1)
    else:
     # cannot get lsname from <ls n="X">
     continue
  else:
   # m1 == None
   m3 = re.search(r'^([^0-9]+\.?) [0-9,. ]+$',b)
   if m3 != None:
    lsname = m3.group(1)
   #elif b.startswith('Spr. (II)'):
   # lsname = 'Spr. (II)'
   else:
    # cannot get lsname from <ls>X</ls>
    continue
  # now we have lsname.
  if False:
   print("%s -> %s" %(lastls,lsname))
  if lsname not in d_approved:
   if lsname not in d_not_approved:
    d_not_approved[lsname] = 0
   d_not_approved[lsname] = d_not_approved[lsname] + 1
   continue
  lsnew = '<ls n="%s">' %lsname
  lslastnew = lslast.replace('<ls>',lsnew)
  new = old.replace(lslast,lslastnew)
  newlines[iline] = new
  nchg = nchg + 1
  ilineprev = iline
  oldprev = old
  change = Change(ilineprev,oldprev,iline,old,new)
  changes = d_approved[lsname]  # previous changes for this lsname
  changes.append(change)
 print("change_6a changes %s lines" %nchg)

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
  if nchg == 0:
   continue
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
   if lnumprev != lnum:
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
 elif option == '3a':
  lsnames_d = get_lsnames_approved(option)
  change_3a(lines, lsnames_d) # update lsnames_d  
 elif option == '3b':
  lsnames_d = get_lsnames_approved(option)
  change_3b(lines, lsnames_d) # update lsnames_d  
 elif option == '4a':
  lsnames_d = get_lsnames_approved(option)
  lsnames_d['SPR.'] = []
  lsnames_d['Verz. d. Oxf. H.'] = [] #  many false positives
  lsnames_d['Z. f. d. K. d. M.'] = []
  change_3a(lines, lsnames_d) # update lsnames_d  
 elif option == '4b':
  lsnames_d = get_lsnames_approved(option)
  change_4b(lines, lsnames_d) # update lsnames_d  
 elif option == '4c':
  lsnames_d = get_lsnames_approved(option)
  change_4c(lines, lsnames_d) # update lsnames_d  
 elif option == '5a':
  lsnames_d = get_lsnames_approved(option)
  change_5a(lines, lsnames_d) # update lsnames_d  
 elif option == '5b1':
  lsnames_d = {}
  lsnames_d['Spr. (II)'] = []
  #lsnames_d['Spr.'] = []
  change_5b(lines, lsnames_d) # update lsnames_d  
 elif option == '5b2':
  lsnames_d = {}
  #lsnames_d['Spr. (II)'] = []
  lsnames_d['Spr.'] = []
  change_5b(lines, lsnames_d) # update lsnames_d  
 elif option == '5b3':
  lsnames_d = {}
  lsnames_d['HALL'] = []
  change_5b3(lines, lsnames_d) # update lsnames_d  
 elif option == '5b4':
  lsnames_d = get_lsnames_approved(option)
  #lsnames_d = {}
  #lsnames_d['HALL'] = []
  change_5b4(lines, lsnames_d) # update lsnames_d  
 elif option == '6a':
  lsnames_d = get_lsnames_approved(option)
  #lsnames_d = {}
  #lsnames_d['HALL'] = []
  change_6a(lines, lsnames_d) # update lsnames_d  
 elif option == '7a':
  lsnames_d = {}
  lsnames_d['VS. PRĀT.'] = []
  #lsnames_d['PAÑCAT.'] = []
  change_7a = change_5b3
  change_5b3(lines, lsnames_d) # update lsnames_d  
 elif option == '7b': # not yet used
  lsnames_d = {}
  lsnames_d['TARKAS.'] = []
  lsnames_d[' MṚKCH.'] = []
  lsnames_d['ŚUK.'] = []
  lsnames_d['Spr.'] = []
  lsnames_d['BRAHMA-P.'] = []
  lsnames_d['ŚĀṄKH. BR.'] = []
  #lsnames_d[''] = []
  #lsnames_d[''] = []
 
  change_7b = change_5b3
  change_5b3(lines, lsnames_d) # update lsnames_d  
 else:
  print('ERROR: unknown option',option)
  exit(1)
 write_changes(fileout,lsnames_d)


 
