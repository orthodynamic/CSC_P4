# Inheritance: all attributes and methods of the base class are copied to the subclass
# BASE CLASS / PARENT CLASS : Main class from which other class will copy
# SUB CLASS ? CHILD CLASS: class that inherits/ copies the attributes and methods from the base class
# library item: book, CD
import datetime
class libraryitem:
    def __int__(self):
        self.__itemID = i
        self.__title = t
        self.__authorArtist = a
        self.__onLoan = False
        self.__dueDate = datetime.date.today()
    # make all get methods
    def borrow(self):
        self.__onLoan = True
        self.__dueDate = datetime.date.today() + datetime.timedelta(weeks=2)
    def returning(self):
        self.__onloan = False
    def printDetails(self):
        print("Title = {0}, Author = {1}, Item ID = {2}, On Loan = {3}".format(self.__title,self.__authorArtist,self.__itemID,self.__onLoan))
# SUB CLASS
# to show inheritance: class subClassName(baseClassName):
class book(libraryitem):
    def __int__(self):
        libraryitem.__int__(self, i, t, a)
        self.__isrequested = False
        self.__requestedBy = 0
    def getisrequested(self):
        return self.__isrequested
    def setisrequested(self):
        self.__isrequested = True
# MAKE CD CLASS
myBook = book("A12", "HarryPotter", "JK ROWLING")
myBook.printDetails()
myBook.borrow()
myBook.printDetails()