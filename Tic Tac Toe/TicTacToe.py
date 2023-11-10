gameboard = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]


# to print game board
def printboard():
    print("-------------------")
    for row in range(3):
        for col in range(3):
            if col == 2:
                print("| ", gameboard[row][col], end='  |')
            else:
                print("| ", gameboard[row][col], end='  ')
        print()
        print("-------------------")


# alter the game board
def userinput(choice, player):
    if choice == 1:
        gameboard[0][0] = player
    elif choice == 2:
        gameboard[0][1] = player
    elif choice == 3:
        gameboard[0][2] = player
    elif choice == 4:
        gameboard[1][0] = player
    elif choice == 5:
        gameboard[1][1] = player
    elif choice == 6:
        gameboard[1][2] = player
    elif choice == 7:
        gameboard[2][0] = player
    elif choice == 8:
        gameboard[2][1] = player
    elif choice == 9:
        gameboard[2][2] = player


# to take user's input
def move(count, playersymbol, name, position):
    status = "False"
    choice = int(input(f"{name} choose your desired location"))
    while status == False:
        for check in range(len(position)):
            if choice != position[check]:
                status = "False"
            else:
                status = "True"
        if status == "False":
            choice = int(input(f"Location entered is already taken, {name} please choose another location"))
    if count % 2 == 0:
        userinput(choice, playersymbol)
    else:
        userinput(choice, playersymbol)
    return choice


# check winning conditions
def conditions(symbol):
    flag = "draw"
    for x in range(3):
        if gameboard[x][0] == symbol and gameboard[x][1] == symbol and gameboard[x][2] == symbol:
            flag = "win"
    for y in range(3):
        if gameboard[0][y] == symbol and gameboard[1][y] == symbol and gameboard[2][y] == symbol:
            flag = "win"
    if gameboard[0][0] == symbol and gameboard[1][1] == symbol and gameboard[2][2] == symbol:
        flag = "win"
    if gameboard[2][2] == symbol and gameboard[1][1] == symbol and gameboard[0][0] == symbol:
        flag = "win"
    return flag


# _______________________________________________________________________________________________________________________

print("--------------------------")
print("| WELCOME TO TIC TAC TOE |")
print("--------------------------")
symbols = ["#", "X", "Y", "+", "$"]
onename = input("Player 1, please enter your name")
player1 = input(f"{onename} please choose your symbol from these {symbols}")
symbols.remove(player1)
twoname = input("Player 2, please enter your name")
player2 = input(f"{twoname} please choose your symbol from these {symbols}")
position = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(9):
    if i % 2 == 0:
        currentsymbol = player1
        currentname = onename
    else:
        currentsymbol = player2
        currentname = twoname
    printboard()
    choice = int(move(i, currentsymbol, currentname, position))
    position.remove(choice)
    gamestatus = conditions(currentsymbol)
    if gamestatus == "win":
        print("-----------------------------")
        print(f'| {currentname} WINS THE GAME! |')
        print("-----------------------------")
        break
    elif i == 8:
        print("---------------")
        print("IT IS A DRAW")
        print("---------------")
printboard()
