 import random 
 import time 
 import os 
  
 round = 1 
 streak = 0 
  
 print("Welcome to 'Guess the number'!") 
 time.sleep(0.2) 
 print("So as the name suggests, you'll be given a random number which you need to guess!") 
 print("Also you will get a random starting number which will indicate if the number is lower or higher than the starting number!") 
 time.sleep(0.2) 
  
 def explanation(): 
     if __name__ == '__main__': 
         start = 'input' 
         while not start in ['y', 'n', 'yes', 'no']: 
             start = input('Do you undestand the basics of the game? (y/n): ') 
         if start == 'y' or start == 'yes': 
             os.system('cls') 
             print("\n") 
             game() 
         else: 
             pass 
             detailed_input = input('Do you want more explanation? (y/n): ') 
             if detailed_input == 'yes' or detailed_input == 'y': 
                 detailed_explanation() 
             else: 
                 return explanation() 
  
  
 def detailed_explanation(): 
     time.sleep(1) 
     print("\nAt the start of the game you will be given a number between 1 and 100 and you need to guess the number that is hidden.\n To help with that you will be given >, < depending on if the number is higher or lower than the hidden number") 
     time.sleep(1) 
     print("You have 10 attempts to guess the number and if you fail to do so you lose the game and a streak if you had one.") 
     time.sleep(1) 
     print("If you however do win you will get a streak point which tells you how many times you won in the row!") 
     time.sleep(5) 
     return explanation() 
  
 def game(): 
  
     global round 
     global streak 
     random_number = random.randint(1, 100) 
     first_number = random.randint(1, 99) 
     while first_number == random_number: 
         first_number = random.randint(1, 99) 
     attempts = 10 
  
     print(f"Game {round}") 
     print(f"The starting number is {first_number}\n") 
     guessed_number = first_number 
     while attempts > 0: 
         if guessed_number > random_number: 
             print(f"\r< {guessed_number}", end = '') 
         else: 
             print(f"\r> {guessed_number}", end = '') 
         guessed_number = int(input(": ")) 
         while not guessed_number < 101: 
             guessed_number = int(input("Invalid guess!: ")) 
              
         attempts = attempts - 1 
         if guessed_number == random_number: 
             streak += 1 
             os.system('cls') 
             print(f"You win! Your streak is {streak}") 
             round += 1 
             return game() 
     print(f"You lose! Your streak is {streak}") 
     round += 1 
  
     return game() 
  
              
  
      
 explanation()
