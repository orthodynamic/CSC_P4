# QUESTION 3
Animal = []  # 20 elements of string
Colour = []  # 10 colours of string
AnimalTopPointer = 0
ColourTopPointer = 0


# 3b(i)

def PushAnimal(DataToPush):
    global AnimalTopPointer
    global Animal
    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer += 1
        return True


def PopAnimal():
    global AnimalTopPointer
    global Animal
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer -= 1
        return ReturnData


def ReadData():
    try:
        fileHandle = open("AnimalData.txt", "r")
        for oneline in fileHandle:
            PushAnimal(oneline.strip())
        fileHandle.close()
    except IOError:
        print("Animal file does not exist")
    try:
        fileHandle = open("ColourData.txt", "r")
        for oneline in fileHandle:
            PushColour(oneline.strip())
        fileHandle.close()
    except IOError:
        print("Colour file does not exist")


def PushColour(DataToPush):
    global ColourTopPointer
    global Colour
    if ColourTopPointer == 20:
        return False
    else:
        Colour[ColourTopPointer] = DataToPush
        ColourTopPointer += ColourTopPointer
        return True


def PopColour():
    global ColourTopPointer
    global Colour
    if ColourTopPointer == 0:
        return ""
    else:
        ReturnData = Colour[ColourTopPointer - 1]
        ColourTopPointer = ColourTopPointer - 1
        return ReturnData


def OutputItem():
    returnedColoured = PopColour()
    returnedAnimal = PopAnimal()
    if returnedAnimal == "":
        PushAnimal(returnedAnimal)
        print("No colour")
    elif returnedAnimal == "":
        PushColour(returnedColoured)
        print("No animal")
    else:
        print(returnedColoured, returnedAnimal)


ReadData()
OutputItem()
OutputItem()
OutputItem()
OutputItem()
