import random
from replit import clear
import assets


def generate_random_number():
  number = random.randint(0,101)
  return number

def reset_screen():
  clear()
  print(assets.logo)

def game_over(lives):
  decision = ""
  if(lives>0):
    while decision not in ["n", "y"]:
      decision = input("You won, do you want to play again? (y/n): ")
    if decision == "n":
      print("Ok, thanks for playing, bye.")
      return False
    else:
      reset_screen()
      return True
  else:
    while decision not in ["n", "y"]:
      decision = input("You lost, do you want to play again? (y/n): ")
    if decision == "n":
      print("Ok, thanks for playing, bye.")
      return False
    else:
      reset_screen()
      return True

difficulty_levels = {
  "1": {"name": "high", "value": 5},
  "2": {"name": "medium", "value": 10}, 
  "3": {"name": "easy", "value": 15},
}

chosen_difficulty = ""
lives = 0

number = generate_random_number()

gameon = True
reset_screen()
while gameon:

  while chosen_difficulty not in ["3", "2", "1"]:
    chosen_difficulty = input("Choose a difficulty: \n[HARD] --> 1\n[MEDIUM] --> 2\n[EASY] --> 3\n")

  if(chosen_difficulty in ["3", "2", "1"] and lives == 0):
    lives = difficulty_levels[chosen_difficulty]["value"]
    
  
  guess= int(input("Guess a number: "))

  if(guess < number):
    lives -=1
    if(lives == 1):
      print(f"Lower, you can guess {lives} more time.")
    elif(lives > 0):
      print(f"Lower, you can guess {lives} more times.")

  elif(guess > number):
    lives -=1
    if(lives == 1):
      print(f"Higher, you can guess {lives} more time.")
    elif(lives > 0):
      print(f"Higher, you can guess {lives} more times.")
    
  if(guess == number or lives == 0):
    gameon = game_over(lives)
    chosen_difficulty = 0
    number = generate_random_number()
    lives = 0
    

