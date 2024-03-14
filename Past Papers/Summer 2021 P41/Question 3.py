# PRIVATE
# CONSTRUCTOR: def __init__()
class TreasureChest:
    # self.__question: STRING
    # self.__answer: INTEGER
    # self.__points: INTEGER
    def __init__(self, ques, ans, pts):
        self.__question = ques
        self.__answer = ans
        self.__points = pts

    def getQuestion(self, ques):
        self.__question = ques

    def checkAnswer(self, ans):
        if ans == self.__answer:
            return True
        else:
            return False

    def getPoints(self, attempts):
        if attempts == 1:
            return self.__points
        elif attempts == 2:
            return self.__points // 2
        elif attempts == 3 or attempts == 4:
            return self.__points // 4
        else:
            return 0

arrayTreasure = [] # ARRAY OF TreasureChest
def readData():
    try:
        # ques: STRING
        # ans: INTEGER
        # pts: INTEGER
        fileHandle = open("TreasureChestData.txt",'r')
        # each line read from the file will contain /n
        # enter key = /n
        # strip() = remove all additional white spaces
        ques = fileHandle.readline().strip()
        while len(ques) != 0:
            ans = int(fileHandle.readline().strip())
            pts = int(fileHandle.readline().strip())
            # arrayName,append(parameter) = adds a new index in the array and stores the value which is in the parameter
            # arrayName.append(classObject(parameters)
            arrayTreasure.append(TreasureChest(ques, ans, pts))
            ques = fileHandle.readline().strip()
        fileHandle.close()
    # IOERROR = When file doesnot exist
    except IOError:
        print("file doesnot exist")

readData()
userInput = int(input("Enter a question number between 1 and 5: "))
while userInput < 1 and userInput > 5:
    userInput = int(input("Incorrect Input, Enter a question number between 1 and 5: "))
retVal = False
attempts = 0
while retVal == False:
    print(arrayTreasure[userInput-1].getQuestion)
    userAns = int(input("Enter your answer: "))
    retVal = arrayTreasure[userInput-1].checkAnswer(userAns)
    attempts += 1
print(arrayTreasure[userInput-1].getPoints(attempts))
