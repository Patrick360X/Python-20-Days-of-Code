'''
# Day - 15:
'''

# dir, __dict__ and help methods 

#dir() is used to return all the attributes and methods available for object
from typing import Any


a = [1, 4, 5]
print(a)
print(dir(a))
print(a.__add__ )
print('\n')

# __dict__ : return a dictionary representation of object's attributes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 2.0

p1 = Person("Pradyumna", 24)
p2 = Person("Paresh", 22)
print(p1.__dict__)
print(p2.__dict__)
print('\n')

# help() method

# print(help(str))
print(help(Person))

# super() keyword: used to inherit parent class properties, attributes and methods into the class class.
print('\n')

class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    
class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)  # here name and id attributes will be inherited from parent class Employee
        self.lang = lang
    
emp1 = Employee("Pradyumna", 234)
emp2 = Programmer("Brendy",235,"Python")

print(emp2.name)
print(emp2.id)
print(emp2.lang)
print('\n')

# Magic/Dunder Methods 

class shop:
    def __init__(self, expense, sales):
        self.expense = expense
        self.sales = sales
    def __repr__(self):
        return (f"Total profit = {self.sales - self.expense} ")
    
    def __call__(self):
        if self.sales > self.expense:
            print("We're in profit")
        else:
            print('We need to recover our expenses')

class customer(shop):
    def __init__(self,name,amtSpend):
        self.name = name
        self.amtSpend = amtSpend
        

    def __str__(self):
        return (f"Customer's name is {self.name} & has spent {self.amtSpend}Rs")

cust1 = shop(23000, 29000)
cust2 = customer("Pradyumna", 1200)

print(cust1.expense)
print(cust1.sales)

print(cust2.name)
print(cust2.amtSpend)

print(str(cust2))
print(repr(cust1))
cust1()   #here we have called the cust1 as function and we get output from the return statement in __call__ Dunder method
print('\n')

# Method Overriding 

class shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y
    
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):  # Here the area method is overwritten in child class from what we get in parent class
        return 3.14 * self.radius * self.radius

rec = shape(3,5)
print(f'Area of Rectangle: {rec.area()}')

c1 = circle(3)
print(f'Area of Circle: {c1.area()}')