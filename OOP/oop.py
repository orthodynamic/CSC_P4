# OBJECT ORIENTED PROGRAMMING
# Class: Attributes and methods
# class definition is blueprint
# Car: Attributes: id, registration, engine size, purchase price. Methods: accel, brake, turn right....
# Private: Hidden from the user/programmer. All attributes private
# Public: Visible for everyone. all methods public
# Getter Method: return attribute
# Setter Method: assign value to attribute
# OOP features: Encapsulation, Inheritance, Polymorphism, Containment(aggregation)
# Encapsulation: Hiding attributes from users

# CAR CLASS
class car:
    # Constructuor: a special type of method that is called to create a new object and initialize its attributes. Is called automatically
    # Constructor is private. No one call constructor
    #init__: the name of constructor in python
    #__ to show something is private
    def __init__(self, s, i):
        self.__CarID = i
        self.__registration = ""
        self.__dateofRegistration = None
        self.__enginesize = s
        self.__purchasePrice = 0
    #Get methods: A method to access its associated attribute
    def getCarID(self):
        return self.__CarID
    def getRegistraion(self):
        return self.__registration
    def getdateofRegistration(self):
        return self.__dateofRegistration
    def getenginesize(self):
        return self.__enginesize
    def getpurchasePrice(self):
        return self.__purchasePrice
    #Set Methods: a method to set the rules of its associated attributes
    #Parameter value is assigned to attribute
    #carID shouldn't change so not set method
    def setregistration(self, r):
        self.__registration = r
    def setdateofRegistration(self,d):
        self.__dateofRegistration = d
    # engine size shouldn't change so no set method
    def setpurchasePrice(self,p):
        self.__purchasePrice = p

myCar = car("ABC123",1000)
myCar.setpurchasePrice(10000000)
myCarEngline = myCar.getenginesize()
print(myCarEngline)
print(myCar.getpurchasePrice())