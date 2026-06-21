""" change_2_3.py
 
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
  # 10%
  ('(Schrift von U.)',
   '(Schrift von <is n="Utkṣepa">U.</is>)'),
  ('<is>Soma</is>steine',
   'Somasteine'),
  # 11%
  ('({%zur Darbringung für%} Bh.)',
   '({%zur Darbringung für%} <is n="Bhagavatī">Bh.</is>)'),
  ('<is>Pr</is>. {%ergangen ist%}',
   '<is n="Prātaranuvāka">Pr.</is> {%ergangen ist%}'),
  ('({%zu%} <is>Yaug</is>.)',
   '({%zu%} <is n="Yaugandharāyaṇa">Yaug.</is>)'),
  ('<is>Yaṣt</is> <ab>d.</ab> M.',
   '<ab n="des">d.</ab> <is n="Mithra">M.</is>'),
  ('eines Mannes <is>Pravarādhy</is>.',
   'eines Mannes <ls>Pravarādhy.</ls>'),
  ('<ls>ŚĀNT. 3,18. <is>Uṇ</is>. 4,31.</ls>',
   '<ls>ŚĀNT. 3,18</ls>. <ls>Uṇ. 4,31</ls>.'),
  # 12%
  ('<is>Dh</is>. {%zehn%} G.',
   '<is n="Dhārtarāṣṭra">Dh.</is> {%zehn%} <is n="Gandharva">G.</is>'),
  ('sich an <is>Pr</is>. wandte',
   'sich an <is n="Prajāpati">Pr.</is> wandte'),
  ('{%Bewohner von%} Dv.',
   '{%Bewohner von%} <is n="Dvārakā">Dv.</is> '),
  ('{%Holzstück von%} U.',
   '{%Holzstück von%} <is n="Udumbara">U.</is>'),
  ('{%Frucht des%} U.',
   '{%Frucht des%} <is n="Udumbara">U.</is>'),
  ('<ls>P. 4,3,58</ls>, <is>Vartt</is>. 1.',
   '<ls>P. 4,3,58, <is n="Vārttika">Vārtt.</is> 1</ls>.'),
  ('nach dem <is>Vartt</is>.',
   'nach dem <is n="Vārttika">Vārtt.</is>'),
  ('<ls>R.</ls> {%zum Freunde machtest%}',
   '<is n="Rāma">R.</is> {%zum Freunde machtest%}'),
  ('{%die von den C. gespielte Laute%}',
   '{%die von den <is n="Caṇḍāla">C.</is> gespielte Laute%}'),
  ('<is>Vaicaṃpāyana</is>',
   '<is>Vaiśaṃpāyana</is>'),
  # 13%
  ('<is>Agamīḍha\'s(</is>',
   '<is>Ajamīḍha</is>ʼs'),
  ('{%die Nachkommen des%} K.',
   '{%die Nachkommen des%} <is n="Kapiṣṭhala">K.</is>'),
  ('{#kamalAnandana#} {%Sohn der%} K.',
   '{#kamalAnandana#} {%Sohn der%} <is n="Kamalā">K.</is>'),
  ('<is>Kaik</is>.',
   '<is n="Kaikeyī">Kaik.</is>'),
  ('<ls>M.</ls> {%aufgeworfene Frage%}',
   '<is n="Māndhātar">M.</is> {%aufgeworfene Frage%}'),
  ('<is>Pūna</is>', 'Pūna'),  # ve1 <iw>
  ('<ls>SVĀMIN</ls> zu <ls><is>AK</is>.</ls>',
   '<ls>SVĀMIN</ls> zu <ls>AK.</ls>'),
  ('_', ' '),  # cleanup 8 instances -- used in v1e but not cdsl
  ('<is>Śir</is>.',
   '<is n="Śirīṣa">Śir.</is>'),
  # 14%
  ('<is>Leṭa(?</is>)',
   '<is>Leṭa</is>(?)'),
  ('<is>Māgadhī</is> übersetzt worden, London 1848.',
   '<ls>Māgadhī übersetzt worden, London 1848</ls>.'),
  ('{%dem U. gehört%}',
   '({%dem <is n="Udgātu">U.</is> gehört%})'),
  ('<is>Kāmali(?</is>)',
   '<is>Kāmali</is>(?)'),
  # 15%
  ('(<ls>LASSEN</ls>, <is>Pentap</is>.',
   '(<ls>LASSEN, Pentap. 67,41</ls>)'),
  ('<ls n="MBH.">67,41</ls>) und {#kAraskfta#}',
   'und {#kAraskfta#}'),
  ('<is>Kārṣ</is>.',
   '<is n="Kārṣāpaṇa">Kārṣ.</is>'),
  ('?</is>',
   '</is>?'),
  ('{%hat mich%} <is>Vas</is>.',
   '{%hat mich%} <is n="Vasiṣṭa">Vas.</is>'),
  ('{%kocht%} <is>Dev</is>.',
   '{%kocht%} <is n="Devadatta">Dev.</is>'),
  ('<is>Var</is>.',
   '<is n="Varuṇa">Var.</is>'),
  ('<is>Śāk</is>.',
   '<is n="Śakuntalā">Śāk.</is>'),
  ('<is>Ar</is>.',
   '<is n="Aruṇa">Ar.</is>'),
  ('Leibe der%} K. {%Geborene%}',
   'Leibe der%} <is n="Kukṣi">K.</is> {%Geborene%}'),
  ('angeblich nach M.',
   'angeblich nach <is n="Medinī">M.</is>'),
  # 16%
  ('<is>Guzerate</is>',
   'Guzerate'),   # <iw>
  ('{%wie bei den%} K. {%und%}',
   '{%wie bei den%} <is n="Kuru">K.</is> {%und%}'),
  ('P. <ls>ŚAT. BR. 3,2,3,15.</ls>',
   '<is n="Pañcāla">P.</is> <ls>ŚAT. BR. 3,2,3,15</ls>.'),
  ('ganz nach P.',
   '<is n="Paurṇamāsī">P.</is>'),
  ('<is>Viśve</is> <is>Devāḥ</is>',
   '<is>Viśve Devāḥ</is>'),
  ('Bewohner von%} <is>Jan</is>.',
   'Bewohner von%} <is n="Janasthāna">Jan.</is>'),
  ('<is>Bṛh</is>.',
   '<is n="Bṛhaspati">Bṛh.</is>'),
  # 17%
  ('<is>Maitr</is>.',
   '<is n="Maitrāvaruṇa">Maitr.</is>'),
  ('({%die sieben%} K.)',
   '({%die sieben%} <is n="Kośala">K.</is>)'),
  #('(?</is>)',
  # '</is>(?)'),
  ('<is>Sūkta(</is>?)',
   '<is>Sūkta</is>(?)'),
  ('{%ein von%} K. {%verfasstes%}',
   '{%ein von%} <is n="Kutsa">K.</is> {%verfasstes%}'),
  ('<ls>P. 4,2,91</ls>, <is>Vartt</is>.',
   '<ls>P. 4,2,91, <is n="Vārttika">Vārtt.</is></ls>'),
  # 18%
  ('<is>Dev</is>.',
   '<is n="Devadatta">Dev.</is>'),
  ('Aps.',
   '<is n="Apsara">Aps.</is>'),
  ('<ls><is>Kṣ</is>. P. 5,3,114</ls>',
   '<is n="Kṣudraka">Kṣ.</is> <ls>P. 5,3,114</ls>'),
  ('<is>Hariśkandra</is>',
   '<is>Hariścandra</is>'),
  ('<is>Vipr</is>.',
   '<is n="Vipracitti">Vipr.</is>'),
  ('{%strömende%} G.',
   '{%strömende%} <is n="Gaṅgā">G.</is>'),
  ('{%acht Verse an die%} G.',
   '{%acht Verse an die%} <is n="Gaṅgā">G.</is>'),
  # 19%
  ('<is>Vira</is>',
   '<is>Vīra</is>'),
  ('Der G.',
   'Der <is n="Gandharva">G.</is>'),
  ('der G.',
   'der <is n="Gandharva">G.</is>'),
  ('Verbindung des G. mit <is>Soma</is>',
   'Verbindung des <is n="Gandharva">G.</is> mit <is>Soma</is>'),
  ('die G. sind thätig',
   'die <is n="Gandharva">G.</is> sind thätig'),
  ('Siebenundzwanzig G.',
   'Siebenundzwanzig <is n="Gandharva">G.</is>'),
  ('<is>Purūravas</is> wird G.',
   '<is>Purūravas</is> wird <is n="Gandharva">G.</is>'),
  ('G. und Menschen',
   '<is n="Gandharva">G.</is> und Menschen'),
  ('Götter, Menschen, G.',
   'Götter, Menschen, <is n="Gandharva">G.</is>'),
  ('G., Manen, Götter',
   '<is n="Gandharva">G.</is>, Manen, Götter'),
  ('Namen von G.',
   'Namen von <is n="Gandharva">G.</is>'),
  ('der vornehmste unter den G.',
   'der vornehmste unter den <is n="Gandharva">G.</is>'),
  ('Sage kennt einen G.',
   'Sage kennt einen <is n="Gandharva">G.</is>'),
  ('{%der sich zu%} V. {%gesellt hat%}',
   '{%der sich zu%} <is n="Viśvāmitra">V.</is> {%gesellt hat%}'),
  ('<is>Ṛṣy</is>.',
   '<is n="Ṛṣyamūka">Ṛṣy.</is>'),
  ('als das höchste%} Br. {%verkündet%}',
   'als das höchste%} <is n="Brahma">Br.</is> {%verkündet%}'),
  # 20%
  ('{%Sohn der%} G., ein <ab>Bein.</ab>',
   '{%Sohn der%} <is n="Gāndinī">G.</is>, ein <ab>Bein.</ab>'),
  ('{%die g. Eheform%}',
   '{%die <is n="gandharva">g.</is> Eheform%}'),
  ('{%Freund der%} G.',
   '{%Freund der%} <is n="Gāyatrī">G.</is>'),
  # next two are 'together'
  ('<is>Padapāṭha</is> zum',
   '<ls>Padapāṭha zum SV.</ls>'),
  ('<ls>SV.</ls> nach <is>Durga</is>',
   'nach <is>Durga</is>'),
  ('<is>Hariv</is>. ein Sohn',
   '<is n="Harivaṃśa">Hariv.</is> ein Sohn'),
  ('<is>Gudap</is>.',
   '<is n="Gudaparinaddha">Gudap.</is>'),
  ('<is>Arj</is>.',
   '<is n="Arjuna">Arj.</is>'),
  ('<is>Dānava(</is>?)',
   '<is>Dānava</is>(?)'),
  # 21%
  ('<ls>WIND. <is>Sancara</is>',
   '<ls>WIND. Sancara'),
  ('<is>Kṛpī</is>',
   '<is>Kṛipī</is>'),   # spelling error?
  ('{%Verehrung der%} G.',
   '{%Verehrung der%} <is n="Gaurī">G.</is>'),
  ('Ufern der%} <is n="Sarasvatī">S.</is>',
   'Ufern der%} <is n="Sarasvatī">S.</is> {%auf%}'),
  ('{%ich habe die Worte des Br. vernommen%}',
   '{%ich habe die Worte des <is n="Brāhmaṇa">Br.</is> vernommen%}'),
  ('{%das Verfahren der%} <is>Atim</is>.',
   '{%das Verfahren der%} <is n="Atimuktālatā">Atim.</is>'),
  ('<is>Āhnikat</is>.',
   '<is n="Āhnikatattva">Āhnikat.</is>'),
  ('<is>Uṇ</is>.',
   '<is n="Uṇādisūtra">Uṇ.</is>'),
  # 22%
  ('{#agastyo hyAcarat#} A.',
   '{#agastyo hyAcarat#} <is n="Agastya">A.</is>'),
  ('{%les Y. qui forment son',
   '{%les <is n="Yavana">Y.</is> qui forment son'),
  ('der C. wird von',
   'der <is n="Caraka">C.</is> wird von'),
  ('{%ein%} R., {%der sich am 14ten',
   '{%ein%} <is n="Rakṣa">R.</is>, {%der sich am 14ten'),
  ('{%die von den C. bewohnte Gegend%}',
   '{%die von den <is n="Cāndrāyaṇa">C.</is> bewohnte Gegend%}'),
  ('<is>Kār</is> 2 aus <ls>KĀŚ.</ls>',
   '<is n="Kārikā">Kār.</is> 2 aus <ls>KĀŚ.</ls>'),
  # 23%
  ('J. vermöchten',
   '<is n="Yādava">Y.</is> vermöchten'),
  ('{%der Sohn der%} C.',
   '{%der Sohn der%} <is n="Citraśikhaṇḍi">C.</is> '),
  ('{%er trug ihm auf nach L. zu gehen%}',
   '{%er trug ihm auf nach <is n="Laṅkā">L.</is> zu gehen%}'),
  ('<is>Ādip</is>.',
   '<is n="Ādiparva">Ādip.</is>'),
  ('<is>Veda(</is>?)',
   '<is>Veda</is>(?)'),
  ('<is>Tatpur</is>.',
   '<is n="Tatpuruṣa">Tatpur.</is>'),
  ('<is>Kār</is> ',
   '<is n="Kārikā">Kār.</is> '),
  ('Bilde des%} V. {%entstanden%}',
   'Bilde des%} <is n="Viṣṇu">V.</is> {%entstanden%}'),
  ('(gleichfalls als Incarnation V.)',
   '(gleichfalls als Incarnation <is n="Viṣṇu">V.</is>)'),
  # 24%
  ('{%der einäugige%} J.',
   '{%der einäugige%} <is n="Janaka">J.</is>'),
  ('<is>Purūravas\'</is>',
   '<is>Purūravas</is>ʼ'),
  ('<ls>MBH. 7, Adhy. 85 — 152.</ls>',
   '<ls>MBH. 7, <is n="Adhyāya">Adhy.</is> 85—152</ls>.'),
  ('<is>Dakka</is>',
   'Dakka'),  # <iw>
  ('<ls>J.</ls> {%entsprechend, die%}',
   '<is n="Jagatī">J.</is> {%entsprechend, die%}'),
  ('<ls>J.</ls> {%eigenthümlich habend',
   '<is n="Jagatī">J.</is> {%eigenthümlich habend'),
  #('<ls>J.</ls> <ls>P. 4,2,55</ls>,',
  # '<is n="Jagatī">J.</is> <ls>P. 4,2,55,'),
  ('<ls>J.</ls> <ls>P. 4,2,55</ls>, <is n="Vārttika">Vārtt.</is>',
   '<is n="Jagatī">J.</is> <ls>P. 4,2,55, <is n="Vārttika">Vārtt.</is></ls>'),
  ('{%der das Wort Br. im Munde führt, der stets an die Br. denkt%}',
   '{%der das Wort <is n="Brāhmaṇa">Br.</is> im Munde führt, der stets an die<is n="Brāhmaṇa">Br.</is> denkt%}'),
  ('<ls>LASSEN, Pentap. 64 (<is>Śl.</is> 9).</ls>',
   '<ls>LASSEN, Pentap. 64 (Śl. 9)</ls>.'),
  ('<ls>RĀJA-TAR. I,550 (<is>Śl.</is> 9).</ls>',
   '<ls>RĀJA-TAR. I, 550 (Śl. 9)</ls>.'),
  # 25%
  ('<is>Bhodisattva</is>', '<is>Bodhisattva</is>'),
  ('<ls>J.</ls>, <ab>Bez.</ab> einer Art von Spiel',
   '<is n="Jīvaputra">J.</is>, <ab>Bez.</ab> einer Art von Spiel'),
  ('<is>Piśākī</is>',
   '<is>Piśācī</is>'),
  ('<is>Dhṛt</is>. {%mit, dass die%}',
   '<is n="Dhṛtarāṣṭra">Dhṛt.</is> {%mit, dass die%}'),
  ('P. {%verbrannt wären%}',
   '<is n="Pāṇḍava">P.</is> {%verbrannt wären%}'),
  ('P. {%erfahren, man weiss nichts von ihnen%}',
   '<is n="Pāṇḍava">P.</is> {%erfahren, man weiss nichts von ihnen%}'),
  ('P. {%Auge auf%}',
   '<is n="Pārtha">P.</is> {%Auge auf%}'),
  ('(<is>Allah</is>.)',
   '(Allah.)'),
  ('<is>Ṭhākur</is>',
   'Ṭhākur'),   # v1e <iw>
  ('<ls>P. 4,2,51</ls>, <is>Vartt</is>.',
   '<ls>P. 4,2,51, <is n="Vārttika">Vārtt.</is></ls>'),
  ('{%die Einwohner von%} T.',
   '{%die Einwohner von%} <is n="Takṣaśilā">T.</is> '),
  ('<is>ta-t\'sa-na</is>',
   'ta-tʼsa-na'),  # v1e <iw>
  ('<is>Ab</is>handlung',
   'Abhandlung'),
  ('{%der Brunnen des%} T.',
   '{%der Brunnen des%} <is n="Tathāgata">T.</is>,'),
  # 26%
  ('{%das Mysterium des%} <is>Tath</is>.,',
   '{%das Mysterium des%} <is n="Tathāgata">Tath.</is>,'),
  ('<is>Rakṣas\'</is>',
   '<is>Rakṣas</is>ʼ'),
  ('<is>Gandharva(?</is>)',
   '<is>Gandharva</is>(?)'),
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
 lines0 = adjust_lines0(lines)
 #lines0 = lines
 lines1 = adjust_lines1(lines0)
 write_lines(fileout,lines1)
