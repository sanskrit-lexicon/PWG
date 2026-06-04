""" change_0d_0e.py
 
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
  ('<ab>ved.</ab>', '<lang>ved.</lang>'),
  ('Instr.Sg.m.<lex>n.</lex>',
   '<ab>Instr.</ab> <ab>Sg.</ab> <lex>m.</lex> <lex>n.</lex>'),
  ('<ls>AUFR.</ls> {%De accentu <ab>comp.</ab>%} § 35. 36. 40. 44,6. 127-132',
   '<ls>AUFR. De accentu comp. § 35. 36. 40. 44,6. 127-132</ls>'),
  ('-<is>Devadatta</is>, {%des%} <ab>D.</ab>',
   '-<is>Devadatta</is>, {%des%} <is n="Devadatta">D.</is>'), 
  #('Ausnahmen: <ab>ebend.</ab> <ls n="P. 5,4,">72.</ls>',
  # 'Ausnahmen: <ls>ebend. 72</ls>.'),
  ('r. {#aMs#}', '<ab n="root">r.</ab>'),
  ('<ls>AUFRECHT</ls> in Zeitschrift für <ab>vergl.</ab> Sprachf. II, Heft 4.',
   '<ls>AUFRECHT</ls>_in_<ls>Zeitschrift für vergl. Sprachf. II, Heft 4</ls>.'),
  ('allein <ab>da.</ab>', 'allein da.'),
  ('Beispiel u. {#akna#} und vgl',
   'Beispiel <ab>u.</ab> {#akna#} und <ab>vgl.</ab>'),
  ('von dem oben <ab>u.</ab>',
   'von dem oben <ab n="und">u.</ab>'),
  ('<ls>Sch. 8,2,16</ls>, 🞄<ab>Sch.</ab>',
    '<ab>Sch.</ab> <ls n="">8,2,16</ls>, <ab>Sch.</ab>'),
  ('<ls>Sch. ', '<ab>Sch.</ab> <ls n="">'),
  ('<ab>ebend.</ab>', '<ls>ebend.</ls>'),
  ('<ab>Sg.</ab> <ab>N.</ab> {#a/kzi#}, V. {#a/kzi#} und {#a/kze#}; <ab>Du.</ab> <ab>N.</ab> V. <ab>Acc.</ab> {#a/kziRI#}, <ab>Instr.</ab> <ab>D.</ab> <ab>Abl.</ab> {#a/kziByAm#}; <ab>Pl.</ab> <ab>N.</ab> V. <ab>Acc.</ab>',
   
   '<ab>Sg.</ab> <ab n="Nom.">N.</ab> {#a/kzi#}, <ab n="Voc.">V.</ab> {#a/kzi#} und {#a/kze#}; <ab>Du.</ab> <ab n="Nom.">N.</ab> <ab n="Voc.">V.</ab> <ab>Acc.</ab> {#a/kziRI#}, <ab>Instr.</ab> <ab>D.</ab> <ab>Abl.</ab> {#a/kziByAm#}; <ab>Pl.</ab> <ab n="Nom.">N.</ab> <ab n="Voc.">V.</ab> <ab>Acc.</ab>'),
  
  ('Formen belegen: <ab>Sg.</ab> <ab>N.</ab> <ab>Acc.</ab>',
   'Formen belegen: <ab>Sg.</ab> <ab n="Nom.">N.</ab> <ab>Acc.</ab>'),
  ('<ab>Du.</ab> <ab>N.</ab> <ab>Acc.</ab>',
   '<ab>Du.</ab> <ab n="Nom.">N.</ab> <ab>Acc.</ab>'),
  ('<ab>Pl.</ab> <ab>N.</ab> <ab>Acc.</ab>',
   '<ab>Pl.</ab> <ab n="Nom.">N.</ab> <ab>Acc.</ab>'),
  ('<is>Caus</is>', '<ab>Caus.</ab>'),
  # u.
  #('<ls>ŚKDR.</ls> <ab>u.</ab> <ls>WILS.</ls>',
  # '<ls>ŚKDR.</ls> <ab n="und">u.</ab> <ls>WILS.</ls>'),
  ('</ls>, <ab>v. u.</ab>',
   ', v. u.</ls>'),
  ('pr. et.', '<ab>praet.</ab>'),
  ('</ls> <ab>a. a. O.</ab>', ' a. a. O.</ls>'),
  ('<ab>indecl.</ab>', '<lex>indecl.</lex>'),
  ('klass. 🞄<ls>Spr.</ls>',
   '<lang>klass.</lang> <ab>Spr.</ab>'),
  ('{%Morinda tinctoria%} <ab>an.</ab>',
   '{%Morinda tinctoria%} <ls n="H.">an.</ls>'),
  ('<ls>Ind. St. I,428</ls>, <ab>N.</ab>',
   '<ls>Ind. St. I,428,N.</ls>'),
  ('<ab>S.</ab> XLII', '<ls n="VS.">S. XLII</ls>'),
  ('{%Barleria longifolia, Lin. Asteracantha l., Nees%}',
   '{%Barleria longifolia, Lin.%} {%Asteracantha <ab n="longifolia">l.</ab>, Nees%}'),
  ('<ls>HAUGHTON</ls>, a Dict. Beng. and <ab>S.</ab>',
   '<ls>HAUGHTON, a Dict. Beng. and S.</ls>'),
  ('<ls>BṚH. ĀR. UP. 1,4,6</ls> (<ab>p.</ab> 150. bei ROER).',
   '<ls>BṚH. ĀR. UP. 1,4,6 (p. 150. bei ROER)</ls>.'),
  ('in den <ab>ind.</ab> <ab>Wörterb.</ab>',
   'in den <ab n="indische">ind.</ab> <ab>Wörterb.</ab>'),
  ('<ab>N.</ab> 🞄(<ls>BOPP) 12,35</ls>',
   '<ls>N. (BOPP) 12,35</ls>'),
  ('{%mit diesen Banden allen binde ich dich <ab>N.</ab> <ab>N.</ab>, von <ab>N.</ab> <ab>N.</ab> stammend, der <ab>N.</ab> <ab>N.</ab> Sohn%}',
   '{%mit diesen Banden allen binde ich dich <ab n="Nomen Nescio">N. N.</ab>, von <ab n="Nomen Nescio">N. N.</ab> stammend, der <ab n="Nomen Nescio">N. N.</ab> Sohn%}'),
  ('<ls>ROTH</ls>, Erläut. <ab>z.</ab> 🞄<ls>NIR. S. 87.</ls> <ab>Anm.</ab> Ein wirkliches {#Adeva#}',
   '<ls>ROTH, Erläut. z. NIR. S. 87. Anm.</ls> Ein wirkliches {#Adeva#}'),
  ('(l. {#garhya#} <ab>st.</ab> {#garha#})',
   '(<ab n="lies">l.</ab> {#garhya#} <ab>st.</ab> {#garha#})'),
  ('R. <ab>Einl.</ab> 5.', '<ls>R. Einl.</ls> 5.'),
  ('<ls>ŚKDR. — S.</ls>', '<ls>ŚKDR.</ls> — <ab>S.</ab>'), # 2
  ('<ab>s.</ab> 🞄<ls>TAITT. UP. 2,8.</ls> (<ab>S.</ab> 103. bei ROER).',
   '<ab>s.</ab> <ls>TAITT. UP. 2,8. (S. 103. bei ROER)</ls>.'),
  ('in der ersten Bed.', 'in der ersten <ab>Bed.</ab>'),
  ('<ls>BṚH. ĀR. UP. 7,6,1. S. u.</ls>',
   '<ls>BṚH. ĀR. UP. 7,6,1</ls>. <ab>S. u.</ab>'),
  ('<ls>ŚKDR. S.</ls>', '<ls>ŚKDR.</ls> <ab>S.</ab>'),  # 4
  (' S.</ls> {#', '</ls> <ab>S.</ab> {#'),  # 17. 4 are wrong
  # ('<ls>VARĀH. BṚH. S.</ls> {#', ''),
  (' 🞄<ls>ROTH</ls>, Erl. zum <ls>NIR. 43</ls>, <ab>Anm.</ab>',
   '<ls>ROTH, Erl. zum NIR. 43, Anm.</ls>'),
  ('2ten <ab>Aufl.</ab>', '2ten Aufl.'),  #32
  ('1sten <ab>Aufl.</ab>', '1sten <ab>Aufl.</ab>'), #7
  ('🞄<ls>ROTH</ls>, <ab>Einl.</ab> zum 🞄<ls>NIR. LVII. fgg.</ls>',
   '<ls>ROTH, Einl. zum NIR. LVII. fgg.</ls>'),
  ('<is>du</is>.', '<ab>du.</ab>'),  #25
  ('eines comp.', 'eines <ab>comp.</ab>'), #2
  ('(vgl.', '(<ab>vgl.</ab>'),
  ('({%die von%} <ab>S.</ab> {%dargebotene Gelegenheit%})',
   '({%die von%} <is n="Saraṇa">S.</is> {%dargebotene Gelegenheit%})'),
  (' auf.', ' <ab>auf.</ab>'),
  ('Diese und die folgende Bedeutung fassen die <ab>ind.</ab>',
   'Diese und die folgende Bedeutung fassen die <ab n="indische">ind.</ab>'),
  ('#} 2,<ab>s.</ab>', '#} 2,s.'),
  ('in Gegenwart, nahe%} (Geg. ',
   'in Gegenwart, nahe%} (<ab n="Gegenwart">Geg.</ab> '),
  ('<ab>neutr.</ab>', '<lex>neutr.</lex>'),
  (' entstanden. <ab>S.</ab> {#mustA#} .',
   ' entstanden. <ab n="Süd">S.</ab> {#mustA#}.'),
  ('</ls> <ab>v. u.</ab>', ' v. u.</ls>'),  # 1169 lines changed
  ('<ls>RAGH. 2,62.</ls> Ganz so im Griechischen, 🞄<ab>z. B.</ab> <ab>d.</ab>',
   '<ls>RAGH. 2,62.</ls> Ganz so im Griechischen, <ab>z. B.</ab> d.'),
  ('<ab>pl.</ab> <ab>an.</ab>', '<ab>pl.</ab> an.'),
  ('<ab>d.</ab> <ab>folg.</ab>',
   '<ab>d. folg.</ab>'), #14
  ('<ab>ind.</ab> Grammatiker', '<ab n="indische">ind.</ab> Grammatiker'),
  ('{%auch etwas Anderes, noch etwas A.%}',
   '{%auch etwas Anderes, noch etwas <ab n="Anderes">A.</ab>%}'),
  ('Salmalia malabarica <ab>Sch.</ab> <ab>u.</ab> Endl.',
   'Salmalia malabarica Sch. u. Endl.'),
  ('<lex>n.</lex> 🞄<ls>Chr.</ls>',
   '<ab>n. Chr.</ab>'),  # A. D. (date) #
  ('<ab>ind.</ab> Lexicographen',
   '<ab n="indische">ind.</ab> Lexicographen'), #3
  ('(eine <ab>ungrammat.</ab> Bildung von {#apsu#})',
   '(eine ungrammat. Bildung von {#apsu#})'),
  ('{%nach dem%} <ab>p.</ab> {%hingekehrt%}',
   '{%nach dem%} <is n="puruṣa">p.</is> {%hingekehrt%}'),
  ('<ab>an.</ab>', 'an.'),  # 37 -  3 will go back to <ab>an.</ab>
  ('<ab>s. v.</ab> a.',
   '<ab>s.</ab> <ab>v. a.</ab>'), #27
  ('🞄<ls>MED. l. 61, s.</ls> {#aBIla#} .',
   '<ls>MED. l. 61</ls>, <ab>s.</ab> {#ABIla#}.'),
  ('<ls n="">S.</ls>', '<ab>S.</ab>'), # 1
  ('<ab>N.N.</ab>', '<ab n="Nomen Nescio">N. N.</ab>'),
  ('<ab>N.</ab> <ab>N.</ab>', '<ab n="Nomen Nescio">N. N.</ab>'),
  ('{%Clypea hernandifolia <ab>W.</ab> <ab>u.</ab> A.%}',
   '{%Clypea hernandifolia W. u. A.%}'), #4
  ('{%Vachellia farnesiana <ab>W.</ab> <ab>u.</ab> A.%}',
   '{%Vachellia farnesiana W. u. A.%}'), #4
  ('<ls>VP. 50</ls>, <ab>N.</ab>',
   '<ls>VP. 50, N.</ls>'),
  ('{%Polanisia icosandra <ab>W.</ab> <ab>u.</ab> A.%}',
   '{%Polanisia icosandra W. u. A.%}'),
  ('{%Terminalia Arjuna <ab>W.</ab> <ab>u.</ab> A.%}', # 3
   '{%Terminalia Arjuna W. u. A.%}'), # 11
  (' der andere <ab>Th.</ab>',
   'der andere <ab n="Theil">Th.</ab>'),
  ('<ab>s. d.</ab> <ab>folg. W.</ab>', 
   '<ab>s.</ab> <ab>d. folg. W.</ab>'),  #2
  ('In der <ab>folg.</ab> <ab>St.</ab>',
   'In der <ab>folg.</ab> <ab n="Stellen">St.</ab>'),
  ('{%Terminalia tomentosa <ab>W.</ab> <ab>u.</ab> A.%}',
   '{%Terminalia tomentosa W. u. A.%}'), #8
  ('{#alaM devadatto hanizyati#} <ab>D.</ab>',
   '{#alaM devadatto hanizyati#} <is n="Devadatta">D.</is>'),
  ('<ab>Gegend.</ab>', 'Gegend.'), # 6
  ('<ab>st.</ab> <ab>d.</ab>', '<ab>st.</ab> d.'), # 1
  ('<ab>ind.</ab> Feigenbaums',
   '<ab n="indische">ind.</ab> Feigenbaums'),
  ('<ab>z.</ab> 🞄<ls>B.</ls>',
   '<ab>z. B.</ab>'), #11
  ('<ab>ind.</ab>', '<lex>ind.</lex>'), # 27 Further changes to come
  ('v. <ls>Chr.</ls>', '<ab>v. Chr.</ab>'),  #B.C.
  ('{%Vatica robusta <ab>W.</ab> <ab>u.</ab> A.%}',
   '{%Vatica robusta W. u. A.%}'), # 7
  (' 🞄<ls>MBH. 3,11052</ls> (<ab>p.</ab> 571).',
   ' <ls>MBH. 3,11052 (p. 571)</ls>.'),
  ('</ls>, <ab>Randgl.</ab>',
   ', Randgl.</ls>'), #5
  ('<ab>lith.</ab>', '<lang>lith.</lang>'), #13
  ('<ab>u. d.</ab> <ab>W.</ab>',
    '<ab>u.</ab> <ab>d. W.</ab>'), #58
  ('</ls> (<ab>p.</ab> 572)',
   ' (p. 572)</ls>'), #8
  ('</ls>, <ab>Anf.</ab>',
   ', Anf.</ls>'), #36
  ('🞄<ls>MBH.</ls> I, <ab>p.</ab> 648, <ab>Z.</ab> 4.',
   '<ls>MBH. I, p. 648, Z. 4</ls>.'),
  ('<lex>adv.</lex> ad.', '<lex>adv.</lex> <ab>ad.</ab>'),
  ('<ab>Ind.</ab> <ab>St.</ab>', '<ls>Ind. St.</ls>'),  #3
  ('<ab>Erll.</ab> zu <ls>NIR. p. 96.</ls>',
   '<ls>Erll. zu NIR. p. 96</ls>.'),
  ('<ls>VEDĀNTAS. 1,10. Comm. 13,13. 25,2 v. u.</ls>',
   '<ls>VEDĀNTAS. 1,10.</ls> <ab>Comm.</ab> <ls n="VEDĀNTAS.">13,13. 25,2 v. u.</ls>'),
  ('<ls>ROTH.</ls> <ab>Erll.</ab> zu <ls>NIR. 117. 122.</ls>',
   '<ls>ROTH, Erll. zu NIR. 117. 122</ls>.'),
  ('</ls> 🞄<ab>fgg.</ab>', ' fgg.</ls>'),
  ('</ls> (<ab>p.</ab> 570)', ' (p. 570)</ls>'), # 4
  ('(l.', '(<ab n="lies">l.</ab>'), #4
  ('<ab>Einl.</ab> zum <ls>SV. XVI.</ls>',
   '<ls>Einl. zum SV. XVI.</ls>'),
  ('</ls>, <ab>Anm.</ab>',
   ', Anm.</ls>'),
  ('</ls> (<ab>p.</ab> 571)',
   ' (p. 571)</ls>'), # 10
  ('die <ab>Ausg.</ab> von 1828, <ab>p.</ab> 40, l. 7',
   '<ls>die <ab>Ausg.</ab> von 1828, p. 40, l. 7</ls>'),
  ('wohl so v.', 'wohl so <ab>v.</ab>'),
  #('', ''),  # (/ 9721.0 122738.0)  8%
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
