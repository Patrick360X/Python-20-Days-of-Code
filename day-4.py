'''
# Day - 4:
'''

#Match Case 

x = int(input("Enter a number: "))

match x:
    case 0:
        print("Number is zero")
    case 2 if (x%2 == 0):
        print("Number is divisible by 2")
    case 3 if (x%3 == 0):
        print("Number is divisible by 3")
    case _ if (x%2==0 and x%3==0):
        print("Number is divisible by both 2 and 3")
    case _ if (x%2==0 or x%3==0):
         print("Number is divisible by both 2 or 3")
    case _:
        print("Number is not divisible by both 2 and 3")

# For loops

name = 'Pradyumna'

for chr in name:
    print(chr, end=',')

print('\n')

colors = ['Red', 'Blue', 'Green', 'Yellow']

for color in colors:
    print(color)
    for clr in color:
        print(clr)
print('\n')

#Range function in for loops

for n in range(10):
    print(n+1)
print('\n')

for k in range(1,x):
    print(k)
print('\n')

for y in range(1,100, 15):
    print(y)
print('\n')

for z in range(100,0, -10):
    print(z)
print('\n')

# While loop

num = int(input("Enter the num: "))

while(num <= 50):
    num = int(input("Enter the num: "))
    print(num)
print("Exiting loop, as no. greater than 50")

print('\n')

count = 7

while(count > 0):
    print(count)
    count = count - 1
else:
    print('Count is now 0')

# Do while loop emulation in python

while True:
    number = int(input("Enter any positive no: "))
    print(number)
    if not number > 0:
        break

# Break = loop chodkar bahar nikal
# continue = skip the current iteration and carry on

for p in range(12):
    if(p == 10):
        break
    print("5 X", p+1, "=", 5*(p+1))

for q in [2,3,4,5,6,8,9,10]:
    if(q%2 != 0):
        continue
    print(q)

i = 0
while True:
    print(i)
    i = i + 1
    if(i == 10):
        break


