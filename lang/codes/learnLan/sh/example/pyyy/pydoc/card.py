#!/usr/bin/python
#coding:utf-8
import collections
from random import choice

#构建一张纸牌类，包含两个元素rank, suit
Card = collections.namedtuple('Card', ['rank', 'suit'])


#
class FrenchDeck:
    #纸牌大小2-K
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    #纸牌属性：方块，梅花，黑桃，红心
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FrenchDeck()
print(len(deck))
print(deck[0], deck[-1])
print("-----------------------")
for i  in range(5):
    print(i, " ", choice(deck))