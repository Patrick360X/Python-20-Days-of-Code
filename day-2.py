'''
# Day - 2:
'''

# Variables and data types

a = 134
b = 'Pradyumna'
c = True
d = None

a1 = 3.6
a2 = complex(3, 2)

print('Type of a is: ' ,type(a))
print('Type of b is: ' ,type(b))
print('Type of c is: ' ,type(c))
print('Type of d is: ' ,type(d))
print('Type of a1 is: ' ,type(a1))
print('Type of a2 is: ' ,type(a2))

#Lists are mutable - ordered collection of objects

list1 = ['Prady', 13, 1.2, ['Pro1', 2], complex(5,2)]
print(list1)

# Tuples are immutable - ordered collection ofobjects

tuple1 = (('Prady, Soham'), ('Gym, Dumbbell'), ('Badminton, shuttle'))
print(type(tuple1))
print(tuple1)

#Dictionary is unordered collection of objects having key:value pair

dict1 = {'Name':'Prady', 'Age': 24, 'canVote': True}
print(dict1)

# Explicit Typecasting

a = '1'
b = '2'

c = int(a) + int(b)

print(c)

#Implicit Typecasting

g = 2
h = 3.6

i = g+h
print(type(i))
print(i)

# Taking using user input

x = int(input("Enter 1st no: "))
y = int(input("Enter 2nd no: "))

print(x + y)