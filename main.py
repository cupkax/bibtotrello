import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode

title_list = []


def get_all_titles(filename):
    file = open(filename, encoding="utf8")
    parser = BibTexParser(common_strings=True)
    parser.customization = convert_to_unicode
    bib_database = bibtexparser.load(file, parser=parser)
    for i in range(0, len(bib_database.entries)):
        title_list.append(bib_database.entries[i].get("title"))


get_all_titles('zotLib.bib')