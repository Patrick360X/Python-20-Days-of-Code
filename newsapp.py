import requests
from bs4 import BeautifulSoup
import json

# # Search for news articles that mention a specific topic or keyword we use /everything
# url = ('https://newsapi.org/v2/everything?'
#        'q=crocodile&'
#        'from=2024-09-28&'
#        'sortBy=popularity&'
#        'apiKey=37fee7c0c0304d3fb0e4e15338e3cb68')

# response = requests.get(url)

# print (response.json())

# # Get the current top headlines for a country or category We'll use the /top-headlines endpoint 

# url = ('https://newsapi.org/v2/top-headlines?'
#        'country=us&'
#        'apiKey=37fee7c0c0304d3fb0e4e15338e3cb68')
# response = requests.get(url)

# soup = BeautifulSoup(response.text,'html.parser')
# print (soup.prettify())

query = input("What do you want to read about: ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-08-29&sortBy=publishedAt&apiKey=37fee7c0c0304d3fb0e4e15338e3cb68"

r = requests.get(url)
# print(r.text)
news = json.loads(r.text)
# print(news,type(news))

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print('\n')