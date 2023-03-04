class Chips:

    def __init__(self, total=100):
        # total can be passed in by user input or use 100 as default value
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet