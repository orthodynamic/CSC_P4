# record is created as class in python
# all attributes in records are public
# private: __
# public: nothing is required
# a class will always have a private constructor: def __init__
# multi line comment: shortcut: ctrl + /
# if attribute init is not given, use parameters

class node:
    # self.data: INTEGER
    # self.nextNode: INTEGER
    def __init__(self, thisData, thisNextNode):
        self.data = thisData
        self.nextNode = thisNextNode

LinkedList = [node(1, 1), node(5, 4), node(6, 7), node(7, -1), node(2, 2),
              node(0, 6), node(0, 8), node(56, 3), node(0, 9), node(0, -1), ]
# LinkedList.append(node(dataValue, NextNodeValue))
startPointer = 0
emptyList = 5

# function: def
# list/arrays are by default public
def outputNodes(LinkedList, startPointer):
    CurrentPointer = startPointer
    while CurrentPointer != -1:
        print(LinkedList[CurrentPointer].data)
        CurrentPointer = LinkedList[CurrentPointer].nextNode

outputNodes(LinkedList, startPointer)

def addNodes(LinkedList, startPointer, emptylist):
    # global startPointer
    # global emptyList
    if emptylist == -1:
        return False
    else:
        userInput = int(input("Enter the data to add: "))
        thisNode = emptylist
        emptyList = LinkedList[emptylist].nextNode
        LinkedList[emptylist].data = userInput
        LinkedList[thisNode].nextNode = -1
        currentPointer = startPointer
        while currentPointer != -1:
            prevPointer = currentPointer
            currentPointer = LinkedList[currentPointer].nextNode
        LinkedList[prevPointer].nextNode = thisNode
        return True

retval = addNodes(LinkedList, startPointer, emptyList)
if retval:
    print("Value added")
else:
    print("Linked list is full")
outputNodes(LinkedList, startPointer)

