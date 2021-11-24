import random 
from art import logo
import time

def deal_card() -> int:
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

user_cards = []
computer_cards = []

for _ in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

def calculate_score(hand):
  cards: list = [] # empty list so that previous sums will be appended into this and re summed

  if type(hand) == int:
    cards.append(hand)
    score = sum(cards)
    if 11 in cards and 10 in cards:
      return 0
    elif 11 in cards and score > 21:
      cards.remove(11)
      cards.append(1)
    return score  
  else:
    score = sum(hand)
    if 11 in hand and 10 in hand:
      return 0
    elif 11 in hand and score > 21:
      hand.remove(11)
      hand.append(1)
    return score

def main_game() -> int:
  print(logo)
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)

  #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
  if user_score == 0:
    print("Black Jack. You win")
    quit()
  elif computer_score == 0:
    print("Dealer black jack. You lose")
    quit()

  #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
  print(f"Your score is {user_score}")
  print(f"The dealer's score is {computer_score}")

  while user_score < 21:
    hit = input("Do you want to draw another card? 'y/n': ")
    if hit == 'y':
      user_cards.append(deal_card())
      user_score = calculate_score(user_cards)
      print(f"Your score is {user_score}")
    elif hit == 'n':
      user_score = calculate_score(user_cards)
      print(f"Your score is {user_score}")
      break

  while computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards) 
    time.sleep(1)
    print(f"The dealer's score is {computer_score}")

  return user_score, computer_score

user_total, computer_total = main_game()

def compare(userT, compT):
  if userT > 21:
    print("Bust")
  elif compT > 21:
    print("Dealer busts")
  elif userT > compT:
    print("You win")
  elif userT < compT:
    print("Dealer wins")
  elif userT == compT:
    print("Draw") 

compare(user_total, computer_total)
