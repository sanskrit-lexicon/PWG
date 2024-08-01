# coding=utf-8
""" link_change_a.py
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


def write_crecs(option,fileout,lines0,crecs0):
 outarr = []
 ntodo = 0
 nok = 0
 assert option in ['OK','TODO']
 lines = []
 crecs = []
 for irec,rec in enumerate(crecs0):
  if rec.status == option:
   line = lines0[irec]
   lines.append(line)
   crecs.append(rec)
 #
 for irec,rec in enumerate(crecs):
  # generate output
  line = lines[irec]
  outarr.append('* %s' % line)
  cline = rec.cline
  if cline == None:
   outarr.append('?')
  else:                 
   for m in re.finditer(r'<ls.*?</ls>',cline):
    outarr.append('  %s' % m.group(0))
  outarr.append('')
 write_lines(fileout,outarr)
 #
 n = len(crecs)
 print('%s cases with status %s written to %s' %(n,option,fileout))
 if False:
  for temp in ['OK','TODO',None]:
   a = [rec for rec in crecs if rec.status == temp]
   print("%s crecs with status %s" %(len(a),temp))
  
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

class ChangeLine:
 def __init__(self,ls,t,ls0,cline):
  self.ls = ls
  self.t = t
  self.ls0 = ls0
  self.cline = cline
  self.status = None
  self.count = None 

def update_crec_count(crecs):
 # modify crec.count
 d = {}
 for crec in crecs:
  key = crec.ls
  if key not in d:
   d[key] = []
  d[key].append(crec)
 for crec in crecs:
  key = crec.ls
  crec.count = len(d[key])
  if False: # dbg
   if key == '<ls n="KATHĀS.">101.</ls>':
    print(crec.count,crec.ls)

def update_crec_status(recs):
 # recs array of ChangeLine objects
 #print('update_cline_status: %s recs enter' % len(recs))
 for rec in recs:
  cline = rec.cline
  if rec.count != 1:
   rec.status = 'TODO'
   # otherwise, we have 'duplicates' which can cause
   # error in processing by make_change_a.py
   continue
  if cline == None:
   rec.status = 'TODO'
  elif '<ls?' in cline:
   rec.status = 'TODO'
  elif 'None' in cline:  # correct a flaw in the logic
   rec.status = 'TODO'   
  else:
   rec.status = 'OK'

def change_line(line,dbg = False):
 ls,t,ls0 = line.split('\t')
 cline = None
 change = ChangeLine(ls,t,ls0,cline) # will modify last parm (cline)
 if t == '-1':
  t = None
 dbg = False
 if dbg:
  print('ls=',ls)
  print('t=',t)
  print('ls0=',ls0)
  
 m = re.search(r'(<ls>KATHĀS. )(.+)</ls>',ls)
 if m == None:
  m = re.search(r'(<ls n="KATHĀS.">)(.+)</ls>',ls)
 if m == None:
  # print('test2 wrong form\n',ls)
  return change
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
 
 cprev = None
 k1 = '<ls n="KATHĀS.">'
 kprob = '<ls? n="KATHĀS.">'
 lsarr = []
 probflag = False
 for i,partseq in enumerate(parsed):
  if dbg:
   print('partseq=',partseq)
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
  elif (s in ('p','pf')) and (t != '-1') and (i == 0):
   lshead = '<ls n="KATHĀS. %s,">' % t
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
 cline = ' '.join(lsarr)
 change.cline = cline
 #change = ChangeLine(ls,t,ls0,cline)
 return change

if __name__=="__main__":
 filein = sys.argv[1]  # linksort4_1
 fileout = sys.argv[2] # emacs org-mode format  OK
 fileout1 = sys.argv[3] # TODO
 lines = read_lines(filein)
 crecs = [] # array of ChangeLine objects
 for line in lines:
  crec = change_line(line)
  ###print(type(crec))
  #exit(1)
  assert type(crec) == ChangeLine
  crecs.append(crec)
 update_crec_count(crecs)
 update_crec_status(crecs)
 write_crecs('OK',fileout,lines,crecs)
 write_crecs('TODO',fileout1,lines,crecs)
 
  
