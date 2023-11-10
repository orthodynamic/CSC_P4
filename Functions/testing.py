def outputspaces(pyramidHeight, rowNum):
    print(" " * (pyramidHeight - (rowNum + 1)), end="")


def outputsymbols(rowNum):
    print("#" * (2 * rowNum + 1), end="")


def updatevalues(rowNum):
    return rowNum + 1


def pyramid(pyramidHeight):
    rowNum = 0
    while (rowNum < pyramidHeight):
        outputspaces(pyramidHeight, rowNum)
        outputsymbols(rowNum)
        rowNum = updatevalues(rowNum)
        print()


pyramid(int(input("Enter pyramid height : ")))