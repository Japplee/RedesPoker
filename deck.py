from collections import namedtuple

Card = namedtuple('Card', 'pinta, valor')  #  no need to write class to represent card
SIGNS = ['Corazones', 'Diamantes', 'Picas', 'Trebol']

class Deck:
    def __init__(self):
        self.cards = [Card(sign, value) for sign in SIGNS for value in range(2,
                                                                             11) +
                      'J Q K A'.split()]

    def __repr__(self):
        return str([str(card) for card in self.cards])

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, item):
        return self.cards[item]

    def __setitem__(self, key, value):
        self.cards[key] = value


deck = Deck()

print deck[51]  # indexing works, prints Card(sign='Hearts', value='K')

print deck[51][0]
"""print len(deck)  # prints 52

print deck[13:16]  # slicing works

import random

random.shuffle(deck)  # shuffle works using no extra code

print deck[11]"""