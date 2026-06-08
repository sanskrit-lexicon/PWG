""" change_0e_0f.py
 
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
  #('', ''),  # (/ 9721.0 122738.0)  8%
  ('abstrol.', '<ab>astrol.</ab>'),
  ('(Gegens.', '(<ab>Gegens.</ab>'),
  (' ad.', ' <ab>ad.</ab>'), #20
  (' Spiel.', ' <ab n="Spielerei">Spiel.</ab>'),
  ('<ls>ROTH</ls>, <ab>Erll.</ab> zu <ls>NIR. 8,7</ls>',
   '<ls>ROTH, Erll. zu NIR. 8,7</ls>'),  
  ('<ls>SĀY.</ls> in der <ab>Einl.</ab> zum 🞄<ls>AIT. BR.</ls>',
   '<ls>SĀY.</ls> in der <ls>Einl. zum AIT. BR.</ls>'), # 2
  ('Erz.', '<ab n="Erzählung">Erz.</ab>'),
  ('oben <ab>S.</ab>', ' oben <ab n="Seite">S.</ab>'),
  ('</ls>, 🞄<ab>v. u.</ab>', ', v. u.</ls>'), #3
  
  ('<ab>u. d.</ab>',
   '<ab>u.</ab> <ab n="dem">d.</ab>'), # 104 requires corrections
  ('<ab>Vgl.</ab> <ab>u.</ab> <ab n="dem">d.</ab>',
   '<ab>Vgl.</ab> <ab>u. d.</ab>'),  # first correction
  ('<ab>vgl.</ab> <ab>u.</ab> <ab n="dem">d.</ab> <ab>simpl.</ab>',
   '<ab>vgl.</ab> <ab>u. d.</ab> <ab>simpl.</ab>'), # second correction
  ('in der <ab>Einl.</ab> <ab>z.</ab> 🞄<ls>ṚV.</ls> <ab>p.</ab> 35.',
   'in der <ls>Einl. z. ṚV. p. 35</ls>.'),
  ('17ten J. ', '17ten <ab n="Jahr">J.</ab>'),
  ('{%<ab>W.</ab> <ab>u.</ab> A.%}', '{%W. u. A.%}'), #6
  ('<ab>W.</ab> <ab>D.</ab> <ls>WHITNEY</ls>',
   '<ls>W. D. WHITNEY</ls>'),
  ('Es stehen <ab>z.</ab> 🞄<ls>B. 47</ls>',
   'Es stehen <ab>z. B.</ab> 47'),
  ('R. <ab>Einl.</ab>', '<ls>R. Einl.</ls>'), #8
  ('<ab>D.</ab> {%kann', '<is n="Devadatta">D.</is> {%kann'),
  ('{%der Laut <ab>u.</ab>%}', '{%der Laut u%}.'),
  ('{%Pimpinella involucrata <ab>W.</ab> <ab>u.</ab> A.%}',
    '{%Pimpinella involucrata W. u. A.%}'),
  ('<ls>VP. 153. 78</ls>, <ab>N.</ab>',
   '<ls>VP. 153. 78, N.</ls>'),
  ('🞄<ls>MBH. 1,364</ls> (<ab>vgl.</ab> <ab>p.</ab> 691, <ab>N.</ab>).',
   '<ls>MBH. 1,364 (vgl. p. 691, N.)</ls>.'),
  ('zwei imperatt.', 'zwei <ab>imperatt.</ab>'),
  ('1sten <ab>Aufl.</ab>', '1sten Aufl.'), #7
  ('<ls n="MBH. 3,">11012</ls> (<ab>p.</ab> 569).',
   '<ls n="MBH. 3,">11012 (p. 569)</ls>.'),
  ('<ab>d.</ab> <lex>folg.</lex>', '<ab>d. f.</ab>'),
  (' imperatt. ', ' <ab>imperatt.</ab> '), #6
  ('<ls>MBH. 1,4897.</ls> Buch 1, <ab>Kap.</ab> 102',
   '<ls>MBH. 1,4897. Buch 1, Kap. 102</ls>'),
  ('</ls>-<ab>Rec.</ab>', '-Rec.</ls>'), #3  10%
  ('(eig.', '(<ab>eig.</ab>'),
  ('<ab>z.</ab> <ab>d. St.</ab>',
   '<ab n="zu">z.</ab> <ab>d. St.</ab>'), #4
  ('<ab>Erll.</ab> zum 🞄<ls>NIRUKTA p. 153.</ls>',
   '<ls>Erll. zum NIRUKTA p. 153</ls>.'),
  ('<ls n="MBH.">3,10557</ls> ({#uzInara#}). <ab>fg.</ab>',
   '<ls n="MBH.">3,10557 ({#uzInara#}). fg.</ls>'),
  ('<ls>VS. 1,27.</ls> <ab>p.</ab> {#57#} .',
   '<ls>VS. 1,27. p. {#68#}.</ls>'),
  ('</ls> 🞄<ab>v. u.</ab>', ' v. u.</ls>'), # 51
  ('(abl.)', '(<ab>abl.</ab>)'),
  ('indentif.', '<ab>identif.</ab>'),
  ('(p. 571)</ls>. <ab>fgg.</ab>',
   '(p. 571). <ab>fgg.</ls>'),
  ('<ab>d.</ab> <ab>fg.</ab>',
   '<ab>d. fg.</ab>'),
  ('({%am Ende der M.) gebadet%}',
   '({%am Ende der <ab n="Menstruation">M.</ab>%}) {%gebadet%}'),
  ('<ab>d.</ab> <ab>vorherg.</ab>',
   '<ab>d. vorherg.</ab>'),
  (' im gen. ', ' im <ab>gen.</ab> '),
  (' nom. voc. ', ' <ab>nom.</ab> <ab>voc.</ab> '),
  ('</ls>, <ab>N.</ab>', ', N.</ls>'), #15
  ('<ls>Ind. St. 1,188, N.</ls> ein Sohn',
   '<ls>Ind. St. 1,188</ls>, <ab>N.</ab> ein Sohn'),
  ('(Gegens). ({#viBinna#})', '(<ab>Gegens.</ab> {#viBinna#})'),
  ('idendentif.', '<ab>identif.</ab>'),
  (' Astr. ', ' <ab n="Astrolog">Astr.</ab> '), #50
  (' d. i. ', ' <ab>d. i.</ab> '), #5
  ('<ab>s.</ab> <ab>S.</ab>',
   '<ab>s.</ab> <ab n="Seite">S.</ab>'), # 3
  (' insbes. ', ' <ab>insbes.</ab> '), #2
  ('(z. B. von Reis)', '(<ab>z. B.</ab> von Reis)'),
  ('</ls> — <ab>Rec.</ab>', '-Rec.</ls>'), #4
  ('{%Coccinia grandis <ab>W.</ab> <ab>u.</ab> A.%}',  
   '{%Coccinia grandis W. u. A.%}'),  # 12%
  ('<ab>Erll.</ab> zu <ls>', '<ls>Erll. zu '), #3
  ('<ls>GILD.</ls>, Scriptorum Arabum <ab>etc.</ab> 🞄<ab>S.</ab> 15. <ls>Z. f. d. K. d. M. IV,107.</ls>',
   '<ls>GILD., Scriptorum Arabum etc. S. 15</ls>. <ls>Z. f. d. K. d. M. IV, 107</ls>.'),
  ('<ls>WILSON</ls> in der 🞄<lex>n.</lex>',
   '<ls>WILSON</ls> in der <ab n="Note">N.</ab> '),
  ('<ls>Verz. d. B. H. No. 664. 823. 849</ls> (<ab>S.</ab> 239, <ab>Z.</ab> 5).',
   '<ls>Verz. d. B. H. No. 664. 823. 849 (S. 239, Z. 5)</ls>.'),
  ('{#kurukata#} <ab>eben.</ab>', '{#kurukata#} eben.'),
  ('({%über den U.%})', '({%über den <ab n="Unterredung">U.</ab>%})'),
  ('<lex>m.</lex> pr. <ab>N. pr.</ab>',
   '<lex>m.</lex> <ab>pl.</ab> <ab>N. pr.</ab>'),
  ('{%ein Schlag mit dem E.%}',
   '{%ein Schlag mit dem <ab n="Ellbogen">E.</ab>%}'),
  ('<ab>Nn.</ab> ppr.', '<ab>Nn. prr.</ab>'),
  ('auch <ab>u.</ab> <ab n="dem">d.</ab> <ab>simpl.</ab>',
   'auch <ab>u. d.</ab> <ab>simpl.</ab>'),
  ('<ab>Einl.</ab> zum 🞄<ls>',
   '<ls>Einl. zum '), #8
  (' Analog. ', ' <ab n="Analogie">Analog.</ab> '),
  ('Handlung <ab>vor.</ab>%}', ' Handlung vor%}'),
  ('auch <ab>u.</ab> <ab n="dem">d.</ab> <ab>desid.</ab>',
   'auch <ab>u. d.</ab> <ab>desid.</ab>'),
  ('(instr.', '(<ab>instr.</ab>'), #7
  ('(c. <ab>acc.</ab> <ab>pers.</ab>)',
   '(<ab n="cum">c.</ab> <ab>acc.</ab> <ab>pers.</ab>)'),
  (' instr. ', ' <ab>instr.</ab> '),
  (' instr.', ' <ab>instr.</ab>'),  # 13%
  ('eig. als auch in übertr. Bed.',
   '<ab>eig.</ab> als auch in <ab>übertr.</ab> <ab>Bed.</ab>'),
  ('<ls>POTT</ls>, Die quin. <ab>u.</ab> vig. Zählm. 🞄<ls>283. fg.</ls>',
   '<ls>POTT, Die quin. u. vig. Zählm. 283. fg.</ls>'),
  ('<ls>Z. d. d. m. G. 2,337, No. 129</ls>, e) und',
   '<ls>Z. d. d. m. G. 2,337, No. 129,e</ls>) und'),
  ('Asiatischen Museum der Kais. Akad. d. Wiss. in <ab>St.</ab> Petersburg.',
   '<ls>Asiatischen Museum der Kais. Akad. d. Wiss. in St. Petersburg.</ls>'),
  ('(genet. des <ab>partic.</ab>)', '(<ab>genet.</ab> des <ab>partic.</ab>)'),
  (' best. ', ' <ab>best.</ab> '), # 9
  ('<ab>franz.</ab>', '<lang>franz.</lang>'),
  ('<ab>vgl.</ab> o. <ab>d.</ab>', '<ab>vgl.</ab> <ab n="oder">o.</ab> <ab>d.</ab>'),
  ('<ab>N.</ab> 🞄[Page2-0161] 🞄pr.',
   '<ab>N. pr.</ab> 🞄[Page2-0161]'),
  (' der <lex>ind.</lex> Laute',
   ' der <ab n="indische">ind.</ab> Laute'),
  ('</ls> (<ab>p.</ab> 569)', ' (p. 569)</ls>'), #4
  (' l. für ', ' <ab n="lectio">l.</ab> für '),
  ('Nr. pr.', '<ab>N. pr.</ab>'),
  ('<ls>BÖHTLINGK</ls> in der <ab>Einl.</ab> zu seiner <ab>Ausg.</ab> <ab>S.</ab> VIII. IX.',
   '<ls>BÖHTLINGK in der Einl. zu seiner Ausg. S. VIII. IX.</ls>'),
  ('<ls>ROTH</ls>, <ab>Einl.</ab> zu ',
   '<ls>ROTH, Einl. zu '),
  ('die deutsche <ab>Uebers.</ab> <ab>S.</ab> 172. <ab>fg.</ab>',
   'die <ls>deutsche Uebers. S. 172. fg.</ls>'),
  (' d. h. ', ' <ab>d. h.</ab> '), #3
  ('<ab>nom.</ab> 🞄[Page2-0225] 🞄<ab>abstr.</ab>',
   '<ab>nom. abstr.</ab> 🞄[Page2-0225] 🞄'),
  ('{%eine Verliebte <ab>u. s. w.</ab> <ab>s.</ab>%} <ab>u.</ab> 1.',
   '{%eine Verliebte <ab>u. s. w.</ab>%} <ab>s. u.</ab> 1.'),
  ('Davon nom <ab>abstr.</ab>',
   'Davon <ab>nom. abstr.</ab>'), #4
  ('<ab>engl.</ab>', '<lang>engl.</lang>'), #6
  ('</ls> (<ab>p.</ab> 570.) <ab>fgg.</ab>',
   ' (p. 570.) fgg.</ls>'),
  ('</ls> (<ab>p.</ab> 339)',
   ' (p. 339)</ls>'),
  ('<ab>denom.</ab> 🞄v.',
   '<ab>denom.</ab> <ab n="von">v.</ab>'),  # 15%
  ('<lex>n.</lex> 2. {#kAlApa#}',
   '<ab>u.</ab> 2. {#kAlApa#}'),
  ('<ab>vgl.</ab> Prolegg. I. <ab>fg.</ab>',
   '<ab>vgl.</ab> <ls>Prolegg. I. fg.</ls>'),
  ('( 🞄<ls>BUCHANAN\'S Hdschrr.</ls>)', 
   '(<ls>BUCHANANʼS Hdschrr.</ls>)'),
  # Begin 06-05-2026
  ('{%der rothe Wollbaum, Salmalia malabarica Schott <ab>u.</ab> Endl.%}',
   '{%der rothe Wollbaum%}, {%Salmalia malabarica Schott u. Endl.%}'),  
  ('<ls>KĀTY. ŚR. 1,5,10</ls> (<ab>S.</ab> 89, <ab>Z.</ab> 8.)',
   '<ls>KĀTY. ŚR. 1,5,10 (S. 89, Z. 8)</ls>.'),
  ('{%die Mutter des Kr.%}',
   '{%die Mutter des <ab n="Kriegsgottes">Kr.</ab>%}'),
  ('{%<ab>N.</ab> rubra%}', '{%N. rubra%}'),
  ('(<ab>St.</ab>: {%familiae dii%})',
   '(<ls>St.</ls>: {%familiae dii%})'),
  ('nom <ab>abstr.</ab>',
   '<ab>nom. abstr.</ab>'), #12
  ('<ab>d.</ab> <ab>vor.</ab>',
   '<ab>d. vor.</ab>'),
  ('(I. {#kenipAta#} <ab>st.</ab> {#kelitAta#})',
   '(<ab n="lies">l.</ab> {#kenipAta#} <ab>st.</ab> {#kelitAta#})'),
  ('Buch 3, <ab>Kap.</ab> 38. <ab>fgg.</ab>',
   '<ls>Buch 3, Kap. 38. fgg.</ls>'),
  ('{%von der Farbe <ab>d.</ab> r. L.%}',
   '{%von der Farbe <ab n="des rothen Lotus">d. r. L.</ab>%}'),
  ('<ab>s.</ab> {%mutual anger, reciprocal wrath.%}',
   '<ab n=???">s.</ab> {%mutual anger, reciprocal wrath%}.'),
  ('</ls>, <ab>fgg.</ab>', ', fgg.</ls>'),
  ('{#koSa#} 1,<ab>p.</ab>',
   '{#koSa#} <ls n="YĀJÑ.">1,p</ls>.'),
  ('vv. II.', '<ab>vv. ll.</ab>'),
  ('<ls>ebend.</ls> 🞄<ls n="VARĀH. BṚH. S. 14,">33.</ls> <ls>Var. l.</ls>',
   '<ls>ebend. 33</ls>. <ab>Var. l.</ab>'),
  ('führt zu <ab>d.</ab> <ab>u.</ab> <ab n="dem">d.</ab> O.',
   'führt zu <ab n="dem und dem Ort">d. u. d. O.</ab>'),
  ('</ls> 🞄<ab>fg.</ab>',
   ' fg.</ls>'),
  ('<ab>S.</ab> 153 — 159.',
   '<ab n=Seiten">S.</ab> 153—159.'),
  ('ITSITSITS',
   '<ab n="Iamb-Trochee-Spondee thrice">ITSITSITS</ab>'),
  ('</ls> (<ab>p.</ab> 572.)',
   ' (p. 572)</ls>.'),
  ('nach einem Aug., während eines Aug.',
   'nach einem <ab n="Augenblick">Aug.</ab>, während eines <ab n="Augenblick">Aug.</ab>'),
  (' Bez. ',  ' <ab>Bez.</ab> '), #3
  ('Theil I, <ab>S.</ab> 820', '<ls>Theil I, S. 820</ls>'),
  ('{%der sich mit fremden Ehefrauen <ab>abgiebt.</ab>%}',
   '{%der sich mit fremden Ehefrauen abgiebt%}.'),
  ('{%a place where grain, etc. is stored for sale%}',
   '{%a place where grain, <ab>etc.</ab> is stored for sale%}'),
  ('(<ab>s.</ab> {#gaRa#} 8. 🞄) <ls>BOEHTL.</ls>, <ab>Einl.</ab> zu <ls>P. XXXIX fgg.</ls>',
   '(<ab>s.</ab> {#gaRa#} 8.) <ls>BOEHTL., Einl. zu P. XXXIX fgg.</ls>'),
  ('(loc.', '(<ab>loc.</ab>'), #3
  ('{%in Bezug <ab>auf.</ab>%}',
   '{%in Bezug auf%}.'),
  ('<ab>u.</ab> <ab n="dem">d.</ab> l. <ab>W.</ab>',
   '<ab>u.</ab> <ab>d. l. W.</ab>'),
  ('<ls>VIŚVA beim Sch.</ls>',
   '<ls>VIŚVA</ls> beim <ab>Sch.</ab>'),
  (' 🞄V. I. : {#BANgika#} .',
   ' <ab>Vgl.</ab>: {#BANgika#} .'),
  ('{%tausend K. besitzend%}',
   '{%tausend <ab n="Kühe">K.</ab> besitzend%}'),  # 20%
  ('<ab>Ind.</ab> zu <ls>P.',
   '<ls>Ind. zu P.'), # 2
  ('<ls>VOP. 4,16</ls> und <ab>S.</ab> 225.',
   '<ls>VOP. 4,16 und S. 225</ls>.'),
  ('<is>Vārtt</is>. 2. <ab>fgg.</ab>',
   '<is>Vārtt</is>. 2. fgg.'),
  ('{%135 Fusss.,81 Reiter,27 Wagen und 27 Eleph.%}',
   '{%135 <ab n="Fusssoldaten">Fusss.</ab>, 81 Reiter, 27 Wagen und 27 <ab n="Elephanten">Eleph.</ab>%}'),
  ('Uneig:', '<ab>Uneig.</ab>:'),
  ('{#guhya#} 🞄(<ls>z. B. MED. j. 18.</ls>',
   '{#guhya#} (<ab>z. B.</ab> <ls>MED. j. 18</ls>.'),
  ('von B. habend',
   'von <ab n="Bester">B.</ab> habend'),
  ('<ls>Z. d. d. m. G. 6,3, N. 3. N.</ls>',
   '<ls>Z. d. d. m. G. 6,3, N. 3</ls>. <ab>N.</ab>'),
  ('in der <ab>Einl.</ab> <ab>S.</ab> 5.',
   'in der <ls>Einl. S. 5</ls>.'),
  ('<ab>Einl.</ab> zur 1sten Ausgabe des <ab>Wörterb.</ab> XXXI.',
   '<ls>Einl. zur 1sten Ausgabe des Wörterb. XXXI.</ls>'),
  ('keine Veranlassung <ab>da.</ab>',
   'keine Veranlassung da.'),
  ('<ls>TS.</ls> <ab>S.</ab> 357, ult.',
   '<ls>TS. S. 357, ult.</ls>'),
  ('<ab>S.</ab> {%auf%}',
   '<is n="Sarasvatī">S.</is> {%auf%}'),
  ('</ls> (<ab>p.</ab> 139).',
   ' (p. 139)</ls>.'),
  ('<ls>MIKLOSICH</ls> (die Wurzeln des Altslovenischen, <ab>S.</ab> 21)',
   '<ls>MIKLOSICH (die Wurzeln des Altslovenischen, S. 21)</ls>'),
  ('<ab>Th.</ab> I, <ab>S.</ab> 820.',
   '<ls>Th. I, S. 820</ls>.'),
  ('<ls>MBH. 3,11039</ls> (<ab>S.</ab> 570).',
   '<ls>MBH. 3,11039 (S. 570).</ls>'),
  ('<ls>BENFEY</ls>, Glossar <ab>z.</ab> <ls>SV. S. 65.</ls>',
   '<ls>BENFEY, Glossar z. SV. S. 65</ls>.'),
  ('in der praef. zu den Radd. III. <ab>fg.</ab>',
   'in der <ls>praef. zu den Radd. III. fg.</ls>'),
  ('praef. zu den Radd. <ab>S.</ab> v.',
   '<ls>praef. zu den Radd. S. v.</ls>'),
  ('{%steckt in dem Feuer, ist enthalten in <ab>d.</ab> F.%}',
   '{%steckt in dem Feuer, ist enthalten in <ab n="dem Feuer">d. F.</ab>%}'),
  ('{%früher im Besitz des <ab>D.</ab> gewesen%}',
   '{%früher im Besitz des <is n="Devadatta">D.</is> gewesen%}'),
  ('<ls>KAUŚ. 44. masc.</ls>',
   '<ls>KAUŚ. 44</ls>. <ab>masc.</ab>'),
  ('(<ab>vgl.</ab> <ab>S.</ab> 515)',
   '(<ab>vgl.</ab> <ab n="Seite">S.</ab> 515)'),
  ('wo TDT <ab>st.</ab> TDI zu lesen ist',
   'wo <ab n="Trochee-Dactyl-Trochee">TDT</ab> <ab>st.</ab> <ab n="Trochee-Dactyl-Iamb">TDI</ab> zu lesen ist'),
  ('<ls>KĀTY. ŚR. 3,4</ls> (<ab>S.</ab> 261,8)',
   '<ls>KĀTY. ŚR. 3,4 (S. 261,8)</ls>'),
  ('(<ab n="lies">l.</ab> {#calanaka#})',
   '(<ab n="lectio">l.</ab> {#calanaka#})'),
  ('{%Piper Chaba <ab>W.</ab> Hunt.%}',
   '{%Piper Chaba W. Hunt.%}'),
  ('<ab>Padap.</ab>', '<is n="Padapāṭha">Padap.</is>'),
  ('<ls>ROTH</ls>, <ab>Erll.</ab> zu <ab>d. St.</ab>',
   '<ls>ROTH, Erll. zu d. St.</ls>'),
  ('(<ab>vgl.</ab> 🞄<ls>MBH. 3,11706</ls>, <ab>S.</ab> 572)',
   '(<ab>vgl.</ab> <ls>MBH. 3,11706, S. 572</ls>)'),  # 23%
  #('<ls>MBH. 3,11076</ls> (<ab>S.</ab> 572',
  # '<ls>MBH. 3,11076</ls> (<ls>S. 572</ls>'),
  ('(<ab>S.</ab> 572; <ab>vgl.</ab> <ls>BHĀG. P. 9,16,3</ls>)',
   '(<ls>S. 572</ls>; <ab>vgl.</ab> <ls>BHĀG. P. 9,16,3</ls>)'),
  ('<ab>u.</ab> <ab n="dem">d.</ab> <ab>folg.</ab> <ab>Art.</ab>',
   '<ab>u. d.</ab> <ab>folg.</ab> <ab>Art.</ab>'),
  ('</ls> (<ab>S.</ab> 572).',
   ' (S. 572)</ls>.'),  #23
  ('im J. 1484 <lex>n.</lex> <ls>Chr.</ls>',
   'im <ab n="Jahr">J.</ab> 1484 <ab>n. Chr.</ab>'),
  (' vgl. {#', ' <ab>vgl.</ab> {#'),
  ('<ls>MBH. 12,12864</ls> (<ab>S.</ab> 818, ult.)',
   '<ls>MBH. 12,12864 (S. 818, ult.)</ls>'),
  ('{%Clypea hernandifolia <ab>W.</ab> und A.%}',
   '{%Clypea hernandifolia W. und A.%}'),
  (' <ab>d.</ab> spät.',
   ' <ab n="der">d.</ab> <ab n="spätern">spät.</ab>'),
  ('</ls> (<ab>S.</ab> 571).',
   ' (S. 571)</ls>.'),
  ('{%die M. liebend%} oder {%von den M. zu lieben%}',
   '{%die <ab n="Menschen">M.</ab> liebend%} oder {%von den <ab n="Menschen">M.</ab> zu lieben%}'),
  ('{%zum vorangegangenen Leben gehörig. im v. L. vollbracht%}',
   '{%zum vorangegangenen Leben gehörig, im <ab n="vorangegangenen Leben">v. L.</ab> vollbracht%}'),
  ('<ab>vgl.</ab> <ab>S.</ab> 514. 515.',
   '<ab>vgl.</ab> <ab n=Seiten">S.</ab> 514. 515.'),
  (' überh.', ' <ab>überh.</ab>'), # 11
  ('<ab>N.</ab> 🞄[Page3-0069] 🞄pr.',
   '<ab>N. pr.</ab> 🞄[Page3-0069] 🞄'),
  ('<ls n="YĀJÑ.">2,206.</ls> <ab>St.</ab>',
   '<ls n="YĀJÑ.">2,206. St.</ls>'),
  ('<ls>P.</ls> 🞄(Bd. II, <ab>S.</ab> 462).',
   '<ls>P. (Bd. II, S. 462)</ls>.'),
  ('in <ab>d.</ab> alt.',
   'in <ab n="der">d.</ab> <ab n="älteren">ält.</ab>'),
  ('{%wir stehen nicht mit <ab>D.</ab> im Bunde%}',
   '{%wir stehen nicht mit <ab n="Dämonen">D.</ab> im Bunde%}'),
  (' nom ag. ',
   ' <ab>nom. ag.</ab>' ),
  ('{%lerne%} <ab>S.</ab> {%kennen%} ',
   '{%lerne%} <is n="Sūcīmukhaṃ">S.</is> {%kennen%} '),
  ('<div n="1">— 5) <ab>u.</ab>',
   '<div n="1">— 5) <lex>n.</lex>'),
  ('<ls>KĀTY. ŚR. 4,5</ls> (<ab>S.</ab> 341).',
   '<ls>KĀTY. ŚR. 4,5 (S. 341)</ls>.'),
  ('Feronia elephantum <ab>Corr.</ab>', 'Feronia elephantum Corr.'),
  ('<ab>p.</ab> 509, ult. 518,14.',
   '<ls n="">p. 509, ult. 518,14</ls>.'),
  ('<ls>LIA. I, Anh.</ls> xx. <ab>fg.</ab>',
   '<ls>LIA. I, Anh. xx. fg.</ls>'),

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
