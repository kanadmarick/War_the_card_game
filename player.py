class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name

    def remove_card(self):
        # Removes the top card from the hand
        return self.hand.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == list:
            self.hand.extend(new_cards)
        else:
            self.hand.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.hand)} cards.'
