# coding=utf-8
""" make_readme_all1.py
"""
from __future__ import print_function
import sys, re, codecs
import glob, os, time

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"lines written to",fileout)


def test():
 dirin = "../"  # sanskrit-lexicon-scans
 # Retrieve a list of all md files in the "files" directory
 #file_list = glob.glob("files/*.txt")
 globparm = '../*/README.md'
 file_list = glob.glob(globparm)
 if True:
  for ifile,file in enumerate(file_list):
   print('%2d %s' %(ifile+1,file))
         
 #print("List of README.md files:", file_list)
 exit(1)

def get_title_line(nrepos):
 parent_path = os.getcwd()
 parts = parent_path.split(os.sep)
 parent_dir = parts[-1] # sanskrit-lexicon-scans
 import time
 current_datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
 title = '%s %s link_target README.md files as of %s' %(nrepos,parent_dir,current_datetime)
 print('title = ',title)
 #exit(1)
 return title
 
def get_readme_md_files():
 globparm = '*/README.md'
 # boesp1\\README.md  sample of file_list
 file_list = glob.glob(globparm)
 if False:
  print(file_list)
  exit(1)
 return file_list
 file_list1 = []
 for file in file_list:
  file1 = file
  file_list1.append(file1)
 return file_list1

if __name__ == "__main__":
 dirin = sys.argv[1]
 fileout = sys.argv[2]  
 current_path = os.getcwd()
 
 #os.chdir('../')
 os.chdir(dirin)
 readme_md_files = get_readme_md_files()
 nrepos = len(readme_md_files)
 print(nrepos,'sanskrit-lexicon-scans directories')
 # output_title = get_title_line(nrepos)
 outrecs = []
 # We are only interested in link-target repos.
 # exclude the others
 repo_exclude = ['abch','linktarget_howto','lrv',
                 'pantankose_unused','pwg',
                 'katyasr_0']
 nrepos_used = 0
 for path in readme_md_files:
  lines = read_lines(path)
  modification_time = os.path.getmtime(path)
  #formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modification_time))
  formatted_time = time.strftime('%Y-%m-%d', time.localtime(modification_time))
  pathparts = path.split(os.sep)
  reponame = pathparts[0]
  # exclude dictionary scan files, by name
  if reponame in repo_exclude:
   print('excluding repo:',reponame)
   continue
  nrepos_used = nrepos_used + 1
  if False:
   # pathparts = ['abch', 'README.md']
   print('path=',path)
   print('parts=',pathparts)
   exit(1)
  #title = '* %s %s' %(formatted_time,reponame)
  # title = '* ' + reponame  # for Emacs org-mode
  outarr = []
  outarr.append('* ==========================================================')
  title = '* %s' % reponame
  outarr.append(title)
  outarr.append('* ==========================================================')
  for line in lines:
   #if re.search(r'^( *)[*]',line):
   # line = '_' + line  # to avoid confusion with markdown lists
   outarr.append(line)
  outrecs.append(outarr)
 # sort by date
 #outrecs1 = sorted(outrecs, key = lambda x: x[0])
 outrecs1 = outrecs # sorted by repo name?
 outlines = []
 print(nrepos_used,'link target directories')
 output_title = get_title_line(nrepos_used)
 outlines.append(output_title)
 for outarr in outrecs1:
  for out in outarr:
   outlines.append(out)
 os.chdir(current_path)
 if False:
  fileout = 'make_readme_all.txt'
  print('Changing output file to',fileout)
 write_lines(fileout,outlines)
 


 
