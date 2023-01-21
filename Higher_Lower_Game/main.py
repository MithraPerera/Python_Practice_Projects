import os
import random
from art import logo, vs
from game_data import data


def choose_random(option_b):
    """Returns an array of 2 instagram account data objects. The 2nd data object from a previous run is passed in and used as the first and a new 2nd object
    is selected from random.
    """
    random_a = option_b
    random_b = random.choice(data)
    # Ensures that 2 of the same accounts are not selected.
    while random_b == random_a:
        random_b = random.choice(data)
    return [random_a, random_b]


def check_winner(choice, a, b):
    """Implements the game logic to test for the winner and returns True if the user won and False if the user lost."""
    if choice == 'A' and a > b:
        return True
    elif choice == 'B' and b > a:
        return True
    else:
        return False

# THIS IMPLEMENTATION STORES THE SCORE WITHIN THE GAME FUNCTION


def game():
    """Implements the full game functionality until the user looses at which the function ends."""
    score = 0
    # Initial 2nd account that is used to pass into the first run of selecting 2 random accounts
    old_option_b = random.choice(data)
    while True:
        options = choose_random(old_option_b)
        print(f"Compare A: {options[0]['name']}, a {options[0]['description']} from {options[0]['country']}")
        print(vs)
        print(f"Against B: {options[1]['name']}, a {options[1]['description']} from {options[1]['country']}")
        user_choice = input("Who has more followers? Type 'A' or 'B': ")
        user_win = check_winner(user_choice, options[0]["follower_count"], options[1]["follower_count"])
        if user_win:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(logo)
            score += 1
            old_option_b = options[1]
            print(f"You're right! Current Score: {score}")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Sorry, that is wrong. Final Score: {score}")
            break


print(logo)
game()


# THIS IMPLEMENTATION STORES THE SCORE GLOBALLY

# score = 0
#
#
# def game(current_score):
#     options = choose_random()
#     print(f"Compare A: {options[0]['name']}, a {options[0]['description']} from {options[0]['country']}")
#     print(vs)
#     print(f"Against B: {options[1]['name']}, a {options[1]['description']} from {options[1]['country']}")
#     user_choice = input("Who has more followers? Type 'A' or 'B': ")
#     user_win = check_winner(user_choice, options[0]["follower_count"], options[1]["follower_count"])
#     if user_win:
#         os.system('cls' if os.name == 'nt' else 'clear')
#     else:
#         os.system('cls' if os.name == 'nt' else 'clear')
#         print(f"Sorry, that is wrong. Final Score: {current_score}")
#         exit()
#
#
# print(logo)
#
# while True:
#     game(score)
#     print(logo)
#     score += 1
#     print(f"You're right! Current Score: {score}")
