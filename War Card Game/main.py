from deck import Deck
from player import Player

player_1 = Player("Mithra")
player_2 = Player("Suran")
game_on = True
deck = Deck()
deck.shuffle()

# Divide the deck in half and give to each player
for x in range(26):
    player_1.add_cards(deck.deal_card())
    player_2.add_cards(deck.deal_card())

round_num = 0

while game_on:

    round_num += 1
    print(f"Round {round_num}")

    if len(player_1.all_cards) == 0:
        print("Player 1, out of cards! Player 2 Wins!")
        game_on = False
    elif len(player_2.all_cards) == 0:
        print("Player 2, out of cards! Player 2 Wins!")
        game_on = False

    # Start a new Round
    player_1_cards = [player_1.remove_one()]
    player_2_cards = [player_2.remove_one()]

    # While at War
    at_war = True

    while at_war:

        if player_1_cards[-1].value > player_2_cards[-1].value:
            player_1.add_cards(player_1_cards)
            player_1.add_cards(player_2_cards)
            at_war = False
        elif player_2_cards[-1].value > player_1_cards[-1].value:
            player_2.add_cards(player_1_cards)
            player_2.add_cards(player_2_cards)
            at_war = False
        else:
            print("WAR!")
            if len(player_1.all_cards) < 3:
                print("Player 1 unable to declare war.")
                print("PLAYER 2 WINS!")
                game_on = False
                break
            elif len(player_2.all_cards) < 3:
                print("Player 2 unable to declare war.")
                print("PLAYER 1 WINS!")
                game_on = False
                break
            else:
                for num in range(3):
                    player_1_cards.append(player_1.remove_one())
                    player_2_cards.append(player_2.remove_one())






