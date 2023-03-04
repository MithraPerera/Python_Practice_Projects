from art import logo
from deck import Deck
from hand import Hand
from chips import Chips

playing = True


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Sorry please provide an integer.")
        else:
            if chips.bet > chips.total:
                print("Sorry, not enough chips. You have {}".format(chips.total))
                break
            else:
                break


def hit(current_deck, hand):
    hand.add_card(current_deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(current_deck, hand):
    while True:
        x = input("Hit or Stand? Enter h or s: ")
        if x[0].lower() == "h":
            hit(current_deck, hand)
            return True
        elif x[0].lower() == "s":
            print("Player stands. Dealer's turn.")
            return False
        else:
            print("Sorry incorrect entry.")


def show_some(player, dealer):
    # Show 1 of dealers cards
    print("\n*** Dealer's Hand ***")
    print("First card hidden!")
    print(dealer.cards[1])

    # Show all 2 of players cards
    print("\n*** Player's Hand ***")
    for card in player.cards:
        print(card)
    print("Value of players hand is: {}".format(player.value))


def show_all(player, dealer):
    # show all dealers cards. Calculate and display value
    print("\n*** Dealer's Hand ***", *dealer.cards, sep='\n')
    # for card in dealer.cards:
    #     print(card)
    print("Value of dealers hand is: {}".format(dealer.value))
    #show all players cards
    print("\n*** Player's Hand ***")
    for card in player.cards:
        print(card)
    print("Value of players hand is: {}".format(player.value))


# End Game Scenarios

def player_busts(player, dealer):
    print("Player Bust!")
    player.chips.lose_bet()


def player_wins(player, dealer):
    print("Player Wins!")
    player.chips.win_bet()


def dealer_busts(player, dealer):
    print("Player Wins!")
    player.chips.win_bet()


def dealer_wins(player, dealer):
    print("Dealer Wins!")
    player.chips.lose_bet()


def push(player, dealer):
    print("Dealer and player tie! PUSH!")


# GAME LOGIC
player_hand = Hand()
dealer_hand = Hand()

while True:
    print(logo)
    print("Welcome to Blackjack!")
    deck = Deck()
    deck.shuffle()
    player_hand.start_fresh()
    dealer_hand.start_fresh()
    # Hand out cards from deck
    for i in range(2):
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
    # Set up the Players chips
    # player_chips = Chips(200)
    # Get players bet
    take_bet(player_hand.chips)
    # Show cards except 1 of the dealers
    show_some(player_hand, dealer_hand)

    while playing:
        # Ask player to Hit or Stand
        playing = hit_or_stand(deck, player_hand)
        # Show cards
        show_some(player_hand, dealer_hand)
        # if player busts, break out of the loop of playing
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand)
            break

    # If player hasn't busted, play dealers hand until they beat the player
    if player_hand.value <= 21:
        while dealer_hand.value < player_hand.value:
            hit(deck, dealer_hand)
        show_all(player_hand, dealer_hand)
        # Different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand)
        else:
            push(player_hand, dealer_hand)

    print("Player's total chips: {}".format(player_hand.chips.total))
    # Ask player to play again
    new_game = input("Play again? Y/N: ")
    if new_game[0].lower() == "n":
        print("Thank you for playing!")
        break









