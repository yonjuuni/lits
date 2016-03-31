import os
from time import sleep
from random import shuffle, choice

PLAYER_MONEY = 100


class Player:

    def __init__(self, name='Bot'):
        self.money = PLAYER_MONEY
        self.name = name
        self.ai = self.name == 'Bot'
        self.score = 0
        self.cards = []

    def print_cards(self):
        if self.ai:
            print("Bot's cards: {} ({} points)".
                  format(' '.join(card.pic for card in self.cards), self.score)
                  )
        else:
            print('Your cards: {} ({} points)'.
                  format(' '.join(card.pic for card in self.cards), self.score)
                  )

    def check_score(self):
        self.score = sum([card.value for card in self.cards])

    def take_turn(self):

        if self.ai:
            print('More? (y/n): ', end='', flush=True)
            for i in range(3):
                sleep(0.5)
                print('.', end='', flush=True)
            if self.score <= 11:
                weight = [(True, 1)]
            elif 11 < self.score <= 15:
                weight = [(True, 50), (False, 50)]
            elif 15 < self.score <= 19:
                weight = [(True, 20), (False, 80)]
            else:
                weight = [(False, 1)]

            res = choice([val for val, cnt in weight for _ in range(cnt)])

            if res:
                print(' y')
                sleep(0.5)
            else:
                print(' n')
                sleep(0.5)

        else:
            ans = input('More? (y/n): ').lower()
            if ans == 'y':
                res = True
            elif ans == 'n':
                res = False
            else:
                print('Incorrect choice.')
                return self.take_turn()
        return res

    def __repr__(self):
        return '{}: {} ({} points)'.format(self.name,
                                           ' '.join(card.pic for card
                                                    in self.cards),
                                           self.score)


class Card:

    def __init__(self, value, suit):
        self.value = value[1]
        self.name = value[0]
        self.suit = suit
        self.pic = value[2][suit]

    def __repr__(self):
        return "<Card: {} of {} {}>".format(self.name, self.suit, self.pic)


class Game:
    """
    Aim of the “OCHKO” game is to get a total of 21 points from your cards.

    Cards/Points:

    Ace    1 or 11 (the player who holds the Ace gets to choose the value
                    of the card).
    Jack   2
    Queen  3
    King   4
    Numbered cards have respective numeric values (6 through 10).

    Rules:

    1. Player should make a bet from 5 to 25.
    2. Player wins as much as they bet. If player bets 10, they win 10 from the
       'Bot' (keeping their original bet).

       * If a player gets OCHKO (10 + Ace or 2 Aces) from the initial draw,
       they win right away and get 2x their bet.

    3. Player loses as much as they bet.
    4. If the hand is a draw, player keeps the bet neither winning nor losing
       money.
    5. Two cards are dealt to each player.
    6. Player can keep their hand as it is.
    7. If a player doesn't have 21 points, they may take additional cards.
    8. The winner is the one who gets the most points, or has 21 points.
    9. If the total score is more than 21 points - player loses.

    """

    def __init__(self, player_name):
        self._cards_per_player = 2
        self.players = [Player(player_name), Player()]
        self.player = self.players[0]
        self.ai = self.players[1]

        self._card_suits = ['spades', 'hearts', 'diamonds', 'clubs']
        self._card_values = [('6', 6, {'spades': '🂦',
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
        self.deck = []

    def _create_deck(self):
        return [Card(value, suit) for value in self._card_values
                for suit in self._card_suits]

    def distribute_cards(self):
        for player in self.players:
            for i in range(self._cards_per_player):
                player.cards.append(self._get_random_card())
            player.check_score()

    def _get_random_card(self):
        if self.deck:
            shuffle(self.deck)
            return self.deck.pop()
        return None

    def add_card(self, player):
        card = self._get_random_card()
        if card.name == 'Ace' and player.score + card.value > 21:
            card.value = 1
        player.cards.append(card)
        player.check_score()
        if player.score > 21:
            for card in player.cards:
                if card.value == 11:
                    player.score -= 10
                    break

    def enter_bet(self):
        bet = input('Make a bet (5 to 25): ')
        try:
            bet = int(bet)
        except ValueError:
            print('Your bet should be an integer, try again.')
            return self.enter_bet()
        else:
            if bet < 5 or bet > 25:
                print('Your bet should be from 5 to 25, try again.')
                return self.enter_bet()
            if bet > self.player.money:
                print("You don't have enough money, your max bet is {}.".
                      format(self.player.money))
                return self.enter_bet()
        return bet

    def reset_cards(self):
        for player in self.players:
            player.score = 0
            player.cards = []
        self.deck = self._create_deck()
        self.distribute_cards()

    def win(self):
        if self.ai.score < self.player.score <= 21:
            return True
        elif (self.player.score > 21 or
              self.player.score < self.ai.score <= 21):
            return False
        else:
            return None

    def new_round(self):

        self.reset_cards()
        bet = self.enter_bet()

        if self.player.score in [21, 22]:
            self.player.print_cards()
            print('OCHKO! {} added to your balance.'.format(bet * 2))
            self.player.money += bet * 2
        else:
            for player in self.players:
                player.print_cards()
                while player.take_turn():
                    self.add_card(player)
                    player.print_cards()
                    if player.score > 21:
                        print('Too much :(')
                        break
                    elif player.score == 21:
                        print('OCHKO!')
                        break
                print()

            res = self.win()
            if res:
                print('You win! {} added to your balance.'.format(bet))
                self.player.money += bet
            elif res is None:
                print("It's a draw. You keep the money.")
            else:
                print('You lose! {} removed from your balance.'.format(bet))
                self.player.money -= bet
        print('Your balance is {}.'.format(self.player.money))

        if self.player.money >= 5:
            ans = ''
            while ans not in ['y', 'n']:
                ans = input('\nAnother round? (y/n): ').lower()
            if ans == 'y':
                os.system('clear')
                return self.new_round()
        else:
            print('You lost all your money.')

    def play(self):
        print("Welcome to OCHKO, {}. Let's play!".format(self.player.name))
        print(self.__doc__)
        input('Press Enter to continue...')
        os.system('clear')
        print('Your balance is {}.'.format(self.player.money))
        self.new_round()
        print('Bye-bye.\n')


def main():
    os.system('clear')
    name = input('Enter your name: ')
    game = Game(name)
    game.play()


if __name__ == '__main__':
    main()
