import random
import os
from art import logo

play_game = True


# Helper Function: Returns a random card from the deck
def random_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


# Helper Function: Returns the total and implements 11 changed to 1 if over 21
def add_cards(hand):
    """Takes in a list of numbers and returns the sum with logic to replace 11 with 1 when necessary for total sum calculation."""
    cards_in_hand = len(hand)
    # for card in hand:
    #     total += card
    total = sum(hand)
    if total > 21 and (hand[cards_in_hand - 1] == 11):
        # replace 11 with a 1
        total = total - 10
    return total


# Helper Function: Prints the winner and ends the game
def game_result(final_user_hand, final_user_total, final_computer_hand, final_computer_total):
    """Takes the  users hand, computers hand and their scores and prints the winner. It then returns False."""

    print(f"Your final hand: {final_user_hand}, final total: {final_user_total}")
    print(f"Computers final hand: {final_computer_hand}, final total: {final_computer_total}")

    # Game Result Logic
    if final_user_total == 21 and final_computer_total == 21:
        print("Double Blackjack! Tie Game 🤯")
    elif final_user_total == 21:
        print("User Wins! 🥳")
    elif final_user_total < 21 < final_computer_total:
        print("User Wins! 🥳")
    elif final_user_total > final_computer_total and (final_user_total < 21) and (final_computer_total < 21):
        print("User Wins! 🥳")
    else:
        print("Computer wins!😭")

    return False


# Single game logic
def blackjack():
    """Implements a single round of blackjack when called."""
    # Initialize Variables
    user_hand = [random_card(), random_card()]
    computer_hand = [random_card(), random_card()]
    computer_total = add_cards(computer_hand)
    game_on = True
    computer_turn = True

    print(f"You cards: {user_hand}, current total: {add_cards(user_hand)}")
    print(f"Computer's first card: {user_hand[0]}")
    while game_on:
        user_hit = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_hit == 'y':
            user_hand.append(random_card())
            user_total = add_cards(user_hand)
            print(f"You cards: {user_hand}, current total: {user_total}")
            print(f"Computer's first card: {user_hand[0]}")
            if user_total > 21:
                game_on = game_result(user_hand, user_total, computer_hand, computer_total)
        else:
            user_total = add_cards(user_hand)
            while computer_turn:
                computer_total = add_cards(computer_hand)
                if computer_total < 17:
                    computer_hand.append(random_card())
                else:
                    computer_turn = False
            game_on = game_result(user_hand, user_total, computer_hand, computer_total)


# Determines if user wants to play or quit
while play_game:
    user_play_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if user_play_choice == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        print("\nWelcome to Blackjack!")
        blackjack()
    else:
        print("Thank you for playing!")
        play_game = False