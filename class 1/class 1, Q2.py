# Ask the user if monkey A and monkey B are smiling, if either or both are smiling you are in trouble

monkeyA = input('is monkey A smiling?')
monkeyB = input('is monkey B smiling?')
if monkeyA == "False" and monkeyB == "False":
    print('you are safe')
else:
    print('you are in trouble')
