05-11-2025
ejf

Problems related to     '<ls n="H. an.">an. '
Ref: https://github.com/sanskrit-lexicon/PWG/issues/104

--------------------------------------------------
Two reference forms in pwg:
 (counts from issue94/lsextract_all.txt)
09971	H. an.	HEMACANDRA'S ANEKĀRTHASAM̃GRAHA, ed. Cal
01797	an.	ANEKĀRTHASAM̃GRAHA (s. H. an.).

'H. an. N,N' forms are linked via
 https://sanskrit-lexicon-scans.github.io/anekarthasamgraha/app1/?N,N

'an. N,N' forms are NOT YET LINKED.


Many of the 'an.' forms are preceded by another
--------------------------------------------------
some counts of regex in current pwg.txt


* DONE 3143 matches in 3142 lines for "<ls>H. an. [0-9]+,[0-9]+"
2 matches for "<ls n="H. an.">[0-9]+,[0-9]+"

link  https://sanskrit-lexicon-scans.github.io/anekarthasamgraha/app1/?N,N
4 matches for "<ls>H. an. [^0-9]"   all are irregular.

* DONE 6 matches for "<ls>H. an. [0-9]+[^0-9,]"  may be typos

aBaya    36623:<ls>H. an. 3. 477.</ls> -> <ls>H. an. 3,477.</ls>
govinda 220299:<ls>H. an. 3. 331.</ls> -> <ls>H. an. 3,331.</ls>
niryUha 386248:<ls>H. an. 765</ls> -> <ls>H. an. 3,765</ls> L=39615 PRINT CHANGE
roka    773042:<ls>H. an. 2. 15.fg.</ls> -> <ls>H. an. 2,15. fg.</ls> 
vayaHsTa 802722:<ls>H. an. 3. 320.</ls> -> <ls>H. an. 3,320.</ls> 
saMvAhana 953624:<ls>H. an. 4. 200. fg.</ls> -> <ls>H. an. 4,200. fg.</ls>
* DONE 1752 matches for "<ls>an. [0-9]+,[0-9]+"  not linked - basicadjust
  basicadjust modified to generate links to 
   https://sanskrit-lexicon-scans.github.io/anekarthasamgraha/app1/?N,N

* DONE OK 0 matches for "<ls n="an.">[0-9]+,[0-9]+"
* DONE OK 2 matches for "<ls n="H. an.">[0-9]+,[0-9]+"  
* TODO 181 matches for "<ls n="H. an.">an. [0-9]+,[0-9]+" markup PROBLEM
  These usually (always?) after a preceding <ls>H. N</ls>

  Solution:  revise pwg manual change
  '<ls n="H. an.">an. '  => '<ls>an. '
