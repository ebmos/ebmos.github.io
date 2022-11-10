import random
import colorama
from colorama import Fore

userWins = 0
compWins = 0


options = ["rock", "paper", "scissors", "quit"]
yesno = ["yes", "no"]

playing = input("Want to play? ")

if playing == "no":
    print("Bye.")
    quit()

if playing not in yesno:
    print("Feil input.")

while True:

    play = input("Rock paper or scissors? (enter quit to quit) ").lower()

    if play not in options:
        print("Feil input.")
        continue

    if play == "quit":
        print("Okay then, bye.")
        break

    randomnumber = random.randint(0,2)
    compChose = options[randomnumber]

    if play == "rock" and compChose == "scissors":
        print("You won! The computer chose", compChose)
        userWins += 1
    
    elif play == "paper" and compChose == "rock":
        print("You lost. The computer chose", compChose)
        userWins += 1

    elif play == "scissors" and compChose == "paper":
        print("You won! The computer")
        userWins += 1

    else:
        print("You lost. The computer chose", compChose)

    if compWins == 3:
        print(Fore.RED + "You lost the bo3.")
        break
    elif userWins == 3:
        print(Fore.BLUE + "You won the bo3.")
        break