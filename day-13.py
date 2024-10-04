'''
# Day - 13:
'''

# Inheritance in OOPS

class Employees:
    def __init__(self, name, id):
        self.name = name  #Public Variable
        self.id = id      #Public Variable

    def showDetails(self):
        print(f'Id: {self.id}, Employee Name: {self.name}')

class jobDescription(Employees):
    def jobDec(self):
        print("I'm a Devops Engineer")

a = Employees('Pradyumna', '83')
b = jobDescription('Abhishek', '85')

a.showDetails()
b.showDetails()
b.jobDec()
print('\n')

# Access Modifiers in Python : Private, Public and Protected Methods

# by adding '__' - double underscores preceeding the method name it is now a private method

class Student: 
    def __init__(self, age, name): 
        self.__age = age      # An indication of private variable
        
        def __funName(self):  # An indication of private function
            self.y = 34
            print(self.y)

class Subject(Student):
    pass

obj = Student(24,"Pradyumna")
obj1 = Subject

# calling by object of class Student
print(obj.__age)
print(obj.__funName())

# calling by object  of class Subject
print(obj1.__age)
print(obj1.__funName())
print('\n')

# Name mangling : technique used to protect class-private and superclass-private attributes from being accidentally overwritten by subclasses. 

class MyClass:
    def __init__(self):
        self._nonmangled_attribute = "I am a nonmangled attribute"
        self.__mangled_attribute = "I am a mangled attribute"

my_object = MyClass()

print(my_object._nonmangled_attribute) # Output: I am a nonmangled attribute
print(my_object.__mangled_attribute) # Throws an AttributeError
print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute
print('\n')

# Protected Access Modifier: are intended to be accessed only by the class itself and its subclasses
# and by adding '_' - single underscores preceeding the method or function name it is now a Protected method

class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()
print(dir(obj))

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())

print('\n')

# Static Methods are methods which belong to class neither than an instance of class (i.e self)

class Math:
    def __init__(self,num):
        self.num = num
    
    def addtonum(self, n):
        self.num = self.num + n
    
    @staticmethod
    def add(a,b):
        return a + b

a = Math(4)
print(a.num)

a.addtonum(7)
print(a.num)

print(Math.add(3,7))
