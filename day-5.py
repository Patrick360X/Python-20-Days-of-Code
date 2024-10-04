'''
# Day - 5:
'''

# Functions

def calculateGMean(a,b):
    Gmean = (a*b)/(a+b)
    print(Gmean)

def greaterNum(a,b):
    if(a>b):
        print('a is greater no. than b')
    elif(b>a):
        print('b is greater no. than a')
    else:
        print('both the no.s are Equal')

calculateGMean(8,9)
calculateGMean(38,96)

greaterNum(2,0)

# Function and its argument types

def average(a, b, c = 3):
    print('The average these 3 values is ', (a+b+c)/3)

average(3,5,2)

average(5, 9) # here the value of c will be taken from function defination as 3
average(a=4, b=3, c=5) #in the case even the value in C will be overwritten by 5 as per function calling

print('\n')
# Variable-length arguments

#A single star before argument will store values in a tuple

def average1(*numbers):    
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print('Average of all these values: ', sum/len(numbers))

average1(1,6,7,9)

print('\n')

#double star before argument will store values in a dictionary like a key-value pair

def myName(**myName): 
    print(type(myName))
    print("Hello", myName["fname"], myName["mname"], myName["lname"])

myName(lname = 'Shirude', mname = 'Narendra', fname = 'Pradyumna')

#Return statement - used to return back the value of expression back to the calling function

print('\n')

def average2(*numbers):  
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)

myAvg = average2(1,6,2,4)
print(myAvg)

#------------------------------------------------------------------------
#-------------------            Lists              ----------------------


#can contain any datatype
#It is mutable and changes can be made like adding another item to an existing list

marks = [5,7,1,"Prash",2,8,True,3,9,0,"Prady"] 

print(marks)
print(marks[0])
print(marks[:])

print(marks[:5])
print(marks[-6:-1])

print(marks[:10:3]) #Jump indexing by 3 

if 4 in marks:
    print('Yes it is present in list')
else:
    print('Not present')

print('\n')


#List Comprehension
print('\n')

l = [i for i in range(8) if i%3 ==0]
print(l)

# list Methods

print('\n')

list1 = [2,5,1,6,2,8,3,2,4,20]

list1.append(12)  #will add new item to list
print(list1)

list1.sort()   #will sort in ascending order
print(list1)

list1.sort(reverse=True) #will sort in descending order
print(list1)

print(list1.index(2)) # find the first occurence where 2 is present in list
print(list1.count(2)) # return the count of times 2 occurs in list

m = list1.copy()   # will create a new list m from existing list and we can modify it won't change the list1
m[0] = 11
print(list1)
print(m)

list1.insert(1,23)  # will insert a new integer 23 at index 1 
print(list1)

m = [24,112,13,54] #new list m will be appended after list1
#list1.extend(m)
#print(list1)

k = list1 + m  #new list k will be created, and the existing list remain the same
print(k)

#------------------------------------------------------------------------
#-------------------            Tuples              ----------------------

tup = (5,7,1,"Prash",2,8,True,3,9,0,"Prady")

print(tup)
print(tup[0])
print(tup[:])

print(tup[:5])
print(tup[-6:-1])

print(tup[:10:3]) #Jump indexing by 3 

if 2 in tup:
    print('Yes it is present in Tuple')
else:
    print('Not present')

print('\n')

# Tuples Methods

tup1 = (1,5,2,7,3,7,5,0,2,3,6,2,8,4)

res = tup1.count(2)
print(res)

res1 = tup1.index(6)
print(res1)

print(len(tup1))