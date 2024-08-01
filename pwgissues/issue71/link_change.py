# coding=utf-8
""" link_change.py
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

def write_clines(option,fileout,lines,clines):
 outarr = []
 ntodo = 0
 nok = 0
 assert option in ['OK','TODO']
 for iline,line in enumerate(lines):
  # outarr.append(line)
  cline = clines[iline]
  status = None
  if cline == None:
   #outarr.append('* TODO %s' % line)
   ntodo = ntodo + 1
   status = 'TODO'
  elif '<ls?' in cline:
   # outarr.append('* TODO %s' % line)
   ntodo = ntodo + 1
   status = 'TODO'
  else:
   # outarr.append('* OK %s' % line)
   nok = nok + 1
   status = 'OK'
  if option != status:
   continue
  if False: # dbg
   if line == '<ls>KATHĀS. 1, 23, 158</ls>':
    print('line=',line)
    print('cline=', cline)
    print('option=',option)
  # generate output
  outarr.append('* %s' % line)
  if cline == None:
   outarr.append('?')
  else:                 
   for m in re.finditer(r'<ls.*?</ls>',cline):
    outarr.append('  %s' % m.group(0))
  outarr.append('')
 write_lines(fileout,outarr)
 #print(len(lines),"lines examined")
 if option == 'OK':
  n = nok
 else:
  n = ntodo
 print('%s marked %s written to %s' %(n,option,fileout))
 
def get_kindpart(part):
 m = re.search(r'^([0-9]+),$',part)
 if m != None:
  return (m.group(1), 'c')
 m = re.search(r'^([0-9]+)\.$',part)
 if m!= None:
  return (m.group(1), 'p')
 if part in ('fg.','fgg.'):
  return (part,'f')
 # unknown part
 return (part,'?')

def unparsed_split(kinds):
 # kinds a non-empty list of 2-tuples
 a = []
 b = []
 ktypes = [kind[1] for kind in kinds]
 s = ''.join(ktypes)
 if s.startswith('cpf'):
  a = [kinds[0],kinds[1],kinds[2]]
  b = kinds[3:]
 elif s.startswith('cp'):
  a = [kinds[0],kinds[1]]
  b = kinds[2:]
 elif s.startswith('pf'):
  a = [kinds[0],kinds[1]]
  b = kinds[2:]
 else:
  a = [kinds[0]]
  b = kinds[1:]
 return (a,b)

def change_line(ls,dbg = False):
 # dbg = (ls == '<ls>KATHĀS. 46, 68. fg. 71. fg.</ls>')
 m = re.search(r'(<ls>KATHĀS. )(.+)</ls>',ls)
 if m == None:
  m = re.search(r'(<ls n="KATHĀS.">)(.+)</ls>',ls)
 if m == None:
  print('test2 wrong form\n',ls)
  return None
 k0 = m.group(1)
 data0 = m.group(2)
 # change nnn,mmm to nnn, mmm  (with space - which is current norm in pwg)
 data = re.sub(r'([0-9]),([0-9])',r'\1, \2',data0)
 # similarly 'nnn.fg' -> 'nnn. fg'
 data = re.sub(r'([0-9])\.(fg)',r'\1. \2',data)
 # for 300+ instances, the last term is a digit, rather than '.'
 # the parsing logic assumes ending period. Work around.
 if not data.endswith('.'):
  data = data + '.'
  periodFlag = True
 else:
  periodFlag = False
 parts = data.split(' ')
 kinds = [get_kindpart(part) for part in parts]
 if dbg:
  print('ls=',ls)
  print('kinds=',kinds)
 parsed = []
 unparsed = kinds
 while unparsed != []:
  a,b = unparsed_split(unparsed)
  parsed.append(a)
  unparsed = b
 cprev = None #
 k1 = '<ls n="KATHĀS.">'
 kprob = '<ls? n="KATHĀS.">'
 lsarr = []
 probflag = False
 for i,partseq in enumerate(parsed):
  sarr = []
  arr = []
  for part in partseq:
   selt = part[1]
   sarr.append(selt)
   if selt == 'p':
    arr.append(part[0] + '.')
   elif selt == 'c':
    arr.append(part[0] + ',')
   else:
    arr.append(part[0])
  s = ''.join(sarr)
  data = ' '.join(arr)
  if (s == 'cpf') or (s == 'cp') :
   if i == 0:
    lshead = k0
   else:
    lshead = k1
   ls = '%s%s</ls>' %(lshead,data)
   cprev = partseq[0]
  elif (s == 'p') and (cprev != None) and (i != 0):
   lshead = '<ls n="KATHĀS. %s,">' % cprev[0]
   ls = '%s%s</ls>' %(lshead,data)
  elif (s == 'pf') and (cprev != None) and (i != 0):
   lshead = '<ls n="KATHĀS. %s,">' % cprev[0]
   ls = '%s%s</ls>' %(lshead,data)
  else:
   lshead = kprob
   ls = '%s%s</ls>' %(lshead,data)
  lsarr.append(ls)   
 if periodFlag:
  # remove ending period from last ls
  last = lsarr.pop()
  last = last.replace('.</ls>','</ls>xx')
  lsarr.append(last)
 if dbg:
  print(data)
  print(kinds)
  for i,partseq in enumerate(parsed):
   print('%s -> %s' %(partseq,lsarr[i]))
 ans = ' '.join(lsarr)
 return ans

if __name__=="__main__":
 filein = sys.argv[1]  # linksort3
 fileout = sys.argv[2] # emacs org-mode format  OK
 fileout1 = sys.argv[3] # TODO
 lines = read_lines(filein)
 clines = []
 for line in lines:
  cline = change_line(line)
  clines.append(cline)
 write_clines('OK',fileout,lines,clines)
 write_clines('TODO',fileout1,lines,clines)
 
  
