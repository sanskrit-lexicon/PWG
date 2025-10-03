issue86fix/readme_mw.txt
09-29-2025 begun ejf
fix mw references to  Pa�catantra, Kosegarten, 1848  

--------------------------------------
forms of reference:
 mw: 
  Pa�cat. N,N  : ipage, linenum
  Pa�cat. R,N  : tantra, verse  R is roman numeral. I,II,III,IV,V
  Pa�cat. Introd. N : prastava N = verse

We use lsfix2.py, with parmfile lsfix2_parm.py
 This version handles both N,N and R,N.
 It is specific to PA�CAT.

============================================================
# split work for mw
python lsfix2.py mw2 temp_mw_0.txt lsfix2_mw_0.txt
(None,280),(all,280) lsfix2_mw_0.txt


34674 : upadAtf : 


good  example 
34 matches for "<ls>Pa�cat. [iv]+, [0-9]+\.?</ls>" in buffer: tempwork_lsfix2_mw_0.txt

cp temp_mw_0.txt temp_mw_1.txt

edits to temp_mw_1.txt


------------------------------------------------
AFter revisions to temp_mw_1.txt:

python lsfix2.py mw2 temp_mw_1.txt lsfix2_mw_1.txt

188286 : vallaBa : Pa�cat. iv, 27/28 : Pa�cat. iv, 67/68 : print change
47157 : kAkaruka : Pa�cat. ix, 15 : Pa�cat. 9, 15 : print change
48576 : kArayitavya : Pa�cat. xxiv : Pa�cat. 24,21 : print change
50471 : kiyat : Pa�cat. lii, 4 : Pa�cat. 52, 4 : print change
50588.3 : kila : Pa�cat. lxxxix, 4 : Pa�cat. 89, 4 : print change
62425: gajADyakza : Pa�cat. iii, 67/68 : Pa�cat. iii, 66/67 : print change
70549 : cakrANkitA : Pa�cat. iii, 73/74 : Pa�cat. iii, 72/73 : print change
78079 : jalavAhaka : Pa�cat. iii, 67/68 : Pa�cat. iii, 66/67 : print change
84047 : tAmbUlavAhaka : Pa�cat. iii, 67/68 : Pa�cat. iii, 66/67 : print change
85572 : tIrTa : Pa�cat. iii, 67/68 : Pa�cat. iii, 66/67 : print change
34674 : upadAtf : Pa�cat. iv, 107 (ed. Bombay) : Pa�cat. (ed. Bombay) iv, 107 : To avoid link to Kosegarten : print change

---

kzIRa	<ls n="Pa�cat. iv,">32</ls>  display link fails ? basicadjust
vrajana	<ls n="Pa�cat.">iii, 268</ls> ? basicadjust
760538	saktuGawAKyAyikA	<ls n="Pa�cat. v,">74</ls>  ? basicadjust
258776	jaqAtman	<ls n="Pa�cat.">iii, 11/12</ls>  ? basicadjust
guRigaRa	<ls>Pa�cat. Introd. 7.</ls>  ? basicadjust

33 matches "<ls>Pa�cat. [iv]+, [0-9]+\.?</ls>  most are ok.see lsfix2_mw_1a.txt
28 matches for "<ls>Pa�cat. [iv]+, [0-9]+/[0-9]+\.?</ls>

  271041	jYApaka	<ls>Pa�cat. iii, 67/68</ls>  cannot find
  664713	viluRw	<ls>Pa�cat. iii, 32/83</ls>  cannot find

 

 2 matches "<ls>Pa�cat. [0-9]+, [0-9]+\.?</ls>
31 matches for "<ls>Pa�cat. [iv]+\.?</ls>"  no link
104 matches in 103 lines for "[iv]+, [0-9]+, [0-9]+"  probably bombay ed.
  Probably Bombay edition.


----------------------------
# No need generate temp_mw_2.txt from temp_mw_1.txt
 as there are no 'fixed' elements

-----------------------------------------------------------
# remake xml from temp_mw_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue86fix
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue86fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

---- documentation in change files
python diff_to_changes_dict.py temp_mw_0.txt temp_mw_1.txt change_mw_1.txt
15 changes written to change_mw_1.txt
