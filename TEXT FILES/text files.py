#open(filmname , mode)
#w = WRITE (create files/ recreates store data)



FileHandle = open("SampleFile.TXT", "w")
FileHandle.write("list of text to store\n")
FileHandle.write("this is my second line\n")
FileHandle.close()

#TASK: Create a file called "names.txt"
#ask user to store 10 names in the file
FileHandle = open("name.txt", 'w')
FileHandle.write("   WORLD XI  \n")
for i in range(10):
    name = input("please enter your name")
    FileHandle.write(name + '\n')
FileHandle.close()

#TASK: Read file "name.txt and copy all names with less than 5 characters in a new file.
#"favNames.txt"
FileHandle = open('name.txt', 'r')
Filename = open("FavNames.txt", 'w')
for i in range(11):
    oneline = FileHandle.readline().strip()
    if len(oneline) < 5:
        Filename.write(oneline)

FileHandle.close()
Filename.close()

FileHandle = open("name.txt", 'a')
lineoftext = "Apended line"
FileHandle.write(lineoftext)
FileHandle.close()

#TASK: Read file "names.txt"and copy names which are not currently in the file "newNames.txt"
#assuming max lines = 10