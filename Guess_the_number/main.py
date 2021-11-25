import random
from art import logo

number = int(random.randint(1,100))

def main_game(answer, difficulty_level) -> None:
  """
  The basic game loop for easy mode. The player will have 10 chances to guess the correct answer 
  """
  if difficulty_level == 'easy':
    attempts_left: int = 10
  elif difficulty_level == 'hard':
    attempts_left: int = 5
  else:
    print("Select a valid option")
    return
  
  attempts_are_remaining: bool = True
  answer: int 

  print(f"{difficulty_level} mode allots you {attempts_left} attempts")
  while attempts_are_remaining == True:
    guess = (int(input("Make a guess: ")))
    
    if (guess == answer):
      print(f"You got it! The answer was {answer}")
      return
    elif guess > answer:
      attempts_left -= 1
      print(f"Your guess was too high. You have {attempts_left} tries left.")
    elif guess < answer:
      attempts_left -= 1
      print(f"Your guess was too low. You have {attempts_left} tries left.")
    
    if attempts_left == 0:
      attempts_are_remaining = False

  print("You lose!")


print(logo)
print(f"""Welcome to the number guessing game!
Pick a number between 1 and 100.
Psst the answer is {number}""")

difficulty = input("Choose a difficulty. 'easy' or 'hard': ")

main_game(number, difficulty)
