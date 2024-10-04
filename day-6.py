'''
# Day - 6:
'''

# Formatted strings

name = input('Enter your name: ')
country = input('Where do you live: ')

print(f'Hi my name is {name} and I live in {country}')

print(f'{30 *2}')

balance = float(input("Enter back balance: "))
print(f'My bank balance {balance:.2f}')   #here 2f refers to give output till 2 decimal values only

# Python Docstrings

def square(n):
    '''This is square function, takes n and returns its square'''
    output = n**2
    return output

n = int(input('Enter any number: '))
print(square(n))
print(square.__doc__)

# PEP8 - Python Enhancement Proposal

#We can get Zen of python by typing import this in python shell

# Recursive function

def factorial(n):
    '''Factorial(n) = n * Factorial(n-1)'''
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))


#Fibonacci series

# f0 = 0
# f1 = 1

# f2 = f1 + f0
# fn = fn-1 + fn-2

def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
    
print(fibonacci(12))
