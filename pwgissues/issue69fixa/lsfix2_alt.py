# coding=utf-8
""" lsfix2_alt.py
  
"""
from __future__ import print_function
import sys, re,codecs
import digentry
from lsfix2_parm import targetobj2

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"lines written to",fileout)

class Instance:
 def __init__(self,matchstr,entry,iline):
  self.entry = entry
  self.iline = iline
  self.status = None
  self.matchstr = matchstr
  self.fixed = ''

class REGEX:
 def __init__(self,regex_raw,ngroup,case):
  self.regex_raw = regex_raw
  self.ngroup = ngroup
  assert case in ('A','B','C')
  self.case = case
  self.regex = re.compile(self.regex_raw)
  
def get_regexes_allx1(lscode):
 lscode1 = lscode.replace('.','[.]')
 a = [
  REGEX(f'<ls>{lscode1} (.*?)</ls>',1) ,
  REGEX(f'<ls n="{lscode1}">(.*?)</ls>',1) ,
  #REGEX(f'<ls n="{lscode1} (.?)">(.*?)</ls>',2) ,
  ]
 return a

def get_regexes_allx3(lscode):
 lscode1 = lscode.replace('.','[.]')
 a = [
  REGEX(f'<ls>{lscode1} (.*?)</ls>',1), 
  REGEX(f'<ls n="{lscode1}(.*?)">(.*?)</ls>',2) ,
  ]
 return a
def get_regexes_all(lscode):
 lscode1 = lscode.replace('.','[.]')
 a = [
  REGEX(f'<ls>{lscode1} (.*?)</ls>',1,'A'), 
  REGEX(f'<ls n="{lscode1}">(.*?)</ls>',2,'B') ,
  REGEX(f'<ls n="{lscode1} (.*?)">(.*?)</ls>',2,'C')
  ]
 return a

def get_status_C(matchstr):
 if re.search(r'^[0-9]+,[abc],[0-9]+\.?$',matchstr):
  return True
 return None

def get_instances_all(entries, lscode,fixopt):
 REGEXES = get_regexes_all(lscode)
 #regs = [re.compile(regex) for regex in regexes_all]
 instances = []
 for entry in entries:
  for iline,line in enumerate(entry.datalines):
   for REGEX in REGEXES:
    regex = REGEX.regex
    for m in re.finditer(regex,line):
     matchstr = m.group(0)
     instance = Instance(matchstr,entry,iline)
     if instance.status == None:
      if REGEX.case in ('A','B'):
       fix_instance(instance,lscode,fixopt)
      elif REGEX.case == 'C':
       x1 = m.group(1)
       x2 = m.group(2)
       matchstr1 = x1 + x2
       first,rest = fix_get_start(matchstr1,fixopt)
       if rest == '':
        instance.status = True
       #status = get_status_C(matchstr1,fixopt)
       #instance.status = status
     instances.append(instance)
 return instances

def fix_get_start(rest,fixopt): 
 N = '[0-9]+'
 A = '[abc]'
 F = 'fg+'
 V = 'v\. l\.'
 Q = '\.?'
 P = '\.'
 if fixopt == '01':
  g1 = f'{N},{A},{N}{P}'
  g0 = f'(?:{g1})'
  h0 = f'(?:)'
  regexes = [f'^({g0}{h0}*)(.*)$']
 elif fixopt == '02':
  g1 = f'{N},{A},{N}{P}'
  g2 = f'{N},{A}{P}'
  g0 = f'(?:{g1}|{g2})'
  h0 = f'(?:)'
  regexes = [f'^({g0}{h0}*)(.*)$']
 elif fixopt == '03':
  g1 = f'{N},{A},{N}{P}'
  g2 = f'{N},{A}{P}'
  g3 = f'No{P} {N}{P}'
  g0 = f'(?:{g1}|{g2}|{g3})'
  h0 = f'(?:)'
  regexes = [f'^({g0}{h0}*)(.*)$']
 elif fixopt == '04':
  g1 = f'{N},{A},{N}{P}'
  g2 = f'{N},{A}{P}'
  g3 = f'No{P} {N}{P}'
  g0 = f'(?:{g1}|{g2}|{g3})'
  h2 = f' {F}{P}'
  h0 = f'(?:{h2})'
  regexes = [f'^({g0}{h0}*)(.*)$']
 elif fixopt == '05':
  g1 = f'{N},{A},{N}{P}'
  g2 = f'{N},{A}{P}'
  g3 = f'No{P} {N}{P}'
  
  g0 = f'(?:{g1}|{g2}|{g3})'
  h1 = f' {N}{P}'  
  h2 = f' {F}{P}'
  h0 = f'(?:{h1}|{h2})'
  regexes = [f'^({g0}{h0}*)(.*)$']
 elif fixopt == '06':
  g1 = f'{N},{A},{N}(?:{P}|$)'
  g2 = f'{N},{A}{P}'
  g3 = f'No{P} {N}{P}'
  
  g0 = f'(?:{g1}|{g2}|{g3})'
  h1 = f' {N}{P}'  
  h2 = f' {F}{P}'
  h0 = f'(?:{h1}|{h2})'
  regexes = [f'^({g0}{h0}*)(.*)$']

 elif fixopt == '07':
  g1 = f'{N},{A},{N}(?:{P}|$)'
  g2 = f'{N},{A}(?:{P}|$)'
  g3 = f'No{P} {N}{P}'
  g0 = f'(?:{g1}|{g2}|{g3})'
  h1 = f' {N}{P}'  
  h2 = f' {F}{P}'
  h3 = f' {A},{N}{P}'
  h0 = f'(?:{h1}|{h2}|{h3})'
  regexes = [f'^({g0}{h0}*)(.*)$']

 elif fixopt == '08':
  g1 = f'{N},{A},{N}(?:{P}|$)'
  g2 = f'{N},{A}(?:{P}|$)'
  g3 = f'No{P} {N}{P}'
  g4 = f'{N},{A}, N{P} {N}{P}'
  g0 = f'(?:{g1}|{g2}|{g3}|{g4})'
  h1 = f' {N}{P}'  
  h2 = f' {F}{P}'
  h3 = f' {A},{N}{P}'
  h0 = f'(?:{h1}|{h2}|{h3})'
  regexes = [f'^({g0}{h0}*)(.*)$']
  
 elif fixopt == '09':
  g1 = f'{N},{A},{N}(?:{P}|$)'
  g2 = f'{N},{A}(?:{P}|$)'
  g3 = f'No{P} {N}{P}'
  g4 = f'{N},{A}, (?:N{P} {N}{P}|{g3})'
  g0 = f'(?:{g1}|{g2}|{g3}|{g4})'
  h1 = f' {N}{P}'  
  h2 = f' {F}{P}'
  h3 = f' {A},{N}{P}'
  h0 = f'(?:{h1}|{h2}|{h3})'
  regexes = [f'^({g0}{h0}*)(.*)$']

 elif fixopt == '10':
  g10 = f'{N},{A},{N}'
  g1 = f'{g10}(?:{P}|$)'
  g20 = f'{N},{A}'
  g2 = f'{g20}(?:{P}|$)'
  g30 = f'No{P} {N}'
  g3 = f'{g30}{P}'
  i1 = f'(?:N{P} {N}{P}|N{P}|{g3})'
  g4 = f'{g20}, {i1}'
  i2 = f'(?:Z{P} {N}{P}|Śl. {N}{P})'
  g5 = f'{g30}, {i2}'
  g0 = f'(?:{g1}|{g2}|{g3}|{g4}|{g5})'
  h1 = f' {N}{P}'  
  h2 = f' {F}{P}'
  h3 = f' {A},{N}{P}'
  h0 = f'(?:{h1}|{h2}|{h3})'
  regexes = [f'^({g0}{h0}*)(.*)$']
 elif fixopt == '11':
  g10 = f'{N},{A},{N}'
  g1 = f'{g10}(?:{P}|$)'
  g20 = f'{N},{A}'
  g2 = f'{g20}(?:{P}|$)'
  g30 = f'No{P} {N}'
  non = g30
  g3 = f'{non}(?:{P}|$)'
  zn = f'Z{P} {N}(?:{P}|$)'
  shl = f'Śl. {N}(?:{P}|$)'
  noz = f'{non}, {zn}'
  noshl = f'{non}, {shl}'
  i1 = f'(?:N{P} {N}{P}|N{P}|{g3}|{noz}|{noshl}|{shl})'
  g4 = f'{g20}, {i1}'
  i2 = f'(?:{zn}|{shl})'
  g5 = f'{non}, {i2}'
  g0 = f'(?:{g1}|{g2}|{g3}|{g4}|{g5})'
  h1 = f' {N}(?:{P}|$)'  
  h2 = f' {F}{P}'
  h3 = f' {A},{N}{P}'
  h0 = f'(?:{h1}|{h2}|{h3})'
  regexes = [f'^({g0}{h0}*)(.*)$']

 elif fixopt == '12':
  g10 = f'{N},{A},{N}'
  g1 = f'{g10}(?:{P}|$)'
  g20 = f'{N},{A}'
  g2 = f'{g20}(?:{P}|$)'
  g30 = f'No{P} {N}'
  non = g30
  g3 = f'{non}(?:{P}|$)'
  zn = f'Z{P} {N}(?:{P}|$)'
  shl = f'Śl. {N}(?:{P}|$)'
  noz = f'{non}, {zn}'
  noshl = f'{non}, {shl}'
  i1 = f'(?:N{P} {N}{P}|N{P}|{g3}|{noz}|{noshl}|{shl})'
  g4 = f'{g20}, {i1}'
  i2 = f'(?:{zn}|{shl})'
  g5 = f'{non}, {i2}'
  i3 = f'\({non}\){P}'
  g6 = f'{g20} {i3}'
  i7 = f'(?:ult{P}|pen{P}|Anm{P} {N}{P}|Kap\.(?: {N}{P})+)'
  g7 = f'{N},{A},{i7}'
  i8 = f'(?:N{P} {N}{P}|{V})'
  g8 = f'{g1} {i8}'
  g0 = f'(?:{g8}|{g1}|{g2}|{g3}|{g4}|{g5}|{g6}|{g7})'
  h1 = f' {N}(?:{P}|$)'  
  #h2 = f' {F}{P}'
  h2 = f'(?: {F}{P}| {V})'
  h3 = f' {A},{N}(?:{P}|$)'
  h4 = f' {A}, {non}(?:{P}|$)'
  h0 = f'(?:{h1}|{h2}|{h3}|{h4})'
  regexes = [f'^({g0}{h0}*)(.*)$']

 elif fixopt == '13':
  g10 = f'{N},{A},{N}'
  g1 = f'{g10}(?:{P}|$)'
  g20 = f'{N},{A}'
  g2 = f'{g20}(?:{P}|$)'
  g30 = f'No{P} {N}'
  non = g30
  g3 = f'{non}(?:{P}|$)'
  zn = f'Z{P} {N}(?:{P}|$)'
  shl = f'Śl. {N}(?:{P}|$)'
  noz = f'{non}, {zn}'
  noshl = f'{non}, {shl}'
  i1 = f'(?:N{P} {N}{P}|N{P}|{g3}|{noz}|{noshl}|{shl})'
  g4 = f'{g20}, {i1}'
  i2 = f'(?:{zn}|{shl})'
  g5 = f'{non}, {i2}'
  i3 = f'\({non}\){P}'
  g6 = f'{g20} {i3}'
  i7 = f'(?:ult{P}|pen{P}|Anm{P} {N}{P}|Kap\.(?: {N}{P})+)'
  g7 = f'{N},{A},{i7}'
  i8 = f'(?:{non}{P})'
  g8 = f'{N}, {i8}'
  g0 = f'(?:{g8}|{g1}|{g2}|{g3}|{g4}|{g5}|{g6}|{g7}|{g8})'
  h1 = f' {N}(?:{P}|$)'  
  #h2 = f' {F}{P}'
  h2 = f'(?: {F}{P}| {V})'
  h3 = f' {A},{N}(?:{P}|$)'
  h4 = f' {A}, {non}(?:{P}|$)'
  h0 = f'(?:{h1}|{h2}|{h3}|{h4})'
  regexes = [f'^({g0}{h0}*)(.*)$']

 elif fixopt == '14':
  g10 = f'{N},{A},{N}'
  g1 = f'{g10}(?:{P}|$)'
  g20 = f'{N},{A}'
  g2 = f'{g20}(?:{P}|$)'
  g30 = f'No{P} {N}'
  non = g30
  g3 = f'{non}(?:{P}|$)'
  zn = f'Z{P} {N}(?:{P}|$)'
  shl = f'Śl. {N}(?:{P}|$)'
  noz = f'{non}, {zn}'
  noshl = f'{non}, {shl}'
  i1 = f'(?:N{P} {N}{P}|N{P}|{g3}|{noz}|{noshl}|{shl})'
  g4 = f'{g20}, {i1}'
  i2 = f'(?:{zn}|{shl})'
  g5 = f'{non}, {i2}'
  i3 = f'\({non}\){P}'
  g6 = f'{g20} {i3}'
  i7 = f'(?:ult{P}|pen{P}|Anm{P} {N}{P}|Kap\.(?: {N}{P})+)'
  g7 = f'{N},{A},{i7}'
  #i8 = f'(?:{non}{P}|N{P} {N}{P}|N{P})'
  i8 = f'(?:{non}{P}|N{P} {N}{P}|N{P}|{N},a\. b\.)'
  g8 = f'(?:{g10}|{N}), {i8}'
  #g9 = f'{N}(?:{P}|)$' 
  g9 = f'{N}{P}$'
  j1 = f'187,b, No. 428,8.'
  j2 = f'{N},a\. b\.'
  j3 = f'{N} \([^)]*?\)\.?'
  j4 = f'No\. {N} \([^)]*?\)\.'
  j5 = f'{N},a, {j4}'
  j6 = f'(?:No. 447 — 450.|202,a, III,26|202,a III,2)'
  j7 = f'(?:25,a \(54\)\.|No. 489, II,12.|208,a \(No. 489, II\).)'
  j8 = f'(?:116,b,\(XI\)\.|{N}-{N}\.?|207,a,36. 38. N. 4.)'
  j9 = f'(?:242,a, No. 593-595.|213, No. 506|241. fg\.)'
  j10=f'(?:361,a, No. 2-4.|235,a,19. b,16 und N. 4.|31-33.)'
  j11 = f'(?:11,b, No. 50-55.|174,b, No. 395. fg., Z. 9.)'
  j12 = f'(?:36,a \(No. 79. fgg.\)|97,a,1, No. 151|117. fg.)'
  j13 = f'(?:25,a,34. b, N. 5.)'
  g10 = f'(?:{j1}|{j2}|{j3}|{j4}|{j5}|{j6}|{j7}|{j8}|{j9}|{j10}|{j11}|{j12}|{j13})'
  g0 = f'(?:{g10}|{g8}|{g1}|{g2}|{g3}|{g4}|{g5}|{g6}|{g7}|{g9})'
  h1 = f' {N}(?:{P}|$)'  
  #h2 = f' {F}{P}'
  h2 = f'(?: {F}{P}| {V})'
  h3 = f' {A},{N}(?:{P}|$)'
  h4 = f' {A}, {non}(?:{P}|$)'
  h0 = f'(?:{h1}|{h2}|{h3}|{h4})'
  regexes = [f'^({g0}{h0}*)(.*)$']

 else:
  print('fix_get_start: unknown fixopt = ',fixopt)
  exit (1)
 #regexes = [f'^({g0}{h0}*)(.*)$'] 
 rest1 = rest.lstrip()  # remove leading space chars
 for regex in regexes:
  m = re.match(regex,rest1)
  if m != None:
   break
 if m == None:
  # fails
  first = ''
  rest = None
 else:
  first = m.group(1)
  rest = m.group(2)
 return first,rest

def analyze(body,fixopt):
 results = []
 rest = body
 while True:
  (first,rest1) = fix_get_start(rest,fixopt) 
  if rest1 == None:
   break
  results.append(first)
  rest = rest1
  if rest == '':
   break # normal finish
 return results,rest

def fix_instance(instance,lscode,fixopt):
 if instance.status != None:
  return
 matchstr = instance.matchstr
 lscode1 = lscode.replace('.','[.]')
 L = lscode1
 start_a = f'<ls>{L}'
 start_b = f'<ls n="{L}">'
 regall = f'^({start_a}|{start_b})(.*)</ls>$'
 m = re.search(regall,matchstr)
 if m == None:
  return
 start = m.group(1)
 body = m.group(2)
 lsend = '</ls>'
 start1 = f'<ls n="{lscode}">'
 results,rest = analyze(body,fixopt)
 if rest != '':
  # fail status remains None
  return
 if len(results) == 1:
  instance.status = True
  return
 start_a1 = start_a.replace('[.]','.')
 start_b1 = start_b.replace('[.]','.')
 expansions = []
 for iresult,result in enumerate(results):
  if iresult == 0:
   if start == start_a1:
    lstart = start + ' '
   elif start == start_b1:
    lstart = start    
  else:
   lstart = start1
  expansion = f'{lstart}{result}{lsend}'
  expansions.append(expansion)
 ans = ' '.join(expansions)
 instance.fixed= ans
 instance.status = 'fixed'
 return

def write_instances(fileout,instances):
 outarr = []
 statd = {}
 
 for instance in instances:
  fixed = instance.fixed
  iline = instance.iline
  entry = instance.entry
  lnum = entry.linenum1 + iline + 1
  k1 = entry.metad['k1']
  status = instance.status
  nparm = '_' #instance.nparm
  out = '%s\t%s\t%s\t%s\t%s\t%s' % (status,nparm,lnum,k1,instance.matchstr,fixed)
  outarr.append(out)
  stat1 = (status,nparm)
  if stat1 not in statd:
   statd[stat1] = 0
  statd[stat1] = statd[stat1] + 1
 write_lines(fileout,outarr)
 return statd
 
def statd_to_statout(statd):
 statarr = []
 tot = 0
 for stat1 in statd:
  count = statd[stat1]
  tot = tot + count
  count1 = str(count)
  key = stat1[0]  # status
  key1 = str(key)
  statval = (key1,count1)
  statval1 = f'{statval}'
  statarr.append(statval1)
 statarr1 = sorted(statarr)
 a = ('all',tot)
 statarr1.append(f'{a}')
 statout = ','.join(statarr1)
 statout1 = re.sub(r"[' ']",'',statout)
 return statout1 

from lsfix2_alt_test import testnoncapture

if __name__=="__main__":
 fixopt = sys.argv[1]
 if len(sys.argv) == 2:
  testnoncapture(analyze,fixopt)
 code = sys.argv[2]
 filein = sys.argv[3]  # xxx.txt kosha
 fileout = sys.argv[4] # output file
 if code not in targetobj2:
  print('Unknown code:',code)
  exit(1)
 targetparms = targetobj2[code]
 lscode = targetparms['lscode']
  
 entries = digentry.init(filein)
 instances_all = get_instances_all(entries,lscode,fixopt)

 statd = write_instances(fileout,instances_all)
 statout = statd_to_statout(statd)
 print(statout,fixopt,fileout)
 
