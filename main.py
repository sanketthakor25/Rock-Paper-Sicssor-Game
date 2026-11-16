#1 for stone
#2 for paper 
#3 scissor
import random

computer = random.randint(1,3)
gamestr = input("Enter your choice: ")
gamedict = { "s" : 1,
             "p" : 2,
             "si" : 3} 
reversedict = {1 : "Stone",
               2 : "Paper",
               3 : "Scissor"}

if gamestr not in gamedict:
    print("Invalid choice!!")
    exit()

game = gamedict[gamestr]
print(f"Your choice is {reversedict[game]}")
print(f"Computer choice is {reversedict[computer]}")

if(computer == game):
    print("Draw!!")
else:
    if(computer == 1 and game == 2):
        print("You Win!!")
    elif(computer == 1 and game == 3):
        print("You lose!")
    if(computer == 2 and game == 1):
        print("You lose!")
    elif(computer == 2 and game == 3):
        print("You win!")
    if(computer == 3 and game == 1):
        print("You lose!")
    elif(computer == 3 and game  == 2):
        print("You win!!")            
    
   
        