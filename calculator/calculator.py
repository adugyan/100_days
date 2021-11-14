from typing import Dict
from art import logo
from replit import clear

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations: Dict[str, int] = { 
  "+": add,
  "-": subtract,
  "*": multiply,                        
  "/": divide      
}

def calculator() -> None:
  print(logo)
  num1 = float(input("What's the first number?: "))

  for symbol in operations:
    print(symbol)
  game_start: bool = True

  while game_start == True:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))

    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    player_choice = input(f"Enter 'y' to continue calculating with {answer} or enter 'n' to start a new calculation: ")
    if player_choice == 'y':
      num1 = answer
    elif player_choice == 'n':
      game_start = False
      clear()
      calculator()

calculator()
