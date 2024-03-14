arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

def linearSearch(searchItem):
    for item in arrayData:
        if item == searchItem:
            return True
    return False

userInput = int(input("enter a value to search: "))
retVal = linearSearch(userInput)
if retVal:
    print("Value found in list")
else:
    print("value not found in list")

def BubbleSort():
    for x in range(len(arrayData)):
        for y in range(len(arrayData)-1):
            if arrayData[y] < arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp

BubbleSort()
print(arrayData)