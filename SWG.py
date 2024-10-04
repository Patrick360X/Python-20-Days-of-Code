'''

computer = S W G
user = S   D W L
       W   L D W
       G   W L D
'''

import random

def check(user, computer):
    if (user == computer):
        return 0
    elif (user == 1 and computer == 2):
        return 1
    elif (user == 2 and computer == 3):
        return 1
    elif (user == 3 and computer == 1):
        return 1
    else:
        return -1

user = int(input(' 1.Snake\n 2.Water\n 3.Gun\nEnter your choice: '))
computer = random.randint(1,3)

print(f"Computer's choice: {computer}")

score = check(user, computer)
if (score == 0):
    print("It's a Draw")
elif (score == 1):
    print("You Win")
else:
    print('You Lose')


