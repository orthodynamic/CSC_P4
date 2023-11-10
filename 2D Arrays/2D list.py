Board = [[0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0]]

#ArrayName[ROW][COL]
Board[1][5] = 5

print("Board 1")
for row in range(6):
    for col in range(7):
        print(Board[row][col], end = '    ')
    print()

print("Board 2")
#COLUMN is always IN
#ROW is always OUT
#ArrayName = [[initVal for col in range(totalCols)] for row in range(totalRows)]
Board2 = [["#" for col in range(3)]for row in range(3)]
for row in range(3):
    for col in range(3):
        print(Board2[row][col], end="  |  ")
    print()