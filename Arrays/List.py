list1 = []
list1.append("Babar Azam")
list1.append("Virat Kohli")
list1.append("Viv Richards")
print(list1)
print(list1[0])
print(f"Length of list1 = {len(list1)}")
for i in range(len(list1)):
    print(list1[i])

list2 = [0,0,0,0,0]
print("Values in list 2")
for i in range(len(list2)):
    print(list2[i])

#arrayName = [initial Value for i in range(size)]
list3 = [1 for i in range(100)]
print("values in list 3")
for j in range(1, len(list3)):
    print(f'{j} = {list3[j]}')