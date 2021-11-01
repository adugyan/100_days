from replit import clear
import random
from hangman_words import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
counter: int = 0
end_of_game = False
lives = 6

# Imports the logo from hangman_art.py and prints it at the start of the game.
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display: list = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear() #gets rid of the backlog 

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
      print("You've already guessed this letter.")
      counter += 1

    if counter == 3:
      print("How many times do we have to teach you this lesson, old man?")
      counter = 0
      lives -= 1
      if lives == 0:
            end_of_game = True
            print("You lose!")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win!")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])
