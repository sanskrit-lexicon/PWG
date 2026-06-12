""" change_0j_0k.py
 
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
  # 06-09-2026.
  # 63%
 
  #('', 
  # ''),

  ('<ls>ebend.</ls> 74. <ab>fgg.</ab>',
   '<ls>ebend. 74. fgg.</ls>'),
  ('T. und <ab>N.</ab>',
   '<ab n="Tag">T.</ab> und <ab n="Nacht">N.</ab>'),

  ('<ab>s. v.</ab> l.',
   '<ab>s.</ab> <ab>v. l.</ab>'),
  ('<ls>KUVALAY. 119,a. Lies 73,3 st. 73,1.</ls>',
   '<ls>KUVALAY. 119,a</ls>. Lies 73,3 <ab>st.</ab> 73,1.'),

  ('<ab>S.</ab> 261 (I,6)',
   '<ls>S. 261 (I, 6)</ls>'),
  ('{%das Lehrbuch der L., das%}',
   '{%das Lehrbuch der <ab n="Logik">L.</ab>, das%}'),

  ('<ls>ŚKDR. Suppl.</ls> <ab>S.</ab> 592',
   '<ls>ŚKDR. Suppl. S. 592</ls>'),
  ('(in übertr. Bed.)',
   '(in <ab>übertr.</ab> <ab>Bed.</ab>)'),

  ('<ab>u.</ab> <ab>s.</ab>',
   '<ab n="und so">u. s.</ab>'),
  ('{%das Sichbeziehen auf, das Hindeuten <ab>auf.</ab>%}',
   '{%das Sichbeziehen auf, das Hindeuten auf%}'),

  ('{#mfnmaru#} 🞄<ab>a. a. O.</ab>',
   '{#mfnmaru#} <ls>a. a. O.</ls>'),
  ('{#˚darSana#} 61. <ab>fgg.</ab>',
   '{#˚darSana#} <ls n="SARVADARŚANAS. 73,">61. fgg.</ls>'),

  ('🞄<ls>BHĀG. P. 10,42,4.</ls> <ab>Z.</ab> 4.',
   '<ls>BHĀG. P. 10,42,4. Z. 4</ls>.'),
  ('Theil 🞄3, <ab>S.</ab> 358).',
   'Theil <ls n="Spr.">3, S. 358</ls>).'),

  ('<ls>SV. <is>Daś</is>. 6,2</ls> (Tüb. <ab>Hdschr.</ab>).',
   '<ls>SV. Daś. 6,2 (Tüb. Hdschr.)</ls>.'),
  ('🞄<ab>Z.</ab> 2 lies 6 st.b.',
   '<ab>Z.</ab> 2 lies 6 <ab>st.</ab> b.'),
  # 64%
  ('<ls>ṚV.</ls> I, <ab>S.</ab> 43, <ab>Z.</ab> 4 <ab>v. u.</ab>',
   '<ls>ṚV. I, S. 43, Z. 4 v. u.</ls>'),
  ('🞄<ab>S.</ab> 100 richtig',
   '<ab n="Seite">S.</ab> 100 richtig'),

  ('🞄<ls>GILDEMEISTER</ls>\'<ab>S.</ab>',
   '<ls>GILDEMEISTER</ls>ʼs.'),
  ('<ls>SŪRYAS.</ls> <ab>S.</ab> 55,4.',
   '<ls>SŪRYAS. S. 55,4</ls>.'),

  ('<ab>vgl.</ab> 🞄104, 26. <ab>fgg.</ab>',
   '<ab>vgl.</ab> <ls n="KATHĀS.">104,26. fgg.</ls>'),
  ('das Reich der Ph.',
   'das Reich der <ab n="Phantasie">Ph.</ab>'),

  ('<ls>SV.</ls> <ab>S.</ab> 273 und Vorrede <ab>S.</ab> VII, <ab>Anm.</ab> 1.',
   '<ls>SV. S. 273</ls> und <ls>Vorrede S. VII, Anm. 1</ls>.'),
  ('{%von der M. gethan%}',
   '{%von der <ab n="Mutter">M.</ab> gethan%}'),

  ('<ab>ed.</ab> 🞄<ls>GORR.</ls>',
   '<ls>ed. GORR.</ls>'),
  ('{%e. <ab>Z.</ab> darstellend%}',
   '<ab n="einen Ziegenbock">e. Z.</ab> {%darstellend%}'),

  ('<ab>N.</ab> 🞄[Page6-0018] 🞄pr.',
   '<ab>N. pr.</ab> 🞄[Page6-0018] 🞄'),
  (' loc. ', ' <ab>loc.</ab> '),

  ('beliebigen L.',
   'beliebigen <ab n="Lebensstadium">L.</ab>'),
  # 65%
  ('(<ab>S.</ab> 571, {#˚yozam#} <ls>ed. Calc.</ls>)',
   '(<ls>S. 571</ls>, {#˚yozam#} <ls>ed. Calc.</ls>)'),

  ('entsprechenden H.',
   'entsprechenden <ab n="Himmelsgegenden">H.</ab>'),
  ('<ab>ed.</ab> 🞄<ls>SCHL.</ls>',
   '<ls>ed. SCHL.</ls>'),

  ('<ls n="R. 5,">12,41.</ls> Bd. IV, <ab>S.</ab> XVIII.',
   '<ls n="R. 5,">12,41. Bd. IV, S. XVIII.</ls>'),
  ('Wurzeln des Altslov. <ab>S.</ab> 15',
   '<ls>Wurzeln des Altslov. S. 15</ls>'),

  ('<ls>MIKLOSICH, <ab>Vgl.</ab> Gr. III, S. VIII</ls>',
   '<ls>MIKLOSICH, Vgl. Gr. III, S. VIII</ls>'),
  ('<ab>S.</ab> 358. <ab>Z.</ab> 13. <ab>fg.</ab>',
   '<ls n="">S. 358. Z. 13. fg.</ls>'),

  ('<ls>AV. PRĀT.</ls> <ab>S.</ab> 63.',
   '<ls>AV. PRĀT. S. 63</ls>.'),
  ('<ab>Einl.</ab> <ab>S.</ab> VII.',
   '<ls>Einl. S. VII.</ls>'),

  ('<ab>vgl.</ab> <ab>S.</ab> 36.',
   '<ab>vgl.</ab> <ab n="Seite">S.</ab> 36.'),
  ('🞄<ls>Spr. 1926</ls>, <ab>v. l.</ab>',
   '<ls>Spr. 1926, l. 1</ls>.'),
  # 66%
  ('<ls>ŚĀK. 18,22</ls> (<ls>v. l. praes.). 104,22</ls>',
   '<ls>ŚĀK. 18,22</ls> (<ab>v. l.</ab> <ab>praes.</ab>). <ls n="ŚĀK.">104,22</ls>'),
  ('<ls>Verz. d. Oxf. H. 342,b,21.</ls> 🞄[Page6-0144] 🞄<ab>fgg.</ab>',
   '<ls>Verz. d. Oxf. H. 342,b,21. fgg.</ls> 🞄[Page6-0144] 🞄'),
  ('<ls>ROTH</ls>, Ueber den Mythus von den Menschengeschlechtern, 🞄<ab>S.</ab> 24. <ab>fgg.</ab>',
   '<ls>ROTH, Ueber den Mythus von den Menschengeschlechtern, S. 24. fgg.</ls>'),
  ('(urspr.', '(<ab>urspr.</ab>'),
  ('<ls>RĀJA-TAR.</ls> <ab>S.</ab> 2. 22. 135. 212.',
   '<ls>RĀJA-TAR. S. 2. 22. 135. 212</ls>.'),
  ('<ab>ed.</ab> <ls>LOIS.</ls>',
   '<ls>ed. LOIS.</ls>'),
  ('<ls>HOEFER</ls>, Vom Infinitiv 🞄<ab>S.</ab> 87. 121',
   '<ls>HOEFER, Vom Infinitiv S. 87. 121</ls>'),
  ('<ls n="VOP.">6,9</ls> <ab>Anf.</ab>',
   '<ls n="VOP.">30. 6,9 Anf.</ls>'),
  ('{%schon als junge Frau R. h.%}',
   '{%schon als junge Frau <ab n="Runzeln habend">R. h.</ab>%}'),
  ('wobei ein O. sich ',
   'wobei ein <ab n="Opferpfosten">O.</ab> sich'),
  ('Note dazu 🞄<ab>S.</ab> 432',
   'Note dazu <ab n="Seite">S.</ab> 432'),
  ('<ls>ṚV.</ls> I, ? <ab>S.</ab> 72,16',
   '<ls>ṚV. I, ? S. 72,16</ls>'),
  ('(<ls>v. l. masc.).</ls>',
   '(<ab>v. l.</ab> <ab>masc.</ab>)'),
  ('<ab>S.</ab> 95,10.',
   '<ab n="Seite">S.</ab> 95,10.'),
  ('<ab>ed.</ab> <ls>BURN.</ls>',
   '<ls>ed. BURN.</ls>'),
  # 67%
  ('<ls>ṚT. 1,5, v. l. 6,13.</ls>',
   '<ls>ṚT. 1,5</ls>, <ab>v. l.</ab> <ls n="">6,13</ls>.'),
  ('<ls>SĀY. N.</ls>',
   '<ls>SĀY.</ls> <ab>N.</ab>'),
  ('{%<ab>Weg.</ab>%}',
   '{%Weg%}.'),
  ('<ab>ed.</ab> <ls>JOHNS.',
   '<ls>ed. JOHNS.'),
  ('<ls>WILSON</ls> in der <ab>Einl.</ab> zur 1ten <ab>Ausg.</ab> des Wörterbuchs 🞄<ab>S.</ab> XXV.',
   '<ls>WILSON in der Einl. zur 1ten Ausg. des Wörterbuchs S. XXV.</ls>'),
  ('<ls>VYUTP. 91.</ls> <ab>Spr.</ab> I, IX.',
   '<ls>VYUTP. 91</ls>. <ls>Spr. I, IX.</ls>'),
  ('ein mit dem Q.',
   'ein mit dem <ab n="Quecksilbers">Q.</ab>'),
  ('<ls>Verz. d. B. H. No. 929</ls> (<ab>S.</ab> 278, Śl. 48). 958. 966.',
   '<ls>Verz. d. B. H. No. 929 (S. 278, Śl. 48). 958. 966</ls>.'),
  ('{%Bewohner der Unt.%}',
   '{%Bewohner der <ab n="Unterwelt">Unt.</ab>%}'),
  ('{%ein Kapitel über <ab>d.</ab> <lex>m.</lex>%}',
   '{%ein Kapitel über <ab n="der musikalischen">d. m.</ab>%}'),
  ('<ls>VOP. 3,77.</ls>  <ab>fg.</ab> <ls n="VOP. 3,">134.</ls>',
   '<ls>VOP. 3,77. fg. 134</ls>.'),
  # 68%
  ('<ab>S.</ab> 235,a.',
   '<ab n="Seite">S.</ab> 235,a.'),
  ('{%eine Gruppe von Nel. <ab>spec.</ab>%}',
   '{%eine Gruppe von%} {%Nel. spec.%}'),
  ('<ls>SV.</ls> <ls>GĀNA</ls> (Tüb. <ab>Hdschr.</ab>)',
   '<ls>SV. GĀNA (Tüb. Hdschr.)</ls>'),
  ('<ls>WILSON</ls> in der <ab>Einl.</ab> zur 1ten <ab>Ausg.</ab> <ab>d.</ab> Wört. XXIII. <ab>fg.</ab>',
   '<ls>WILSON in der Einl. zur 1ten Ausg. d. Wört. XXIII. fg.</ls>'),
  ('🞄<ab>S.</ab> 6. 7.',
   '<ab n="Seiten">S.</ab> 6. 7.'),
  ('<ls>TS.</ls> <ab>Comm.</ab>',
   '<ls>TS. Comm.</ls>'),
  ('<ab>ed.</ab> 🞄[Page6-0360] 🞄Bomb.',
   '<ls>ed. Bomb.</ls> 🞄[Page6-0360] 🞄'),
  ('lithogr. <ab>Ausg.</ab>',
   '<ls>lithogr. Ausg.</ls>'),
  ('<ab>N.</ab> 🞄[Page6-0374] 🞄pr.',
   '<ab>N. pr.</ab> 🞄[Page6-0374] 🞄'),
  ('<ab>ed.</ab> 🞄<ls>JOHNS. 2090</ls>',
   '<ls>ed. JOHNS. 2090</ls>'),
  ('<ls>R. 2,55,21</ls> <ab>ed.</ab> Seramp.',
   '<ls>R. 2,55,21 ed. Seramp.</ls>'),
  (' <ab>eben.</ab> ',
   ' eben. '),
  ('in v. 7 annehmen, dessen letzter <is>Pāda</is> mit v. 8',
   'in <ab n="vers">v.</ab> 7 annehmen, dessen letzter <is>Pāda</is> mit <ab n="vers">v.</ab> 8'),
  ('{%durch%} <ab>S.</ab>',
   '{%durch%} <ab n="Süd">S.</ab>'),
  ('(<ab>S.</ab> 570, <ab>med.</ab>)',
   '(<ls>S. 570</ls>, <ab>med.</ab>)'),
  ('(<ab>vgl.</ab> 🞄<ls>STENZLER</ls> zu <ls>ĀŚV. GṚHY.</ls> <ab>S.</ab> 69)',
   '(<ab>vgl.</ab> <ls>STENZLER</ls> zu <ls>ĀŚV. GṚHY. S. 69</ls>)'),
  # 69%
  ('<ab>ed.</ab> 🞄<ls>LOIS.</ls>',
   '<ls>ed. LOIS.</ls>'),
  ('so v. <ab>d.</ab>',
   '<ab>v. a.</ab>'),
  ('Species von Ag.',
   'Species von <ab n="Agallochum">Ag.</ab>'),
  ('<ab>ed.</ab> (Bomb.).',
   '<ls>ed. (Bomb.)</ls>.'),
  ('({#vilapizyataH#} <ab>partic.</ab> füt.)',
   '({#vilapizyataH#} <ab>partic.</ab> <ab>fut.</ab>)'),
  
  # 70%
  
  ('{%sich niederlassen <ab>auf.</ab>%}',
   '{%sich niederlassen auf%}.'),
  ('<lex>n.</lex> des 15ten <ab>astr.</ab>',
   '<ab>N.</ab> des 15ten <ab>astr.</ab>'),
  ('Monatsber. <ab>d.</ab> <ab>Berl.</ab> 🞄<ls>Ak. d. Ww. 1868, S. 100.</ls>',
   '<ls>Monatsber. d. Berl. Ak. d. Ww. 1868, S. 100</ls>.'),
  ('<ls>VET. in LA. (III) 19,3. Inschr.</ls>',
   '<ls>VET. in LA. (III) 19,3</ls>. <ab>Inschr.</ab>'),
  ('<ls>ERNST KUHN</ls>, <ls>KACCĀYANAPPAKARAṆAB</ls> Specimen <ab>S.</ab> 20.',
   '<ls>ERNST KUHN, KACCĀYANAPPAKARAṆAE Specimen S. 20</ls>.'),
  ('einem El. gleichend',
   'einem <ab n="Elephanten">El.</ab> gleichend'),
  ('<ab>ed.</ab> Cow.',
   '<ls>ed. Cow.</ls>'),
  ('(<ls>HALĀY.</ls> <ab>Ind.</ab> <ab>u.</ab> {#kawu#})',
   '(<ls>HALĀY. Ind.</ls> <ab>u.</ab> {#kawu#})'),
  ('<ls>NYĀYAS. 1,1,1</ls> 🞄(<ab>S.</ab> 6, <ab>Z.</ab> 2).',
   '<ls>NYĀYAS. 1,1,1 (S. 6, Z. 2)</ls>.'),
  ('<ls>Verz. d. Oxf. H. 311,a,1</ls> 🞄[Page6-0592] 🞄<ab>v. u.</ab>',
   '<ls>Verz. d. Oxf. H. 311,a,1 v. u.</ls> 🞄[Page6-0592] 🞄'),
  
  # 71%
  
  ('meisten Comm.',
   'meisten <ab>Comm.</ab>'),
  ('<ab>partic.</ab> füt.',
   '<ab>partic.</ab> <ab>fut.</ab>'),
  ('<F>*⁾ dat.',
   '<F>*⁾ <ab>dat.</ab>'),
  ('<ls>SCHMIDT</ls> und <ls>BÖHTLINGK</ls>, <ab>Verz.</ab> der tib. <ab>Hdschrr.</ab> 6.',
   '<ls>SCHMIDT und BÖHTLINGK, Verz. der tib. Hdschrr. 6</ls>.'),
  ('({#vaka#} <ab>ed.</ab> 🞄<ls>BURN. 23). 10,66,9.</ls>',
   '({#vaka#} <ls>ed. BURN. 23</ls>). <ls n="BHĀG. P. ed. Bomb.">10,66,9</ls>.'),
  ('(<ab>acc.</ab> <ab>st.</ab> loc).',
   '(<ab>acc.</ab> <ab>st.</ab> <ab>loc.</ab>)'),
  ('<ab>S.</ab> 136. <ab>fg.</ab>',
   '<ab n="Seite">S.</ab> 136. <ab>fg.</ab>'),
  ('{%einbest. Metrum: 4 Mal%}',
   '{%ein <ab>best.</ab> Metrum: 4 Mal%}'),
  ('{%Terminalia iomentosa <ab>W.</ab> und A.%}',
   '{%Terminalia iomentosa W. und A.%}'),
  ('({#vaMSESca#} <ab>ed.</ab> SCHL. 8)',
   '({#vaMSESca#} <ls n="R.">ed. SCHL. 8</ls>)'),
  ('benutzten Hdschrr. und',
   'benutzten <ab>Hdschrr.</ab> und'),

  # 72%
  
  ('<ls>Verz. d. Oxf. H. 260,a, N.</ls> <ab>Z.</ab> 3.',
   '<ls>Verz. d. Oxf. H. 260,a, N. Z. 3.</ls>'),
  ('desselben 🞄<ab>S.</ab> VIII.',
   'desselben <ab n="Seite">S.</ab> VIII.'),
  ('{%Polanisia icosandra <ab>W.</ab> et. A.%}',
   '{%Polanisia icosandra W. et. A.%}'),
  ('<ls>AIT. UP.</ls> <ab>S.</ab> 184.',
   '<ls>AIT. UP. S. 184</ls>.'),
  ('<ls n="Verz. d. Oxf. H.">211,a,8</ls> und 2 <ab>v. u.</ab>',
   '<ls n="Verz. d. Oxf. H.">211,a,8 und 2 v. u.</ls>'),
  ('in comp. mit dem Orte',
   'in <ab>comp.</ab> mit dem Orte'),

  # 73%
  
  ('<ls>ĀPAST. beim Schol.</ls>',
   '<ls>ĀPAST.</ls> beim <ab>Schol.</ab>'),
  ('<ls>PALLAS</ls>, Sammlung hist. Nachr. über die mongolischen Völkerschaften II, <ab>Pl.</ab> IX, Fig. 22',
   '<ls>PALLAS, Sammlung hist. Nachr. über die mongolischen Völkerschaften II, Pl. IX, Fig. 22</ls>'),
  ('<ls>PRAB. 12,1. Inschr.</ls>',
   '<ls>PRAB. 12,1</ls>. <ab>Inschr.</ab>'),
  ('<ls>ŚĀNT. 2,2</ls>, <ab>Comm.</ab>',
   '<ls>ŚĀNT. 2,2, Comm.</ls>'),
  ('<ls>SCHÜTZ\'S</ls> <ab>Uebers.</ab>',
   '<ls>SCHÜTZʼs Uebers.</ls>'),
  ('{%über den%} <ab>p.</ab> <ab>d. h.</ab>',
   '{%über den%} <is n="paryāya">p.</is> <ab>d. h.</ab>'),
  ('<ab>ed.</ab> SCHL. <ls n="HIT.">127,11</ls>',
   '<ls n="HIT.">ed. SCHL. 127,11</ls>'),
  ('<ls>TRIK.</ls> <ab>Ind.</ab>',
   '<ls>TRIK. Ind.</ls>'),

  # 74%
  
  #('{#kriyA˚#} <ls>AV. PRĀT.</ls> <ab>S.</ab> 261 (II,1).',
  # '{#kriyA˚#} <ls>AV. PRĀT. S. 261 (II, 1)</ls>.'),
  ('<ls>AV. PRĀT.</ls> <ab>S.</ab> 261 (II,1).',
   '<ls>AV. PRĀT. S. 261 (II, 1)</ls>.'),
  ('<ls>BHAR. beim Schol.</ls>',
   '<ls>BHAR.</ls> beim <ab>Schol.</ab>'),
  ('verbunden%} u. s. w.',
   'verbunden%} <ab>u. s. w.</ab>'),
  ('{#rAmaRA#} <ab>ed.</ab> <ls>SCHL.</ls>',
   '{#rAmaRA#} <ls>ed. SCHL.</ls>'),
  ('<ls>GAṆIT.</ls> 🞄<ls>MADHYAMĀDH. 6</ls>, <ab>Comm.</ab>',
   '<ls>GAṆIT. MADHYAMĀDH. 6, Comm.</ls>'),
  ('🞄<span>N.</span> {%eines zu den%}',
   '<ab>N.</ab> {%eines zu den%}'),
  ('<ls>SV.</ls> <ls>GĀNA</ls> Tüb. <ab>Hdschr.</ab>',
   '<ls>SV. GĀNA Tüb. Hdschr.</ls>'),
  ('{%gewiss, gerade, <ab>eben.</ab>%}',
   '{%gewiss, gerade, eben%}.'),

  # 75%
  
  ('<ls>SIDDHĀNTAŚIR.</ls> <ab>ed.</ab> <ls>BĀPŪD. S. 54.</ls>',
   '<ls>SIDDHĀNTAŚIR. ed. BĀPŪD. S. 54</ls>.'),
  ('<ls>HALL</ls> in der <ab>Einl.</ab> zu <ls>VĀSAVAD. 50.</ls>',
   '<ls>HALL in der Einl. zu VĀSAVAD. 50</ls>.'),
  ('<ls>M. 11,59. fgg.</ls> (<ab>S.</ab> 358, <ab>Z.</ab> 15).',
   '<ls>M. 11,59. fgg. (S. 358, Z. 15)</ls>.'),
  ('<ls>GOLĀDHY. 6,16</ls>, <ab>Comm.</ab>',
   '<ls>GOLĀDHY. 6,16, Comm.</ls>'),
  ('Flüssigem 🞄(<ls>z. B. <is>Soma</is>)</ls> <ls>Ind. St. 10,381.</ls>',
   'Flüssigem (<ab>z. B.</ab> <is>Soma</is>) <ls>Ind. St. 10,381</ls>.'),

  ('🞄<ls>VS. 5,9</ls> <ab>s.</ab>',
   '<ls>VS. 5,9</ls> <ab>S.</ab>'),
  ('<ab>z. B.</ab> <ab>S.</ab> 5,2,10,3.',
   '<ab>z. B.</ab> <ls>TS. 5,2,10,3</ls>.'),

  # 76%
  
  ('<ab>ed.</ab> <ls>Lois.</ls>',
   '<ls>ed. Lois.</ls>'),
  ('(<ab>vgl.</ab> <ab>u.</ab> 1. {#viD)#} . 🞄<span>N.</span>',
   '(<ab>vgl.</ab> <ab>u.</ab> <hom>1.</hom> {#viD#}). <ab>N.</ab>'),
  ('<ab>S.</ab> 23, <ab>Z.</ab> 5. {#SItopacAra˚#} 🞄<ab>Z.</ab> 3.',
   '<ab n="Seite">S.</ab> 23, <ab>Z.</ab> 5. {#SItopacAra˚#} <ab>Z.</ab> 3.'),
  ('(excl.)', '(<ab>excl.</ab>)'),
  ('<ls>ŚĀNT. 3,7</ls>, <ab>Comm.</ab>',
   '<ls>ŚĀNT. 3,7, Comm.</ls>'),
  ('<ab>vgl.</ab> u {#balAka#}',
   '<ab>vgl.</ab> <ab>u.</ab> {#balAka#}'),
  ('<ls n="P. 1,">2,44</ls>, <ab>Comm.</ab>',
   '<ls n="P. 1,">2,44, Comm.</ls>'),
  ('<ls>VOP. 2,5</ls>, <ab>Comm.</ab>',
   '<ls>VOP. 2,5, Comm.</ls>'),
  ('<ls>KAP. 1,49. Inschr.</ls>',
   '<ls>KAP. 1,49</ls>. <ab>Inschr.</ab>'),
  ('{#viBraMSa#} <ab>D.</ab>',
   '{#viBraMSa#} <ls n="Devarāja">D.</ls>'),
  ('<ls>GAṆIT.</ls> 🞄<ls>GRAHACCHĀYĀDH. 2</ls>, <ab>Comm.</ab> <ls>GOLĀDHY.</ls> <ls>GOLAB. 20. 13, Comm.</ls>',
   '<ls>GAṆIT. GRAHACCHĀYĀDH. 2, Comm.</ls> <ls>GOLĀDHY. GOLAB. 20. 13, Comm.</ls>'),
  ('pr. <ls n="KATHĀS.">(II) 196, v. l. 446</ls>',
   '<ls>Spr. (II) 196</ls>, <ab>v. l.</ab> <ls n="">446</ls>'),

  # 77%
  
  ('🞄<ls>GAṆIT.</ls> 🞄<ls>BHAGAṆĀDH. 13</ls>, <ab>Comm.</ab>',
   '<ls>GAṆIT. BHAGAṆĀDH. 13, Comm.</ls>'),
  ('</ls>, <ab>Comm.</ab>',
   ', Comm.</ls>'), #32
  ('<ls>Verz. d. B. H. No. 933. 935</ls> (<ab>S.</ab> 284. XXIII). 958. 963.',
   '<ls>Verz. d. B. H. No. 933. 935 (S. 284. XXIII). 958. 963</ls>.'),
  ('<ls>CHĀND. UP. S. 1. Inschr.</ls>',
   '<ls>CHĀND. UP. S. 1</ls>. <ab>Inschr.</ab>'),
  ('<ab>ed.</ab> Pol.',
   '<ls>ed. Pol.</ls>'),
  ('<ab>Buddh.</ab> <ab>Trigl.</ab> <ls>8,b.</ls>',
   '<ls>Buddh. Trigl. 8,b</ls>.'),
  ('(nom).',
   '(<ab>nom.</ab>)'),
  ('gerichtet%} Comm. zu',
   'gerichtet%} <ab>Comm.</ab> zu'),

  # 78%
  
  ('<ls>BRAHMAS.</ls> <ab>S.</ab> 96.',
   '<ls>BRAHMAS. S. 96</ls>.'),
  ('<ls>ŚĀṄKH. BR. 17,3. masc.</ls>',
   '<ls>ŚĀṄKH. BR. 17,3</ls>. <ab>masc.</ab>'),
  (' u. s. w.:',
   ' <ab>u. s. w.</ab>:'),
  ('<ab>Einl.</ab> zum <ls>ṚV.</ls>',
   '<ls>Einl. zum ṚV.</ls>'),
  ('<ls>HĀLA</ls> <ab>S.</ab> 259.',
   '<ls>HĀLA S. 259</ls>.'),
  ('<ab>S.</ab> 33. <ab>fg.</ab>',
   '<ab n="Seite">S.</ab> 33. <ab>fg.</ab>'),

  # 79%
  
  ('<ab>D.</ab> zu <ls>NIR. 4,18</ls>',
   '<ls n="Durgasiṃha">D.</ls> zu <ls>NIR. 4,18</ls>'),
  ('<ab>vgl.</ab> <ab>S.</ab> 28.',
   '<ab>vgl.</ab> <ab n="Seite">S.</ab> 28.'),
  ('(auch {#sve gfhe#} nach <ab>D.</ab>)',
   '(auch {#sve gfhe#} nach <ls n="Devarāja">D.</ls>)'),
  ('Commentar zu Buch XII. <ab>fgg.</ab>',
   'Commentar zu <ls>Buch XII. fgg.</ls>'),
  ('<ls>MĀṆḌ. UP.</ls> <ab>S.</ab> 402. 406. 411. <ab>fgg.</ab>',
   '<ls>MĀṆḌ. UP. S. 402. 406. 411. fgg.</ls>'),
  ('<ls>VP. 213</ls>, 🞄<lex>n.</lex> des 27ten',
   '<ls>VP. 213</ls>, <ab>N.</ab> des 27ten'),
  ('{%Terminalia Arjuna <ab>W.</ab> und A.%}',
   '{%Terminalia Arjuna W. und A.%}'),
  ('<ab>u.</ab> 🞄[Page6-1419] 🞄<ab>s.</ab> <ab>w.</ab>',
   '<ab>u. s. w.</ab> 🞄[Page6-1419] 🞄'),

  # 80%
  
  ('<ls>BṚH.</ls> <ls>AH.</ls> <ls>UP.</ls> <ab>S.</ab> 30. 114. 252.',
   '<ls>BṚH. ĀR. UP. S. 30. 114. 252</ls>.'),
  ('<ab>S.</ab> 6.',
   '<ab n="Seite">S.</ab> 6.'),
  (' u. s. w.)', ' <ab>u. s. w.</ab>)'),

  # 81%
  
  ('<ls>CAREY</ls> (<ab>Gramm.</ab> 🞄<ab>S.</ab> 20)',
   '<ls>CAREY (Gramm. S. 20)</ls>'),
  ('<ls>SMARADĪPIKĀ</ls> (Tüb. <ab>Hdschr.</ab>).',
   '<ls>SMARADĪPIKĀ (Tüb. Hdschr.)</ls>.'),
  ('🞄<ls>WILSON</ls>, Dict. 1te <ab>Aufl.</ab> XXXVIII.',
   '<ls>WILSON, Dict. 1te Aufl. XXXVIII.</ls>'),
  ('<ls>VS.</ls> <ab>S.</ab> {#58#}.',
   '<ls>VS. S. {#58#}.</ls> '),
  ('(<ab>vgl.</ab> {#Sambara#}) 🞄<ls>TBR.</ls> <ab>Comm.</ab>',
   '(<ab>vgl.</ab> {#Sambara#}) <ls>TBR. Comm.</ls>'),
  ('(nach <ab>D.</ab> {#ASrayamAtmano dAru udakamanyadvA)#}',
   '(nach <ls n="Durgasiṃha">D.</ls> {#ASrayamAtmano dAru udakamanyadvA#})'),
  ('{#prasTa#} nach 🞄<ls>TS. Comm.</ls>',
   '{#prasTa#} nach <ls>TS.</ls> <ab>Comm.</ab>'),

  # 82%
  
  ('<ab>D.</ab> = {#atibalavatA muktAm#}',
   '<ls n="Durgasiṃha">D.</ls> = {#atibalavatA muktAm#}'),
  ('🞄<ls>WILSON</ls> (2te <ab>Aufl.</ab>)',
   '<ls>WILSON (2te Aufl.)</ls>'),
  ('<ls n="Verz. d. Oxf. H.">169,a,39. fg. b,2</ls> und <ab>N.</ab> 1. <ls n="Verz. d. Oxf. H.">176,b,5.</ls>',
   '<ls n="Verz. d. Oxf. H.">169,a,39. fg. b,2 und N. 1. 176,b,5</ls>.'),
  ('(<ab>vgl.</ab> auch 2te <ab>Aufl.</ab> 🞄<ls n="VP.">2,63, N.).</ls>',
   '(<ab>vgl.</ab> auch <ls n="VP.">2te Aufl. 2,63, N.</ls>)'),
  ('({#SAstravidaH#} <ab>ed.</ab> 🞄<ls>COWELL 130,5</ls>)',
   '({#SAstravidaH#} <ls>ed. COWELL 130,5</ls>)'),
  ('(<ab>vgl.</ab> <ab>Erll.</ab> 🞄<ab>S.</ab> 222)',
   '(<ab>vgl.</ab> <ls>Erll. S. 222</ls>)'),
  ('<ls>MṚCCH.</ls> <ab>Einl.</ab> <ab>S.</ab> v.',
   '<ls>MṚCCH. Einl. S. v.</ls>'),
  ('<ls n="KĀTY. ŚR. 4,2,">40.</ls> <ab>S.</ab> 210,3. 21.',
   '<ls n="KĀTY. ŚR. 4,2,">40. S. 210,3. 21.</ls>'),
  ('{#KaYjanotpAta˚#} 🞄<ab>S.</ab>',
   '{#KaYjanotpAta˚#} <ab n="Seite">S.</ab>'),
  ('<ls n="Verz. d. Oxf. H.">50,b,5.</ls> <ls n="Verz. d. Oxf. H.">100,a,40.</ls> <ls n="Verz. d. Oxf. H.">105,a,11</ls> und <ab>N.</ab> 4',
   '<ls n="Verz. d. Oxf. H.">50,b,5. 100,a,40. 105,a,11 und N. 4</ls>'),
  ('({#SArageravAH#} die Hdschr).',
   '({#SArageravAH#} die <ab>Hdschr.</ab>)'),
  ('(78 nach <ls>Chr.</ls>)',
   '(78 nach <ab>Chr.</ab>)'),
  ('{%Salmalia malabarica <ab>Sch.</ab> und E., Wollbaum%}',
   '{%Salmalia malabarica Sch. und E., Wollbaum%}'),
  ('(so <ab>ed.</ab> Bomb)',
   '(so <ls>ed. Bomb.</ls>)'),
  ('<ab>ed.</ab> 🞄<ls>COWELL 65,8</ls>',
   '<ls>ed. COWELL 65,8</ls>'),
  ('{%Diospyros embryopteris <ab>Pers.</ab>',
   '{%Diospyros embryopteris Pers.'),
  ('(2te <ab>Aufl.</ab> 🞄<ls n="VP.">4,63</ls>)',
   '(<ls n="VP.">2te Aufl. 4,63</ls>)'),

  # 83%
  
  ('<ab>S.</ab> 657, Śl. 31.',
   '<ls>S. 657, Śl. 31</ls>.'),
  ('Comm. zu <ls>KĀVYĀD. 1,56.</ls>',
   '<ab>Comm.</ab> zu <ls>KĀVYĀD. 1,56</ls>.'),
  ('🞄<ls>VEṆĪS.</ls> <lang>lith.</lang> <ab>Ausg.</ab> am Ende.',
   '<ls>VEṆĪS. lith. Ausg.</ls> am Ende.'),
  (' suderl. ', ' <ab>superl.</ab> '),
  ('<ls>KĀṬHOP.</ls> <ab>S.</ab> 73.',
   '<ls>KĀṬHOP. S. 73</ls>.'),
  ('Monatsberr. <ab>d.</ab> k. pr. Ak. <ab>d. Ww.</ab> in Berlin 🞄<ls n="HALL">1868, S. 106. 111.</ls>',
   '<ls>Monatsberr. d. k. pr. Ak. d. Ww. in Berlin 1868, S. 106. 111</ls>.'),
  ('13,114. 209. <ab>fg.</ab> 2422. 2431. 4530.',
   '<ls n="MBH.">13,114.</ls> <ls n="MBH. 13,">209. fg.</ls> <ls n="MBH. 13,">2422.</ls> <ls n="MBH. 13,">2431.</ls> <ls n="MBH. 13,">4530.</ls>'),

  # 84%
  
  ('<ls>DIEZ</ls>, <ab>Etym.</ab> Wört. <ab>d.</ab> romanischen Sprachen',
   '<ls>DIEZ, Etym. Wört. d. romanischen Sprachen</ls>'),
  ('<lang>lith.</lang> <ab>Ausg.</ab> 33,56.',
   '<ls>lith. Ausg. 33,56</ls>.'),
  ('<ab>ed.</ab> 🞄GORR.',
   '<ls>ed. GORR. 26</ls>'),
  ('{%wie ein A.%} oder {%F. herabschiessend%}',
   '{%wie ein <ab n="Adlers">A.</ab>%} oder <ab n="Falken">F.</ab> {%herabschiessend%}'),
  ('Worterklärung, nach <ab>D.</ab>',
   'Worterklärung, nach <ls>D.</ls>'),
  ('die neuere Ausg liest ',
   'die neuere <ab>Ausg.</ab> '),
  ('<ls>ŚĀṄKH. ŚR. 18,24,18. pass.</ls>',
   '<ls>ŚĀṄKH. ŚR. 18,24,18</ls>. <ab>pass.</ab>'),

  # 85%
  
  ('<ab>ed.</ab> 🞄[Page7-0377] 🞄Bomb.).',
   '<ls>ed. Bomb.</ls>). 🞄[Page7-0377] 🞄'),
  ('<ab>nom.</ab> {%ag. der sich an Jmd%}',
   '<ab>nom. ag.</ab> {%der sich an Jmd%}'),
  ('<ab>Anm.</ab> auf 🞄<ab>S.</ab> 4.',
   '<ls>Anm. auf S. 4</ls>.'),
  ('<ab>Comm.</ab> <ab>S.</ab> 5.',
   '<ab>Comm.</ab> <ab n="Seite">S.</ab> 5.'),
  ('<ls>VĀSAVAD.</ls> <ab>Comm.</ab> <ab>S.</ab> 9.',
   '<ls>VĀSAVAD.</ls> <ab>Comm.</ab> <ab n="Seite">S.</ab> 9.'),
  ('{#˚paka#} <ab>ed.</ab> 🞄<ls>TR.</ls>)',
   '{#˚paka#} <ls>ed. TR.</ls>).'),
  (' (med). ',
   ' (<ab>med.</ab>) '),
  ('{%Terminalia Arjuna <ab>W.</ab> et. A.%}',
   '{%Terminalia Arjuna W. et. A.%}'),
  ('(= {#kElAsa#} Comm)',
   '(= {#kElAsa#} <ab>Comm.</ab>)'),
  ('sechsten M.',
   'sechsten <ab n="Mahlzeit">M.</ab>'),
  ('1ten <ab>Aufl.</ab>',
   '1ten Aufl.'),
  ('<ab>ed.</ab> <ls>POL.</ls>)',
   '<ls>ed. POL.</ls>'),

  # 86%
  ('<ab>vgl.</ab> 14, <is>Adhy</is>. 3. <ab>fgg.</ab>',
   '<ab>vgl.</ab> <ls n="MBH.">14, Adhy. 3. fgg.</ls>'),
  
  ('{%einen Vertrag%} a. <ab>s.</ab> <ab>w.</ab>',
   '{%einen Vertrag%} <ab>u. s. w.</ab>'),
  ('<ls n="UTTARARĀMAC. (ed. COWELL)">26,12</ls> (<ab>ed.</ab> COWELL).',
   '<ls n="UTTARARĀMAC.">26,12 (ed. COWELL)</ls>.'),
  ('<ls>TAITT. UP.</ls> <ab>S.</ab> 32.',
   '<ls>TAITT. UP. S. 32</ls>.'),
  ('(<ab>S.</ab> 570; zu schreiben {#vedIsaM˚#})',
   '(<ls>S. 570</ls>; zu schreiben {#vedIsaM˚#})'),
  ('({#˚tama#} superl).',
   '({#˚tama#} <ab>superl.</ab>)'),
  ('R. <ab>S.</ab> 14.',
   '<ls>R. S. 14</ls>.'),
  ('<ls>VARĀH. BṚH. S. 2, S. 3, Z. 1 v. u.</ls> <ab>S.</ab> 6, <ab>Z.</ab> 14.',
   '<ls>VARĀH. BṚH. S. 2, S. 3, Z. 1 v. u. S. 6, Z. 14</ls>.'),
  ('(<ab>vgl.</ab> <ls>KERN</ls> in der Vorrede 21. <ab>fg.</ab>).',
   '(<ab>vgl.</ab> <ls>KERN</ls> in der <ls>Vorrede 21. fg.</ls>).'),
  ('(<ab>instr.</ab> oder im comp. vorangehend)',
   '(<ab>instr.</ab> oder im <ab>comp.</ab> vorangehend)'),
  ('<ls n="KĀTY. ŚR.">Comm. 543,2.</ls>',
   '<ab>Comm.</ab> <ls n="KĀTY. ŚR.">543,2</ls>.'),
  ('<lex>adj.</lex> comp:',
   '<ab>adj. comp.</ab>:'),
  ('<lang>lith.</lang> <ab>Ausg.</ab>',
   '<ls>lith. Ausg.</ls>'),
  ('{%nicht a. <ab>d.</ab> <ab>S.</ab> h.%}',
   '{%nicht <ab n="an der Sinnenwelt hängend">a. d. S. h.</ab>%}'),
  ('({#mOryasaciva#} <ab>ed.</ab> Bomb).',
   '({#mOryasaciva#} <ls>ed. Bomb.</ls>)'),
  ('({#SaraM sfjyaM#} [!] {#jyAyuktaM cakAra#} Comm).',
   '({#SaraM sfjyaM#} [!] {#jyAyuktaM cakAra#} <ab>Comm.</ab>).'),

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
