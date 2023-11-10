gameboard = [[1,2,3],
             [4,5,6],
             [7,8,9]]

def printboard():
    for row in range(3):
        for col in range(3):
            print(gameboard)
        print()
printboard()