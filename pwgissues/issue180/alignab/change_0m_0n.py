""" change_0m_0n.py
 
"""
import sys,re
import codecs

def read_lines(filein):
 lines = []
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  for line in f:
   lines.append(line.rstrip('\r\n'))
 print(f'{len(lines)} lines read from {filein}')
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,'w','utf-8') as f:
  for out in outarr:
   f.write("%s\n" % out)
 print(f'{len(outarr)} lines written to {fileout}')


def adjust_lines1(lines):
 replacements = [
  # 06-11-2026.  correcting xml errors
  
  ('<ls n="MBH. 3,">11046 (p. 571). <ab>fgg.</ls>',
   '<ls n="MBH. 3,">11046 (p. 571). fgg.</ls>'),
  ('<ls>ROTH, Einl. zu <ls>NIR. VIII.</ls>',
   '<ls>ROTH, Einl. zu NIR. VIII.</ls>'),
  ('<ls>ROTH, Einl. zu <ls>NIR. LXIII.</ls>',
   '<ls>ROTH, Einl. zu NIR. LXIII.</ls>'),
  ('<<ls>BENFEY</ls>', '<ls>BENFEY</ls>'),
  ('<ls>HARIV. 11042<ls>HARIV. 11042 (S. 791)</ls>.',
   '<ls>HARIV. 11042 (S. 791)</ls>.'),
  ('<ls>LOIS.</ls> in der Vorrede zu AK. S. IX.</ls>',
   '<ls>LOIS. in der Vorrede zu AK. S. IX.</ls>'),
  ('<ls n="HARIV.">11064<ls>HARIV. 11042 (S. 791)</ls>.',
   '<ls n="HARIV.">11064 (S. 791)</ls>'),
  ('<ls>HARIV. 11056<ls>HARIV. 11042 (S. 791)</ls>.',
   '<ls>HARIV. 11056 (S. 791)</ls>'),
  ('jenes {%S. {%spontaneum%}', 'jenes {%S. spontaneum%}'),
  ('<ls n="HARIV.">11048<ls>HARIV. 11042 (S. 791)</ls>.',
   '<ls n="HARIV.">11048 (S. 791)</ls>.'),
  ('Kampfart%} 🞄<ls n="HARIV.">11048<ls>HARIV. 11042 (S. 791)</ls>',
   'Kampfart%} <ls n="HARIV.">11048 (S. 791)</ls>'),
  ('<ls n="HARIV.">6852.</ls> <ls n="HARIV.">11056<ls>HARIV. 11042 (S. 791)</ls>.',
   '<ls n="HARIV.">6852.</ls> <ls n="HARIV.">11056 (S. 791)</ls>.'),
  ('{#tadAScaryaM samaBavadyat#} 🞄<ab>u. s. w.</ab> <ls>HARIV. 11044<ls>HARIV. 11042 (S. 791)</ls>. ',
   '{#tadAScaryaM samaBavadyat#} 🞄<ab>u. s. w.</ab> <ls>HARIV. 11044 (S. 791)</ls>. '),
  ('<ls n="MBH.">12,4278.</ls> 🞄<ls>HARIV. 11041<ls>HARIV. 11042 (S. 791)</ls>.',
   '<ls n="MBH.">12,4278.</ls> 🞄<ls>HARIV. 11041 (S. 791)</ls>.'),
  ('prakArAndvAtriMSadvicaran#} 🞄<ls>HARIV. 11048<ls>HARIV. 11042 (S. 791)</ls>.',
   'prakArAndvAtriMSadvicaran#} <ls>HARIV. 11048 (S. 791)</ls>.'),
  ('falsch übersetzt) 🞄<ls>HARIV. 11047<ls>HARIV. 11042 (S. 791)</ls>.falsch übersetzt {#carantastsarumArgAMSca DanurmArgAMSca SikzayA#}',
   'falsch übersetzt) <ls>HARIV. 11047 (S. 791)</ls>. {#carantastsarumArgAMSca DanurmArgAMSca SikzayA#'),

  ('{%ein Sprung gegen Jmd hin, auf Jmd%} 🞄<ls>MBH. 6,2283.</ls> 🞄<ls>HARIV. 11048<ls>HARIV. 11042 (S. 791)</ls>.',
   '{%ein Sprung gegen Jmd hin, auf Jmd%} 🞄<ls>MBH. 6,2283.</ls> 🞄<ls>HARIV. 11048 (S. 791).'),
  ('{%eine <ab>best.</ab> Kampfart%} 🞄<ls>HARIV. 11048<ls>HARIV. 11042 (S. 791)</ls>.',
   '{%eine <ab>best.</ab> Kampfart%} 🞄<ls>HARIV. 11048 (S. 791)</ls>.'),
  ('<ls n="R. 3,34,">11.</ls> falsch übersetzt) 🞄<ls>HARIV. 11047<ls>HARIV. 11042 (S. 791)</ls>.',
   '<ls n="R. 3,34,">11.</ls> falsch übersetzt) 🞄<ls>HARIV. 11047 (S. 791)</ls>.'),
  ('<is>Bāṇa</is> 🞄<ls>HARIV. 11017<ls>HARIV. 11042 (S. 791)</ls>.',
   '<is>Bāṇa</is> 🞄<ls>HARIV. 11017 (S. 791)</ls>.'),
  ('<ls>HARIV. 11053<ls>HARIV. 11042 (S. 791)</ls>.',
   '<ls>HARIV. 11053 (S. 791)</ls>.'),
  ('<ls>HARIV. 11036<ls>HARIV. 11042 (S. 791)</ls>.',
   '<ls>HARIV. 11036<ls> (S. 791)</ls>.'),
  ('<ls>HARIV. 11048<ls>HARIV. 11042 (S. 791)</ls>. 13494. 15977.',
   '<ls>HARIV. 11048 (S. 791)</ls> <ls n="HARIV.">13494.</ls> <ls n="HARIV.">15977.</ls>'),
  ('<ls>HARIV. 11048 (S. 791). <ls n="HARIV.">13494.</ls>',
   '<ls>HARIV. 11048 (S. 791).</ls> <ls n="HARIV.">13494.</ls>'),
  ('<ls n="HARIV.">11062<ls>HARIV. 11042 (S. 791)</ls>.',
   '<ls n="HARIV.">11062 (S. 791)</ls>.'),
  ('wird mit den ls>Bomb.',
   'wird mit den <ls>Bomb.'),
  ('<<ab>Sp.</ab>', '<ab>Sp.</ab>'),
  (' ls>Bomb. Ausgg.</ls>',
   ' <ls>Bomb. Ausgg.</ls>'), #25
  ('<ab n=???">s.</ab>',
   '<ab n="???">s.</ab>'),
  ('<ab n=Seiten">S.</ab>',
   '<ab n="Seiten">S.</ab>'), #2
  ('<ab n=und">u.</ab>', '<ab n="und">u.</ab>'),
  ('<ab n=Seite">S.</ab>', '<ab n="Seite">S.</ab>'), #3
  ('<ls>ROTH, Einl. zu <ls>NIR. XV. fgg.</ls>',
   '<ls>ROTH, Einl. zu NIR. XV. fgg.</ls>'),
  ('<ls>HARIV. 11036<ls> (S. 791)</ls>',
   '<ls>HARIV. 11036 (S. 791)</ls>'),
  ('<<', '<'),
  ('<ls>ROTH, Einl. zu <ls>NIR. LVII. fgg.</ls>',
   '<ls>ROTH, Einl. zu NIR. LVII. fgg.</ls>'),
  ('2te <Aufl', '2te Aufl'),
  #('', ''),
  #('', ''),
 ]
 newlines = []
 nchg = 0
 for iline,line in enumerate(lines):
  newline = line
  for old,new in replacements:
   newline = newline.replace(old,new)
  if newline != line:
   nchg = nchg + 1
  newlines.append(newline)
 print(f'{nchg} line(s) changed')
 return newlines

if __name__=="__main__":
 filein = sys.argv[1]  # base
 fileout = sys.argv[2] # adjusted base
 
 lines = read_lines(filein)

 lines1 = adjust_lines1(lines)
 #lines2 = adjust_lines2(lines1)
 write_lines(fileout,lines1)
