

List = []
NumberOfItems = len(List)
for pointer in range(1, NumberOfItems):
    ItemToBeInserted = List[pointer]
    CurrentItem = pointer - 1
    while List[CurrentItem] > ItemToBeInserted and CurrentItem > -1:
        List[CurrentItem + 1] = List[CurrentItem]
        CurrentItem -= -1
    List[CurrentItem + 1] = ItemToBeInserted