myStr = "This is Cedar College"
print(myStr[5])
print(chr(65))
print(ord('A'))
print(len(myStr))

#[start : end]
#if left is empty : end = length
#if right is empty : end = length
#if left is negative : start = length - value
#if right is negative : end = length - value

#mid
print(myStr[2:6])
print(myStr[0:3])

#left
print(myStr[:4])
print(myStr[:-4])

#right
print(myStr[1:])
print(myStr[-1:])

print(myStr.lower())
print(myStr.upper())

mynum = 7.99
print(int(mynum))

strnum = "7"
print(int(strnum))

strnum2 = "7.45"
print(int(float(strnum2)))