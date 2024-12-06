# coding=utf-8
""" linksort.py for BHĀG. P.
"""
from __future__ import print_function
import sys, re,codecs
import digentry  

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

def get_links1(entries):
 recs = []
 regex1raw = r'<ls>BHĀG\. P\..*?</ls>'
 regex2raw = r'<ls n="BHĀG\. P\..*?">.*?</ls>'
 regex1 = re.compile(regex1raw)
 regex2 = re.compile(regex2raw)
 for ientry,entry in enumerate(entries):
  text = ' '.join(entry.datalines)
  a1 = re.findall(regex1,text)
  a2 = re.findall(regex2,text)
  for x in a1:
   recs.append(x)
  for x in a2:
   recs.append(x)
 return recs

def get_standard_regexes():
 X = "BHĀG\. P\."
 d1 = "([0-9]+)"
 d2 = "([0-9]+)"
 d3 = "([0-9]+)"
 # r"X (ABC|DEF)?"  syntax for optional matces
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
 for iregex,regex in enumerate(regexes):
  print('%s %s' %(iregex+1,regex))
 return regexes

def get_links2(allrecs):
 newrecs = []
 regexes = get_standard_regexes()
 nok = 0
 notok = 0
 for irec,rec in enumerate(allrecs):
  # rec is a text
  found = False
  for iregex,regex in enumerate(regexes):
   m = re.search(regex,rec)
   if m != None:
    found = True
    break # no need to check other regexes
  if found:
   nok = nok + 1
   newrec = rec
  else:
   notok = notok + 1
   newrec = '%s ?' % rec
  newrecs.append(newrec)
 print('%s ok, %s ?, %s total' %(nok,notok,len(allrecs)))
 return newrecs

def get_links3(entries):
 recs1 = []
 recs2 = []
 # standard links
 sregexes = get_standard_regexes()
 # any link see get_links1
 regex1raw = r'<ls>M\..*?<?ls>'
 regex2raw = r'<ls n="M\..*?">.*?</ls>'
 regex1 = re.compile(regex1raw)
 regex2 = re.compile(regex2raw)

 d = {}
 for ientry,entry in enumerate(entries):
  text = ' '.join(entry.datalines)
  a1 = re.findall(regex1,text)
  a2 = re.findall(regex2,text)
  for x in a1:
   standard = False
   for sregex in sregexes:
    if re.search(sregex,x):
     standard = True
     break
   if not standard:
    recs1.append(x)
  for x in a2:
   standard = False
   for sregex in sregexes:
    if re.search(sregex,x):
     standard = True
     break
   if not standard:
    recs2.append(x)
 print(len(recs1),"non-standard of type1")
 print(len(recs2),"non-standard of type2")
 return recs1,recs2

def get_links4(entries):
 recs1 = []
 # standard links
 sregexes = get_standard_regexes()
 # any link see get_links1
 regex1raw = r'<ls>M\..*?<?ls>'
 regex2raw = r'<ls n="M\..*?">.*?</ls>'
 regex1 = re.compile(regex1raw)
 regex2 = re.compile(regex2raw)
 regex0raw = r'<ls.*?</ls>' # ALL ls - not only M
 regex0 = re.compile(regex0raw)
 
 d = {}
 for ientry,entry in enumerate(entries):
  text = ' '.join(entry.datalines)
  a = re.findall(regex0,text)
  b = []
  for x in a:
   standard = False
   t = -1  # taranga
   for isregex,sregex in enumerate(sregexes):
    m = re.search(sregex,x)
    if m != None:
     if len(m.groups()) == 2:
      standard = True
      t = m.group(1)  
      break
   b.append((standard,t,x))
  for i,y in enumerate(b):
   standard,t,x = y
   if standard:
    continue
   # x is non-standard. generate a record
   if not (re.search(regex1,x) or re.search(regex2,x)):
    continue
   recdefault = (x,'-1','NA')
   if i == 0:
    rec = recdefault
   else:
    y0 = b[i-1]
    standard0,t0,x0 = y0
    if standard0:
     rec = (x,t0,x0)
    else:
     rec = (x,-1,x0)
   recs1.append(rec)
   if False and (len(recs1) == 1) : # dbg
    x,t,x0 = rec
    print('chk: x=',x)
    print('     t=',t)
    print('    x0=',x0)
    exit(1)
 print(len(recs1),"non-standard records")
 return recs1

def get_links5(entries):
 # almost same as links4.  Returns also metaline in each record
 recs1 = []
 # standard links
 sregexes = get_standard_regexes()
 # any link see get_links1
 regex1raw = r'<ls>M\..*?<?ls>'
 regex2raw = r'<ls n="M\..*?">.*?</ls>'
 regex1 = re.compile(regex1raw)
 regex2 = re.compile(regex2raw)
 regex0raw = r'<ls.*?</ls>' # ALL ls - not only M
 regex0 = re.compile(regex0raw)
 
 d = {}
 for ientry,entry in enumerate(entries):
  metaline = entry.metaline
  text = ' '.join(entry.datalines)
  a = re.findall(regex0,text)
  b = []
  for x in a:
   standard = False
   t = -1  # taranga
   for isregex,sregex in enumerate(sregexes):
    m = re.search(sregex,x)
    if m != None:
     if len(m.groups()) == 2:
      standard = True
      t = m.group(1)  
      break
   b.append((standard,t,x,metaline))
  for i,y in enumerate(b):
   standard,t,x,meta = y
   if standard:
    continue
   # x is non-standard. generate a record
   if not (re.search(regex1,x) or re.search(regex2,x)):
    continue
   recdefault = (x,'-1','NA',metaline)
   if i == 0:
    rec = recdefault
   else:
    y0 = b[i-1]
    standard0,t0,x0,metaline = y0
    if standard0:
     rec = (x,t0,x0,metaline)
    else:
     rec = (x,-1,x0,metaline)
   recs1.append(rec)
   if False and (len(recs1) == 1) : # dbg
    x,t,x0 = rec
    print('chk: x=',x)
    print('     t=',t)
    print('    x0=',x0)
    exit(1)
 print(len(recs1),"non-standard records")
 return recs1

def option_5_helper(recs,lines):
 # first, get metaline map
 d = {}
 for rec in recs:
  (x,t,x0,meta) = rec
  if meta not in d:
   d[meta] = []
  d[meta].append(rec)
  
 newlines = []
 metaline = None
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   metaline = line
   imeta = iline
   newlines.append(line)
   continue
  if line.startswith('<LEND>'):
   metaline = None
   if newlines[imeta].startswith('* '):
    newline = '* ' + line
   else:
    newline = line
   newlines.append(newline)
   continue
  if metaline == None:
   newlines.append(line)
   continue
  # a normal dataline.
  # Search for matching recs
  if metaline not in d:
   newlines.append(line)
   continue
  recsmatch = d[metaline]
  newline = line
  for rec in recsmatch:
   x,t,x0,meta = rec
   newline = newline.replace(x,'** '+x)
  newlines.append(newline)
  # also mark metaline  * is for emacs org
  oldmeta = newlines[imeta]
  if oldmeta.startswith('* '):
   pass # nothing to do
  else:
   newmeta = '* TODO ' + oldmeta
   newlines[imeta] = newmeta
 return newlines

if __name__=="__main__":
 option = sys.argv[1]
 filein = sys.argv[2]  # xxx.txt
 fileout = sys.argv[3] # 
 entries = digentry.init(filein)
 all_recs = get_links1(entries)
 #all_recs_sorted = sorted(all_recs)
 
 if option == '1':
  write_lines(fileout,all_recs)
 elif option == '2':
  # all records. Non-standard marked with ending
  newrecs = get_links2(all_recs)
  write_lines(fileout,newrecs)
 elif option == '3':
  recs1,recs2 = get_links3(entries)
  recs1_sort = sorted(recs1)
  recs2_sort = sorted(recs2)
  recs = recs1_sort + recs2_sort
  write_lines(fileout,recs)
 elif option == '4':
  recs1= get_links4(entries)
  recs1_sort = sorted(recs1,key = lambda x: x[0])
  recs = recs1_sort
  outarr = ['%s\t%s\t%s' % (x,t,x0) for x,t,x0 in recs]
  write_lines(fileout,outarr)
 elif option == '5':
  recs1= get_links5(entries) # 
  # recs1_sort = sorted(recs1,key = lambda x: x[0])
  lines = read_lines(filein)
  newlines = option_5_helper(recs1,lines)
  #outarr = ['%s\t%s\t%s' % (x,t,x0) for x,t,x0 in recs]
  write_lines(fileout,newlines)
 else:
  print('ERROR option unknown:',option)
  exit(1)

