
tooltips for pwg

../count_ab_8.txt         # abbrev with counts
../count_lex_5.txt        # lex with counts
extant tooltip files
PWG ../pwgab_input_1c.txt     # jim/revision of ../pwgab_input.txt
PWK pwab_input.txt            # jim-thomas?/csl-pywork/
GAS ../pwgab_input_draft.txt  # gasyoun/claude
NON abbrev not in any of the 3 sources

Initialize file that combines all 5 files for comparison
multi-line records:
* TODO : abbrev : count : sources ( PWG PWK GAS NON)
SRC TIP  (a line for each source; if NON

python combine1.py combine1.txt combine1_unused.txt  # input file names in combine1.py

* combine1_work.txt
cp combine1.txt combine1_work.txt
Edit manually and 'choose' the 'best' display
   This is noted by an '=' in the count line.

* pwgab_input_new.txt
# constructed by program from combine1_work.txt
python combine1_extract.py combine1_work.txt pwgab_input_new.txt

* REMOVE <ab> markup
---
<ab>c.</ab>  -> c.  (136)
  {these are references to certain sections of an entry
  \([0-9]\),<ab>c.</ab> -> \1,c.  (78)
---
\([0-9]\),<ab>d.</ab> -> \1,d.   (49)
---
<ab>Corr.</ab> -> Corr.   - e.g.  Thespesia populnea (Corrêa)
---
proparax. proparoxytone (1)  proparax. -> proparox.
--- <ab>Dec.</ab>  (70)
ambiguous : December  for some,
  many others Bot. name: Remove <ab>:
    Desmodium gangeticum <ab>Dec.</ab>
    Uraria lagopodioides <ab>Dec.</ab>
--- Pers.  3rd word in plant names.
     {%Sesbania aegyptiaca <ab>Pers.</ab>%}  etc. keep <ab>?
* Add markup
--- ved.  (470+)
--- s.
abbreviation 'See'  German word for 'See' ?

{%eine Verliebte <ab>u. s. w.</ab> s.%} <ab>u.</ab> 1.   ??
{#agre#}¦ s. {#agra#} .   
----
<ls>PAÑCAT. 34,16</ls> (<ab>ed.</ab> orn. 30,20).
-------------------------------------------
* Random notes
Zitat.  is modern German spelling of Citat.
Kausativ ... Causativ
etc.
---  s. abbreviation 'See'
{%eine Verliebte <ab>u. s. w.</ab> s.%} <ab>u.</ab> 1.   ??
{#agre#}¦ s. {#agra#} .   
---
St. : 22  this abbreviation is used in different senses
---
(<lex>f.</lex> {#A): vfzaBEkasahasrA gAH#}
8364 matches in 8289 lines for "{#[^#(]*)"
--- W.
  When 3rd word in botanical name, <ab>W.</ab> -> W.
    {%Vatica robusta <ab>W.</ab> <ab>u.</ab> A.%}
  Sometimes <ab>W.</ab> should remain marked:
    <ls>ŚKDR.</ls> <ab>u.</ab> dem letzten <ab>W.</ab>
---
 overlap PAREN and ITALICS
(bei <ab>Zeitww.</ab> des {%Schützens, Sichrettens)%}
 
* THE END
