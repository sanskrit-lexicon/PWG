""" Program to concatenate the three pwgbibX_roman.txt files
  where X = 1,23,4
  There are some different conventions used in the files.
  The program tries to iron these out.

"""

import sys,re,codecs
class VolumeIn(object):
 def __init__(self,incode):
  self.incode=incode
  self.filein = "pwgbib%s_roman.txt"%incode
  with codecs.open(self.filein,"r","utf-8") as f:
   self.lines = [x.rstrip('\r\n') for x in f]


def parse_vol(volcode,venumflag):
 """ nbeflag = True: Use entry number within volume as line number for <HI>
     nbeflag = False: Use line number within volcode as line number for
 """
 outarr = []
 vol = VolumeIn(volcode)
 volcode = vol.incode[0] 
 venum = 0 # sequence number of <HI> (entry) line within volume
 if volcode == '2':
  vol3page = '[Page003-a+ 18]'
 else:
  vol3page = None
 for iline,line in enumerate(vol.lines):
  line = line.strip()
  if line == '': # skip blank lines, if any
   continue
  page=None
  if (volcode == '4') and (iline == 0):
   # pwgbib4 doesn't have page on first line.
   # construct it
   page = '[Page1219-1a+ 21]'
   line = line + ' ' + page
  mpage = re.search(r'^(.*?) +(\[Page.*?\]) *$',line)
  if mpage:
   line = mpage.group(1)
   page = mpage.group(2)
   if iline == 0:
    if venumflag:
     linenum=0
     lineid = '%s.%03d' % (volcode,linenum)  
     outarr.append("%s %s" %(lineid,page))
     volnote = "[Volume %s: Abbreviations from Sanskrit Literature]" %volcode
     outarr.append("%s %s" %(lineid,volnote))
    else:
     outarr.append(page)
     volnote = "[Volume %s: Abbreviations from Sanskrit Literature]" %volcode
     outarr.append(volnote)
    page=None
  if volcode == '1':
   if not line.startswith('<>'):
    print "parse_1 ERROR 1",line.encode('utf-8')
    exit(1)
   line = line[2:] # skip '<>'
  # special logic for case when 
  # (a) this line has a page element and
  # (b) the next line is a continuation line
  if page:
   if volcode == '1':
    starts = ('<><H>','<><HI>')
   else:
    starts = ('<H>','<HI>')
  if page and not vol.lines[iline+1].startswith(starts) and (page != vol3page):
   line = line + ' ' + page
   page = None
  # remove 'wide-spacing' coding {|xxx|} -> xxx
  line = line.replace('{|','') #
  line = line.replace('|}','') #
  linenum = iline+1
  lineid = '%s.%03d' % (volcode,linenum)  
  if line.startswith('<H>'):
   if venumflag:
    linenum=0
    lineid = '%s.%03d' % (volcode,linenum)  
   out = '%s %s' %(lineid,line)
   outarr.append(out)
  elif line.startswith('<HI>'):
   if venumflag:
    venum = venum + 1
    linenum = venum
    lineid = '%s.%03d' % (volcode,linenum)  
   m = re.search(r'<HI>(.*?)=(.*)$',line)
   if m:
    line = '<HI code="%s">%s=%s' %(m.group(1).strip(),m.group(1),m.group(2))
   else:
    line = line.replace('<HI>','<HI code="None">')
   out = '%s %s' %(lineid,line)
   outarr.append(out)
  else: 
   # a 'continuation' line.  append to previous outarr
   if venumflag:
    newout = "<lb>%s" % line
   else:
    newout = "<lb n='%s'/>%s" %(lineid,line)
   idx = len(outarr)-1
   oldout = outarr[idx]
   out = oldout + newout
   outarr[idx]=out
  if page: # for all but the first page, which is handled above
   if (volcode == '2') and (page == vol3page):
    # change volume to volume 3
    volcode = vol.incode[1]
   if venumflag:
    linenum=0
    lineid = '%s.%03d' % (volcode,linenum)  
    outarr.append("%s %s" %(lineid,page))
   else:
    outarr.append(page)
   if (volcode == '3') and (page == vol3page):
    if venumflag:
     linenum = 0
    lineid = '%s.%03d' % (volcode,linenum)  
    volnote = "[Volume %s: Abbreviations from Sanskrit Literature]" %volcode
    outarr.append(volnote)
    venum = 0
 return outarr

if __name__ == "__main__":
 fileout = sys.argv[1]
 incodes=['1','23','4']
 vol_all = []
 for incode in incodes:
  vol_all = vol_all + parse_vol(incode,venumflag=True)

 with codecs.open(fileout,"w","utf-8") as f:
  for line in vol_all:
   f.write(line+'\n')
 
  
