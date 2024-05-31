from bs4 import BeautifulSoup
import requests

url = 'https://souda-kyoto.jp/travel/koyo/'
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
koyo = soup.find('div',{'id':'koyo'})
print(soup)
def scrape_koyo(koyo):
    pass