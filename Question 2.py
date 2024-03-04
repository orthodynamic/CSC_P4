class saledata:
    def __init__(self, i, q):
        self.__ID = i
        self.__Qty = q

global CircularQueue
CircularQueue = [saledata("", i) for i in range(5)]
global Head
global Tail
global NumberOfItems
Head = 0
Tail = 0
NumberOfItems = 0

 takes a new record as a parameter
• inserts the record in the circular queue at the element pointed to by Tail
• updates pointers and other variables as required
• returns −1 if the circular queue is full
• returns 1 if the record is stored successfully.

def Enqueue(saleitem):
    global  Tail
    global NumberOfItems
    global CircularQueue
    if NumberOfItems != 5:
        CircularQueue[Tail] = saleitem
        Tail = (Tail=1)%5
        return 1
    else:
        return -1

def Dequeue():
    global Head
    global NumberOfItems
    if NumberOfItems == 0:
        return saledata("", -1)
    else:
        retVal = CircularQueue
        Head = (Head+1)%5
        NumberOfItems -= 1
        return retVal


