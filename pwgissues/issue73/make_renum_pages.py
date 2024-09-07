# coding=utf-8
""" make_renum_pages.py  for manu
"""
# 
import sys,re,codecs
import os

def makesh(voldata,dirin,dirout):
 dirin1 = dirin
 print('dirin1=',dirin1)
 filesin = os.listdir(dirin1)
 print(len(filesin),"files in",dirin1)
 filepatin = voldata['inpat']
 filepatout = voldata['outpat']
 # os.chdir('../')
 ans = []
 for i,filein in enumerate(filesin):
  m = re.search(filepatin,filein)
  if m == None:
   print('skipping file',filein)
   continue
  parm = m.group(1) # the page number
  num = int(parm)
  fileout = filepatout % num
  pathin = '%s/%s' % (dirin,filein)
  pathout = '%s/%s' %(dirout,fileout)
  # quote  pathin since there is a space
  pathinq = "'%s'" %pathin
  sh = "cp %s %s" %(pathinq,pathout)
  ans.append(sh)
 return ans 

def write_script(fileout,shfile):
 with codecs.open(fileout,"w","utf-8") as f:
   n = len(shfile)
   # f.write('echo "copying %s files from vol%s"\n' %(n,vol))
   #f.write('cd ../\n')
   for sh in shfile:
    f.write(sh+'\n')
 print(len(shfile),"lines written to",fileout)

voldatad = {
    # '#' is placeholder
 'manupages': {'inpat': 'manu ([0-9]+).pdf',
          'outpat': '%03d.pdf'},
       
 #'vol2': 'Katha_sarit_sagara_1862_better #.pdf',  # '#' is placeholder
 
}
if __name__ == "__main__":
 dirin = sys.argv[1]
 assert dirin in ['manupages']
 dirout = sys.argv[2]
 fileout = sys.argv[3]
 voldata = voldatad[dirin]
 shfile = makesh(voldata,dirin,dirout)
 write_script(fileout,shfile)
  

