# make a 2 player rock, paper, scissor game that runs for n rounds. ask user for n value
# output winner of each round and game
point1 = 0
point2 = 0
print("WELCOME TO ROCK PAPER SCISSOR GAME")
print("PRESS r FOR ROCK")
print("PRESS p FOR PAPER")
print("PRESS s FOR SCISSOR")
n = int(input("enter the number of rounds you want to play"))
for round in range(1, n+1):
    print("ROUND", round, "STARTS")
    p1: str = input("player 1, enter your choice")
    p2: str = input("player 2, enter your choice")
    if p1 == p2:
        point1 = point1 + 0
        point2 = point2 + 0
        print("round", round, "is tied")
    elif p1 == 'r' and p2 == 's' or p1 == 'p' and p2 == 'r' or p1 == 's' and p2 == 'p':
        point1 = point1 + 1
        print("player 1 is winner of round", round)
    else:
        point2: int = point2 + 1
        print("player 2 is winner of round", round)
print()
if point1 == point2:
    print("the game is tied")
elif point1 > point2:
    print("player 1 wins the game")
else:
    print("player 2 wins the game")
