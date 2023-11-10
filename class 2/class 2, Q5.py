# ask user for the number of fishes and size of the fishes and print that many fishes

fishnum = int(input("enter number of fishes"))
fishsize = int(input("enter size of each fish"))
for count in range(fishnum):
    for x in range(1, fishsize+1):
        spacenum = fishsize-x
        for space in range(spacenum):
           print(" ", end='')
        symbolnum = (x * 2)-1
        for symbol in range(symbolnum):
           print("#", end='')
        print()
    for y in range(fishsize, 0, -1):
        spacenum = fishsize-y
        for space in range(spacenum):
            print(" ", end='')
        symbolnum = (y * 2)-1
        for symbol in range(symbolnum):
            print("#", end='')
        print()
    for z in range(y+1, fishsize+1):
        spacenum = fishsize-z
        for space in range(spacenum):
            print(" ", end='')
        symbolnum = (z*2)-1
        for symbol in range(symbolnum):
            print("#", end='')
        print()
    print()
print()
