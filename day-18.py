'''
# Day - 18:
'''

# Walrus operator : used to assign a value to variable as a part of larger expression.

a = True

print(a:= False)


# fruits = list()

# while True:
#     fruit = input("Enter a fruit you like: ")
#     if fruit == 'quit':
#         break
#     fruits.append(fruit)

# Above code and be written using Walrus operator implementation

# dishes = list()

# while(dish := input("Enter your fav dishes: ")) != 'quit':
#     dishes.append(dish)

# print("\n")
# print(dishes)

# Shutil built-in module - used to perform various operation on file and system

import shutil

# shutil.copy('wrtfile.txt','wrtfilecopy.txt')
# shutil.copy2('wrtfile.txt','wrtfilecopy.txt')

# shutil.move('Python Course/Tutorial - 1', 'Tutorial - 1')
# shutil.rmtree('rmdirectory')

# requests module used to get,post,fetch the details on a page
# bs4[beautiful soup] module used for web scrapping the info on HTML pages

import requests

# Ex -1

# response = requests.get('https://www.3blue1brown.com/')  
# print(response.text)

# Ex - 2

# url = 'https://jsonplaceholder.typicode.com/posts'

# data = {
#     "title" : 'Mr.',
#     "body" : 'Pradyumna',
#     "userId" : 1,
#   }

# headers = {
#     'Content-type': 'application/json; charset=UTF-8',
#   }
# response =requests.post(url, headers= headers, json=data)

# print(response.text)

# Ex - 3
from bs4 import BeautifulSoup

url = 'https://byteblogger.netlify.app/'
res = requests.get(url)

soup = BeautifulSoup(res.text,'html.parser')

for heading in soup.find_all('h2'):
    print(heading.text)

# print(soup.prettify())