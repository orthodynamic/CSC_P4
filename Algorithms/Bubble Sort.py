# BUBBLE SORT

MyList = [321,142,2131,31,3,12,3,12,1,421,3,21,3,21,31,23,12]
MaxIndex = len(MyList)-1
n = MaxIndex - 1
for i in range(MaxIndex):
    for j in range(n+1):
        if MyList[j] > MyList[j+1]:
            Temp = MyList[j]
            MyList[j] = MyList[j+1]
            MyList[j+1] = Temp
    n -= 1
print(MyList)