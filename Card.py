from dataclasses import dataclass
from enum import Enum
@dataclass

class Card:
    rank:str
    suit:int

class Suit(Enum):
    HEARTS = "hearts"
    SPADES = "spades"
    DIAMONDS = "diamonds"
    CLUBS = "clubs"

ranks = ["Ace", "2", "3", "4", "5", "6", "7","8", "9", "10", "Jack", "Queen", "King"]

deck = []

for suit in Suit:
    for rank in ranks:
        deck.append(Card(rank,suit))
"""
hand = deck
del hand[::5]
print(len(deck))
"""

#Reference: Here since a list is mutable when we assign deck to hand we are accessing the same memory address as deck and thus modifying hand causes the deck to change as well
correct_hand = deck.copy()
del correct_hand[::5]
print(len(deck))
