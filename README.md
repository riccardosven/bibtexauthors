# bibtexauthors
A python script to format author lists in bibtex

Formats an author line according to the following rules:

```
   Author Authorson -> Authorson, A.
   Authorson, Author -> Authorson, A.
```

In addition, it can shorten long author lists by replacing all authors after a centain number with an arbitrary string.

## Standalone use
Used to parse a file
```
  bibtexauthors.py [-h] [-y] [-s [SHORTEN]] [-a [SHORTENAS]] filein fileout
```
takes the bibtex file `filein` and formats all authors according to the rules supplied.

Keyword arguments:
 - `yes` skips asking for confirmation
 - `shorten` replace the authors after this number (default False)
 - `shortenas`   -- string to replace the authors with (default 'et al.')
 
**Usage Example**:
 Sample input file
 ```
% cat input.bib
@article{authorsson2018article,
  author = {Authorsson, Author Junior},
  title = {An article},
  year = 2018,
}

@book{authorsson2018book,
  author = {Author Authorsson and Editor Editorsson and Reviewer Senior Reviewersson},
  title = {A book},
  year = 2018,
}
```
Just format author field
```
% bibtexauthors.py -y input.bib output.bib  
% cat output.bib 
@article{authorsson2018article,
  author = {Authorsson, A. J.},
  title = {An article},
  year = 2018,
}

@book{authorsson2018book,
  author = {Authorsson, A. and Editorsson, E. and Reviewersson, R. S.},
  title = {A book},
  year = 2018,
}
```
Format authors and shorten them to first authors (remaining authors shortened to "etc.")
```
% bibtexauthors.py -y --shorten 1 --shortenas "etc." input.bib output.bib
% cat output.bib 
@article{authorsson2018article,
  author = {Authorsson, A. J.},
  title = {An article},
  year = 2018,
}

@book{authorsson2018book,
  author = {Authorsson, A. etc.},
  title = {A book},
  year = 2018,
}
```
 
## Python use
Use the function
```
  formatauthors(authorsin, shorten=False, shortenas="et al.")
```
Takes the string authorsin, formats it and shortens it according to the rules provided.

Usage Example:
```
  from bibtexauthors import formatauthors
  >>> linein = "Authorsson, Author and Editorsson, Editor and Reviewersson, Reviewer Senior"
  >>> formatauthors(linein)
  'Authorsson, A. and Editorsson, E. and Reviewersson, R. S.'
  >>> formatauthors(linein,shorten=1)
  'Authorsson, A. et al.'
  >>> formatauthors(linein,shorten=2)
  'Authorsson, A. and Editorsson, E. et al.'
  >>> formatauthors(linein,shorten=1, shortenas="with friends")
  'Authorsson, A. with friends'
```
