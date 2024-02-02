# Binary Search

SearchItem = None
List = []
MaxItems = len(List)
found = False
SearchFailed = False
First = 0
Last = MaxItems - 1
Middle = None
while not found and not SearchFailed:
    Middle = (First + Last)//2
    if List[Middle] == SearchItem:
        found = True
    elif First >= Last:
        SearchFailed = True
    elif List[Middle] > SearchItem:
        Last = Middle - 1
    else:
        First = Middle + 1
if found == True:
    print(Middle)
else:
    print("Item not present in array")
