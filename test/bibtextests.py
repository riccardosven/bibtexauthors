#!/bin/python

import unittest
import filecmp

import sys
import os
sys.path.append("../src")
from bibtexauthors import formatauthors

class TestBibtexAuthors(unittest.TestCase):

    def test_oneauthor_1(self):

        linein = "Author Junior Authorsson"
        expected = "Authorsson, A. J."

        lineout = formatauthors(linein)
        self.assertEqual(lineout, expected)

    def test_oneauthor_2(self):

        linein = "Authorsson, Author Junior"
        expected = "Authorsson, A. J."

        lineout = formatauthors(linein)
        self.assertEqual(lineout,expected)

    def test_manyauthors_1(self):

        linein = "Authorsson, Author and Editorsson, Editor and Reviewersson, Reviewer Senior"
        expected = "Authorsson, A. and Editorsson, E. and Reviewersson, R. S."

        lineout = formatauthors(linein)
        self.assertEqual(lineout, expected)


    def test_manyauthors_2(self):
        linein = "Author Authorsson and Editor Editorsson and Reviewer Senior Reviewersson"
        expected = "Authorsson, A. and Editorsson, E. and Reviewersson, R. S."

        lineout = formatauthors(linein)
        self.assertEqual(lineout, expected)

    def test_shorten_1(self):

        linein = "Authorsson, Author and Editorsson, Editor and Reviewersson, Reviewer Senior"
        expected = "Authorsson, A. et al."
        lineout = formatauthors(linein, shorten=1)

        self.assertEqual(lineout, expected)


    def test_shorten_2(self):
        linein = "Author Authorsson and Editor Editorsson and Reviewer Senior Reviewersson"
        expected = "Authorsson, A. et al."

        lineout = formatauthors(linein, 1)
        self.assertEqual(lineout, expected)

    def test_file_1(self):

        os.system("python3 ../src/bibtexauthors.py -y --shorten 1 input.bib testfile.bib ")
        retval = self.assertTrue(filecmp.cmp("testfile.bib", "expected1.bib"))
        os.remove("testfile.bib")
        return retval

    def test_file_1(self):

        os.system("python3 ../src/bibtexauthors.py -y --shorten 2 --shortenas 'among others' input.bib testfile.bib ")

        retval = self.assertTrue(filecmp.cmp("testfile.bib", "expected2.bib"))
        os.remove("testfile.bib")
        return retval


if __name__ == '__main__':
    unittest.main()
