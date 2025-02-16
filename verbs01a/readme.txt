
pwg/verbs01a.

Analysis of pwg verbs and upasargas, revised
This work was done in a temporary subdirectory (temp_verbs01a) of csl-orig/v02/pwg/.

The shell script redo.sh reruns 5 python programs, from mwverb.py to preverb1.py.


* mwverbs
python mwverb.py mw ../../mw/mw.txt mwverbs.txt
#copy from v02/mw/temp_verbs
#cp ../../mw/temp_verbs/verb.txt mwverbs.txt
each line has 5 fields, colon delimited:
 k1
 L
 verb category: genuinroot, root, pre,gati,nom
 cps:  classes and/or padas. comma-separated string
 parse:  for pre and gati,  shows x+y+z  parsing prefixes and root

* mwverbs1.txt
python mwverbs1.py mwverbs.txt mwverbs1.txt
Merge records with same key (headword)
Also  use 'verb' for categories root, genuineroot, nom
and 'preverb' for categories pre, gati.
Format:
 5 fields, ':' separated
 1. mw headword
 2. MW Lnums, '&' separated
 3. category (verb or preverb)
 4. class-pada list, ',' separated
 5. parse. Empty for 'verb' category. For preverb category U1+U2+...+root

* pwg_verb_filter.

python pwg_verb_filter.py ../pwg.txt pwg_verb_exclude.txt pwg_verb_include.txt pwg_verb_filter.txt

pwg_verb_exclude.txt contains metalines for records that are NOT verbs,
but that have some of the patterns for roots.  
pwg_verb_include.txt contains metalines for records that are believed to be
verbs, but that are not identified by the verb patterns.
These files are derived empirically.

Patterns for roots:
 3 = '¦[ ,]*{#[^#]*t[ie]#}'   Example: {#aMSApay#}¦, {#aMSApa/yati#} 
 D = '<ls>DHĀTUP.'
 N = '[dD]enom[.] von'
 S = Sautra
 U = Has upasarga text. <div n="p">— {#([a-zA-Z]+)#}
  (pwg_verb_exclude_lex.txt)

Counts of total patterns:
0201 3
0778 3D
0011 3DN
0013 3DNU
0002 3DS
0001 3DSU
0461 3DU
0061 3N
0001 3NU
0002 3S
0001 3SU
0039 3U
0301 D
0006 DN
0001 DNS
0007 DNU
0002 DS
0001 DSU
0219 DU
0103 N
0006 NU
0010 S
0001 SU
0408 U
0002 X
Total 2638 entries identified as verbs.

Format of file pwg_verb_filter.txt:
;; Case 0001: L=13, k1=aMSay, k2=aMSay, code=N

* pwg_verb_filter_map
python pwg_verb_filter_map.py pwg_verb_filter.txt pw_mw_map_edit.txt mwverbs1.txt pwg_verb_filter_map.txt

Get correspondences between pwg verb spellings and
 - pwg verb spellings
 - mw verb spellings
Uses pw_mw_map_edit.txt  , which contains some correspondences
developed by earlier work with PW dictionary.

Format of pwg_verb_filter_map.txt:
 Adds a field mw=xxx to each line of pwg_verb_filter.txt,
indicating the MW root believed to correspond to the PWG root.
For example, aMSay in PWG is believed to correspond to aMS in MW.
;; Case 0001: L=13, k1=aMSay, k2=aMSay, code=N, mw=aMS

In 42 cases, no correspondence could be found. These use 'mw=?'. For example:
;; Case 0044: L=3913, k1=apary, k2=apary, code=N, mw=?

* preverb1.txt
python preverb1.py slp1 ../pwg.txt pwg_verb_filter_map.txt mwverbs1.txt pwg_preverb1.txt

For each of the entries of pwg_verb_filter_map.txt, the program analyzes the
text of PWG looking for upasargas.  An upsarga is identifed by the pattern
`'<div n="p">— {#([a-zA-Z]+)#}`.

The number of upasargas found is reported on a line for the verb entry.
The first PWG verb entry has no upasargas:
;; Case 0001: L=13, k1=aMSay, k2=aMSay, code=N, #upasargas=0, mw=aMS (diff)

The fourth PWG verb entry has 2 upasargas:
```
;; Case 0004: L=165, k1=akz, k2=akz, code=DU, #upasargas=2 (1/1), mw=akz (same)
01        nis        akz               nirakz               nirakz yes nis+akz
02        sam        akz               samakz               samakz no 
```
For each upasarga, an attempt is made to match the prefixed verb to a
known MW prefixed verb.  
In this example, nis+akz was matched to MW nirakz; The 'yes' notation
indicates the prefixed verb match.
However, the upasarga 'sam' with the root 'akz' found no match in MW, using
the spelling 'samakz'; the 'no' notation indicates this.

Altogether, there are currently 6773 'yes' cases, and 1588 'no' cases.

Case 6 illustrates another subtlety of the PWG-MW matching process.
```
;; Case 0006: L=606, k1=aGAy, k2=aGAy, code=NU, #upasargas=1 (1/0), mw=aGAya (diff)
01        aBi       aGAy              aByaGAy             aByaGAya yes aBi+aGAya
```
The PWG root 'aGAy' is matched with the mw root 'aGAya'.
When combined with the upasarga 'aBi',  the implicit PWG prefixed verb is
'aByaGAy'; and the corresponding MW prefixed verb is 'aByaGAya'. In this case 
there is an EXPLICIT MW entry for 'aByaGAya', hence the 'yes' notation.  
Incidentally, the parsing expression 'aBi+aGAya' is taken from MW.

There are many varied (sandhi) spelling changes occur when certain combinations of upasargas
are combined with certain roots.  My derivation of these changes is empirical, by which
I mean a mis-mash of rules which lead to as many correspondences as possible.  Also, 
some of the spelling conventions of MW come into play.

Thus, it is inevitable that some of the 'no' cases contain errors in the derived 
spellings of PWG preverb and MW preverb. For example,
```
09        pra       nart              praRart               praRft no 
10     saMpra       nart           sampranart            sampranft no 
```
Probably one of these two theoretical spellings is 'wrong'.  

8356 upasargas found in 1160 PWG entries.  
1478 verb entries have no upasargas.

6906 upasargas are mapped to MW prefixed verbs.
1459 upasargas are not matched to MW prefixed verbs.

---------------------------------------------------------------
