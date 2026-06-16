""" change_1_2.py
 
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
  ('<is>Hindi</is>',
   '<lang>Hindi</lang>'),
  ('<is>prākr</is>.',
   '<lang>prākr.</lang>'),
  ('{#kIl = krIq#} im <is>Prākṛt</is>', '{#kIl = krIq#} im <lang>Prākṛt</lang>'),
  ('(<ls>ved.).</ls>', '(<lang>ved.</lang>).'),
  ('<ls>VIKR. 25,18</ls> im <is>Prākrit</is>.',
   '<ls>VIKR. 25,18</ls> im <lang>Prākrit</lang>.'),
  ('<ls>SHAKESP.</ls> <lang>Hindust.</lang> Dict.',
   '<ls>SHAKESP. Hindust. Dict.</ls>'),
  ('so <ab>v. a.</ab> das <lang>deutsche</lang>',
   'so <ab>v. a.</ab> das deutsche'),
  ('{%trahere%} und goth. {%dragan%}',
   '{%trahere%} und <lang>goth.</lang> {%dragan%}'),
  ('im <is>Prākrit</is>. fehlerhaft für',
   'im <lang>Prākrit</lang>. fehlerhaft für'),
  ('Titel einer {%<lang>Prākrit</lang>%}- Grammatik',
   'Titel einer {%Prākrit%}- Grammatik'),
  ('Titel der {%<lang>Prākrit</lang>%}- Grammatik des <is>Vararuci</is>',
   'Titel der {%Prākrit%}- Grammatik des <is>Vararuci</is>'),
  ('Titel einer {%<lang>Prākrit</lang>%}-Grammatik von <is>Nārāyaṇa</is>',
   'Titel einer {%Prākrit%}-Grammatik von <is>Nārāyaṇa</is>'),
  ('Schrift über die {%<lang>Prākrit</lang>-Metra%}',
   'Schrift über die {%Prākrit-Metra%}'),
  ('Titel von <is>Vararuci\'s</is> {%<lang>Prākrit</lang>%}-Grammatik',
   'Titel von <is>Vararuci</is>ʼs {%Prākrit%}-Grammatik'),
  ('({#prA˚ + la˚#}) Titel einer {%<lang>Prākrit</lang>%}-Grammatik',
   '({#prA˚#} + {#la˚#}) Titel einer {%Prākrit%}-Grammatik'),
  ('{%Lehrbuch der <lang>Prākrit</lang>-Sprache%}',
   '{%Lehrbuch der Prākrit-Sprache%}'),
  ('(nicht Sohn, wie die <lang>deutsche</lang> Uebersetzung hat)',
   '(nicht Sohn, wie die deutsche Uebersetzung hat)'),
  ('{#BImarAtrI#} (im <lang>Prākrit</lang>',
   '{#BImarAtrI#} (im Prākrit'),
  ('<ab>v. l.</ab> im <is>Prākrit</is>.',
   '<ab>v. l.</ab> im <lang>Prākrit</lang>.'),
  ('und litth. maiszas',
   'und <lang>litth.</lang> maiszas'),
  ('<ls>MĀLAV. 32,7</ls> im <is>Prākrit</is>.',
   '<ls>MĀLAV. 32,7</ls> im <lang>Prākrit</lang>.'),
  ('<ls>KATHĀS. 117,93.</ls> im <lang>Prākrit</lang>',
   '<ls>KATHĀS. 117,93</ls>. im Prākrit'),
  ('<ls>MṚCCH. 13,4. 121,16</ls> im <is>Prākrit</is>.',
   '<ls>MṚCCH. 13,4. 121,16</ls> im <lang>Prākrit</lang>.'),
  ('<ls>VIKR. 82</ls> (im <lang>Prākrit</lang>).',
   '{%Kummer%} <ls>VIKR. 82</ls> (im Prākrit).'),
  ('<ls>LA. (III) 88,6.</ls> im <lang>Prākrit</lang>:',
   '<ls>LA. (III) 88,6</ls>. im Prākrit:'),
  ('{#˚Sataka#} (im <lang>Prākrit</lang>)',
   '{#˚Sataka#} (im Prākrit)'),
  ('<ls>ŚĀK. 59,17</ls> im <lang>Prākrit</lang>).',
   '<ls>ŚĀK. 59,17</ls> (im Prākrit).'),
  ('{%des Metrums%}). im <lang>Prākrit</lang>',
   '{%des Metrums%}). im Prākrit'),
  ('<ls>ŚĀK. 47,7</ls> (im <lang>Prākrit</lang>).',
   '<ls>ŚĀK. 47,7</ls> (im Prākrit).'),
  ('<ls>HĀLA Anh. 51. 59</ls> (im <lang>Prākrit</lang>).',
   '<ls>HĀLA Anh. 51. 59</ls> (im Prākrit).'),
  ('(im <lang>Prākrit</lang>)',
   '(im Prākrit)'),
  ('{#saMgadatTa#} im <lang>Prākrit</lang>',
   '{#saMgadatTa#} im Prākrit'),
  ('<ls>PRAB. 105,14.</ls> im <lang>Prākrit</lang>',
   '<ls>PRAB. 105,14</ls>. im Prākrit'),
  ('eines <lang>Prākrit</lang>-Grammatikers',
   'eines Prākrit-Grammatikers'),
  ('Titel eines Gedichts in <lang>Prākrit</lang>',
   'Titel eines Gedichts in Prākrit'),
  ('in <lang>Prākrit</lang> und in stehender Stellung',
   'in Prākrit und in stehender Stellung'),
  #('im <lang>Prākrit</lang>\n<ls>ŚĀK. CH. 110,4.</ls>',
  # 'im Prākrit\n<ls>ŚĀK. CH. 110,4.</ls>'),
  ('(Nachträge) im <lang>Prākrit</lang>',
   '(Nachträge) im Prākrit'),
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

def adjust_lines0(lines):
 ans = lines
 lnum = 1078685
 iline = lnum - 1
 assert ans[iline] == 'im <lang>Prākrit</lang>'
 ans[iline] = 'im Prākrit'
 return ans
if __name__=="__main__":
 filein = sys.argv[1]  # base
 fileout = sys.argv[2] # adjusted base
 
 lines = read_lines(filein)
 lines0 = adjust_lines0(lines)
 lines1 = adjust_lines1(lines0)
 write_lines(fileout,lines1)
