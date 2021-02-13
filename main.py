import os
import shutil

import bibtexparser
import trello
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode
from trello import TrelloClient


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


# Titles from bibliography file
titles = get_titles('Dropbox/org/research/zotLib.bib')

# Define Trello Client
TRELLO_API_KEY = os.getenv('TRELLO_API_KEY')
TRELLO_TOKEN = os.getenv('TRELLO_TOKEN')
client = TrelloClient(
    api_key=TRELLO_API_KEY,
    token=TRELLO_TOKEN,
)


class TrelloBib():
    current_board = trello.Board
    current_list = trello.List
    list_of_cards = []

    def __init__(self, board_name, list_name):
        self.board_name = board_name
        self.list_name = list_name

        # Get Board
        for board in client.list_boards():
            if board.name == self.board_name:
                self.current_board = board

        # Get Trello List
        for list in self.current_board.list_lists():
            if list.name == self.list_name:
                self.current_list = list

        # Get Cards in the List
        for card in range(0, len(self.current_list.list_cards())):
            self.list_of_cards.append(self.current_list.list_cards()[card].name)


# Define Board (classname(BoardName,ListName))
mqg = TrelloBib('MQ Games Research', 'Literature')

cards_not_in_bib = set(titles).difference(mqg.list_of_cards)
for items in cards_not_in_bib:
    mqg.current_list.add_card(items)