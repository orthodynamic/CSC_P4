"""
Procedure = VOID FUNCTIONS
Functions = FRUITFUL FUNCTIONS
"""

# void functions
def inputOddNumber():
    number = 0
    while number % 2 == 0:
        number = int(input("enter odd number"))
    print("valid number entered")
# main program starts here
inputOddNumber()

# void functions with parameters
def outputsymbol(numofsymbols, symbol):
    for count in range(numofsymbols):
        print(symbol, end=' ')
    print()
# main program starts here
outputsymbol(10, "#")

# fruitful functions
def inputOddNumber():
    number = 0
    while number % 2 == 0:
        number = int(input("enter odd number"))
    print("valid number entered")
    return number
# main program starts here
newnumber = inputOddNumber()
print(f'{newnumber} is the returned value')

# fruitful functions with parameters
def sumrange(firstvalue, lastvalue):
    sum = 0
    for thisvalue in range(firstvalue, lastvalue + 1):
        sum = sum + thisvalue
    return sum
# main program starts here
NewNumber = sumrange(10,15)
print(NewNumber)

#byref functions (python do not have byref functions, thus we would try to implement a function that works just like a by reference function)

def adjustValuesForNextBox(spaces, symbols):
    spaces = spaces - 1
    symbols = symbols + 2
    return spaces, symbols
# main program starts here
numofspaces = int(input("enter number of spaces : "))
numofsymbols = int(input("enter number of symbols : "))
numofspaces, numofsymbols = adjustValuesForNextBox(numofspaces, numofsymbols)
print(numofspaces)
print(numofsymbols)


