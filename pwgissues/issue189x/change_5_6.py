""" change_5_6.py
 
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
  # 72% Begin 06-20-2026 
  ( 'Austheilung des%} P. {%Statt%}',
   'Austheilung des%} <is n="Puroḍāśa">P.</is> {%Statt%}'),
  ('{%zu dem Rest des%} Pr.',
   '{%zu dem Rest des%} <is n="Prāyaṇīya">Pr.</is>'),
  ('In Betreff des Bindevocals <ab>s.</ab> <is>Kār.</is>',
   'In Betreff des Bindevocals <ab>s.</ab> <is n="Kārikā">Kār.</is>'),
  ('<ls><is>Kār.</is> 8</ls> aus <ls>SIDDH. K.</ls>',
   '<ls><is n="Kārikā">Kār.</is> 8</ls> aus <ls>SIDDH. K.</ls>'),
  ('{%suchte den%} <is>Vṛ</is>.',
   '{%suchte den%} <is n="Vṛtra">Vṛ.</is>'),
  ('A. {%wohnt nach Belieben im Schooss',
   '<is n="Agni">A.</is> {%wohnt nach Belieben im Schooss'),
  ('reden von den <is>Aśvin</is>.',
   'reden von den <is n="Aśvināḥ">Aśvin.</is>'),
  # 73%
  ('{%das Zusammenkleben der A.%}',
   '{%das Zusammenkleben der <is n="Aklinna">A.</is>%}'),
  ('{%gewisse krankhafte Auswüchse an den A.%}',
   '{%gewisse krankhafte Auswüchse an den <is n="Aklinna">A.</is>%}'),
  ('{%wenn der%} <is>Kṣ</is>. {%will%}',
   '{%wenn der%} <is n="Kṣatriya">Kṣ.</is> {%will%}'),
  ('<ls><is>Kār.</is> 6. 9</ls> aus <ls>SIDDH. K.</ls>',
   '<ls><is n="Kārikā">Kār.</is> 6. 9</ls> aus <ls>SIDDH. K.</ls>'),
  ('{%die Bewohner von%} <is>Tām</is>.',
   '{%die Bewohner von%} <is n="Tāmalipti">Tām.</is>'),
  ('{%zogen den Wagen des%} <is>Śikh</is>.',
   '{%zogen den Wagen des%} <is n="Śikhaṇḍin">Śikh.</is>'),
  ('<is>bareśman</is>', '<iw>bareśman</iw>'),
  # 74%
  ('<is>Kār.</is> zu <ls>P. 1,1,14.</ls>',
   '<is n="Kārikā">Kār.</is> zu <ls>P. 1,1,14</ls>.'),
  ('<is>Kār.</is>', '<is n="Kārikā">Kār.</is>'),   # global
  # <
  ('<is>Bṛhas-</is>',
   '<is>Bṛhaspati</is>'),
  ('<is>-pati</is>',
   ''),
  ('{%ein Fürst der%} <is>Vāṭ</is>.',
   '{%ein Fürst der%} <is n="Vāṭadhāna">Vāṭ.</is>'),
  ('{%die Opfermusik der%} <is>Sobh</is>.',
   '{%die Opfermusik der%} <is n="Sobhari">Sobh.</is>'),
  ('in <is n="Adhyāya">Adhy.</is> 27.',
   'in <is n="Adhyāya">Adhy.</is> 27.'),
  ('{#vAlikAjya/viDa#} {%von%} <is>Vāl</is>.',
   '{#vAlikAjya/viDa#} {%von%} <is n="Vālikājya">Vāl.</is>'),
  ('<ls>MĀRK. P. S. 659, <is>Śl</is>. 4.</ls>',
   '<ls>MĀRK. P. S. 659, Śl. 4</ls>.'),
  ('<ls>WEBER, JYOT. 94. <is>Nakṣ</is>. 2,300. 373.</ls>',
   '<ls>WEBER, JYOT. 94</ls>. <ls>Nax. 2,300. 373</ls>.'),
  # 75%
  ('P. (ging) <ls>ṚV. 7,9,2.</ls>',
   '<is n="Paṇī">P.</is> (ging) <ls>ṚV. 7,9,2</ls>.'),
  ('erhält nicht den Bindevocal {#i#} <is n="Kārikā">Kār.</is>',
   'erhält nicht den Bindevocal {#i#} <ls n="Kārikā">Kār. 2</ls>'), # v1e why 'ls' ?
  ('<ls>WINDISCHMANN, <is>Sancara</is> S. 108.</ls>',
   '<ls>WINDISCHMANN, Sancara S. 108</ls>.'),
  ('<ls>H. 39.</ls> eine Tochter <is>Da-</is>',
   '<ls>H. 39.</ls> eine Tochter <is>Dakṣa</is>ʼs'), #
  ('<is>-kṣa</is>ʼs',
   ''),
  ('<is>Beyapur</is>',
   '<iw>Beyapur</iw>'),
  ('Stadt und District im <is>Dekkhan</is>',
   'Stadt und District im <iw>Dekkhan</iw>'),
  ('<is>Mīrzāpur</is>',
   '<iw>Mīrzāpur</iw>'),
  ('<is>Khandeṣ</is>',
   '<iw>Khandeṣ</iw>'),
  # 76%
  ('Pr., {%so dass der Zwischenraum eines%} Pr.',
   '<is n="Pradeśa">Pr.</is>, {%so dass der Zwischenraum eines%} <is n="Pradeśa">Pr.</is>'),
  ('<ls>WINDISCHMANN, <is>Sancara</is> 93,1 v. u.</ls>',
   '<ls>WINDISCHMANN, Sancara 93,1 v. u.</ls>'),
  # 77%
  ('{%die Nachkommen des%} <is>Vir</is>.',
   '{%die Nachkommen des%} <is n="Virūpākṣa">Vir.</is>'),
  ('{%zum Geschlecht%} <is>Bh</is>.',
   '{%zum Geschlecht%} <is n="Bhoja">Bh.</is>'),
  ('{%den Fingern des%} V.',
   '{%den Fingern des%} <is n="Vivasvat">V.</is>'),
  ('<ls>WEBER, JYOT. 94. <is>Nakṣ</is>. 2,300. 374.</ls>',
   '<ls>WEBER, JYOT. 94</ls>. <ls>Nax. 2,300. 374</ls>.'),
  # 78%
  ('(<is>Śunaka</is>ʼs) und Vater <is>Dhṛti</is>ʼs',
   '(<is>Śunaka</is>ʼs) und Vater <is>Dhṛiti</is>ʼs'),  # v1e spelling?
  ('{%Geschichte der%} <is>UP</is>.',
   '{%Geschichte der%} <is n="Upakośa">Up.</is>'),
  # 79%
  ('({%das ältere%} <is>Vaiy</is>.)',
   '({%das ältere%} <is n="Vaiyākaraṇabhūṣaṇa">Vaiy.</is>)'),
  ('{%der auf dem Berge%} V.',
   '{%der auf dem Berge%} <is n="Veṅkaṭeśvara">V.</is>'),
  ('({%diese drei Berge sind%} V.)',
   '({%diese drei Berge sind%} <is n="Veda">V.</is>)'),
  ('{%Aussprüche des%} V.',
   '{%Aussprüche des%} <is n="Veda">V.</is>'),
  ('vollkommen vertraut mit dem%} V.',
   'vollkommen vertraut mit dem%} <is n="Veda">V.</is>'),
  ('{%als%} V. {%zu erkennen%}',
   '{%als%} <is n="Vāsudeva">V.</is> {%zu erkennen%}'),
  ('{%in der Entfernung der beiden%} <is>Ret</is>.',
   '{%in der Entfernung der beiden%} <is n="Retaḥ">Ret.</is>'),
  ('{%ein Bewohner von%} <is>Vid</is>.',
   '{%ein Bewohner von%} <is n="Vidarbha">Vid.</is>'),
  ('nach <is>Nīlak</is>. {%von Höhlen',
   'nach <is n="Nīlakaṇṭha">Nīlak.</is> {%von Höhlen'),
  # 80%
  ('{%bis der%} <is n="Piśāca">Piś.</is> {%erscheint%}',
   '{%bis der%} <is n="Piśāca">Piś.</is> {%erscheint%}'),
  ('{%die Viereinigkeit%} <is>Puruṣotta-</is>',
   '{%die Viereinigkeit%} <is>Puruṣottama</is>ʼs'),
  ('<is>-ma</is>ʼs ', ##
   ''),
  ('gegen <is>PAT</is>.',
   'gegen <is n="Patañjali">Pat.</is>'),
  ('Unterschriften der <is>Adhyy</is>.',
   'Unterschriften der <is n="Adhyāyas">Adhyy.</is>'),
  # 81%
  ('{%der Sohn der%} <is>Śak</is>.',
   '{%der Sohn der%} <is n="Śakuntalā">Śak.</is>'),
  ('des 200sten <is>Adhyy</is>.',
   'des 200sten <is n="Adhyāyas">Adhyy.</is>'),
  ('({%unter dem%} <is>Nakṣatra</is> <is>Śat</is>. {%geboren%})',
   '({%unter dem%} <is>Nakṣatra</is> <is n="Śatabhiṣaj">Śat.</is> {%geboren%})'),
  ('{%ich habe mich gegen den%} <is>Nam</is>.',
   '{%ich habe mich gegen den%} <is n="Namuci">Nam.</is>'),
  ('(śañvara) wohl fehlerhaft für {#saMvara#} .',
   '(<is>śañvara</is>) wohl fehlerhaft für {#saMvara#}.'),
  # 82%
  ('{%der Gatte der%} <is>Śarv</is>.',
   '{%der Gatte der%} <is n="Śarvarī">Śarv.</is>'),
  ('<is>Uttara</is>ʼs und <is>Śal</is>.',
   '<is>Uttara</is>ʼs und <is n="Śalaṅkaṭa">Śal.</is>'),
  ('{#I#} <ab>patron.</ab> der <is>Kṛipī</is>',
   '{#I#} <ab>patron.</ab> der <is>Kṛpī</is>'),
  # 83%
  ('Śl. {#Sunake#}',
   '<is n="Śloka">Śl.</is> {#Sunake#}'),
  #  84%
  ('{%die Sprache der%} Ś.',
   '{%die Sprache der%} <is n="Śūrasena">Ś.</is>'),
  ('{#sa˚#} {%mit —, ohne%} Śj.',
   '{#sa˚#} {%mit —, ohne%} <is n="Śyāparṇa">Śy.</is>'),
  ('{%zu den%} Śj. {%gehörig%}',
   '{%zu den%} <is n="Śyāparṇa">Śy.</is> {%gehörig%}'),
  ('{#cARqAla#} <is>Śuddhit</is>.',
   '{#cARqAla#} <ls>ŚUDDHIT.</ls>'),
  ('{%die Geschichte von%} <is>Śy.</is>',
   '{%die Geschichte von%} <is n="Śyāvāśva">Śy.</is>'),
  ('in der <is>Saṃh</is>. auch {#SraTA˚#}',
   'in der <is n="Saṃhitā">Saṃh.</is> auch {#SraTA˚#}'),
  ('{%im Sternbild%} R. {%sich befindend%',
   '{%im Sternbild%} <is n="Revatī">R.</is> {%sich befindend%}'),
  ('<ls>WEBER, JYOT. 27. fg. 34. 112. fg. <is>Nakṣ</is>. 1,312. 2,300. 315. 325. 354. fg. 375. 389.</ls>',
   '<ls>WEBER, JYOT. 27. fg. 34. 112. fg.</ls> <ls>Nax. 1,312. 2,300. 315. 325. 354. fg. 375. 389</ls>.'),
  ('<ls>P. 6,1,27</ls>, <is>Vārtt</is>',
   '<ls>P. 6,1,27, <is n="Vārttika">Vārtt.</is></ls>'),
  # 85%
  ('<is>aśrusti</is>, <is>śraoṣa</is>',
   '<iw>açrusti</iw>, <iw>çraosha</iw>'),
  ('<is>qāśtra</is> <ab>d. i.</ab> <is>hvāśtra</is>.',
   '<iw>qâçtra</iw> <ab>d. i.</ab> <iw>hvāśtra</iw>.'),
  ('%sechs mit dem%} <is>Yaj</is>.',
   '{%sechs mit dem%} <is n="Yajamāna">Yaj.</is>'),
  # 86%
  ('{%so dass es%} <is>Dhṛt</is>. {%hören konnte%}',
   '{%so dass es%} <is n="Dhṛtarāṣṭra">Dhṛt.</is> {%hören konnte%}'),
  ('<is>Adyhāya</is>',
   '<is>Adhyāya</is>'),
  ('<ls>WEBER, JYOT. 101. fg. 104. <is>Nakṣ</is>. 2,336. 350. fg.</ls>',
   '<ls>WEBER, JYOT. 101. fg. 104</ls>. <ls>Nax. 2,336. 350. fg.</ls>'),
  ('{%das Hinübergehen zu%} Bh.',
   '{%das Hinübergehen zu%} <is n="Bharata">Bh.</is>'),
  ('<is>hakhman</is>', '<iw>hakhman</iw>'),
  # 88%
  ('{%mit dem%} <is>Gṛhap</is>.',
   '{%mit dem%} <is n="Gṛhapati">Gṛhap.</is>'),
  ('{%zwischen%} K. {%und%} V.',
   '{%zwischen%} <is n="Kṣatra">K.</is> {%und%} <is n="Viśa">V.</is> '),
  # 89%
  ('{#saMpadAnuzwup#} <is>An</is>.',
   '{#saMpadAnuzwup#} <is n="Anuṣṭup">An.</is> '),
  ('{%von%} <is>Sar</is>. {%verfasst%}',
   '{%von%} <is n="Sarasvatī">Sar.</is> {%verfasst%}'),
  ('{%der Halsschmuck der%} <is>Sar</is>.',
   '{%der Halsschmuck der%} <is n="Sarasvatī">Sar.</is>'),
  ('{%ein Lobgesang auf%} <is>Sar</is>.',
   '{%ein Lobgesang auf%} <is n="Sarasvatī">Sar.</is>'),
  ('<is>Śicupālavadha</is>',
   '<is>Śiśupālavadha</is>'),
  # 90%
  ('<is>KĀŚ</is>. zu <ls>P. 5,3,83.</ls>',
   '<is n="Kāśikā">Kāś.</is> zu <ls>P. 5,3,83</ls>.'),
  ('<is>Aditya</is>',
   '<is>Āditya</is>'),
  ('{#vEnateya˚#} {%mit%} V.',
   '{#vEnateya˚#} {%mit%} <is n="Vainateya">V.</is>'),
  ('<is>Paribh</is>.',
   '<is n="Paribhāṣenduśekhara">Paribh.</is>'),
  ('<is>Hary</is>. ist ein Nachkomme',
   '<is n="Haryaśvata">Hary.</is> ist ein Nachkomme'),
  ('{#viSva˚#} {%nebst den%} V.',
   '{#viSva˚#} {%nebst den%} <is n="Viśva">V.</is>'),
  ('{#lakzmaRena#} {%an%} L.',
   '{#lakzmaRena#} {%an%} <is n="Lakṣmaṇa">L.</is>'),
  ('{%zu einem leibhaftigen%} C.',
   '{%zu einem leibhaftigen%} <is n="Caṇḍāla">C.</is>'),
  # 91%
  ('Ṛk. und <is>Sāman</is>',
   '<is>Ṛc</is> und <is>Sāman</is>'),
  ('<ls>ŚAT. BR. 14,4,1,24.</ls> Ṛc. <is>Sāman</is>',
   '<ls>ŚAT. BR. 14,4,1,24</ls>. <is>Ṛc</is>, <is>Sāman</is>'),
  ('{%die Anwohner der%} <is>Sar</is>.',
   '{%die Anwohner der%} <is n="Sarasvatī">Sar.</is>'),
  ('Brahmanen von der <is>Sar</is>.',
   'Brahmanen von der <is n="Sarasvatī">Sar.</is>'),
  ('{%Sohnes der%} <is>Sar</is>.',
   '{%Sohnes der%} <is n="Sarasvatī">Sar.</is>'),
  ('<is>Sav</is>. {%stammend%}',
   '<is n="Savitar">Sav.</is> {%stammend%}'),
  ('<span>N.</span> <ls>MBH. 1,4462.</ls>',
   '<is n="Nāgapura">N.</is> <ls>MBH. 1,4462</ls>.'),
  ('<ls><is>Nakṣ</is>. 2,281, N., Z. 3 v. u.</ls>',
   '<ls>Nax. 2,281, N., Z. 3 v. u.</ls>'),
  # 92%
  ('<ls>VĀLAKH. 11.</ls> mit dem <ab>patron.</ab> <is>Tārkṣyaputra Suparṇa</is>',
   '<ls>VĀLAKH. 11.</ls> mit dem <ab>patron.</ab> <is>Tārkṣyaputra</is>'),
  # 93%
  ('Theiles des heutigen <is>Guzerat</is>',
   'Theiles des heutigen <iw>Guzerat</iw>'),
  ('<is>Soastos</is>',
   '<iw>Soastos</iw>'),
  ('<is>Kophen</is>, heut zu Tage <is>Suwad</is>.',
   '<iw>Kophen</iw>, heut zu Tage <iw>Suwad</iw>.'),
  # 94%
  ('{%mit%} <is>Indra</is> {%verbunden, sammt%} I.',
   '{%mit%} <is>Indra</is> {%verbunden, sammt%} <is n="Indra">I.</is>'),
  ('{%ein Kind der%} <is n="Siṃhikā">S.</is>',
   '{%ein Kind der%} <is n="Siṃhikā">S.</is>'),
  ('<ls>R.</ls> <ls>Verz. d. Oxf. H. 398,a, No. 144</ls>',
   '<is n="Rudra">R.</is> <ls>Verz. d. Oxf. H. 398,a, No. 144</ls>'),
  ('saukaryā \'udyatayā',
   '<is>saukaryā ʼudyatayā</is>'),
  ('<is>Sucruta</is>',
   '<is>Suśruta</is>'),
  ('{%tausend%} <is>St</is>. {%habend%}',
   '{%tausend%} <is n="Starī">St.</is> {%habend%}'),
  # 95%
  ('<ls><is>St</is>.</ls> <ls>ŚAT. BR. 8,6,1,4.</ls>',
   '<is n="Stoma">St.</is> <ls>ŚAT. BR. 8,6,1,4</ls>.'),
  ('{%der Weg geht —, führt nach%} Sr.',
   '{%der Weg geht —, führt nach%} <is n="Srughna">Sr.</is>'),
  ('{%das%} A. {%hat einen Stumpf%}',
   '{%das%} <is n="Agni">A.</is> {%hat einen Stumpf%}'),
  ('{%des Bildes von%} V.',
   '{%des Bildes von%} <is n="Viṣṇu">V.</is>'),
  # 96%
  ('<is>śrū</is>',
   '<iw>çrû</iw>'),
  ('{#paYcAlAn#} {%bei den%} <is>Pañc</is>.',
   '{#paYcAlAn#} {%bei den%} <is n="Pañcāla">Pañc.</is>'),
  # 97%
  ('{%er gedachte seines geliebten%} <is>Kṛ</is>.',
   '{%er gedachte seines geliebten%} <is n="Kṛṣṇa">Kṛ.</is>'),
  ('{%mit einer gemeinsamen Schlussgabe an%} Sv.',
   '{%mit einer gemeinsamen Schlussgabe an%} <is n="Sviṣṭakṛt">Sv.</is>'),
  # 98%
  ('im Epos ist <is>Har</is>. ein Sohn',
   'im Epos ist <is n="Hariścandra">Har.</is> ein Sohn'),
  ('{%auf%} <is>Hari</is> {%bezüglich%}, H. {%betreffend.%}',
   '{%auf%} <is>Hari</is> {%bezüglich%}, <is n="Hari">H.</is> {%betreffend%}.'),
  ('{%die Tochter des%} <is n="Himavant">Him.</is>',
   '{%die Tochter des%} <is n="Himagiri">Him.</is>'),
  # 99%
  ('<ls>H.</ls> <ls>Verz. d. Oxf. H. 249,b,25.</ls>',
   '<is n="Heramba">H.</is> <ls>Verz. d. Oxf. H. 249,b,25</ls>.'),
  ('<ls>Pariśiṣṭa zum SV.</ls> weissen <is>Yajus</is>',
   '<is>Pariśiṣṭa</is> zum weissen <is>Yajus</is>'),
  ('Bei P. vielleicht {%wägen%}',
   'Bei <is n="Pāṇini">P.</is> vielleicht {%wägen%}'),
  ('<span>N.</span> zu <ls>Spr. (II) 5323.</ls>',
   '<is n="Nīlakaṇṭha">N.</is> zu <ls>Spr. (II) 5323</ls>.'),
  ('{%gelangt mit Sonnenaufgang nach%} <is>Māh</is>.',
   '{%gelangt mit Sonnenaufgang nach%} <is n="Māhiṣmatī">Māh.</is>'),
  ('{%dem%} P. {%verderblich.%}',
   '{%dem%} <is n="Parṇa">P.</is> {%verderblich%}.'),
  ('{%erreicht mit Sonnenaufgang%} <is>Māh</is>.',
   '{%erreicht mit Sonnenaufgang%} <is n="Māhiṣmatī">Māh.</is>'),
  ('<is>Ātreya</is> {%liegende%} <is>Ā.</is>',
   '<is>Ātreya</is> {%liegende%} <is n="Ātreya">Ā.</is>'),
  # Bhṛigu v1e spelling error  See adjust_lines0
  ('der Weiber der <is>Kṣemavṛddhi</is>',
   'der Weiber der <is>Kṣemavṛiddhi</is>'), #v1e spelling error
  ('<is>areśman</is> in <is>areśmoṣūta</is>.',
   '<iw>areçman</iw> in <iw>areçmoshûta</iw>.'),
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

def adjust_lines0(lines):
 ans = lines
 lnum = 1111491
 iline = lnum - 1
 assert ans[iline] == '<is>Bhṛgu</is>ʼs'
 ans[iline] = '<is>Bhṛigu</is>ʼs'
 return ans
if __name__=="__main__":
 filein = sys.argv[1]  # base
 fileout = sys.argv[2] # adjusted base
 
 lines = read_lines(filein)
 lines0 = adjust_lines0(lines)
 #lines0 = lines
 lines1 = adjust_lines1(lines0)
 write_lines(fileout,lines1)
