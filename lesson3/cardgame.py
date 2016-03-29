"""
Rules: http://www.durbetsel.ru/2_21.htm

The document below will describe engine of a card game.
The game would have four types of objects:
1. Game object - number of players, number of cards, types of cards, card priority, etc.
2. Card object - card specific details (name, value [if any], suit [if any], etc.)
3. Player object - current cards
4. Bank object - data and methods that are bank-related
"""

from pprint import pprint
from random import shuffle, choice


DEFAULT_BANK = 100
PLAYER_MONEY = 1000
TOTAL_PLAYERS = 3


class Player:

    def __init__(self):
        self.money = PLAYER_MONEY
        self.banker = False
        self.reset_cards()

    def check_score(self):
        return sum([card.value for card in self.cards])

    def reset_cards(self):
        self.score = 0
        self.cards = []


class Card:

    def __init__(self, value, suit):
        self.value = value[1]
        self.name = value[0]
        self.suit = suit
        self.pic = value[2][suit]

    def __repr__(self):
        return "<Card: {} of {} {}>".format(self.name, self.suit, self.pic)


class Bank:

    def __init__(self):
        self.reset()

    def reset(self, player=None):
        if player:
            player.money += self.amount
        self.amount = DEFAULT_BANK
    
    def add(self, top_up):
        self.amount += top_up


class Game:
    
    def __init__(self):
        self.__cards_per_player = 2
        self.players = [Player() for i in range(TOTAL_PLAYERS)]
        self.__card_suits = ['spades', 'hearts', 'diamonds', 'clubs']
        self.__card_values = [('6', 6, {'spades': '🂦',
                                        'clubs': '🃖',
                                        'diamonds': '🃆',
                                        'hearts': '🂶'}),
                              ('7', 7, {'spades': '🂧',
                                        'clubs': '🃗',
                                        'diamonds': '🃇',
                                        'hearts': '🂷'}),
                              ('8', 8, {'spades': '🂨',
                                        'clubs': '🃘',
                                        'diamonds': '🃈',
                                        'hearts': '🂸'}),
                              ('9', 9, {'spades': '🂩',
                                        'clubs': '🃙',
                                        'diamonds': '🃉',
                                        'hearts': '🂹'}),
                              ('10', 10, {'spades': '🂪',
                                          'clubs': '🃚',
                                          'diamonds': '🃊',
                                          'hearts': '🂺'}),
                              ('Jack', 2, {'spades': '🂫',
                                           'clubs': '🃛',
                                           'diamonds': '🃋',
                                           'hearts': '🂻'}),
                              ('Queen', 3, {'spades': '🂭',
                                            'clubs': '🃝',
                                            'diamonds': '🃍',
                                            'hearts': '🂽'}),
                              ('King', 4, {'spades': '🂮',
                                           'clubs': '🃞',
                                           'diamonds': '🃎',
                                           'hearts': '🂾'}),
                              ('Ace', 11, {'spades': '🂡',
                                           'clubs': '🃑',
                                           'diamonds': '🃁',
                                           'hearts': '🂱'}),
                              ]
        self.deck = self.__create_deck()
        self.__distribute_cards()
        self.bank = Bank()
        
    def __create_deck(self):
        return [Card(value, suit) for value in self.__card_values 
                                  for suit in self.__card_suits]

    def __distribute_cards(self):
        for player in self.players:
            for i in range(self.__cards_per_player):
                player.cards.append(self.get_random_card())

    def get_random_card(self):
        if self.deck:
            shuffle(self.deck)
            return self.deck.pop()
        return None

    def add_card(self, player):
        card = self.get_random_card()
        player.cards.append(card)
        player.score += card.value

    def make_move(self):
        # return True if player adds card or False otherwise
        pass

    def get_input(self):
        TOTAL_PLAYERS = input('Number of players: ')
        
    def play(self):
        self.get_input()

            # if make_move(player):
            #     self.add_card(player)



def main():
    game = Game()
    game.play()


if __name__ == '__main__':
    main()
