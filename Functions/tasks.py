# TASK1 : make a function that takes 2 parameters and returns their sum
def SumOfNumbers(firstvalue, secondvalue):
    total = firstvalue + secondvalue
    return total
firstnum = int(input("please enter first  number"))
secondnum = int(input("please enter second number"))
numsum = SumOfNumbers(firstnum, secondnum)
print(f'sum of {firstnum} and {secondnum} is {numsum}')

#TASK2 : make a function that calls another function that takes input of a number and validates if it is positive
# output multiplication table of the number in the first function
def posnum(number):
    while number < 0:
        number = int(input("invalid number, please enter a positive number"))
    return number
def MultTable():
    usernum = int(input("enter a positive number"))
    usernum = posnum(usernum)
    for i in range(1, 11):
        product = usernum * i
        print(f'{usernum}   x   {i}  =  {product}')

MultTable()

#TASK3 : make a function pyramid, that calls outputspaces(), updatevalues(), outputsymbols() as required

def outputsymbols(line):
    print("#" * ((line * 2) + 1), end='')

def outputspaces(size, line):
        print(" " * (size - (line + 1)), end='')

def updatevalue(line):
    return line + 1

def pyramid():
    pysize = int(input("enter pyramid size"))
    linenum = 0
    while(linenum < pysize):
        outputspaces(pysize, linenum)
        outputsymbols(linenum)
        linenum = updatevalue(linenum)
        print()

pyramid()