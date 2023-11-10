#Q1. Ask user for the age and output if the user is an adult or not
#Q2. Ask user if monkey A and Monkey B are smiling, if either or both are smiling you are in trouble
#Q3. Ask user if he/she is on vacation & if it's a weekday. Output if the user can sleep late
#q4. Ask user for their lucky number & output if the Lucky Number is odd or even

age = int(input("please enter your age"))
if age > 17:
    print("you are an adult")
else:
    print("you are not an adult")





monkeyA = input("is monkey A smiling? type yes or no")
monkeyB = input("is monkey B smiling? type yes or no")
if monkeyA == "yes" or monkeyB == "yes":
    print("you are in trouble")
else:
    print("you are safe")




vacation = input("are you on a vacation? type yes or no")
weekday = input("is it a weekday? type yes or no")
if vacation == "yes" or weekday == "no":
    print("you can sleep late")
else:
    print("you cannot sleep late")




luckynum = int(input("what is your lucky number?"))
if luckynum%2 == 0:
    print("your lucky number is even")
else:
    print("your lucky number is odd")
