# coding=utf-8
""" link_change.py for pwg bhagp_bur
"""
from __future__ import print_function
import sys, re,codecs
import digentry  

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_outrecs(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outrecs),"cases written to",fileout)

def write_recs(fileout,recs):
 outrecs = []
 for irec,rec in enumerate(recs):
  if rec.lnum == None:
   print('write_recs problem:',rec.linein)
  outarr = []
  outarr.append('; %s' %rec.metaline)
  outarr.append('; %s -> %s' %(rec.oldword,rec.newword))
  outarr.append('%s old %s' % (rec.lnum,rec.line))
  outarr.append(';')
  outarr.append('%s new %s' % (rec.lnum,rec.newline))
  outrecs.append(outarr)
 write_outrecs(fileout,outrecs)

def write_outrecs(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outrecs),"cases written to",fileout)

def write_lines(fileout,outarr,printFlag=False):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    if out == None:
     out = '?'
    f.write(out+'\n')
 if printFlag:
  print(len(outarr),"lines written to",fileout)

def write_lines_simple(fileout,outarr,printFlag=True):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    #if out == None:
    # out = '?'
    f.write(out+'\n')
 if printFlag:
  print(len(outarr),"lines written to",fileout)

def check_standard(ls,sregs):
 used = []
 for ireg,sreg in enumerate(sregs):
  if re.search(sreg,ls):
   used.append((ireg,sreg))
 return (len(used) == 1)

def check_standarda(ls,sregs):
 used = []
 for ireg,sreg in enumerate(sregs):
  m = re.search(sreg,ls)
  if m:
   used.append((m,ireg))
 flag = (len(used) == 1)
 if flag:
  m,ireg = used[0]
 else:
  m,ireg = None,-1
 return flag,m,ireg

def get_standard_regexes(X):
 d1 = "([0-9]+)"
 d2 = "([0-9]+)"
 d3 = "([0-9]+)"
 # r"X (ABC|DEF)?"  syntax for optional matches
 # optional . OR optional fg. OR optional fgg.
 Y = "(\.| fg\.| fgg\.|\. fg\.|\. fgg\.)?"
 regexraws = [
  r'<ls>%s</ls>' % X,
  r'<ls>%s %s,%s,%s%s</ls>' %(X,d1,d2,d3,Y),
  r'<ls n="%s">%s,%s,%s%s</ls>' %(X,d1,d2,d3,Y),
  r'<ls n="%s %s,">%s,%s%s</ls>' %(X,d1,d2,d3,Y),
  r'<ls n="%s %s,%s,">%s%s</ls>' %(X,d1,d2,d3,Y),
 ]
 regexes = list(map(re.compile,regexraws))
 return regexes,regexraws

X = r'BHĀG\. P\.'
X1 = 'BHĀG. P.'
#X = 'Z'
sregs, sregraws = get_standard_regexes(X)

def get_test1_regexes(X):
 d1 = "([0-9]+)"
 d2 = "([0-9]+)"
 d3 = "([0-9]+)"
 # r"X (ABC|DEF)?"  syntax for optional matches
 # optional . OR optional fg. OR optional fgg.
 Y = "( fg\.| fgg\.|\. fg\.|\. fgg|\.|)?"
 regexraws = [
  r'<ls>%s %s,%s,%s%s (.*)</ls>' %(X,d1,d2,d3,Y),
  r'<ls n="%s">%s,%s,%s%s (.*)</ls>' %(X,d1,d2,d3,Y),
  r'<ls n="%s %s,">%s,%s%s (.*)</ls>' %(X,d1,d2,d3,Y),
  r'<ls n="%s %s,%s,">%s%s (.*)</ls>' %(X,d1,d2,d3,Y),
 ]

 regexes = list(map(re.compile,regexraws))
 return regexes,regexraws

def test1(filein,fileout):
 # python link_change.py 
 lines_all = read_lines(filein)
 nok1 = 0
 ntodo1 = 0
 sregs,sregsraw = get_standard_regexes(X)
 ilinestodo1 = []
 for iline,line in enumerate(lines_all):
  used = []
  for ireg,sreg in enumerate(sregs):
   sregraw = sregraws[ireg]
   if re.search(sreg,line):
    used.append((ireg,sregraw))
  if len(used) == 1:
   nok1 = nok1 + 1
  else:
   ntodo1 = ntodo1 + 1
   ilinestodo1.append(iline)
 print('test1 nok1=%s, ntodo1=%s' % (nok1,ntodo1))
 sregs2,raws2 = get_test1_regexes(X)
 nok2 = 0
 ntodo2 = 0
 data2 = []
 nomatch2 = 0
 for iline in ilinestodo1:
  line = lines_all[iline]
  used = []
  for ireg,sreg in enumerate(sregs2):
   m = re.search(sreg,line) 
   if m != None:
    used.append((iline,ireg,m))
  if len(used) == 1:
   nok2 = nok2 + 1
   data2.append(used[0])
  elif len(used) == 0:
   #print('no match2: %s' %line)
   nomatch2 = nomatch2 + 1
  else:
   print('chk:',line)
   print(used)
   #exit(1)
 print('test1 nok2=%s, ntodo2=%s, nomatch2=%s,' % (nok2,ntodo2,nomatch2))
 #assert ntodo2 == 0
 # debug output for ireg=0 type:
 # r'<ls>%s %s,%s,%s%s (.*)</ls>' %(X,d1,d2,d3,Y),
 outarr = []
 #print(len(data2),' data2 length')
 iregcount = {}
 for data in data2:
  iline,ireg,m = data
  if ireg not in iregcount:
   iregcount[ireg] = 0
  iregcount[ireg] = iregcount[ireg] + 1
  #if ireg != 0:
  # continue
  line = lines_all[iline]
  (d1,d2,d3,y,rest) = m.groups()
  if (ireg == 0):
   x = '<ls>%s' % X
  else:
   x = '<ls n="%s' % X
  if y == None:
   y = ''
  #part1 = '%s,%s,%s%s' %(d1,d2,d3,y)
  part1 = '<ls>%s %s,%s,%s%s</ls>' %(X1,d1,d2,d3,y)
  part2 = '<ls n="%s">%s</ls>' %(X1,rest)
  #outarr.append('*%s' % line)
  #outarr.append(' ' + part1)
  #outarr.append(' ' + part2)
  outarr.append('%s\t%s\t%s' %(line,part1,part2))

 print(iregcount)
 write_lines_simple(fileout,outarr)

def get_test2_regexes(X):
 return get_test1_regexes(X)

def construct_outdata(data,iregcount):
 iline,ireg,m,line = data
 #outarr = []  
 if ireg not in iregcount:
  iregcount[ireg] = 0
 iregcount[ireg] = iregcount[ireg] + 1
 #line = lines_all[iline]
 (d1,d2,d3,y,rest) = m.groups()
 if y == None:
  y = ''
 if ireg == 0: # X1 is global variable
  part1 = '<ls>%s %s,%s,%s%s</ls>' %(X1,d1,d2,d3,y)
 else:
  part1 = '<ls n="%s">%s,%s,%s%s</ls>' %(X1,d1,d2,d3,y)
 part2 = '<ls n="%s">%s</ls>' %(X1,rest)
 outarr = (line,part1,part2)
 return outarr

def test2_analyze(line,sregs2):
 nfound = 0 # number of regexes matching line
 ans = (-1,-1) 
 for ireg,sreg in enumerate(sregs2):
  m = re.search(sreg,line) 
  if m != None:
   ans = ireg,m
   nfound = nfound + 1
 if nfound not in (0,1):
  # multiple matches
  print('ERROR test2_analyze: no matches found for line\nline')
  exit(1)
 return ans
  
def test2(filein,fileout):
 # python link_change.py 
 lines_all = read_lines(filein)
 nok1 = 0
 ntodo1 = 0
 X = r'BHĀG\. P\.'
 sregs,sregsraw = get_standard_regexes(X)
 ilinestodo1 = []
 sregs2,raws2 = get_test2_regexes(X)
 nok2 = 0
 ntodo2 = 0
 data2 = []
 nomatch2 = 0
 outarr = []
 iregcount = {}
 for iline,line in enumerate(lines_all):
  flag = check_standard(line,sregs)  
  if flag:
   nok1 = nok1 + 1
   continue # this line is standard
  ntodo1 = ntodo1 + 1
  ireg,m = test2_analyze(line,sregs2)
  if ireg == -1:
   # this line can't be handled here
   nomatch2 = nomatch2 + 1
   continue
  nok2 = nok2 + 1
  data = (iline,ireg,m,line)
  lses = construct_outdata(data,iregcount)
  line,part1,part2 = lses
  # try to construct from part2 (the rest)
  dbg = line == '<ls n="BHĀG. P.">3,5,5. 4,6,7. 24,61</ls>'
  dbg = False
  if dbg: print('line:  ',line)
  if dbg: print('part1: ',part1)
  parsed = [line,part1]
  while True:   
   line1,part1,part2 = lses
   if dbg: print('part2: ',part2)
   flag = check_standard(part2,sregs)
   if dbg: print('flag : ',flag)
   if flag:
    # part2 is standard. Add to parsed and break the while loop
    if dbg: print('appending standard',part2)
    parsed.append(part2)
    break
   ireg2,m2 = test2_analyze(part2,sregs2)
   if dbg: print('ireg2=',ireg2)
   if ireg2 == -1:
    # can't proceed further
    parsed.append(part2)
    if dbg: print('appending other',part2)
    break
   # further analyis succeeds
   #parsed.append(part2)
   data = (-1,ireg2,m2,part2)
   _iregcount = {}
   lses = construct_outdata(data,_iregcount)
   line1a,part1a,part2a = lses
   parsed.append(part1a)
  # back totop of loop
  out = '\t' . join(parsed)
  outarr.append(out)

 print('test2 nok1=%s, ntodo1=%s' % (nok1,ntodo1))
 print('test2 nok2=%s, ntodo2=%s, nomatch2=%s,' % (nok2,ntodo2,nomatch2))
 print(iregcount)
 write_lines_simple(fileout,outarr)

def get_test3_regexes(X):
 d1 = "([0-9]+)"
 d2 = "([0-9]+)"
 d3 = "([0-9]+)"
 # r"X (ABC|DEF)?"  syntax for optional matches
 # optional . OR optional fg. OR optional fgg.
 Y = "( fg\.| fgg\.|\. fg\.|\. fgg|\.)?"
 regexraws = [
  r'<ls n="%s">%s,%s%s</ls>' %(X,d1,d2,Y),
  #r'<ls n="%s">%s%s (.*)</ls>' %(X,d1,Y),
  r'<ls n="%s">%s%s</ls>' %(X,d1,Y),
 ]

 regexes = list(map(re.compile,regexraws))
 return regexes,regexraws

def test3_analyze(line,sregs):
 nfound = 0 # number of regexes matching line
 ans = (-1,-1) 
 for ireg,sreg in enumerate(sregs):
  m = re.search(sreg,line) 
  if m != None:
   ans = ireg,m
   nfound = nfound + 1
 if nfound not in (0,1):
  # multiple matches
  print('ERROR test3_analyze: multiple matches found for line\n',line)
  exit(1)
 return ans

def test3(filein,fileout):
 # python link_change.py 
 lines_all = read_lines(filein)
 nok1 = 0
 ntodo1 = 0
 X = r'BHĀG\. P\.'
 sregs,sregsraw = get_standard_regexes(X)
 ilinestodo1 = []
 sregs3,raws3 = get_test3_regexes(X)
 nok2 = 0
 ntodo2 = 0
 data2 = []
 nomatch2 = 0
 outarr = []
 iregcount = {}
 for ilineall,lineall in enumerate(lines_all):
  ientry,lnum,line = lineall.split('\t')
  flag,m,ireg = check_standarda(line,sregs)  
  if flag: # this line is standard
   nok1 = nok1 + 1
   continue 
  ntodo1 = ntodo1 + 1
  lineall_prev = lines_all[ilineall-1]  # assume ilineall>0 - a fact of this
  ientry_prev,lnum_prev,line_prev = lineall_prev.split('\t')
  flag_prev,m_prev,ireg_prev = check_standarda(line_prev,sregs)
  if not flag_prev:
   # this line can't be handled here
   nomatch2 = nomatch2 + 1
   continue
  if ireg_prev == 0:
   # this line can't be handled here
   nomatch2 = nomatch2 + 1
   continue
  if ientry_prev != ientry:
   # this line can't be handled here
   nomatch2 = nomatch2 + 1
   continue
  (d1p,d2p,d3p,yp) = m_prev.groups()
  if yp == None:
   yp = ''
  ireg,m = test3_analyze(line,sregs3)
  if ireg == -1:
   # this line can't be handled here
   nomatch2 = nomatch2 + 1
   continue
  if ireg == 0:
   d2,d3,y = m.groups()
   d1 = d1p
  elif ireg == 1:
   d3,y = m.groups()
   d1 = d1p
   d2 = d2p
  else:
   print('test3 error\n%s\n%s' %(line_prev,line))
   exit(1)
  if y == None:
   y = ''
  nok2 = nok2 + 1
  parsed = []
  parsed.append(line)
  part1 = '<ls n="%s">%s,%s,%s%s</ls>' %(X1,d1,d2,d3,y)
  parsed.append(part1)
  # recursive lo
  while False:
   line1,part1,part2 = lses
   flag = check_standard(part2,sregs)
   if flag:
    # part2 is standard. Add to parsed and break the while loop
    if dbg: print('appending standard',part2)
    parsed.append(part2)
    break
   ireg2,m2 = test2_analyze(part2,sregs2)
   if dbg: print('ireg2=',ireg2)
   if ireg2 == -1:
    # can't proceed further
    parsed.append(part2)
    if dbg: print('appending other',part2)
    break
   # further analyis succeeds
   #parsed.append(part2)
   data = (-1,ireg2,m2,part2)
   _iregcount = {}
   lses = construct_outdata(data,_iregcount)
   line1a,part1a,part2a = lses
   parsed.append(part1a)
   # back to top of while loop
  # while loop is done
  # out = ientry lnum line_prev 
  outrec = [ientry,lnum,line_prev] + parsed
  out = '\t' . join(outrec)
  outarr.append(out)

 print('test2 nok1=%s, ntodo1=%s' % (nok1,ntodo1))
 print('test2 nok2=%s, ntodo2=%s, nomatch2=%s,' % (nok2,ntodo2,nomatch2))
 print(iregcount)
 write_lines_simple(fileout,outarr)

if __name__=="__main__":
 option = sys.argv[1]
 filein = sys.argv[2]  # linksort_n.txt
 fileout = sys.argv[3] # emacs org-mode format  OK
 X = r'BHĀG\. P\.'
 if option == '1':
  test1(filein,fileout)
 elif option == '2':
  test2(filein,fileout)
 elif option == '3':
  test3(filein,fileout)
 else:
  print('unknown option:',option)
  exit(1)
