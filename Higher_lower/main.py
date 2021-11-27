import random
import os
from art import logo, vs
from game_data import data

print(logo)

def game_loop():
  """
  Pack the follower_count into variables
  a. compare the selection to both of the variables 
  
  """
  winner: int # will contain the higher follower count
  score: int = 0 # records how many round the player has won
  end_game: bool = False
  option_A: int # will contain the value for A
  option_B: int # containes the value for option B

  while end_game == False:
    both_follower_count: list = [] # empty list that both of the follower counts will be appended into so that the highest one can be extracted for a later step
    option_A = data[random.randrange(len(data))]
    option_B = data[random.randrange(len(data))]

    # format the values for A
    A_name = option_A['name']
    A_description = option_A['description']
    A_country = option_A['country']
    A_count = option_A['follower_count']

    # format the values for B
    B_name = option_B['name']
    B_description = option_B['description']
    B_country = option_B['country']
    B_count = option_B['follower_count']

    print(f"Compare A: {A_name}, a {A_description}, from {A_country}. Hint : {A_count}")
    print(vs)
    print(f"Against B: {B_name}, a {B_description}, from {B_country}. Hint : {B_count}")


    both_follower_count.append(A_count)
    both_follower_count.append(B_count)
    winner = max(both_follower_count)

    selection = input("Who has more followers? Type 'A' or 'B': ").upper()

    if selection == 'A':
      selection = A_count
    elif selection == 'B':
      selection = B_count

    if selection == winner:
      os.system('clear')
      score += 1
      print(logo)
      print(f"You're right! Current score: {score}")
    else:
      print(f"Sorry, that's wrong. Final Score: {score}")
      end_game = True

game_loop()
