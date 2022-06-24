import math
import random
from matplotlib import pyplot


class Player:
    def __init__(self, bal, game):
        self.bal = bal
        self.bet = 0

        self.game = game
        self.ai = False

        self.cards = []

        self.finished = False

    def add_bet(self, amount):
        if self.bal >= amount:
            self.bal -= amount
            self.bet += amount

            return True
        else:
            return False

    def add_card(self, card):
        self.cards.append(card)

    def hand(self):
        card = self.game.take()

        self.cards.append(card)

        return True

    def double(self):
        bet = self.bet

        if self.add_bet(bet):
            print("doubled")
            return self.hand()
        else:
            print("can't double")
            return self.hand()

    def is_busted(self):
        score = self.game.get_score(self.cards)

        if score > 21:
            print("busted")

            """reset bet"""
            self.bet = 0

            self.finished = True

            return True
        else:
            return False

    def has_blackjack(self):
        score = self.game.get_score(self.cards)

        if score == 21:
            print("blackjack")
            if not self.game.house_has_bj:
                self.bal += self.bet * 2.5
            else:
                self.bal += self.bet

            self.bet = 0

            self.finished = True
            return True
        else:
            return False

    def ai_bet(self, cap, amount):
        value = self.game.true_deck()

        if value > 0:
            if value > cap:
                self.add_bet(amount)
            elif value < cap:
                self.add_bet(amount/2)
        else:
            self.add_bet(amount/10)

    def ai_play(self, house_cards):
        score = self.game.get_score(self.cards)
        house_score = self.game.get_score(house_cards)
        plan_array = {2: {2: "h", 3: "h", 4: "h", 5: "h", 6: "h", 7: "h", 8: "h", 9: "h", 10: "h", 11: "h"},
                      3: {2: "h", 3: "h", 4: "h", 5: "h", 6: "h", 7: "h", 8: "h", 9: "h", 10: "h", 11: "h"},
                      4: {2: "h", 3: "h", 4: "h", 5: "h", 6: "h", 7: "h", 8: "h", 9: "h", 10: "h", 11: "h"},
                      5: {2: "h", 3: "h", 4: "h", 5: "h", 6: "h", 7: "h", 8: "h", 9: "h", 10: "h", 11: "h"},
                      6: {2: "h", 3: "h", 4: "h", 5: "h", 6: "h", 7: "h", 8: "h", 9: "h", 10: "h", 11: "h"},
                      7: {2: "h", 3: "h", 4: "h", 5: "h", 6: "h", 7: "h", 8: "h", 9: "h", 10: "h", 11: "h"},
                      8: {2: "h", 3: "h", 4: "h", 5: "h", 6: "h", 7: "h", 8: "h", 9: "h", 10: "h", 11: "h"},
                      9: {2: "h", 3: "d", 4: "d", 5: "d", 6: "d", 7: "h", 8: "h", 9: "h", 10: "h", 11: "h"},
                      10: {2: "d", 3: "d", 4: "d", 5: "d", 6: "d", 7: "d", 8: "d", 9: "d", 10: "h", 11: "h"},
                      11: {2: "d", 3: "d", 4: "d", 5: "d", 6: "d", 7: "d", 8: "d", 9: "d", 10: "d", 11: "h"},
                      12: {2: "h", 3: "h", 4: "s", 5: "s", 6: "s", 7: "h", 8: "h", 9: "h", 10: "h", 11: "h"},
                      13: {2: "s", 3: "s", 4: "s", 5: "s", 6: "s", 7: "h", 8: "h", 9: "h", 10: "h", 11: "h"},
                      14: {2: "s", 3: "s", 4: "s", 5: "s", 6: "s", 7: "h", 8: "h", 9: "h", 10: "h", 11: "h"},
                      15: {2: "s", 3: "s", 4: "s", 5: "s", 6: "s", 7: "h", 8: "h", 9: "h", 10: "h", 11: "h"},
                      16: {2: "s", 3: "s", 4: "s", 5: "s", 6: "s", 7: "h", 8: "h", 9: "h", 10: "h", 11: "h"},
                      17: {2: "s", 3: "s", 4: "s", 5: "s", 6: "s", 7: "s", 8: "s", 9: "s", 10: "s", 11: "s"},
                      18: {2: "s", 3: "s", 4: "s", 5: "s", 6: "s", 7: "s", 8: "s", 9: "s", 10: "s", 11: "s"},
                      19: {2: "s", 3: "s", 4: "s", 5: "s", 6: "s", 7: "s", 8: "s", 9: "s", 10: "s", 11: "s"},
                      20: {2: "s", 3: "s", 4: "s", 5: "s", 6: "s", 7: "s", 8: "s", 9: "s", 10: "s", 11: "s"}}

        return plan_array[score][house_score]

    def set_default(self):
        self.cards = []
        self.finished = False

    def show_score(self):
        return self.game.get_score(self.cards), self.cards


class House(Player):
    def __init__(self, bal, game):
        super().__init__(bal, game)
        self.hidden_cards = []

    def add_hidden_card(self, card):
        self.hidden_cards.append(card)

    def un_hide(self):
        self.cards.extend(self.hidden_cards)
        self.hidden_cards = []

    def ai_play_house(self):
        if self.game.get_score(self.cards + self.hidden_cards) > 16:
            return "s"
        else:
            return "h"


class Blackjack:
    def __init__(self, deck_size):
        self.deck_size = deck_size
        self.card_types = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        self.cards = self.reload_deck()

        self.card_count = 0

        self.house_has_bj = False

    def reload_deck(self):
        return {key: 4 * self.deck_size for key in self.card_types}

    def take(self):
        card = random.choice(list(self.cards.keys()))

        """setup card_counter"""
        self.card_score(card)

        if self.cards[card] == 1:
            self.cards.pop(card)
        else:
            self.cards[card] -= 1

        return card

    @staticmethod
    def get_score(lst):
        value = 0
        ace = 0

        for v in lst:
            if v == "A":
                ace += 1

            elif v in ("J", "Q", "K"):
                value += 10

            else:
                value += int(v)

        while ace > 0:
            max_ace = 21 - value

            if max_ace >= 11:
                value += 11
                ace -= 1
            else:
                value += 1
                ace -= 1

        return value

    def play(self, players, hs):
        for player in players:
            card = self.take()
            player.add_card(card)

        card = self.take()
        hs.add_card(card)

        for player in players:
            card = self.take()
            player.add_card(card)

        card = self.take()
        hs.add_hidden_card(card)

        print(f"house: {h.show_score()}")
        if self.get_score(h.cards + h.hidden_cards) == 21:
            self.house_has_bj = True
            print("house has blackjack")

        for i, player in enumerate(players):
            print(f"player_{i}: {player.show_score()}")
            if player.has_blackjack():
                print("blackjack")

        "prevent playing case house blackjack"
        if not self.house_has_bj:

            for i, player in enumerate(players):
                if not player.finished:
                    print(f"player_{i}: {player.show_score()}")

                    playing = True
                    while playing:
                        if player.ai:
                            cmd = player.ai_play(h.cards)
                        else:
                            cmd = input(f"player_{i}: 's', 'h', 'd': ")

                        if cmd == "s":
                            playing = False

                        elif cmd == "h":
                            playing = player.hand()

                        elif cmd == "d":
                            playing = player.double()

                        if player.is_busted():

                            playing = False

                        elif player.has_blackjack():
                            playing = False

                        print(f"player_{i}: {player.show_score()}")

            print("house playing...")
            h.un_hide()
            print(f"house: {self.get_score(h.cards + h.hidden_cards), h.cards, h.hidden_cards}")

            playing = True
            while playing:
                cmd = h.ai_play_house()
                if cmd == "s":
                    playing = False

                elif cmd == "h":
                    playing = h.hand()

                if h.is_busted():
                    playing = False

                elif h.has_blackjack():
                    playing = False

                print(f"house: {self.get_score(h.cards + h.hidden_cards)}")

        """paying out"""
        for i, player in enumerate(players):
            if not player.finished:
                player.finished = True

                score = self.get_score(player.cards)
                if (score > self.get_score(h.cards + h.hidden_cards)) or h.is_busted():
                    print(f"player_{i}: won {player.bet * 2}")

                    player.bal += player.bet * 2

                elif score == self.get_score(h.cards + h.hidden_cards):
                    print(f"player_{i}: won {player.bet}")
                    player.bal += player.bet

                player.bet = 0

    def card_score(self, card):
        if card in ("10", "J", "Q", "K", "A"):
            self.card_count -= 1
        elif card in ("2", "3", "4", "5", "6"):
            self.card_count += 1

    def true_deck(self):
        value = self.card_count/math.ceil(sum(self.cards.values()))
        return value


b = Blackjack(30)

b1 = []
b2 = []
b3 = []
b4 = []

p1 = Player(100000, b)
p2 = Player(100000, b)
p3 = Player(100000, b)
p4 = Player(100000, b)

p1.ai = True
p2.ai = True
p3.ai = True
p4.ai = True

for i in range(1000):

    if sum(b.cards.values()) < 40:
        b.__init__(30)

    #input("start: ")

    p1.set_default()
    p2.set_default()
    p3.set_default()
    p4.set_default()

    p1.ai_bet(7, 100)
    p2.ai_bet(9, 100)
    p3.ai_bet(10, 100)
    p4.add_bet(100)

    h = House(1000, b)
    player_list = [p1, p2, p3, p4]

    b.play(player_list, h)

    print(p1.bal, p2.bal, p3.bal)

    b1.append(p1.bal)
    b2.append(p2.bal)
    b3.append(p3.bal)
    b4.append(p4.bal)
    print(i)

print(p1.bal, p2.bal, p3.bal, p4.bal)

pyplot.plot(b1, color="r")
pyplot.plot(b2, color="g")
pyplot.plot(b3, color="b")
pyplot.plot(b4, color="y")
pyplot.show()


