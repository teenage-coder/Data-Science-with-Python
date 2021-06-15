import random

times = int(input("How many chancess you want to play: "))


print("****************")
print("*   Rock - 0   *")
print("*  Paper - 1   *")
print("* Scissors - 2 *")
print("****************")
print("")

playerScore = 0
opponentScore = 0
chancess = 0

while (chancess != times):

    opponent = random.randint(0,2)
    player   = int(input("Enter your choice (0-2): "))

    if (opponent == player):
        print("Its a tie!")


    if (opponent == 0 and player == 1):
        print("You Won!")
        playerScore = playerScore + 1
        chancess += 1

    if (opponent == 0 and player == 2):
        print("You Lost")
        opponentScore = opponentScore + 1
        chancess += 1

    if (opponent == 1 and player == 0):
        print("You Lost")
        opponentScore = opponentScore + 1
        chancess += 1

    if (opponent == 1 and player == 2):
        print("You Won!")
        playerScore = playerScore + 1
        chancess += 1

    if (opponent == 2 and player == 0):
        print("You Won")
        playerScore = playerScore + 1
        chancess += 1

    if (opponent == 2 and player == 1):
        print("You Lost!")
        opponentScore = opponentScore + 1
        chancess += 1

    print("****************")
    
print("")
print("")

print("Score Board")
print("*******************")
print("Wins:      ", playerScore)
print("Losses     ",opponentScore)
print("*******************")


