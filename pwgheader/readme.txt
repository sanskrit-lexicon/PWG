
The two listings 'pwgheader.txt' and 'pwgdel.txt' 
are copied from Cologne server today (Jul 25, 2021),
from directory PWGScan/2013/orig.

They were originally part of Thomas' digitization of pwg.
In the course of Jim's work begun Nov 21, 2013, these were deleted.

Here are notes (from PWGScan/2013/pywork/readme.org):
```
* pwg-header.txt and pwg0.txt and pwgdel.txt (amended Nov 26, 2013; Nov 5,2014)

in pywork,
new: (Nov 5, 2014)
python26 pwgall.py ../orig/pwg_orig_utf8_slp1.txt ../orig/pwgheader.txt ../orig/pwg0.txt ../orig/pwgdel.txt


old:
python26 pwgall.py ../orig/pwg_orig_utf8.txt ../orig/pwgheader.txt ../orig/pwg0.txt ../orig/pwgdel.txt
test:
python26 pwgall.py ../orig/pwg_orig_utf8.txt ../orig/oldpwgheader.txt ../orig/oldpwg0.txt ../orig/oldpwgdel.txt

corrected line 174555
corrected line 174579
1127 lines written to ../orig/pwgheader.txt
264822 lines written to ../orig/pwg0.txt
78 lines written to ../orig/pwgdel.txt

(previous run, with pwgdel, checks:
1127 lines written to ../orig/pwgheader.txt
264900 lines written to ../orig/pwg0.txt
)

line numbers in emacs can be displayed by:
 M-x global-linum-mode
It was discovered that (in pwg_orig.txt),
line 174477  ...[Page05.1677]
through
line 174554   (blank)
should be deleted and
line 174555 ...[Page05.1679] should be corrected to [Page05.1677]
line 174579 ...[Page05.1680] should be corrected to [Page05.1678]
TM concurs.

The pwgall program changed to do these things.
The deleted lines (174477 - 174554) are written to pwgdel.txt.
```

