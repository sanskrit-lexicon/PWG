## pwg_ls/pwg_dhaval/readme.md 

This folder contains programs that extract the literary sources from pwg.xml. 
The programs are modeled after those used to do a similar analysis of
the pw.xml literary sources in the [PWK repository](https://github.com/sanskrit-lexicon/PWK/).

Directory abbrvwork_v0 contains a direct application of the analysis done
for PW.  It provides a more efficient implementation.

Directory abbrvwork contains some revisions, taking into account some of
the particulars of PWG that were not present in PW.


#------------ The following are original notes from PW work. They
are retained for possible future use while the work on PWG is under development.

# Abbreviations of PWG  TODO
Run `makeabbrv.sh` from pywork/abbrvwork directory to regenerate the lists.

See [this](http://drdhaval2785.github.io/pw/abbrv/display.html) for output of the code.

# Dependencies
[lxml](http://lxml.de/) to parse pw.xml

### preparation of local GitHub/pwgxml/pwg.xml
  makeabbrv.sh uses pwg.xml as data input.  
  It further is written to assume that pwg.xml is in directory
   GitHub/pwgxml,
  where 'GitHub' is the directory containing the PWG repository.
  To get pwgxml, put the following script in GitHub directory as pwgxml_init.sh,
  and run under 'GitBash' as 'sh pwgxml_init.sh.
  Then, you will be ready to run 'sh makeabbrv.sh' in pwg_dhaval/abbrvwork.
```
echo "downloading pwgxml.zip"
curl -o pwgxml.zip http://www.sanskrit-lexicon.uni-koeln.de/scans/PWGScan/2013/downloads/pwgxml.zip
echo "unzipping pwgxml.zip to folder xml"
unzip pwgxml.zip
echo "renaming xml to pwgxml"
rm -r pwgxml
mv xml pwgxml
echo "removing pwgxml.zip"
rm pwgxml.zip

```

# Logic
1. `<ls>something</ls>` tag usually holds the literary source data.

2. Output of all scripts are stored in abbrvoutput folder.

3. The text `something` is scraped via lxml and stored in abbrvlist.txt file (1st raw file).

4. abbrvlist.txt file still has some references which are pure numbers. We have discarded them as of now and stored them in purenumberabbrvlist.txt (byproduct). (See https://github.com/sanskrit-lexicon/PWG/issues/11 for details).

5. The list which is not pure numbers, but has some alphabet preceding it is stored in properrefs.txt (raw file 2).

6. The properrefs.txt file still has entries like `TA7N2D2JA-BR.25,13,3.` where the last entries are the canto / shloka number. They need to be removed.

7. The canto or shloka numbers are removed and only unique entries, sorted alphabetically are kept in cleanrefs.txt (raw file 3).

8. Errors usually come solo. Therefore, we have kept a code which sorts cleanrefs based on their occurrences. Sorted data is stored in sortedcrefs.txt. Sorting is done first based on number of occurrences and then alphabetically.

9. sortedcrefs.txt has the data is `ls@key1@key2@Lnumber@occurrence`.

10. It is difficult to read the `ls`, because it is in Anglisized Sanskrit. Therefore we add another field `lsinIAST@ls@key1@key2@Lnumber@occurrence` in  sortedcrefsiast.txt via `transcoder/as_roman.py` file.

11. The file `displayhtml.php` takes sortedcrefsiast.txt as input and gives the following output `SrNo-Lno-ReferenceinAS-ReferenceinIASTwithlinktowebpage-key1withlinktopdf-key2-counter`.

12. This file displayhtml.php would make it easy to locate the reference in dictionaries.

13. For corrections, copy the file `sortedcrefs.txt` as `finalabbrv.txt`. (This is not automated, because otherwise it may be overwritten if handled recklessly).

14. If there are errors found in HTML file, correct the `referenceinAS` in the finalabbrv.txt file.

15. If there is no error, place a ';' before the line in finalabbrv.txt.

16. Once the testing is over, run `python postprocess.py`. It would separate the file into change.txt and nochange.txt.

17. Jim would have to find a way to integrate these files into XML corrections.


# Improvements in statistics
1. First run - 3679 entries

2. After removing terminal period(.) i.e. `clean = clean.strip('.')` - 3341 entries


