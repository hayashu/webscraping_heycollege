import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.imdb.com/search/keyword/?keywords=public-domain&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=movie'
response = requests.get(url)

soup = BeautifulSoup(response.content,'html.parser')
movie = soup.find('div',{'class':'lister-item mode-detail'})
title = movie.find('h3').find('a').text
director = movie.find_all('p',{'class':'text-muted text-small'})[1].find('a').text
gross = movie.find_all('p',{'class':'text-muted text-small'})[2].find_all('span',{'name':'nv'})[1]['data-value']

movies = soup.find_all('div',{'class':'lister-item mode-detail'})


def movie_scraiping(movie):
    title = movie.find('h3',{'class':'lister-item-header'}).find('a').text
    director = movie.find_all('p',{'class':'text-muted text-small'})[1].find('a').text
    try:
        gross = movie.find_all('p',{'class':'text-muted text-small'})[2].find_all('span',{'name':'nv'})[1]['data-value']
    except :
        gross = ''

    return{"title":title,'director':director,'gross':gross
    }

records = []
for movie in movies:
    
    records.append(movie_scraiping(movie))
    
print(records)

df = pd.DataFrame(records)
df.to_csv('test.csv')
