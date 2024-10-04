'''
# Day - 9:
'''

# Short hand use of if-else loop

a = 345
b = 3424

print("A") if a>b else print("=") if a == b else print("B")

c = 9 if a < b else 0
print(c)
print('\n')

#Enumerate is build-in function in Python

#Allows you to loop over the items in sequences like [List, tuple or string]
#and get index and value of each element in sequence at the same time

fruits = ['Banana', 'Kivi', 'Rasberry', 'Mango']

for index, fruit in enumerate(fruits,start=1):
    print(index, fruit)
print('\n')

#inside enumerate function we can give the starting index as well

str = 'Pradyumna'

for index, s in enumerate(str):
    print(index,s)

# Virtual Enviroment is used to isolate python envs on a single machine

# # Create a virtual environment
# python -m venv myenv

# # Activate the virtual environment (Linux/macOS)
# source myenv/bin/activate

# # Activate the virtual environment (Windows)
# myenv\Scripts\activate.bat

# # Deactivate the virtual environment
# deactivate

# # Output the list of installed packages and their versions to a file
# pip freeze > requirements.txt

# # Install the packages listed in the requirements.txt file
# pip install -r requirements.txt

#Import
print('\n')
# import math as m
# from math import *   { Not usually recommended }
# from math import sqrt as s
import math 

print(f'Square root of 9 is: {math.sqrt(9)}')
print('\n')

print(dir(math))
print(type(math.nan))

# __name__ == '__main__': is an idiom 

# import secretlang

# secretlang.encode()
# secretlang.decode()

