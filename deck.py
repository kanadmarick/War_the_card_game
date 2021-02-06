# This is a deck class
from card import Card
import random


class Deck:
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
              'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

    def __init__(self):
        self.full = []

    def full_deck(self):
        for suit in Deck.suits:
            for rank in Deck.ranks:
                self.full.append(Card(suit, rank))  # Creates a full stack of cards

    def shuffle(self):
        random.shuffle(self.full)  # Does not return anything

    def one_deal(self):
        return self.full.pop()  # Removes one card from the list of all cards

    def divide_cards(self, players_num):
        # Divide the stack into the players
        players = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
        self.full_deck()
        self.shuffle()
        for n in range(1, players_num + 1):
            for i in range(int(52 / players_num)):
                players[n].append(self.one_deal())
        return players
