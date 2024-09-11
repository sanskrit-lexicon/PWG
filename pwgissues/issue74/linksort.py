# coding=utf-8
""" linksort.py
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
 regex1raw = r'<ls>M\..*?<?ls>'
 regex2raw = r'<ls n="M\..*?">.*?</ls>'
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
 regex1raw = r'<ls>M\. ([0-9]+), ([0-9]+)\.?</ls>'
 regex2raw = r'<ls n="M\. ([0-9]+),">([0-9])+\.?</ls>'
 regex3raw = r'<ls n="M\.">([0-9]+), ([0-9])+\.?</ls>'
 regex4raw =  r'<ls>M\.</ls>'
 regex5raw = r'<ls>M\. ([0-9]+), ([0-9]+)\. fgg?\.</ls>'
 regex6raw = r'<ls n="M\. ([0-9]+),">([0-9])+\. fgg?\.</ls>'
 regex7raw = r'<ls n="M\.">([0-9]+), ([0-9])+\. fgg?\.</ls>'
 regex1 = re.compile(regex1raw)
 regex2 = re.compile(regex2raw)
 regex3 = re.compile(regex3raw)
 regex4 = re.compile(regex4raw)
 regex5 = re.compile(regex5raw)
 regex6 = re.compile(regex6raw)
 regex7 = re.compile(regex7raw)
 regexes = (regex1,regex2,regex3,regex4,regex5,regex6,regex7)
 return regexes

def get_links2(entries):
 recs = []
 regexes = get_standard_regexes()
 d = {}
 for ientry,entry in enumerate(entries):
  text = ' '.join(entry.datalines)
  for iregex,regex in enumerate(regexes):
   for m in re.finditer(regex,text):
    if iregex == 3:
     v = (0,0) # no parameters
    else:
     v1 = int(m.group(1))
     v2 = int(m.group(2))
     v = (v1,v2)
    if v not in d:
     d[v] = 0
    d[v] = d[v] + 1

 keys = sorted(d.keys())
 ntot = 0
 for v in keys:
  n = d[v]
  recs.append('%s,%s (%s)'%(v[0],v[1],n))
  ntot = ntot + n
 print(ntot,"total number of 'regular' links")
 return recs

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
 if option == '1':
  recs = get_links1(entries)
  recs1 = sorted(recs)
  write_lines(fileout,recs1)
 elif option == '2':
  recs_sorted = get_links2(entries)
  write_lines(fileout,recs_sorted)
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

