print('Welcome to Code-Decode!')

x = int(input('Enter your Choice \n 1.Encoding \n 2.Decoding \n -> '))

def encode(input):
    if len(input) >= 3:
        print(input[1::] + input[0])
    else:
        print(input[::-1])

def decode(input):
    if len(input) >= 3:
        print(input[-1] + input[:-1])
    else:
        print(input[::-1])

if x == 1:
    encode(input("Enter text you want to encode: "))
elif x == 2:
    decode(input("Enter text you want to decode: "))
else:
    print('Wrong choice, Select 1 or 2')