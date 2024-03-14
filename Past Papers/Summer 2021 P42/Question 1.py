# part a

class node:
    def __init__(self, d, n):
        self.data = d
        self.nextNode = n
# part b

LinkedList = [node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),
              node(0,6),node(0,8),node(56,3),node(0,9),node(0,-1),]
startPointer = 0
emptyList = 5

# part ci
def outputNodes(LinkedList, startPointer):
    CurrentNodePointer = startPointer
    while CurrentNodePointer != -1:
        print(LinkedList[CurrentNodePointer].data)
        CurrentNodePointer = LinkedList[CurrentNodePointer].nextNode

# part cii
outputNodes(LinkedList, startPointer)

# part di

def addNode(LinkedList, startPointer, emptyList):
    NewData = int(input("Please enter new data item"))
    if emptyList != -1:
        NewPointer = emptyList
        LinkedList[NewPointer].data = NewData
        emptyList = LinkedList[emptyList].nextNode
        ThisPointer = startPointer
        PreviousPointer = ThisPointer
        while ThisPointer != -1 and LinkedList[ThisPointer].data < NewData:
            PreviousPointer = ThisPointer
            ThisPointer = LinkedList[ThisPointer].data
        if ThisPointer == startPointer:
            LinkedList[NewPointer].nextNode = startPointer
            startPointer = NewPointer
        else:
            LinkedList[NewPointer].nextNode =LinkedList[PreviousPointer].nextNode
            LinkedList[PreviousPointer].nextNode = NewPointer
        return True
    else:
        return False

# part dii


if addNode(LinkedList, startPointer, emptyList):
    print("Node added to the Linked List")
else:
    print("No space in Linked List")
outputNodes(LinkedList, startPointer)

