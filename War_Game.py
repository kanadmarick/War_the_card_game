from card import Card
from deck import Deck
from player import Player
import random

deck = Deck()
stack = deck.divide_cards(2)
player1 = Player(input('Player one please enter your name: \n'))
player2 = Player(input('Player2 please insert your name:\n'))
player1.hand = stack[1]
player2.hand = stack[2]


def empty():
    if len(player1.hand) == 0:
        print(f'{player1.name} is out of cards! {player2.name} is the winner')
        game_on = False

    elif len(player2.name) == 0:
        print(f'{player2.name} is out of cards! {player1.name} is the winner')
        game_on = False

    else:
        game_on = True


def display_cards(i=0):
    print(f'{player1.name} has {player1.hand[i]}')
    print(f'{player2.name} has {player2.hand[i]}')


print('Welcome to card game War!')
print('The rules are simple')
print('The biggest card wins')
print('If both cards have the same value the game moves to War!')
print('When in war each player selects 4 cards from their deck')
print('War goes on until one player wins!')

game_on = True
round_num = 0
while game_on:

    round_num += 1
    print(f'Round number {round_num}')

    empty()
    display_cards()

    if player1.hand[0].return_value() > player2.hand[0].return_value():
        player1.add_cards(player2.remove_card())
        print(f'{player1.name} has won the round!')
        random.shuffle(player1.hand)
    elif player1.hand[0].return_value() < player2.hand[0].return_value():
        player2.add_cards(player1.remove_card())
        print(f'{player2.name} has won the round!')
        random.shuffle(player1.hand)
    else:
        print('War!')
        at_war = True
        empty()
        war_round = 0
        while at_war:
            for i in [1, 2, 3, 4]:
                empty()
                war_round += 1
                print(f'War round {war_round}!')

                if len(player1.hand) < 5:
                    print(f'{player1.name} does not have enough cards for war!')
                    print(f'{player2.name} wins at War!')
                    game_on = False
                    at_war = False
                    break

                elif len(player2.hand) < 5:
                    print(f'{player2.name} does not have enough cards for war!')
                    print(f'{player1.name} wins at War!')
                    game_on = False
                    at_war = False
                    break

                elif player1.hand[i].return_value() > player2.hand[i].return_value():
                    display_cards(i)
                    player1.add_cards(player2.hand.pop(i))
                    print(f'{player1.name} has won this War round!')
                    at_war = False
                    break
                elif player1.hand[i].return_value() < player2.hand[i].return_value():
                    display_cards(i)
                    player2.add_cards(player1.hand.pop(i))
                    print(f'{player2.name} has won this War round!')
                    at_war = False
                    break
        random.shuffle(player1.hand)
        random.shuffle(player2.hand)
