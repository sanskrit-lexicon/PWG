
Three types of changes made by Jim to the index_panc.txt
The result is index.txt
So all changes could be examined by
 diff index_panc.txt index.txt

Here are notes on the changes.
-------------------------------------------
TYPOS: indexer please note!

old: 88	I	321	331	71
new: 88	I	327	331	71

old: 94	I	260	364a	77
new: 94	I	360	364a	77

old: 127	II	28b	31	110
new: 127	II	28	31	110

old: 150	II	132b	140a	133
new: 150	II	132	140a	133

old: 183	III	99	103	166
new: 183	III	99	106	166

old: 185	III	112	115	168
new: 185	III	112	116	168
  Note: page 185 missing numbers identifying
  shlokas 113, 114, and 116.

old: 219	III	261	267a	202
new: 219	III	261	266	202

old: 223	IV	6b	9a	206
new: 223	IV	6	9a	206

old: 264	V	36b	40	247
new: 264	V	37b	40	247

old: 269	V	58	58	252
new: 269	V	58	59	252

-------------------------------------------
These adjustments by Jim are arbitrary,
not typos.

old: 33	I	81a	86a	16
new: 33	I	81	86a	16

old: 73	I	257c	265a	56
new: 73	I	257	265a	56

old: 120	I	475b	475b	103
new: 120	I	475b	475	103

old: 151	II	140b	140b	134
new: 151	II	140b	140	134

old: 179	III	87b	87b	162
new: 179	III	87b	87	162

old: 279	V	84b	84b	262
new: 279	V	84b	84	262

old: 201	III	201a	201a	184
new: 201	III	201	201a	184

old: 207	III	222a	222a	190
new: 207	III	222	222a	190

---------------------------------------------------------
'systematic' changes, for purpose of app1
Not typos.

Remove pdf pages  1-19
Remove pdf pages 284-289
change page 283:
 old: 283	V	---	---	266
 new: 283	V	93	93	266
    So this closing page will be accessible

------------
Several pages have no shlokas (verses).
These are coded as '---' in fromv, tov
Change these to previous tov
  this is done in make_js_index.py in no_shloka function
Example.
old: 63	I	---	---	46
new: 63	I	228	228	46
