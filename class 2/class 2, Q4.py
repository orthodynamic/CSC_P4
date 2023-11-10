# ask user for the size of the pyramid and output the pyramid of that height

pysize = int(input("please enter the size of the pyramid"))
for x in range(1, pysize+1):
    spacenum = pysize-x
    for space in range(spacenum):
        print(" ", end="")
    symbolnum = (x * 2)-1
    for symbol in range(symbolnum):
            print("#", end="")
    print()

print()



