'''
# Day - 12:
'''

#Object-Oriented Programming - Classes and objects

# A class is a template used for creating objects

class myDetails:
    name = 'Pradyumna'
    occupation = 'Data Analyst'
    worksAt = 'FIS'

    def info(self):
        print(f"{self.name} works at {self.worksAt} as {self.occupation}")

# Self ka matlab vo object jiske liye ye method call kiya jaa raha hai

a = myDetails()
b = myDetails()

b.name = 'Abhishek'
# print(a.name, a.worksAt)

a.info()
b.info()

# Constructor : is special method of class used to create & initialize an object of the class
# These constructors are invoked automatically when an object of a class is created.
# It can not return any value other than None.

class emp:
    print("\n Below are employee details")

    def __init__(self,n,o):   #Parameterized Constructor
        self.name = n
        self.occupation = o
    
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = emp("Pradyumna", "Data Analyst")
b = emp("Madhukar", "Software Developer")

a.info()
b.info()

# Decorators : allows you to modify the behaviour of functions and Methods
# Provide us the ways to extend the functionality without changing the Source code.

def dec_func(fx):
    def mfx(*args, **kwargs):    # *args == Tuple datatype, **kwargs == Dictionary datatype
        print('\nGood Morning')
        fx(*args, **kwargs)
        print('Thanks for using this function')
    return mfx

@dec_func
def hello():
    print("Hello world")

@dec_func
def add(a, b):
    print(a + b)

hello()
add(1,2)

# Getters and Setters

print('\n')
class myClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f'Value is {self._value}')

    @property
    def TenXValue(self):
        return 10 * self._value
    
    @TenXValue.setter
    def TenXValue(self,new_val):
        self._value = new_val
    
obj = myClass(10)
print(obj._value)
obj.show()

obj.TenXValue = 100
print(obj.TenXValue)
obj.show()


# Use of getter can help you access the values of object's properties, while
# keeping the internal representation hidden, and hence can be mostly used 
# for Encapsulation and data validation