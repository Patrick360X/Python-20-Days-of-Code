'''
# Day - 16:
'''

# Operator overloading : allows developers to redefine the mathematical and 
# comparison operators for custom data types

class vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,x):
        return vector(self.i + x.i , self.j + x.j , self.k + x.k)


v1 = vector(2,5,7)
print(v1)

v2 = vector(4,2,5)
print(v2)

v3 = vector(1,7,2)
print(v3)

print(f"Addition of 3 vectors:{v1+v2+v3}")
print(type(v1+v2+v3))
print('\n')
# Single Inheritance : simplest of all inheritance

class Animal:
    def __init__(self,name,species):
        self.name = name 
        self.species = species

    def make_sound(self):
        print("Sound made by an animal")

class Dog(Animal):
    def __init__(self, name, bread):
        Animal.__init__(self,name, species="Dog")
        self.bread = bread

    def make_sound(self):
        print("Bark!!")

class Cat(Animal):
    def __init__(self, name, bread, type):
        Animal.__init__(self,name, species="Cat")
        self.bread = bread
        self.type = type
    
    def make_sound(self):
        print("Meow, Meow")


a = Animal("Jessy","Cat")
a.make_sound()

d = Dog("Jack", "Rottweiler")
d.make_sound()

c = Cat("Tracy", "Persian", "Hybrid")
c.make_sound()

print('\n')

# Multiple Inheritance: Allows a child class to inherit attributes and properties from multiple parent classes

class Dancer:
    def __init__(self, name, Danceform):
        self.name = name
        self.Danceform = Danceform
    
    def show(self):
        print(f"My name is {self.name} and my dance form is {self.Danceform}")

class Singer:
    def __init__(self, name, style):
        self.name = name
        self.style = style
    
    def show(self):
        print(f"My name is {self.name} and my singing style is {self.style}")

class Event(Dancer,Singer):
    def  __init__(self,name,Danceform,style):
        self.name = name
        self.Danceform = Danceform
        self.style = style

E1 = Event("Shivani", "Kathak", "Classical")
E1.show()  
# this will call show method from Dancer class as 
#it was defined at first position in Child class i.e. Event Class

print(Event.mro()) # mro is Method resolution Operator mainly used to determine the order in which parent classes are searched for attributes and methods

print('\n')

# Multi-Level Inheritance : [A -> B -> C]

class animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def showDetails(self):
        print(f"Dog Name : {self.name}")
        print(F"Species : {self.species}")

class dog(animal):
    def __init__(self, name, bread):
        animal.__init__(self,name,species = "Dog")
        self.bread = bread

    def showDetails(self):
        animal.showDetails(self)
        print(f"Bread : {self.bread}")

class Rottweiler(dog):
    def __init__(self,name,color):
        dog.__init__(self,name,bread="Guard-dog")
        self.color = color

    def showDetails(self):
        dog.showDetails(self)
        print(f"Color : {self.color}")

d1 = Rottweiler("Jackie", "Black")
d1.showDetails()

print(Rottweiler.mro())