import random
import colorama
from colorama import Fore

print("Welcome to a 'Guess the number' game!")

play = input("Wish to proceed? ").lower()
options = ["yes", "no"]

if play not in options:
    print("Incorrect input.")

if play == "no":
    quit()

while True:

    randomNumber = random.randint(1,25)

    number = int(input(Fore.WHITE + "What number is the computer thinking of? (1-25): ").lower())

    if number > randomNumber:
        print(Fore.RED + "Too high, go lower.")

    if number < randomNumber:
        print(Fore.RED + "Too low, go higher.")

    if number == randomNumber:
        print(Fore.GREEN + "Congratulations, you won!")
        break