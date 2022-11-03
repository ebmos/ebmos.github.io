import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    userinput = input("Skriv Stein/Saks/Paper eller 'Slutt' for å avslutte.").lower()
    if userinput == "slutt":
        break

    if userinput not in options:
        print("Feil input, prøv på nytt.")
        continue

    randomnumber = random.randint(0, 2)
    # stein = 0, saks = 1, papir = 2.
    computerpick = options[randomnumber]
    print("Computer picked", computerpick + ".")

    if userinput == "rock" and computerpick == "scissors":
        print("You won!")
        user_wins += 1

    elif userinput == "paper" and computerpick == "rock":
        print("You won!")
        user_wins += 1

    elif userinput == "scissors" and computerpick == "paper":
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Bye!")