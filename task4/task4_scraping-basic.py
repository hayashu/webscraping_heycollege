import requests
from bs4 import BeautifulSoup

url = 'https://example.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
h1 = soup.find('h1')
print(h1.text)
p = soup.find_all('p')
print(p)
a_tag =soup.find('a')['href']
print(a_tag)