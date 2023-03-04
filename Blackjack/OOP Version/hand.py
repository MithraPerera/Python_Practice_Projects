from deck import values
from chips import Chips


class Hand:

    def __init__(self):
        self.cards = []  # start with an empty list for the hand
        self.value = 0  # start with a zero value
        self.aces = 0  # attribute to keep track of aces
        self.chips = Chips()

    def add_card(self, card):
        # card passed will be from Deck classes Deal method
        self.cards.append(card)
        self.value += values[card.rank]  # passing in the rank as the key to get the value

        #track aces
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        # If total value of hand is greater than 21 and there is more than 0 aces
        # 0 is False and any other number is treated as True
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def start_fresh(self):
        self.cards = []
        self.value = 0
        self.aces = 0