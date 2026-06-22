
06-21-2026 begin ejf

## 

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issues/191

# this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue191

* Andhrabharati version v1e of pwg.txt
# local copy . See #180 for a zip of this
../issue180/temp_ab_pwg_v1e.txt

 api1/salt_common.php       | 220 +++++++++++++++
 api1/salt_entries.php      |  39 +++
 api1/salt_entriesClass.php |  55 ++++
 api1/salt_graphql.php      |  14 +
 api1/salt_graphqlClass.php | 122 ++++++++
 api1/salt_ids.php          |  33 +++
 api1/salt_idsClass.php     |  27 ++
 api1/salt_selftest.php     |  77 ++++++
 basicadjust.php            |   6 +-
 basicdisplay.php           |   8 +-
 dictinfo.php               |   7 +-
 dispitem.php               |   2 +-
 doc/readme.md              |   5 +-
 doc/salt_api_handoff.md    | 216 +++++++++++++++
 doc/salt_api_usecases.md   | 145 ++++++++++
 doc/salt_entries.md        | 100 +++++--
 doc/salt_graphql.md        |  45 ++-
 doc/salt_ids.md            |  36 ++-
 getword_data.php           |   4 +-
 sample/dictnames.js        |   1 +
 24 files changed, 1896 insertions(+), 48 deletions(-)
 
-------------------------------------
* pwg history in csl-orig
cd /c/xampp/htdocs/cologne/csl-orig/
git pull

git log --follow --pretty=format:"%ad %h %an %s" --date=short -- v02/pwg/pwg.txt > temp_history_pwg.txt

mv temp_history_pwg.txt /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue191/history_pwg.txt

* temp_pwg_c10d4c8.txt pwg commit preceding v1e
Dr. Dhaval Patel PWG fully copied from v1e of AB

cd /c/xampp/htdocs/cologne/csl-orig/
git show c10d4c8:v02/pwg/pwg.txt > temp_pwg_c10d4c8.txt

mv temp_pwg_c10d4c8.txt /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue191/
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue191


* temp_pwg_7d90e9d.txt  pwg commit -- v1e
Dr. Dhaval Patel PWG fully copied from v1e of AB

git show 7d90e9d:v02/pwg/pwg.txt > temp_pwg_7d90e9d.txt

mv temp_pwg_7d90e9d.txt /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue191/

diff ../issue180/temp_ab_pwg_v1e.txt temp_pwg_7d90e9d.txt 
272053c272053
< <div n="1">— 3〉 <lex>n.</lex> <bot>Costus arabicus<bot> {%oder%} <bot>speciosus</bot> ({#kuzWa#}) <ls>ŚABDAC.</ls>_im_<ls>ŚKDR.</ls>
---
> <div n="1">— 3〉 <lex>n.</lex> <bot>Costus arabicus</bot> {%oder%} <bot>speciosus</bot> ({#kuzWa#}) <ls>ŚABDAC.</ls>_im_<ls>ŚKDR.</ls>

* temp_pwg_5bdfb72.txt latest commit to pwg
2026-06-21 5bdfb72 Dr. Dhaval Patel PWG pending blank n=""
   LS added. Close https://github.com/sanskrit-lexicon/PWG/issues/189

cd /c/xampp/htdocs/cologne/csl-orig/

git show 5bdfb72:v02/pwg/pwg.txt > temp_pwg_5bdfb72.txt

mv temp_pwg_5bdfb72.txt /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue191/

* pull csl-pywork

cd /c/xampp/htdocs/cologne/csl-pywork/
git pull
 v02/generate_ab_bib_ls.sh                   |   2 +-
 v02/makotemplates/downloads/redo_all.sh     |  23 +-
 v02/makotemplates/pywork/hw.py              |  12 +-
 v02/makotemplates/pywork/hwparse.py         |   2 +-
 v02/makotemplates/pywork/make_xml.py        |  50 +-
 v02/makotemplates/pywork/one.dtd            |  22 +-
 v02/makotemplates/pywork/sqlite/sqlite.py   |   6 +-
 v02/redo_cologne_all.sh                     |   1 +
 v02/redo_xampp_all.sh                       |   1 +

* pull csl-websanlexicon
cd /c/xampp/htdocs/cologne/csl-websanlexicon/
git pull

 v02/dictparms.py                              |  15 +-
 v02/distinctfiles/nmmb/web/webtc/pdffiles.txt |  40 ++
 v02/makotemplates/web/webtc/basicadjust.php   |   2 +-
 v02/makotemplates/web/webtc/basicdisplay.php  |   8 +-
 v02/makotemplates/web/webtc/dictinfo.php      |   5 +-
 v02/makotemplates/web/webtc/dispitem.php      |   2 +-
 v02/makotemplates/web/webtc/getword_data.php  |   4 +-
 v02/redo_cologne_all.sh                       |   1 +
 v02/redo_xampp_all.sh                         |   1 +

* pull csl-apidev
cd /c/xampp/htdocs/cologne/csl-apidev/
git pull
remote: Enumerating objects: 38, done.
remote: Counting objects: 100% (25/25), done.
remote: Compressing objects: 100% (8/8), done.
remote: Total 38 (delta 18), reused 17 (delta 17), pack-reused 13 (from 1)
Unpacking objects: 100% (38/38), 53.30 KiB | 359.00 KiB/s, done.
From https://github.com/sanskrit-lexicon/csl-apidev
   6db450b..9f930ab  master     -> origin/master
Updating 6db450b..9f930ab
Fast-forward
 .ai_state.md               |  57 ++++
 CHANGELOG.md               |  47 ++++
 LICENSE                    | 675 +++++++++++++++++++++++++++++++++++++++++++++
 README.md                  |   3 +-
 api1/salt_common.php       | 220 +++++++++++++++
 api1/salt_entries.php      |  39 +++
 api1/salt_entriesClass.php |  55 ++++
 api1/salt_graphql.php      |  14 +
 api1/salt_graphqlClass.php | 122 ++++++++
 api1/salt_ids.php          |  33 +++
 api1/salt_idsClass.php     |  27 ++
 api1/salt_selftest.php     |  77 ++++++
 basicadjust.php            |   6 +-
 basicdisplay.php           |   8 +-
 dictinfo.php               |   7 +-
 dispitem.php               |   2 +-
 doc/readme.md              |   5 +-
 doc/salt_api_handoff.md    | 216 +++++++++++++++
 doc/salt_api_usecases.md   | 145 ++++++++++
 doc/salt_entries.md        | 100 +++++--
 doc/salt_graphql.md        |  45 ++-
 doc/salt_ids.md            |  36 ++-
 getword_data.php           |   4 +-
 sample/dictnames.js        |   1 +
 24 files changed, 1896 insertions(+), 48 deletions(-)
 create mode 100644 LICENSE
 create mode 100644 api1/salt_common.php
 create mode 100644 api1/salt_entries.php
 create mode 100644 api1/salt_entriesClass.php
 create mode 100644 api1/salt_graphql.php
 create mode 100644 api1/salt_graphqlClass.php
 create mode 100644 api1/salt_ids.php
 create mode 100644 api1/salt_idsClass.php
 create mode 100644 api1/salt_selftest.php
 create mode 100644 doc/salt_api_handoff.md
 create mode 100644 doc/salt_api_usecases.md

* validate displays of pwg, mw, ap

* csl-apidev further change to basicadjust.php, basicdisplay.php
# for compatibility with csl-websanlexicon.
cd /c/xampp/htdocs/cologne/csl-websanlexicon/
sh apidev_copy.sh
* DONE csl-apidev  push
* DONE generate pwg displays with current csl-orig pwg.txt  OK
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok

* xmltags for temp_pwg_c10d4c8.txt
python xmltag.py temp_pwg_c10d4c8.txt xmltag_c10d4c8.txt
# 14 distinct tags written to xmltag_c10d4c8.txt

* xmltags for temp_pwg_5bdfb72.txt
python xmltag.py temp_pwg_5bdfb72.txt xmltag_5bdfb72.txt
32 distinct tags written to xmltag_5bdfb72.txt
* xmltag_diff.txt
python abdiff.py xmltag_c10d4c8.txt xmltag_5bdfb72.txt xmltag_diff.txt
* lang tag
former usage: <lang n="LANGNAME">TEXT</lang>
old:  hw = 'a', L=3
<lang>griech.</lang> <lang n="greek">ἀ, ἀν</lang>
new:
<lang>griech.</lang> <gk>ἀ, ἀν</gk>

Note: tooltips missing.
 Revised pwgab_input.txt at #188 (pushed csl-pywork to github).

* THE END
