
Improve ls markup in pwg

pwgbib_input.txt is from csl-pywork/v02/distinctfiles/pwg/pywork/pwgauth/

pwg_00.txt is csl-orig/v02/pwg/pwg.txt at commit
   e4ebfb11e8b610a6559b0cbced0f2715aee95323

python lsfilter.py abbrev pwg_01.txt pwg_tooltip.txt lsfilter_01.txt
python lsfilter.py 'ṚV.' pwg_00.txt pwg_tooltip.txt lsfilter_RV.txt

python lsfilter.py 'ṚV.' pwg_01.txt pwg_tooltip.txt lsfilter_RV_0.txt
  # 0-parameters
python lsfilter_irreg.py 'ṚV.' pwg_01.txt pwg_tooltip.txt lsfilter_RV_irreg.txt
python lsfilter_irreg.py 'ṚV.' pwg_00.txt pwg_tooltip.txt lsfilter_RV_irreg_before.txt


 See readme_filter_RV_initial.txt for initial statistics on ṚV. with
 number of parameters.
 Currently about 13000 out of 18000 have 3 parameters (the desired)
 We want to recode the remainder so that most will end up with 3 parameters.


changes_01.txt
python changes_01a.py 'ṚV.' pwg_00.txt pwg_tooltip.txt temp_changes_01a.txt
  ṚV.  3 parameters with irregularities (about 134)
  unresolved in todo_changes_01a.txt (about 50)
  about 80 changes made in changes_01.txt

python changes_01b.py 'ṚV.' pwg_01.txt pwg_tooltip.txt temp_changes_01b.txt
  <ls>ṚV. a, b, c. d, e, f.<ls> =>
  <ls>ṚV. a, b, c.</ls> <ls n="ṚV.">d, e, f.</ls>
  1400 cases found
python changes_01c.py 'ṚV.' pwg_01.txt pwg_tooltip.txt temp_changes_01c.txt
  <ls>ṚV. a, b, c. d, e, f. g, h, i.<ls> =>
  <ls>ṚV. a, b, c.</ls> <ls n="ṚV.">d, e, f.</ls> <ls n="ṚV.">g, h, i.</ls>
  339 cases found
python changes_01d.py 'ṚV.' pwg_01.txt pwg_tooltip.txt temp_changes_01d.txt
  # similar, but with 12 parameters
  76 cases
python changes_01e.py 'ṚV.' pwg_01.txt pwg_tooltip.txt temp_changes_01e.txt
  # similar, but with 15 parameters
  13 cases
python changes_01f.py 'ṚV.' pwg_01.txt pwg_tooltip.txt temp_changes_01f.txt
  # partial factoring of ṚV.
  
python updateByLine.py pwg_00.txt changes_01.txt pwg_01.txt

cp pwg_01.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt

Next add markup to 'numerical' ls elements preceded by ṚV. ls elements.
Do this in another version of pwg.
cp pwg_01.txt pwg_02.txt

python changes_02a.py 'ṚV.' pwg_02.txt pwg_tooltip.txt temp_changes_02a.txt

# the remaining unmarked numerical ls cases for RV.
python lsfilter_none.py 'ṚV.' pwg_02.txt pwg_tooltip.txt temp_lsfilter_none.txt

python changes_02b.py 'ṚV.' pwg_02.txt pwg_tooltip.txt temp_changes_02b.txt

python changes_02a.py 'ṚV.' pwg_02.txt pwg_tooltip.txt temp_changes_02a_2.txt

python changes_02b.py 'ṚV.' pwg_02.txt pwg_tooltip.txt temp_changes_02b_2.txt

python changes_02a.py 'ṚV.' pwg_02.txt pwg_tooltip.txt temp_changes_02a_3.txt
python changes_02b.py 'ṚV.' pwg_02.txt pwg_tooltip.txt temp_changes_02b_3.txt
python changes_02a.py 'ṚV.' pwg_02.txt pwg_tooltip.txt temp_changes_02a_4.txt
python changes_02b.py 'ṚV.' pwg_02.txt pwg_tooltip.txt temp_changes_02b_4.txt
python changes_02a1.py 'ṚV.' pwg_02.txt pwg_tooltip.txt temp_changes_02a1_1.txt

python changes_02c.py 'ṚV.' pwg_02.txt pwg_tooltip.txt temp_changes_02c_1.txt
python changes_02a.py 'ṚV.' pwg_02.txt pwg_tooltip.txt temp_changes_02a_5.txt
python changes_02b.py 'ṚV.' pwg_02.txt pwg_tooltip.txt temp_changes_02b_5.txt
python changes_02a.py 'ṚV.' pwg_02.txt pwg_tooltip.txt temp_changes_02a_6.txt
python changes_02b.py 'ṚV.' pwg_02.txt pwg_tooltip.txt temp_changes_02b_6.txt
python temp_lsfilter_none.py 'ṚV.' pwg_02.txt pwg_tooltip.txt temp.txt

python changes_02a.py 'ṚV.' pwg_02.txt pwg_tooltip.txt temp_changes_02a_7.txt
python changes_02b.py 'ṚV.' pwg_02.txt pwg_tooltip.txt temp_changes_02b_7.txt

python updateByLine.py pwg_01.txt changes_02.txt pwg_02.txt

cp pwg_02.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt

python lsfilter_irreg.py 'ṚV.' pwg_02.txt pwg_tooltip.txt lsfilter_RV_irreg_02.txt
-------------------------------------------------------------
'ṚV.' appearing other than in <ls>ṚV.  or <ls n="ṚV.
cp pwg_02.txt pwg_03.txt
python changes_03a.py 'ṚV.' pwg_03.txt pwg_tooltip.txt temp_changes_03a.txt
  268 cases generated.
  
python updateByLine.py pwg_02.txt changes_03.txt pwg_03.txt

cp pwg_03.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt

python lsfilter_irreg.py 'ṚV.' pwg_03.txt pwg_tooltip.txt lsfilter_RV_irreg_03.txt
------------------------------------------------------------
python dict_2_changes.py pwg_00.txt pwg_03.txt changes.txt

python lsextract.py 'ṚV.' pwg_00.txt pwg_tooltip.txt lsextract_RV_00.txt
python lsextract.py 'ṚV.' pwg_03.txt pwg_tooltip.txt lsextract_RV_03.txt

python lsfilter_irreg.py 'ṚV.' pwg_03.txt pwg_tooltip.txt lsfilter_RV_irreg_03.txt
python lsfilter_irreg.py 'ṚV.' pwg_00.txt pwg_tooltip.txt lsfilter_RV_irreg_00.txt
python lsfilter_0parm.py 'ṚV.' pwg_03.txt pwg_tooltip.txt lsfilter_RV_0parm_03.txt
