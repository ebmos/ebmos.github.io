import random
import colorama
from colorama import Fore

userWins = 0
compWins = 0


options = ["rock", "paper", "scissors", "quit"]
yesno = ["yes", "no"]

playing = input("Want to play? (yes/no) ")

if playing == "no":
    print("Bye.")
    quit()

if playing not in yesno:
    print("Feil input.")

while True:

    play = input(Fore.WHITE + "Rock paper or scissors? (enter quit to quit) ").lower()

    if play not in options:
        print("Feil input.")
        continue

    if play == "quit":
        print("Okay then, bye.")
        break

    randomnumber = random.randint(0,2)
    compChose = options[randomnumber]

    if play == "rock" and compChose == "scissors":
        print(Fore.GREEN + "You won!")
        print(Fore.WHITE + "The computer chose", compChose)
        userWins += 1
    
    elif play == "paper" and compChose == "rock":
        print(Fore.GREEN + "You won!")
        print(Fore.WHITE + "The computer chose", compChose)
        userWins += 1

    elif play == "scissors" and compChose == "paper":
        print(Fore.GREEN + "You won!")
        print(Fore.WHITE + "The computer chose", compChose)
        userWins += 1

    else:
        print(Fore.RED + "You lost.")
        print(Fore.WHITE + "The computer chose", compChose)

    if compWins == 3:
        print(Fore.RED + "You lost the bo3. Your score was", userWins)
        break
    else: 
        print(Fore.YELLOW + "You won the bo3! Your score was", userWins)
        break