'''
# Day - 3:
'''

# Strings are immutable

name = 'Pradyumna'
print('My name is ', name)
print('\n')


str = "He said I'd like to have an apple"
print(str[0])
print(str[1])

print('\n')

for chr in name:
    print(chr)
print('\n')
print(len(name))

#String Slicing operations
print('\n')

print(name[0:4])
print(name[:7]) #by default the first value is set to 0th index

print(name[:-1])  
print(name[-1:-5])  # no output as index's don't match
print(name[2:-4])
print(name[-7:9])

#String Methods
print('\n')

str1 = '$$$Pradyumna$$$$$$$$$'
str2 = '$$$$$ Prash $$$ Prashant'

print(len(str1))
print(str1.upper())
print(str1.lower())
print(str1.rstrip("$"))
print(str2.lstrip("$"))

print(str2.split(' '))

print(str2.replace('Pras', 'Prady'))


# if-else-elif loops

a = int(input('Enter your age: '))
print('Your age is ', a)

if(a > 18):
    print("You can drive if you've license")
elif(a == 18):
    print('Apply for license and then drive')
else:
    print("You cannot drive, it's not safe")

#Nested if-else loop

num = int(input("Enter num: "))

if(num < 0):
    print("The number is negative")
elif(num > 0):
    if(num > 0 and num <= 10):
        print("Number is between 0-10")
    elif(num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is Zero")
