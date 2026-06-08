""" change_ab_v1c_v1d.py
 
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
  ('<ab>adj.</ab>', '<lex>adj.</lex>'), # 2
  ('<ab>adj. Comp.</ab>', '<ab>adj. comp.</ab>'), # 7
  ('<lang>pers.</lang>', '<ab>pers.</ab>'), #16
  ('{%Fisch%} dies, und ', '{%Fisch%} <ab>dies.</ab> und '),
  ('<ls>SUŚR. 1,333, (323 <ab>gedr.</ab>) 19. 8</ls>',
   '<ls>SUŚR. 1,333, (323 gedr.) 19. 8</ls>'),
  ('die auch sonst weibl. personificirt werden',
   'die auch sonst <ab>weibl.</ab> personificirt werden'), #1
  ('<ab n="Süd">S.</ab> {#apyayadIkzita#}',
   '<ab>S.</ab> {#apyayadIkzita#}'),   # Sehen (?) = See
  ('<ls>ŚĀK. 88. <ab>ad.</ab> 78</ls>',
   '<ls>ŚĀK. 88. ad. 78</ls>'),
  ('<ab>copul.</ab> <ab>comp.</ab>',
   '<ab>copul. comp.</ab>'),
  ('<ls>MBH. 1,364 (<ab>vgl.</ab> p. 691, N.)</ls>',
   '<ls>MBH. 1,364 (vgl. p. 691, N.)</ls>'),
  ('zwei <ab>imperat.</ab>', 'zwei <ab>imperatt.</ab>'),
  ('<ab>imperat.</ab> von {#marj#}',
   '<ab>imperatt.</ab> von {#marj#}'),
  ('<ab n="und>u.</ab>', '<ab n="und">u.</ab>'),
  ('</ls>-<ab>Rec.</ab>', '-Rec.</ls>'), #5
  ('(<ab>genit.</ab> des <ab>partic.</ab>)',
   '(<ab>genet.</ab> des <ab>partic.</ab>)'),
  ('<ls>ŚAIVATANTRA <ab>folg.</ab> 64</ls>',
   '<ls>ŚAIVATANTRA folg. 64</ls>'),
  ('<ab>engl.</ab>', '<lang>engl.</lang>'),
  ('(<ls>BUCHANANʼs <ab>Hdschrr.</ab></ls>)',
   '(<ls>BUCHANANʼs Hdschrr.</ls>)'),
  ('<ls>KUMĀRAS. 7,27</ls> (<ls>ST.</ls>',
   '<ls>KUMĀRAS. 7,27</ls> (<ls>St.</ls>'),
  ('davon nom <ab>abstr.</ab>',
   'davon <ab>nom. abstr.</ab>'),
  ('abgiebt.', '<ab>abgiebt.</ab>'),
  ('<ab>Vgl.</ab> {#KurAlika#} <ls>ŚKDR.</ls>',
   '<ab>v. l.</ab> {#KurAlika#} <ls>ŚKDR.</ls>'),
  ('<ls>KĀTY. <ab>a. a. O.</ab> und 4,2,10</ls>',
   '<ls>KĀTY. a. a. O. und 4,2,10</ls>'),
  ('von {#jIv#} <ab n="und">u.</ab> <ab>caus.</ab>',
   'von {#jIv#} <ab>simpl.</ab> <ab n="und">u.</ab> <ab>caus.</ab>'),
  ('<ab>potent.</ab> {%spiritu praeditus%}',
   '{%potente spiritu praeditus%}'),
  ('(<ls>SV.</ls> <ab>v. l.</ab>).',
   '(<ls>SV. v. l.</ls>).'),
  (' <ab>s. u.</ab> d. vorhergehenden Worte.',
   ' <ab>s. u.</ab> <ab>d.</ab> vorhergehenden Worte.'),
  ('<lex>adj.</lex> <ab>comp.</ab>',
   '<ab>adj. comp.</ab>'), #10
  ('<ab>lith.</ab>', '<lang>lith.</lang>'),
  ('<ls>BURNOUF <ab>a. a. O.</ab> LXXXV. fgg.</ls>',
   '<ls>BURNOUF a. a. O. LXXXV. fgg.</ls>'),
  ('<ls>JOHAENTGEN <ab>a. a. O.</ab> S. 5. 18</ls>',
   '<ls>JOHAENTGEN a. a. O. S. 5. 18</ls>'),
  ('<ls>TBR. <ab>Comm.</ab> I, S. 26,3</ls>',
   '<ls>TBR. Comm. I, S. 26,3</ls>'),
  ('<ls>Calc. Ausg.</ls>', '<ab>Calc. Ausg.</ab>'),
  ('<ls>Verz. d. Pet. <ab>Hdschr.</ab> No. 35</ls>',
   '<ls>Verz. d. Pet. Hdschr. No. 35</ls>'),
  ('<ls>Verz. d. Pet. <ab>Hdschr.</ab> No. 91</ls>',
   '<ls>Verz. d. Pet. Hdschr. No. 91</ls>'),
  ('<ls>WILSON <ab>a. a. O.</ab> XL.</ls>',
   '<ls>WILSON a. a. O. XL.</ls>'),
  ('<ab>s. u.</ab> <hom>1.</hom> {#praT#} <ab n="und">u.</ab> <ab>caus.</ab>',
   '<ab>s. u.</ab> <hom>1.</hom> {#praT#} <ab>simpl.</ab> <ab n="und">u.</ab> <ab>caus.</ab>'), 
  ('<ls>VP. 444 (<ab>vgl.</ab> N. 12)</ls>.',
   '<ls>VP. 444 (vgl. N. 12)</ls>.'),
  ('<ls>BHĀG. P. 5,5,32. 26,23 ed.</ls> <ls>BURN.</ls>',
   '<ls>BHĀG. P. 5,5,32. 26,23</ls> <ls>ed. BURN.</ls>'),
  ('(von <hom>3.</hom> {#Buj#} <ab n="und">u.</ab> <ab>caus.</ab>)',
   '(von <hom>3.</hom> {#Buj#} <ab>simpl.</ab> <ab n="und">u.</ab> <ab>caus.</ab>)'),
  ('<ls>Pet. <ab>Hdschr.</ab> 13,a,3</ls>.',
   '<ls>Pet. Hdschr. 13,a,3</ls>.'),
  #('(<ab>vgl.</ab> <ab>Sp.</ab> 519, <ab>Z.</ab> 35. <ab>fgg.</ab>)',
  # '(<ab>vgl.</ab> <ls>Sp. 519, Z. 35. fgg.</ls>)'),
  ('<ls>ṚV. <ab>Comm.</ab> I, S. 22</ls>.',
   '<ls>ṚV. Comm. I, S. 22</ls>.'),
  ('<ls>AUFRECHT <ab>a. a. O.</ab> 246,a, N. 1</ls>.',
   '<ls>AUFRECHT a. a. O. 246,a, N. 1</ls>.'),
  ('<ls>ŚĀRṄG. PADDH. Pet. <ab>Hdschr.</ab> 50,b (73,b)</ls>.',
   '<ls>ŚĀRṄG. PADDH. Pet. Hdschr. 50,b (73,b)</ls>.'),
  ('der <ls>Einl.</ab> zu NIR. XXIII.</ls>',
   'der <ls>Einl. zu NIR. XXIII.</ls>'),
  #('', ''),
  #('', ''),
  #('', ''),
  #('', ''),
  #('', ''),
  #('', ''),
  #('', ''),
  #('', ''),
  #('', ''),
  #('', ''),
  #('', ''),
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
