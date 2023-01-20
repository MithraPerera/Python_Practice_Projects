import os
import random
from art import logo, vs
from game_data import data


def choose_random():
    random_a = random.choice(data)
    random_b = random.choice(data)
    while random_b == random_a:
        random_b = random.choice(data)
    return [random_a, random_b]


def check_winner(choice, a, b):
    if choice == 'A' and a > b:
        return True
    elif choice == 'B' and b > a:
        return True
    else:
        return False

# THIS IMPLEMENTATION STORES THE SCORE WITHIN THE GAME FUNCTION

# def game():
#     score = 0
#     while True:
#         options = choose_random()
#         print(f"Compare A: {options[0]['name']}, a {options[0]['description']} from {options[0]['country']}")
#         print(vs)
#         print(f"Against B: {options[1]['name']}, a {options[1]['description']} from {options[1]['country']}")
#         user_choice = input("Who has more followers? Type 'A' or 'B': ")
#         user_win = check_winner(user_choice, options[0]["follower_count"], options[1]["follower_count"])
#         if user_win:
#             os.system('cls' if os.name == 'nt' else 'clear')
#             print(logo)
#             score += 1
#             print(f"You're right! Current Score: {score}")
#         else:
#             os.system('cls' if os.name == 'nt' else 'clear')
#             print(f"Sorry, that is wrong. Final Score: {score}")
#             break
#
#
# print(logo)
# game()


# THIS IMPLEMENTATION STORES THE SCORE GLOBALLY

score = 0


def game(current_score):
    options = choose_random()
    print(f"Compare A: {options[0]['name']}, a {options[0]['description']} from {options[0]['country']}")
    print(vs)
    print(f"Against B: {options[1]['name']}, a {options[1]['description']} from {options[1]['country']}")
    user_choice = input("Who has more followers? Type 'A' or 'B': ")
    user_win = check_winner(user_choice, options[0]["follower_count"], options[1]["follower_count"])
    if user_win:
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Sorry, that is wrong. Final Score: {current_score}")
        exit()


print(logo)

while True:
    game(score)
    print(logo)
    score += 1
    print(f"You're right! Current Score: {score}")
