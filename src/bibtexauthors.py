#!/bin/python
'''Formatter for author fields in bibtex'''

from argparse import ArgumentParser
import re

def formatauthors(authorsin, shorten=False, shortenas="et al."):
    '''
    Formats an author line according to the following rules:

        Author Authorson -> Authorson, A.
        Authorson, Author -> Authorson, A.

    If shorten is set to an integer, authors after this number are replaced
    with et al.

    Keyword arguments:
    shorten     -- replace the authors after this number (default False)
    shortenas   -- string to replace the authors with (default 'et al.')

    '''

    authorsout = [] # Formatted output authors
    for author in authorsin.split(' and '):
        author = author.strip() # Split individual authors

        nameout = [] # Formatted author
        if ',' in author: # The author is of the form Last, First

            lastname, firstnames = author.split(',') # Split into vector of [Last, First]

            nameout.append(lastname + ', ') # Append Last name

            firstnames = re.split('-| ', firstnames.strip()) # Split vector of First names
            nameout.extend(name[:1] + '. ' for name in firstnames) # Abbreviate first name and append to out

        else: # The author is of the form First Last
            names = author.split(' ') # Split into vector of [First, Last]
            nameout.append(names[-1]) # Append Last name
            nameout.append(', ')
            nameout.extend(name[:1] + '. ' for name in names[:-1]) # Abbreviate first name and append to out

        authorsout.append(''.join(nameout)) # Join name and append to author list

    shortened = False
    if shorten:
        while len(authorsout) > shorten:
            del authorsout[-1]
            shortened = True

    authorsout = 'and '.join(authorsout).strip()

    if shortened:
        authorsout += " "+shortenas

    return authorsout



if __name__ == "__main__":

    PARSER = ArgumentParser()
    PARSER.add_argument('-y', '--yes', action="store_true", help='accept all changes')
    PARSER.add_argument('-s', '--shorten', action="store", nargs='?', type=int, default=False, help='shorten author list')
    PARSER.add_argument('-a', '--shortenas', action="store", nargs ='?', default='et al.', help='string to replace the shortened authors')
    PARSER.add_argument('filein')
    PARSER.add_argument('fileout')

    ARGS = PARSER.parse_args()

    with open(ARGS.filein, 'r') as fin:
        with open(ARGS.fileout, 'w') as fout:

            for linein in fin:
                if not linein.strip().startswith('author'):
                    fout.write(linein)
                    continue

                authorsin = re.findall(r'{(.*)}', linein.strip())[0] # Extract authors
                authorsout = formatauthors(authorsin, ARGS.shorten, ARGS.shortenas)

                if ARGS.yes: # Do not ask for confirmation
                    fout.write(f'  author = {{{authorsout}}},\n')
                else:
                    s = input(f'{authorsin} -> {authorsout}? [Yn]')
                    if s == 'n':
                        fout.write(linein)
                    else:
                        fout.write(f'  author = {{{authorsout}}},\n')
