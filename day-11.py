'''
# Day - 11:
'''

# seek(): It will read the file from that position, 
# tell(): It will tell you the current position of pointer in file, 
# truncate(): It will truncate the characters in file after that position

# with open('sample.txt', 'w') as f:
#     f.write('Pradyumna is awesome')

# with open('sample.txt', 'r') as f:
#     f.seek(10) # Move to the 10th byte in the file

#     data = f.read(10) # It will read next 10 bytes
#     print(data)

# with open('wrtfile1.txt', 'r') as f:
#     data = f.read(10)  # It will read 10 bytes in file

#     curr_position = f.tell() # Save the current position
#     print(curr_position)

#     f.seek(curr_position) # Seek to the saved position

# with open('sample.txt', 'a') as f:
#     f.write(', and I know it')
#     f.truncate(10) 
#     # it will truncate characters after 10 bytes 
#     #and make the total file size as 10 bytes

with open('sample.txt', 'r') as f:
    print(f.read())
print('\n')

# Lambda functions : used to create anonymous functions without a name.

double = lambda x: x*2
cube = lambda x : x*x*x
avg = lambda x,y,z : (x + y + z) /3

print(double(2))
print(cube(2))
print(avg(2,5,7))

def apply(fx, val):
    return fx(val) + 8

ex = apply(cube, 3)
print(ex)

# Map(), Reduce() and filter() : higher order functions in Python
# these 3 function types take a sequence of characters and return a new sequence

# Functions which can take other functions as an argument it is called higher order function


l = [1,6,4,3,2,8,9]
# newl = []

# for item in l:
#     newl.append(cube(item))

# print(newl)

newl = list(map(cube, l))
print(newl)

def fil_func(a):
    return a > 2

# filterList = list(filter(fil_func, l))
filterList = list(filter(lambda x: x > 2, l))
print(filterList)

# For reduce function we need to first import it

from functools import reduce

avg1 = reduce(lambda x,y: (x+y)/2, l)
print(avg1)

print('\n')

# is keyword vs '==' comparison operators

a = '2'
b = 2

print(a is b)  # exact location of object in memory
print(a == b)  # value

# Suppose if 2 constant values are assigned to a variable it will take up 
# the same memory space and hence in that case it will return True

# For Ex: strings, integers, tuples etc all the immutable objects having same value
# will be stored at same location in memory by our smart python