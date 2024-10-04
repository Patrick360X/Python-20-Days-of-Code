'''
# Day - 10:
'''

# OS module -used for bulk operation to simplyfy the task performed

import os

if not os.path.exists:
    os.mkdir('Python Course')

# for i in range(0,100):
#     os.mkdir(f'Python Course/Day - {i+1}')

# if we want to rename the files under the directory

# for i in range(0,100):
#     os.rename(f'Python Course/Day - {i+1}', f'Python Course/Tutorial - {i+1}')

# to find how many tutorials are present here

folders = os.listdir('Python Course')

print(os.getcwd())

# for folder in folders:
#     print(folder)
#     print(os.listdir(f'Python Course/{folder}'))

# Local and global variables

x = 20  # global variable

def val():
    global x
    x = 12   # we can change local variable to global variable using global keyword
    y = 10   #Local variable

    print(x)
    print(y)

val()
print(x)
print('\n')

# File operations

# 1. Reading a file
# f = open('Myfile.txt', 'r')

# txt = f.read()
# print(txt)
# f.close()

# 2. Writing in a file

# f = open('wrtfile.txt', 'w')

# f.write('Hello Buddy')
# f.close()

# 3. Appending content in an existing file

# f = open('wrtfile.txt', 'a')

# f.write('\n How you doin?')
# f.close

# Instead of always closing the file to see the changes we can make use of 'with' keyword

with open('wrtfile.txt', 'r') as f:
    txt = f.read()
    print(txt)

# Readlines, writelines functionalities in Python

f = open('myfile.txt','r')
i = 0

while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(',')[0])
    m2 = int(line.split(',')[1])
    m3 = int(line.split(',')[2])

    print(f'Marks of student {i} in Maths: {m1}')
    print(f'Marks of student {i} in Physics: {m2}')
    print(f'Marks of student {i} in Chemistry: {m3}')
    print('\n')


f = open('wrtfile1.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']

f.writelines(lines)
f.close()

# If we have N no. of elements in list and for iterating through 
# it we can only use for loop with write function 

with open('wrtfile1.txt', 'a') as f:
    lines = ['Line 4', 'Line 5', 'Line 6']
    for line in lines:
        f.write(line + '\n')
