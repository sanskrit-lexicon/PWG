#-*- coding:utf-8 -*-
"""make_change_gorr.py
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 
class Change(object):
 def __init__(self,metaline,page,iline,old,new,reason,iline1,line1,new1):
  self.metaline = metaline
  self.page = page
  self.iline = iline
  self.old = old
  self.new = new
  self.reason = reason
  self.iline1 = iline1
  self.line1 = line1
  self.new1 = new1

def change_out(change,ichange):
 outarr = []
 case = ichange + 1
 #outarr.append('; TODO Case %s: (reason = %s)' % (case,change.reason))
 try:
  ident = change.metaline
 except:
  print('ERROR:',change.iline,change.old)
  exit(1)
 if ident == None:
  ident = change.page
 outarr.append('; ' + ident)
 
 # change for iline
 lnum = change.iline + 1
 line = change.old
 new = change.new
 outarr.append('%s old %s' % (lnum,line))
 outarr.append('%s new %s' % (lnum,new))
 outarr.append(';')

 # possible change for iline1
 if change.iline1 != None:
  lnum = change.iline1 + 1
  line = change.line1
  new = change.new1
  outarr.append('%s old %s' % (lnum,line))
  outarr.append('%s new %s' % (lnum,new))
  outarr.append(';')

 # dummy next line
 return outarr

def write_changes(fileout,changes):
 with codecs.open(fileout,"w","utf-8") as f:
   for ichange,change in enumerate(changes):
    outarr = change_out(change,ichange)
    for out in outarr:
     f.write(out+'\n')
 print(len(changes),"possible changes written to",fileout)

def init_changes(lines):
 changes = []
 metaline = None
 page = None
 for iline,line in enumerate(lines):
  if iline == 0: # %***This File is E:\\APTE.ALL, Last update 11.09.06 
   continue  # 
  #line = line.rstrip('\r\n')
  if line.startswith('<L>'):
   metaline = line
   imetaline1 = iline+1
   continue
  if line == '<LEND>':
   metaline = None
   imetaline = None
   continue
  if line.startswith('[Page'):
   page = line
   continue
  line0 = line.strip()
  if line0 != '<ls>R.</ls>':
   continue
  iline1 = iline + 1
  line1 = lines[iline1]
  if not line1.startswith('<ls>GORR.'):
   continue
  newline = ''
  newline1 = re.sub(r'^<ls>','<ls>R. ',line1)
  reason = 'Gorr'
  change = Change(metaline,page,iline,line,newline,reason,
                  iline1,line1,newline1)
  changes.append(change)
 print(len(changes),'lines changed')
 return changes

def unused_write_changes(fileout,changes):
 outrecs = []
 for change in changes:
  lnum = change.iline+1
  old = change.line
  new = change.newline
  metaline = re.sub(r'<k2>.*$','',change.metaline)
  outarr = []
  outarr.append('; -------- %s' % metaline)
  outarr.append('%s old %s' %(lnum,old))
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,new))
  # 2nd line
  lnum = change.iline1+1
  old = change.line1
  new = change.newline1
  outarr.append('; -------- ')
  outarr.append('%s old %s' %(lnum,old))
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,new))
  
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')


if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # change transactions
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 changes = init_changes(lines) # 
 write_changes(fileout,changes)
 
