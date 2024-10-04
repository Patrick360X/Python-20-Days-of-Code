'''
# Day - 7:
'''

#Sets

# Sets is used to stored unordered types of objects and which are unchangable.
# We also cannot store duplicate items twice.
# Items in set can occur in random order so we can't access them using indexes

s = {1, 7.6, 0, 23, True, "Prady"}
print(s)

#If we want to create an employeesty set it can be done as below

ps = set()
print(type(ps))

for items in s:
    print(items)

#Methods for set: union(), update(), intersection(), intersection_update()

c1 = {'Delhi', 'Mumbai', 'Hyberabad', 'Kolkata'}
c2 = {'Shimla', 'Munnar', 'Delhi', 'Hampi', 'Amritsar'}
c3 = {'Punjab', 'Amritsar'}

print(c1.union(c2))
print(c1, c2)

c1.update(c3)
print(c1)

print(c1.intersection(c2))
c3.intersection_update(c1)
print(c3)
print(c1)
print('\n')

#Symetric_difference, difference and difference_update 

act1 = {'Paraglyding', 'Horse Riding', 'Bumjee Jumping', 'Trampoline', 'River rafting'}
act2 = {'Parasailing', 'Banana ride', 'Horse Riding', 'Trampoline'}

act3  = act1.symmetric_difference(act2)
print(act3)

act1.symmetric_difference_update(act2)
print(act1)
print(act2)
print('\n')

city1 = {'Miami', 'LA', 'LV', 'Toronto'}
city2 = {'Washington DC', 'California', 'Miami', 'Ohio', 'Chicago'}

city3 = city1.difference(city2)
print(city3)

city1.difference_update(city2)
print(city1)
print(city2)

#Other methods in Sets
print('\n')

print(city1.isdisjoint(city2))
print(city3.issuperset(city1))
print(city2.issuperset(city3))

print(city1.issubset(city3))

city1.add('NYC')
print(city1)

city2.remove('Ohio')  #if item is not present it will through a keyerror
print(city2)

city2.discard('Ohia') # discard method will not through a keyerror
print(city2)

item = city3.pop()
print(city3)
print(item)

# del(city3) # this delete entire set

city3.clear()
print(city3)

# if an item is present or not

if 'LA' in city2:
    print('LA is there in Set')
else:
    print('LA is not present in Set')

#Dictionary - ordered collection of objects

print('\n')

employees = {
    'Pradyumna': 83,
    'Rahul' : 58,
    'Neha' : 57,
    'Arif' : 87,
    'Abhishek' : 81
}

print(employees)
print(employees['Pradyumna'])

# print(employees['Som'])  # will through an error if key is not present
print(employees.get('Som')) # will return None if key is not found

print(employees.values())
print(employees.keys())
print(employees.items())
print('\n')

for key, value in employees.items():
    print(f"{key}'s employee id is {value}")
print('\n')

managers = {
    'Karthik' : 15,
    'Jayashree' : 49,
    'Som' : 36
}

employees.update(managers)
print(employees)
print(managers)

managers.clear()
employees.pop('Jayashree')
employees.popitem()

print(employees)

del employees['Karthik']
print(employees)

employees.update({'Som' : 46})
print(employees)

# we can use else statement after for and while loops
print('\n')

#Ex -1 : else statement will execute

for i in range(9):
    print(i)

else:
    print("We've completed the execution ")

#Ex - 2: for loops will break after condition is matched and it will not execute the else statement
print('\n')

for i in range(8):
    print(i)
    if(i == 5):
        break

else:
    print("We've completed the execution ")

# Ex - 3 : using while loop and if we use continue it will still execute the else statement
print('\n')

i = 0
while i < 10:
    print(i)
    i = i + 1
    if(i == 6):
        continue

else:
    print("We've completed the execution ")