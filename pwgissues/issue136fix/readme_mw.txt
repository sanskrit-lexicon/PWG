
mw  
python lsfix2.py mw temp_mw_0.txt lsfix2_mw_0.txt

298 lines written to lsfix2_mw_0.txt
(None, 3) 298

lsfix2 does not handle fixes to mw, since first parm is in roman.
Identify problems by sequence of manual regexes

cp temp_mw_0.txt temp_mw_1.txt

138 <ls>KātyŚr. [ixv]+, [0-9]+, [0-9]+\.?</ls>  ;; linked
 10 <ls n="KātyŚr.">[ixv]+, [0-9]+, [0-9]+\.?</ls>  ;; linked
  5 <ls n="KātyŚr. [xiv]+,">[0-9]+, [0-9]+\.?</ls>  ;; linked
  5 <ls n="KātyŚr. [xiv]+, [0-9]+,">[0-9]+\.?</ls>  ;; linked
(+ 138 10 5 5) = (158)
Irregular linked: (3)
<ls>KātyŚr. vii, 8, 2 f.</ls>	  ;; linked
<ls>KātyŚr. iii, 3, 12/13</ls>	  ;; linked
<ls>KātyŚr. xxvi, 7, 50/51.</ls>  ;; linked

 20 <ls n="KātyŚr.">[xiv]+\.?</ls>  ;; not linked
 84 <ls>KātyŚr. [xiv]+\.?</ls> ;; not linked
 13 <ls>KātyŚr. [xiv]+, [0-9]+\.?</ls> ;; not linked
  8 <ls>KātyŚr. [xiv]+ f+.?</ls>  ;; not linked
  2 <ls n="KātyŚr.">xii f.</ls>  ;; not linked
  5 <ls>KātyŚr. [xiv]+, [0-9]+, <ab>Paddh.</ab></ls>
  (+ 20 84 13 8 2 5) (132)

misc. not linked: (5)
<ls n="KātyŚr.">iv, 8, <ab>Paddh.</ab></ls>
<ls>KātyŚr. iv, <ab>Paddh.</ab></ls>
<ls>KātyŚr. <ab>Comm.</ab></ls>
<ls>KātyŚr. <ab>Paddh.</ab></ls>
<ls>KātyŚr. <ab>Paddh.</ab></ls>

(+ 158 3 132 5) ==  (298)

NO CHANGES TO mw.

