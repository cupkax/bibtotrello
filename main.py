import os
import shutil

import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode


def get_titles(bib_dir):
    # Get bibtex file in current working directory
    shutil.copy(
        str(os.path.join(os.path.expanduser('~'), bib_dir)),
        str(os.getcwd()))
    bib_data = open('zotLib.bib', encoding='utf-8')
    t = []
    parser = BibTexParser(common_strings=True)  # common_strings parameters is required to parse months
    parser.customization = convert_to_unicode  # latex to unicode
    # Load the bibtex file
    bib_database = bibtexparser.load(bib_data, parser=parser)
    # Iterate through the bibtex and append titles to list
    for i in range(0, len(bib_database.entries)):
        t.append(bib_database.entries[i].get("title"))
    return t


get_titles('Dropbox/org/research/zotLib.bib')