import random
from words import word_list
from artwork import logo, stages
import os

lives = 6
end_of_game = False

print(logo)
# Pick a random work from words lis
chosen_word = random.choice(word_list)
print(f"for debugging only: Chosen word is {chosen_word}")
# Generate an emplty list to and populate it with "_" corresponging to letters in chosen word
display = []
for letter in chosen_word:
    display.append("_")

# Ask user to guess a letter and convert to lower case.

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    os.system('clear')

    if guess in display:
        print(f"You already guessed {guess}")

    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if guess == letter:
            display[i] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess} which is not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(f"{' '.join(display)}\n")
    print(stages[lives])
    
    if "_" not in display:
        end_of_game = True
        print("You Win")

