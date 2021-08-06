""" remark_ls.py
 utility function to reformat a complex ls in PWG
 Main routine is remark_pwg.
 
"""
import sys,re;

def remark_pwg_helper2(parms):
 parmgroups = []
 nparms = len(parms)
 iparm = 0
 comma = ','
 period = '.'
 error = [],'BAD PARM SEQUENCE'
 # this works for 2 as standard number of parameters
 while iparm < nparms:
  parm = parms[iparm]
  pval,ptype = parm
  if ptype == comma:
   iparm1 = iparm + 1
   if iparm1 == nparms:
    return error
   parm1 = parms[iparm1]
   pval1,ptype1 = parm1
   if ptype1 != period:
    return error
   parmgroups.append([parm,parm1])
   iparm = iparm + 2
   continue
  elif ptype == period:
   parmgroups.append([parm])
   iparm = iparm + 1
  else:
   return error
 return parmgroups,True

def remark_pwg(lselt,abbrev,nparmabbrev):
 default = (lselt,'TODO')
 error = (lselt,'ERROR')
 m = re.search('^<ls>%s (.*)</ls>$' % abbrev,lselt)
 if m == None:
  return default
 parmstr = m.group(1)
 parmsraw = parmstr.split(' ')
 parms = []
 for parm in parmsraw:
  m = re.search(r'^([0-9]+)([,.])$',parm)
  if m == None:
   # bad parameter exit the routine
   return error
  parms.append((m.group(1),m.group(2)))
 if nparmabbrev == 2:
  parmgroups,status = remark_pwg_helper2(parms)
  if status != True:
   return (lselt,status)
 else:
  return default
 if False: #debug
  print(len(parmgroups),'parmgroups')
  for pg in parmgroups:
   print(pg)
 # construct sequence of ls elements from parmgroups
 ans = []  # sequence of strings represent ls elements
 prev1 = None
 for parmgroup in parmgroups:
  if prev1 == None:
   # first one, require 2 elements in parmgroup
   if len(parmgroup) != 2:
    return error
   parm1,parm2 = parmgroup
   a1 = '%s%s' % parm1
   a2 = '%s%s' % parm2
   elt = '<ls>%s %s %s</ls>' %(abbrev,a1,a2)
   ans.append(elt)
   prev1 = a1
  elif len(parmgroup) == 2:
   parm1,parm2 = parmgroup
   a1 = '%s%s' % parm1
   a2 = '%s%s' % parm2
   elt = '<ls n="%s">%s %s</ls>' %(abbrev,a1,a2)
   ans.append(elt)
   prev1 = a1
  elif len(parmgroup) == 1:
   parm2 = parmgroup[0]
   a2 = '%s%s' % parm2
   elt = '<ls n="%s %s">%s</ls>' %(abbrev,prev1,a2)
   ans.append(elt)
   # no reset of prev1
 ans_str = ' '.join(ans)
 return ans_str,'OK'

def test():
 tests = [
     ('<ls>TS. PRAT 1, 2. 3, 4.</ls>','TS. PRAT',2),
     ('<ls>TS. PRAT 1, 2. 4.</ls>','TS. PRAT',2),
     ('<ls>TS. PRAT 1, 2. 4. 5, 6. 7.</ls>','TS. PRAT',2),
     ('<ls>TS. PRAT 1, 2, 4.</ls>','TS. PRAT',2),
 ]
 for lselt,abbrev,nparmabbrev in tests:
  new,status = remark_pwg(lselt,abbrev,nparmabbrev)
  print('lselt  = ',lselt)
  print('abbrev = ',abbrev,', nparmabbrev = ',nparmabbrev)
  print('status = ',status)
  print('remark = ',new)
  print()
if __name__ == "__main__":
 test()
 
