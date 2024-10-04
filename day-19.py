'''
# Day - 19:
'''

# Generators: 

# allows uo to generate iterable sequence of values and this 
# generator function returns generator object which generates values 
# one-by-one and then iterates over it 

# Can be created using yeild keyword in a function

def my_generator():
    for i in range(50):
        yield i

g1 = my_generator()
print(next(g1))
print(next(g1))
print(next(g1))

# Benefits of using generators is that it generates values on the fly,
# which eventually saves on memory as it doesn't needs to store 
# all the values at once and they're lazy functions as they'll only generate values if they're requested.

# Function caching: 

# used to improve the performance of a program by storing the results of a 
# particular function call so that if the same is called again and we can reuse 
# the result of it thus saving time on computation 

from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*10

# print(fx(20))
# print("Done for 20")

# print(fx(11))
# print("Done for 11")

# print(fx(15))
# print("Done for 15")

# print(fx(20))  ## here the function with same value is called again so it will return the values stored in cache without computing for the result again
# print("Done for 20")

# print(fx(30))
# print("Done for 30")

# Regular Expression: allows us to match and manipulate strings based on patterns

import re

pattern = '[A-Z]+orem'
text = '''
Lorem Ipsum is simply dummy text of the printing and typesetting 
industry. Borem Ipsum has been the industry's standard dummy text 
ever since the 1500s, when an unknown printer took a galley of type 
and scrambled it to make a type specimen book. It has survived not 
only five centuries, but also the leap into electronic typesetting,
remaining essentially unchanged. It was popularised in the 1960s with 
the release of Letraset sheets containing Sorem Ipsum passages, 
and more recently with desktop publishing software like Aldus 
PageMaker including versions of Korem Ipsum.
'''

# Used to search if the pattern is present or not and returns boolean value. 
# if found returns first occurence

match = re.search(pattern,text)
print(match)

# used to iterate over all the objects found with matching pattern
print('\n')
matches = re.finditer(pattern, text)

for match in matches:
    print(f'Start Index: {match.span()[0]}')
    print(f'End Index: {match.span()[1]}')
    print(f'Match found: {text[match.span()[0]:match.span()[1]]}\n')

# used to find all the occurences of the pattern in given text
out = re.findall(pattern,text)
print(out)

print('\n')

url = f'https://regexr.com/'
print(f'For more learning on Regex, visit: {url}')
