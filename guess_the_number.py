from art import logo
import os #it helps cleaning the previous stage
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check user's guess against actual answer
def check_answer(guess, number, turns): # to activate = check_answer(guess, number)
    """Checks answer against guess. Returns the number of turns remaining"""
    if guess == number:
      print(f"The number is {number}. You Win 😁")
      # game_end = True
    elif guess > number:
      print("Too hight")
      return turns - 1 
    elif guess < number:
      print("Too low")
      return turns - 1
    else:
      print("You need to write a number beetween 1 and 100. Try again")
      
def set_difficulty(): #to activate = set_dificulty() 
  """Select the difficulty"""
  game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if game_difficulty == "easy":
    return EASY_LEVEL_TURNS #It helps me to find the number of turns for the 'turns' variable
  elif game_difficulty == "hard":
    return HARD_LEVEL_TURNS #It helps me to find the number of turns for the 'turns' variable

# def number_of_turns():

def play_game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  number = random.randint(1, 101) 
  # print(f"Pssst, the correct answer is {number}")
  turns = set_difficulty()
  
  #Let the user guess the number
  guess = 0
  while guess != number:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, number, turns)
    if turns == 0:
      print("You lost ☹️, try again")
      return # It ends the function 'play_game'
    elif guess != number:
      print("Guess again")
while input("\nDo you want to guess the number? Type 'y' or 'n': \n") == "y":
  os.system('cls' if os.name == 'nt' else 'clear') #with this code the game would clean the previous stage
  play_game() #Does the user want to play another game?