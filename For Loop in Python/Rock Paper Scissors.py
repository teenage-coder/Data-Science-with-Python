import random

chancess = int(input("How many chancess you want to play: "))


print("****************")
print("*   Rock - 0   *")
print("*  Paper - 1   *")
print("* Scissors - 2 *")
print("****************")
print("")

playerScore = 0
opponentScore = 0
tie = 0


for i in range(chancess):

    opponent = random.randint(0,2)
    player   = int(input("Enter your choice (0-2): "))


    if (opponent == player):
        print("Tie")
        tie = tie + 1

    if (opponent == 0 and player == 1):
        print("You Won!")
        playerScore = playerScore + 1

    if (opponent == 0 and player == 2):
        print("You Lost")
        opponentScore = opponentScore + 1

    if (opponent == 1 and player == 0):
        print("You Lost")
        opponentScore = opponentScore + 1

    if (opponent == 1 and player == 2):
        print("You Won!")
        playerScore = playerScore + 1

    if (opponent == 2 and player == 0):
        print("You Won")
        playerScore = playerScore + 1

    if (opponent == 2 and player == 1):
        print("You Lost!")
        opponentScore = opponentScore + 1

    print("****************")
    
print("")
print("")

print("Score Board")
print("*******************")
print("Total Tie: ", tie)
print("Wins:      ", playerScore)
print("Losses     ",opponentScore)
print("*******************")


