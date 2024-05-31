import requests
from bs4 import BeautifulSoup
import time
import os
import pandas as pd
import codecs
from urllib.parse import urljoin



result =[]

company_text = []

url = 'https://www.nextcity.jp/36/1/'

res = requests.get(url)
res.raise_for_status()
html = BeautifulSoup(res.content,'html.parser')

detail_url_list = html.find_all('table',class_ = 'content kensaku_item zenbu')
length = len(detail_url_list)

for m in range(length):                      
    company_text = detail_url_list[m].find('a').get_text()
    company_name = company_text.split('-')
    result.append(company_name[0])
    

time.sleep(5)


for n in range(99):

    next_url = ('https://www.nextcity.jp/36/1/'+str(n+2)+'.html')

    res2 = requests.get(next_url)
    res2.raise_for_status()
    html = BeautifulSoup(res2.content,'html.parser')

    detail_url_list2 = html.find_all('table',class_ = 'content kensaku_item zenbu')
    length = len(detail_url_list2)

    for l in range(length):                      
        company_text2 = detail_url_list2[l].find('a').get_text()
        company_name2 = company_text2.split('-')
        result.append(company_name2[0])
        
    
    time.sleep(5)
    print(n)

df = pd.DataFrame(result)
df.to_csv('save_csvs_name.csv')
    
