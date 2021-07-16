#-*- coding:utf-8 -*-
""" dict_2_changes.py
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 
class Change(object):
 def __init__(self,metaline,iline,old,new):
  self.metaline = metaline
  self.iline = iline
  self.old = old
  self.new = new

def init_changes(lines1,lines2):
 changes = [] # array of Change objects
 metaline = None
 imetaline1 = None
 page = None
 for iline,line1 in enumerate(lines1):
  line2 = lines2[iline]
  if iline == 0: # %***This File is E:\\APTE.ALL, Last update 11.09.06 
   continue  # 
  if line1.startswith('<L>'):
   metaline = line1
   imetaline1 = iline+1
  if line1 == line2:
   continue
  # generate a change
  change = Change(metaline,iline,line1,line2)
  changes.append(change)
 print(len(changes),'changes found')
 return changes

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
  ident = 'No metaline available'
 outarr.append('; ' + ident)
 # change for iline
 lnum = change.iline + 1
 line = change.old
 new = change.new
 outarr.append('%s old %s' % (lnum,line))
 outarr.append('%s new %s' % (lnum,new))
 outarr.append(';')
 return outarr

def write_changes(fileout,changes,filein1,filein2):
 with codecs.open(fileout,"w","utf-8") as f:
   for ichange,change in enumerate(changes):
    outarr = change_out(change,ichange)
    for out in outarr:
     f.write(out+'\n')
 print(len(changes),"changes written to",fileout)


if __name__=="__main__":
 filein1 = sys.argv[1] #  xxx.txt (first version)
 filein2 = sys.argv[2] #  xxx.txt (second version)
 fileout = sys.argv[3] # possible change transactions
 
 with codecs.open(filein1,"r","utf-8") as f:
  lines1 = [x.rstrip('\r\n') for x in f]
 with codecs.open(filein2,"r","utf-8") as f:
  lines2 = [x.rstrip('\r\n') for x in f]
 if len(lines1) != len(lines2):
  print('ERROR: require same number of lines in  the two input files')
  exit(1)
 print(len(lines1),'lines compared')
 changes = init_changes(lines1,lines2)
 write_changes(fileout,changes,filein1,filein2)
 
