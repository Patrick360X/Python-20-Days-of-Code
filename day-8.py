'''
# Day - 8:
'''

#Exception handling

num = (input('Enter any number: '))
print(f'Multiplication table for {num} is: ')

try:
    for i in range(1, 11):
        print(f'{int(num)} X {i} = {int(num)*i}')

except:
    print('Invalid Input')
# and we can handle all sorts of error like ValueError, KeyError etc.

print('Some imp lines of code')
print('Executed successfully')

# Use of Finally keyword - The block of code will always executed even if the function has already returned a value

def func1():
    try:
        l = [1,6,3,8]
        i = int(input('Enter the value of index: '))
        print(l[i])
        return 1
    except:
        print('Index not found, or some error occured')
        return 0
    finally:
        print("I'll always be executed")

x = func1()
print(x)

#Raising custom errors

a = int(input("Enter a no. btw 3 till 7: "))

if ( a < 3 or a > 7):
    raise ValueError('Number entered is not btw 3 till 7')
else:
    print(a)

b = input('Enter a value: ')

if(b == 'quit'):
    exit()
elif(int(b) < 5 or int(b) > 8):
    raise ValueError('Number entered is not btw 3 till 7')
else:
    print(int(b))
