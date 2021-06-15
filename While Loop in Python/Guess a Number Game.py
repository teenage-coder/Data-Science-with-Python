import random


chancess = 1
number = random.randint(0,9)

while (True):

    guess  = int(input("Enter a number (0-9): "))

    if (number == guess):
        print("You've guessed the number correctly")
        break
    else:
        print("You loss!")
        chancess += 1

    print("*****************")

print("Chancess: ",chancess)
