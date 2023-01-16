#Step 5

import random
from hangman_words import word_list
from hangman_art import stages, logo

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
user_answer = []
game_on = True
lives = 6
user_guesses = []

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

print(logo)
print("\nWelcome to Hangman in the Console!")
print("Your word is:")

#Create blanks
for letter in chosen_word:
    user_answer.append("_")
print(user_answer)

#TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
#TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.

while game_on and (lives > 0):
    correct_guess = False
    if "_" in user_answer:
        guess = input("\nGuess a letter: ").lower()
        if guess not in user_guesses:
            user_guesses.append(guess)

            # Check guessed letter
            for index in range(len(chosen_word)):
                if chosen_word[index] == guess:
                    user_answer[index] = guess
                    correct_guess = True

            print(user_answer)

            #TODO-2: - Import the stages from hangman_art.py and make this error go away.
            if not correct_guess:
                lives -= 1
                print(stages[lives])
                print(f"'{guess}' is not in the word.")
            else:
                print(stages[lives])
        else:
            print(f"You have already said '{guess}'.\n")

    else:
        game_on = False

if lives == 0:
    print("\nYou lose!")
else:
    print("\nYou win!")