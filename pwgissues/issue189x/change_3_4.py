""" change_3_4.py
 
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
  # 26% Begin 06-17-2026 9PM

  ('<is>Gandharva(</is>?)',
   '<is>Gandharva</is>(?)'),
  ('<is>Brāhmaṇa</is> {%der%} <is>Tal</is>.',
   '<is>Brāhmaṇa</is> {%der%} <is n="Talavakāra">Tal.</is>'),
  ('{%die einblättrige%} <is>Tav</is>.',
   '{%die einblättrige%} <is n="Tavakṣīrī">Tav.</is>'),
  ('{%betreffend, an%} T.',
   '{%betreffend, an%} <is n="Tanūnapāt">T.</is>'),
  # 27%
  ('{%die von den%} T.',
   '{%die von den%} <is n="Tārkṣya">T.</is>'),
  ('<is>Tālaj</is>.',
   '<is n="Tālajangha">Tālaj.</is>'),
  ('<is>Tugriern</is>',
   'Tugriern'),  # v1e <iw>
  ('<is>Tugriers</is>',
   'Tugriers'),  # v1e <iw>
  #('{%freut, gern bei dem%} T. {%ist%}',
  # '{%freut, gern bei dem%} <iw n="Tugriers">T.</iw> {%ist%}'),
  ('{%Fürst der%} T.',
   '{%Fürst der%} <is n="Turuṣka">T.</is>'),
  ('{%zur Gruppe der%} T.',
   '{%zur Gruppe der%} <is n="Tuṣita">T.</is>'),
  ('\'</is>',
   '</is>ʼ'),
  ('23,b,5.</ls> <ab>N.</ab> einer <is>Mātṛkā</is>',
   '23,b,5</ls>. <ab>N.</ab> einer <is>Mātṛikā</is>'),  # v1e spelling error
  ('2655.</ls> eines Sohnes des <is>Dhṛtarāṣṭra</is>',
   '2655</ls>. eines Sohnes des <is>Dhṛitarāṣṭra</is>'),
  ('{%das%} T. {%des Lichtherrn (der Sonne?%})',
   '{%das%} <is n="Tejonātha">T.</is> {%des Lichtherrn (der Sonne?)%}'),
  ('<is>Vartt</is>.',
   '<is n="Vārttika">Vārtt.</is>'),
  # 28%
  ('<is>Vikr</is>.',
   '<is n="Vikramāditya">Vikr.</is>'),
  # 2026-06-18 BEGIN
  ('{#vEvasvatAt#} {%vor%} V.',
   '{#vEvasvatAt#} {%vor%} <is n="Vaivasvata">V.</is>'),
  ('{%ein Fürst der%} Tr.',
   '{%ein Fürst der%} <is n="Trigarta">Tr.</is>'),
  ('<is>Trita</is> und Feridun',
   '<is>Trita</is> und <is>Feridun</is>'),
  ('{%die Verbrennung von%} Tr.',
   '{%die Verbrennung von%} <is n="Tripura">Tr.</is>'),
  ('{%im ersten%} J.',
   '{%im ersten%} <is n="Yuga">Y.</is>'),
  ('({%für%} Tr. {%opfernd%})',
   '({%für%} <is n="Triśaṅku">Tr.</is> {%opfernd%})'),
  ('{%Kardamomen von%} Guzerate',
   '{%Kardamomen von%} <is>Guzerate</is>'),
 ('{#apUpa#} {%dem%} <is>Try</is>.',
  '{#apUpa#} {%dem%} <is n="Tryambaka">Try.</is>'),
  ('{%verbunden, von%} TV.',
   '{%verbunden, von%} <is n="Tvaṣṭar">Tv.</is>'),
  (' Kār. ',
   ' <is n="Kārikā">Kār.</is> '),
  # 29%
  ('<ab>u.</ab> A.',
   '<ab n="und">u.</ab> <is n="Agni ??">A.</is>'),
  ('lakzmaRaH#} L. {%zeigte',
   'lakzmaRaH#} <is n="Lakṣmaṇa">L.</is> {%zeigte'),
  ('wie in den Ś.',
   'wie in den <is n="Śāstradarśana">Ś.</is>'),
  ('{%der König der%} <is>Daś</is>.',
   '{%der König der%} <is n="Daśārṇa">Daś.</is>'),
  ('aus dem Stamme der%} <is>Daś</is>.',
   'aus dem Stamme der%} <is n="Daśārha">Daś.</is>'),
  ('eines Abschnitts im TV.',
   'eines Abschnitts im <is n="TaittirīyaVeda">TV.</is>'),
  # 30%
  ('<is>Śridāma(n</is>?)',
   '<is>Śridāma(n?)</is>'),
  ('<is>Dāsam</is>.',
   '<is n="Dāsamitri">Dāsam.</is>'),
  ('zum Andenken des%} <is>Dhṛ</is>.',
   'zum Andenken des%} <is n="Dhṛtarāṣṭra">Dhṛ.</is>'),
  ('<is>Dhanv</is>.',
   '<is n="Dhanvantari">Dhanv.</is>'),
  # 31%
  ('<is>Śl.</is>', 'Śl.'),  #75
  
  ('Fürsten der%} J.',
   'Fürsten der%} <is n="Yadu">Y.</is>'),
  #('<is>Krauñkadvīpa</is>',
  # '<is>Krauñcadvīpa</is>'),
  ('<ab>N.</ab> der Bewohner eines <is>Varṣa</is> in <is>Krauñkadvīpa</is>',
   '<ab>N.</ab> der Bewohner eines <is>Varṣa</is> in <is>Krauñcadvīpa</is>'),
  ('<is>Dschugará</is>',
   'Dschugará'),  # v1e <iw>
  ('<ls>BRAHMAVAIV. P.</ls>, <is>Śrīkṛṣṇajanmakhaṇḍa</is>',
   '<ls>BRAHMAVAIV. P., Śrīkṛṣṇajanmakhaṇḍa</ls>'),
  ('<is>Mārkaṇḍ. P.</is>',
   '<ls>Mārkaṇḍ. P.</ls>'),
  ('<is>Vit</is>.',
   '<is n="Vitasti">Vit.</is>'),
  # 32%
  ('und Königs von <is>Krauñcadvīpa</is>',
   'und Königs von <is>Krauñkadvīpa</is>'),  # spelling?
  #('<ab>N.</ab> der Bewohner eines <is>Varṣa</is> in <is>Krauñcadvīpa</is>',
  # '<ab>N.</ab> der Bewohner eines <is>Varṣa</is> in <is>Krauñkadvīpa</is>'),
  ('{%begleitet, mit%} <is>Kṛ</is>.',
   '{%begleitet, mit%} <is n="Kṛṣṇa">Kṛ.</is>'),
  ('{%der Feind des%} <is>Dv</is>.',
   '{%der Feind des%} <is n="Dvividāri">Dv.</is>'),
  ('{%die von den%} <is>Dvyākṣ</is>.',
   '{%die von den%} <is n="Dvyākṣāyaṇa">Dvyākṣ.</is>'),
  ('<is>AgniSoma</is>',
   '<is>Agni-Soma</is>'),
  ('{#bali#}) an <is>Dh</is>.',
   '{#bali#}) an <is n="Dhanvantari">Dh.</is>'),
  ('{%die von%} <is>Dh</is>.',
   '{%die von%} <is n="Dhanvantari">Dh.</is>'),
  # 33
  ('atyarIricannidamUnamakranniti#} {%die%} G.',
   'atyarIricannidamUnamakranniti#} {%die%} <is n="Gandharva">G.</is>'),
  ('{%wenn Jmd mit dem%} <is>Pr.</is>',
   '{%wenn Jmd mit dem%} <is n="Prayāja">Pr.</is>'),
  ('P. <ls>MBH. 10,703.</ls>',
   '<is n="Pāṇḍava">P.</is> <ls>MBH. 10,703</ls>.'),
  ('<is>Dh</is>. zusammen genannt',
   '<is n="Dhātar">Dh.</is> zusammen genannt'),
  ('<is>Aryaman</is> hat <is>Dh</is>.',
   '<is>Aryaman</is> hat <is n="Dhātar">Dh.</is>'),
  ('zu zählen wäre. <is>Dh</is>.',
   'zu zählen wäre. <is n="Dhātar">Dh.</is>'),
  ('Vom Epos an erscheint <is>Dh</is>.',
   'Vom Epos an erscheint <is n="Dhātar">Dh.</is>'),
  ('Zeit ist <is>Dh</is>.',
   'Zeit ist <is n="Dhātar">Dh.</is>'),
  ('Dh. als einer der 7',
   '<is n="Dhātar">Dh.</is> als einer der 7'),
  ('(<is>Gaṇabhedanāmādhy</is>.)',
   '(<is n="Gaṇabhedanāmādhyāya">Gaṇabhedanāmādhy.</is>)'),
  ('<ls n="VARĀH. BṚH. S. 105,">107</ls> (<ls>ANUKR.</ls>),12',
   '<ls n="VARĀH. BṚH. S. 105,">107 (<is n="ANUKRAMAṆIKĀ">ANUKR.</is>), 12</ls>'),
  # 34%
  ('(<is>Nāga</is>), <is>Dhṛ</is>.',
   '(<is>Nāga</is>), <is n="Dhṛtarāṣṭra">Dhṛ.</is>'),
  ('identificirt mit <is>Dhṛtar</is>.',
   'identificirt mit <is n="Dhṛtarāṣṭra">Dhṛtar.</is>'),
  ('{%er beabsichtigte dem Br. Gewalt anzuthun%}',
   '{%er beabsichtigte dem <is n="Brahma">Br.</is> Gewalt anzuthun%}'),
  ('der%} R.',
   'der%} <is n="Ratnamāla">R.</is>'),
  ('<span>N.</span> <ls>AIT. BR. 6,24.</ls>',
   '<is n="Nabhāka">N.</is> <ls>AIT. BR. 6,24</ls>.'),
  # 35%
  ('<is>Yellinghy</is>',
   'Yellinghy'),  # v1e <iw>
  ('<is>Nuddea</is>',
   'Nuddea'),  # v1e <iw>
  ('{%ein neuerer%} <is>Ved</is>.',
   '{%ein neuerer%} <is n="Vedāntin">Ved.</is>'),
  ('<is>Nābh</is>. {%herrührend <ab>u. s. w.</ab>%}',
   '<is n="Nābhanediṣṭha">Nābh.</is> {%herrührend <ab>u. s. w.</ab>%}'),
  ('{%den Namen%} C. {%führend%}',
   '{%den Namen%} <is n="Candrasaras">C.</is> {%führend%}'),
  ('<is>Mīm</is>.',
   '<is n="Mīmāṃsā">Mīm.</is>'),
  ('<is>nāonhaitya</is>.',
   'nâonhaitya.'),   # v1e <iw>
  # 36%
  ('verzweifelnd die <is>Ind</is>.',
   'verzweifelnd die <is n="Indumatī">Ind.</is>'),
  ('{%aus%} <is>Kh</is>. {%gemacht%}',
   '{%aus%} <is n="Khadira">Kh.</is> {%gemacht%}'),
  ('von wo die%} J. {%entfernt sind%}',
   'von wo die%} <is n="Yādava">Y.</is> {%entfernt sind%}'),
  ('{%nach dem der%} <is>Dv</is>. {%benannt wird%}',
   '{%nach dem der%} <is n="Dvīpa">Dv.</is> {%benannt wird%}'),
  ('<is>Dvipa</is> {%den Namen giebt%}',
   '<is>Dvīpa</is> {%den Namen giebt%}'),
  ('{%das Eingehen in das%} <is>Br</is>.',
   '{%das Eingehen in das%} <is n="Brahman">Br.</is>'),
  ('{%von den%} P. {%erlöst%}',
   '{%von den%} <is n="Pāṇḍava">P.</is> {%erlöst%}'),
  # 37%
  ('({%für%} V.)',
   '({%für%} <is n="Virāṭ">V.</is>)'),
  ('{#sruGnasya#} {%nach%} Sr.',
   '{#sruGnasya#} {%nach%} <is n="Srughna">Sr.</is>'),
  ('<is>devak</is>.',
   '<is n="devakarmāḥ">devak.</is>'),
  # 38%
  ('P. <ls>MBH. 5,7504</ls>',
   '<is n="Pañcāla">P.</is> <ls>MBH. 5,7504</ls>'),
  ('{%es beginne das Spiel um%} <is>Dam</is>.',
   '{%es beginne das Spiel um%} <is n="Damayantī">Dam.</is>'),
  ('{%der kluge%} <is>Jay</is>.',
   '{%der kluge%} <is n="Jayāpīḍa">Jay.</is>'),
  ('{#sAvitrIpatita#} {%der%} <is>Sāv</is>.',
   '{#sAvitrIpatita#} {%der%} <is n="Sāvitrī">Sāv.</is>'),
  ('{%die vom%} <is>Vet</is>.',
   '{%die vom%} <is n="Vetāla">Vet.</is>'),
  ('{#pattrISva˚#} {%das%} T.',
   '{#pattrISva˚#} {%das%} <is n="Tīrtha">T.</is>'),
  # 39%
  ('P. des <is>Keśava</is> <ab>astrol.</ab>',
   '<is n="Paddhati">P.</is> des <is>Keśava</is> <ab>astrol.</ab>'),
  ('P., <ab>Bein.</ab> des Königs',
   '<is n="Padmāvatī">P.</is>, <ab>Bein.</ab> des Königs'),
  ('{%der Sohn des%} <is>Padm</is>.',
   '{%der Sohn des%} <is n="Padmottara">Padm.</is>'),
  ('{%kehrten%} <is>Bh</is>.',
   '{%kehrten%} <is n="Bhīṣma">Bh.</is>'),
  ('<ls>WEBER, <is>Nakṣatra</is> 298.</ls>',
   '<ls>WEBER, Nakṣatra 298</ls>.'),
  ('<is>ŚV</is>. {%sich befand%}',
   '<is n="Śvaphalka">Śv.</is> {%sich befand%}'),
  # 40%
  ('<is>Puna</is>',
   'Puna'),  # v1e <iw>
  ('Mutter des <is>Hir</is>.',
   'Mutter des <is n="Hiraṇyaroman">Hir.</is>'),
  ('P. {%dröhnend%}',
   '<is n="Parjanya">P.</is> {%dröhnend%}'),
  ('{%von%} P. {%belebt%}:',
   '{%von%} <is n="Parjanya">P.</is> {%belebt%}'),
  ('{%den%} P. {%zum Gatten habend%}',
   '{%den%} <is n="Parjanya">P.</is> {%zum Gatten habend%}'),
  ('{%in%} P.\'s oder',
   '{%in%} <is n="Parjanya">P.</is>ʼs oder'),
  ('{%durch%} P. {%genährt%}',
   '{%durch%} <is n="Parjanya">P.</is>'),
  ('P. 11. {#paryagniM karoti#}',
   '<is n="Paryagni">P.</is> <ls n="AIT. BR. 2,">11</ls>. {#paryagniM karoti#}'),
  ('{%die Tochter des%} <is>Him</is>.',
   '{%die Tochter des%} <is n="Himavant">Him.</is>'),
  ('(auch 5 <is>Suv</is>.)',
   '(auch 5 <is n="Suvarṇa">Suv.</is>)'),
  ('<is>Plassey</is>',
   'Plassey'),  # v1e <iw>
  ('{%wenn der Mond das%} L. {%nicht sieht%}',
   '{%wenn der Mond das%} <is n="Lagna">L.</is> {%nicht sieht%}'),
  ('P. <ls>UJJVAL.</ls>',
   '<is n="Pañcāla">P.</is> <ls>UJJVAL.</ls>'),
  ('P. <ls>P. 4,1,178</ls>',
   '<is n="Pañcāla">P.</is> <ls>P. 4,1,178</ls>'),
  ('<is>Putcabarry</is>',
   'Putcabarry'),  # v1e <iw>
  ('{#sUtra˚#} P. in den Unterschriften. ',
   '{#sUtra˚#} <is n="Pāṭha">P.</is> in den Unterschriften.'),
  ('<ls>WEBER</ls>, <is>Nakṣatra</is> 375.',
   '<ls>WEBER, Nakṣatra 375</ls>.'),
  ('<ls>WEBER, <is>Nakṣatra</is> II,281.</ls>',
   '<ls>WEBER, Nakṣatra II, 281</ls>.'),
  ('{%die von%} P. {%verfasste Grammatik%}',
   '{%die von%} <is n="Pāṇini">P.</is> {%verfasste Grammatik%}'),
  ('{%das Herz — die Quintessenz einer%} <is>Pār</is>.',
   '{%das Herz — die Quintessenz einer%} <is n="Pāramitā">Pār.</is>'),
  # 41%
  ('P., so heissen die Abschnitte im',
   '<is n="Pārijāta">P.</is>, so heissen die Abschnitte im'),
  ('{%jenseits%} VIŚ.',
   '{%jenseits%} <is n="Viśoka">Viś.</is>'),
  ('<is>Pravarādhy</is>.',
   '<ls>Pravarādhy.</ls>'),
  ('{#himavatpArSve#} {%am%} <is>Him</is>.',
   '{#himavatpArSve#} {%am%} <is n="Himavant">Him.</is>'),
  ('{%eines der 8 Gesichter des%} <is>Bh</is>.',
   '{%eines der 8 Gesichter des%} <is n="Bhairava">Bh.</is>'),
  #('<is>Rakṣas</is>, <is>Piśāka</is>',
  # '<is>Piśāca</is>'),
  ('<is>Dakṣa</is>ʼs und Mutter der <is>Piśāka</is>.',
   '<is>Dakṣa</is>ʼs und Mutter der <is>Piśāca</is>.'),
  ('{%die Sprache der%} <is>Piś</is>.',
   '{%die Sprache der%} <is n="Piśāca">Piś.</is>'),
  ('<is>Piś</is>.',
   '<is n="Piśāca">Piś.</is>'),
  # 42%
  ('<ab>Einl.</ab> zu P.',
   '<ab>Einl.</ab> zu <is n="Pāṇini">P.</is>'),
  ('{#purovfzendra#} {%den%} <is>Vṛ</is>.',
   '{#purovfzendra#} {%den%} <is n="Vṛṣendra">Vṛ.</is>'),
  ('{%im Besitz der Welt%} Br.',
   '{%im Besitz der Welt%} <is n="Brahmaloka">Br.</is>'),
  ('{#stotra˚#} {%vor dem%} <is>St</is>.',
   '{#stotra˚#} {%vor dem%} <is n="Stotra">St.</is>'),
  ('Sohnes des Su<is>śānti</is>',
   'Sohnes des <is>Suśānti</is>'),
  ('P. <ab>N.</ab> <ls>KĀTY. ŚR. 24,7,36.</ls>',
   '<is n="Puruṣa">P.</is> <ab>N.</ab> <ls>KĀTY. ŚR. 24,7,36</ls>.'),
  ('P. <ab>N.</ab> <ls>LĀṬY. 10,13,4.</ls>',
   '<is n="Puruṣa">P.</is> <ab>N.</ab> <ls>LĀṬY. 10,13,4</ls>.'),
  ('{%mit%} P. {%versehen%}',
   '{%mit%} <is n="Puroruc">P.</is> {%versehen%}'),
  ('ist P. der Götter',
   'ist <is n="Purohita">P.</is> der Götter'),
  ('P. <ls>MBH. 2,119.</ls> {#pulinda#}',
   '<is n="Pulinda">P.</is> <ls>MBH. 2,119</ls>. {#pulinda#}'),
  ('{%Tochter des%} P., <ab>Bein.</ab> der Gemahlin <is>Indra</is>ʼs (<ab>vgl.</ab> {#pOlomI#})',
   '{%Tochter des%} <is n="Puloma">P.</is>, <ab>Bein.</ab> der Gemahlin <is>Indra</is>ʼs (<ab>vgl.</ab> {#pOlomI#})'),
  ('(Mutter des <is>Lobha</is>). eine der 16 <is>Mātṛkā</is>',
   '(Mutter des <is>Lobha</is>). eine der 16 <is>Mātṛikā</is>'),  # v1e spelling error
  ('<is>Mahimnaḥ</is> <is>stavaḥ</is>',
   '<is>Mahimnaḥ stavaḥ</is>'),
  ('<ls>VARĀH. BṚH. S. 107 (Anukramaṇī),6.</ls>',
   '<ls>VARĀH. BṚH. S. 107</ls> (<is>Anukramaṇī</is>), 6.'),
  ('P., {%die Zeit, da der Mond im Sternbilde%} P. {%steht%},',
   '<is n="Puṣya">P.</is>, {%die Zeit, da der Mond im Sternbilde%} <is n="Puṣya">P.</is>'),
  # 2026-06-18 end
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

def unused_adjust_lines0(lines):
 ans = lines
 lnum = 125626
 iline = lnum - 1
 assert ans[iline] == ', <is>Vartt</is>. 1.'
 ans[iline] = ''
 ans[iline - 1] = ans[iline - 1] + ', <is>Vartt</is>. 1.'
 return ans
if __name__=="__main__":
 filein = sys.argv[1]  # base
 fileout = sys.argv[2] # adjusted base
 
 lines = read_lines(filein)
 #lines0 = adjust_lines0(lines)
 lines0 = lines
 lines1 = adjust_lines1(lines0)
 write_lines(fileout,lines1)
