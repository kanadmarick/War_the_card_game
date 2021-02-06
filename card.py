# This a card class


class Card:
    # A card must have a suit
    # A card must have a rank
    # A card must have a colour
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
              'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

    def __init__(self, suit, rank):
        self.suit = suit.title()
        self.rank = rank.title()

    def __str__(self):
        return self.rank + ' ' + 'of' + ' ' + self.suit  # Example: Ace of Spades

    def return_color(self):
        # Returns the color of the card
        if self.suit in ['Hearts', 'Diamonds']:
            return 'This is a Red Card'
        else:
            return 'This is a Black Card'

    def is_face_card(self):
        # Returns true for face cards
        return self.rank in ['King', 'Queen', 'Joker']

    def return_value(self):
        return Card.values[self.rank]
