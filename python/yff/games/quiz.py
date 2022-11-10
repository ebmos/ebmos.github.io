print("Welcome to my quiz.")

playing = input("Wish to proceed? (y/n): ")
if playing != "y":
    playing2 = input("Are you sure? (y/n)")
if playing2 == "y":
    playing3 = input("Are you sure you're sure..? (y/n)")
if playing3 == "y":
    print("Fine.")
    quit()

print("Alrighty, let's game.")
score = 0

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

if score == 3:
    print("You got all questions correct.")
else:
    print("You got " + str(score) + " questions correct.")