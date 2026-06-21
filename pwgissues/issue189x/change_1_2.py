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
  ('<is>avy</is>.', 'avy.'),
  ('<is>Śaṃkar</is>.', '<is>Śaṃkar.</is>'),
  ('{%Br. beschützt',
   '{%<is>Br.</is> beschützt'),
  ('<is>KŪRMA-P.</is>', '<ls>KŪRMA-P.</ls>'),
  ('<is>padap</is>.',
   '<ls n="Padapāṭha">padap.</ls>'),
  ('<is>Suśr</is>.',
   '<ls>SUŚR.</ls>'),
  ('<is>Vaij</is>.', '<is n="Vaijayantī">Vaij.</is>'),
  ('<is>Kull</is>.', '<ls n="Kullūka">Kull.</ls>'),  # oddity ls n=
  ('<ls>ŚIVA</ls>, <is>Śiv</is>.', '<is>Śiva</is>, <ls>ŚIV.</ls>'),
  ('<ls>MED. <is>kh</is>.',
   '<ls>MED. kh.'),
  ('<ls>ŚIVA</ls>, <ls>ŚIV.</ls>',
   '<is>Śiva</is>, <ls>ŚIV.</ls>'),
  ('<is>Padap</is>.',
   '<ls n="Padapāṭha">padap.</ls>'), # oddity ls n=
  ('<ls>R.</ls> {%Armen gefallen%}',
   '<is n="Rāvaṇa">R.</is> {%Armen gefallen%}'),
  ('<is>Dschemschid</is>', 'Dschemschid'),  # v1e: <iw>Dschemschid</iw>
  ('<is>Feridun</is>', 'Feridun'), #v1e <iw>Feridun</iw>
  ('(<is>Aymer?</is>)', '(Ajmer?)'),
  ('die Nachkommen des A.', 'Nachkommen des <is n="Ajavasti">A.</is>'),
  ('<ls>ŚĀRṄG. PADDH.</ls> <is>Sāmānyarājapraśaṃsā</is>.',
   '<ls>ŚĀRṄG. PADDH. Sāmānyarājapraśaṃsā</ls>.'),
  ('A. in eine bestimmte Person',
   '<is n="Atharvan">A.</is> in eine bestimmte Person'),
  ('A. ist bei der Erschaffung',
   '<is n="Atharvaṇa">A.</is> ist bei der Erschaffung'),
  ('<is>Ang</is>.',
   '<is n="Angiras">Ang.</is>'),
  ('<is>Ath</is>.',
   '<is n="Atharvan">Ath.</is>'),
  ('<is>Kāś</is>.', '<is n="Kāśikā">Kāś.</is>'),
  ('brahmadattaH#} Br.',
   'brahmadattaH#} <is n="Brahmadatta">Br.</is>'),
  ('{%die%} Kh. {%ist grösser als der%} Dr.',
   '{%die%} <is n="Khārī">Kh.</is> {%ist grösser als der%} <is n="Droṇa">Dr.</is>'),
  ('R. {%setzte%}',
   '<is n="Rākśasa">R.</is> {%setzte%}'),
  #('<is>Padap.</is> {#ananu\'kftya#}',
  # '<ls n="Padapāṭha">padap.</ls> {#ananu\'kftya#}'),
  ('<is>Padap.</is>',
   '<ls n="Padapāṭha">padap.</ls>'),
  ('{%ich werde%} R. {%das Geleit geben%}',
   '{%ich werde%} <is n="Rāma">R.</is> {%das Geleit geben%}'),
  ('{%aus Gehorsam zu%} Bh.',
   '{%aus Gehorsam zu%} <is n="Bharata">Bh.</is>'),
  ('(gegen K.)',
   '(gegen <is n="Kaikeyya">K.</is>)'),
  ('Sohn <is>Āyu</is>ʼs (<is>Āyus\'</is>)',
   'Sohn <is>Āyu</is>ʼs (<is>Āyus</is>ʼ)'),
  ('zwischen dir und K.',
   'zwischen dir und <is n="Kātyāyanī">K.</is>'),
  ('vAkyamabravIt#} R. {%im',
   'vAkyamabravIt#} <is n="Rāvaṇa">R.</is> {%im'),
  ('<ls>R.</ls> im <ls>VYAVAHĀRAT.',
   '<is n="Raghunandana">R.</is> im <ls>VYAVAHĀRAT.'),
  ('<ls>SV.</ls> <ls>Ind. St. I,59.</ls>',
   '<ls>Ind. St. I,59.</ls>'),
  ('<is>Pariśiṣṭa</is> zum',
   '<ls>Pariśiṣṭa zum SV.</ls>'),
  ('<ls>M.</ls> {%noch%} Ś.',
   '<is n="Mādhava">M.</is> {%noch%} <is n="Śiva">Ś.</is>'),
  ('<is>Trig</is>.',
   '<is n="Trigarta">Trig.</is>'),
  ('{%die Nachkommen des%} <is>A</is>.',
   '{%die Nachkommen des%} <is n="Apiśala">A.</is>'),
  ('<is>Kādamb</is>.',
   '<is n="Kādambarī">Kādamb.</is>'),
  ('<is>Gov</is>.',
   '<is n="Govinda">Gov.</is>'),
  ('{#BaradvAjABi˚#} {%des%} Bh. (<ab>obj.</ab>)',
   '{#BaradvAjABi˚#} {%des%} <is n="Bharadvāja">Bh.</is>'),
  ('{%der den <is>Soma</is>saft auspressende Priester%}',
   '{%der den Somasaft auspressende Priester%}'),
  ('<ls>M.</ls> <ls>R. 3,46</ls>',
   '<is n="Marīci">M.</is> <ls>R. 3,46</ls>'),
  ('<is>Amritsir</is>',  # v1e iw
   'Amritsir'),
  
  # 5%
  
  ('<ls>MED. <is>avy.</is>',
   '<ls>MED. avy.'),
  ('{%wenn der%} A. {%in der%}',
   '{%wenn der%} <is n="Adhvaryu">A.</is> {%in der%}'),
  ('dieselbe%} A. {%gerichtet ist%}',
   'dieselbe%} <is n="Apsara">A.</is> {%gerichtet ist%}'),
  ('I. {%gehörig%}',
   '<is n="Indra.">I.</is> {%gehörig%}'),
  ('<is>Cakrav</is>.', '<is n="Cakravartin">Cakrav.</is>'),
  ('<is>Trip</is>.', '<is n="Tripurāvadāna">Trip.</is>'),
  ('<is>Kur</is>.',
   '<is n="Kurkṣetra">Kur.</is>'),  # Spelling error?
  ('schlechter als%} A.) {#purIm#}',
   'schlechter als%} <is n="Alakā">A.</is>'),
  ('<is>Avas</is>.',
   '<is n="Avasarpiṇī">Avas.</is>'),
  ('<is>Uts</is>.',
   '<is n="Utsarpiṇī">Uts.</is>'),
  ('<is>Uts.</is>',
   '<is n="Utsarpiṇī">Uts.</is>'),
  ('{%die%} O. {%erreicht ihr',
   '{%die%} <is n="Oṣadhi">O.</is> {%erreicht ihr'),
  # 6%
  
  ('<is>Adhy</is>.',
   '<is n="Adhyāya">Adhy.</is>'),
  ('Gemahlin%} R. {%berichten%}',
   'Gemahlin%} <is n="Rāma">R.</is> {%berichten%}'),
  ('{%Litanei an%} A. {%und die%}',
   '{%Litanei an%} <is n="Agni">A.</is> {%und die%}'),
  ('<ls>M.</ls> <ls>AIT. BR. 3,35.',
   '<is n="Māruta">M.</is> <ls>AIT. BR. 3,35.'),
  ('<is>Agnīdh</is>.',
   '<is n="Agnīdhra">Agnīdh.</is>'),
  ('(Tochter <is>Agni\'s?</is>)',
   '(Tochter <is>Agni</is>ʼs?)'),
  # 7%
  ('M. {%den Anfang macht%}, <ab>d. h.</ab> M.',
   '<is n="Marīci">M.</is> {%den Anfang macht%}, <ab>d. h.</ab> <is n="Marīci">M.</is>'),
  ('<ls>R.</ls> {%erblickte%}',
   '<is n="Rāma">R.</is> {%erblickte%}'),
  ('<is>Mādhy</is>.',
   '<is n="Mādhyaṃdina">Mādhy.</is>'),
  ('{%König der%} <is>Ā</is>.',
   '{%König der%} <is n="Āmbaṣṭha">Ā.</is>'),
  ('{%er machte%} R. {%zu schaffen%}',
   '{%er machte%} <is n="Rāma">R.</is> {%zu schaffen%}'),
  # 8%
  ('<ab>Beiw.</ab> des R. in den',
   '<ab>Beiw.</ab> des <is n="Ṛṣi">R.</is> in den'),
  ('gefallener <is>Brahmanen</is>',
   'gefallener Brahmanen'),
  ('des%} M. {%errathen hatte%}',
   'des%} <is n="Muni">M.</is> {%errathen hatte%}'),
  ('sich über%} V. {%und wurden',
   'sich über%} <is n="Vaiśvānara">V.</is> {%und wurden'),
  # 9%
  ('<is>Āhv</is>.',
   '<is n="Āhvāraka">Āhv.</is>'),
  ('mit der%} T. {%vereinigt%}',
   'mit der%} <is n="Tāmraparṇi">T.</is> {%vereinigt%}'),
  ('dass es%} <is>Bh</is>.',
   'dass es%} <is n="Bhaimī">Bh.</is>'),
  ('(<is>Brahman?</is>)',
   '(<is>Brahman</is>?)'),
  ('{%den dem%} <is>Ā.</is> {%vorangehenden',
   '{%den dem%} <is n="Āṣāḍha">Ā.</is> {%vorangehenden'),
  ('dass die%} K. {%am Leben',
   'dass die%} <is n="Kauravya">K.</is> {%am Leben'),
  ('{%<is>nemaqyāmahī</is> <is>iṣūidyāmahī</is> <is>thwā</is> <is>mazdā</is> <is>ahurā</is>%}',
   '{%nemaqyāmahī iṣūidyāmahī thwā mazdā ahurā%}'),  # ve1 <iw>
  ('<is>Adhv</is>.',
   '<is n="Adhvaryu">Adhv.</is>'),
  ('({%vor%} V. {%Angesicht%})',
   '({%vor%} <is n="Vaidarbhī">V.</is> {%Angesicht%})'),
  ('durch%} L. {%Pfeile',
   'durch%} <is n="Lakṣmaṇa">L.</is> {%Pfeile'),
  ('(<is>Śiva?</is>)',
   '(<is>Śiva</is>?)'),
  ('{%der erhabene%} U.',
   '{%der erhabene%} <is n="Uccaiḥ">U.</is>'),
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

def unused_adjust_lines0(lines):
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
 #lines0 = adjust_lines0(lines)
 lines0 = lines
 lines1 = adjust_lines1(lines0)
 write_lines(fileout,lines1)
