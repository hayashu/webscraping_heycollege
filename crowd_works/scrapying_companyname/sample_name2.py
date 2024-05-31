import requests
from bs4 import BeautifulSoup

"""""
import time
import os
import pandas as pd
import codecs
from urllib.parse import urljoin



result =[]
urls = []
company_text = []

for m in range(1,11):

    url = 'https://www.nextcity.jp/36/6/'+str(m)+'.html'
    urls.append(url)
    length = len(urls)


for n in range(length):
    print(n)
    next_url = urls[n]

    
    res = requests.get(next_url)
    res.raise_for_status()
    html = BeautifulSoup(res.content,'lxml')

    detail_url_list = html.find_all('table',class_ = 'content kensaku_item zenbu')
    length = len(detail_url_list)

    for l in range(length):                      
        company_text = detail_url_list[l].find('a').get_text()

        print(company_text)
    
    time.sleep(5)

"""""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import chromedriver_binary
import pandas as pd

# ブラウザを開く。
driver = webdriver.Chrome()
# Googleの検索TOP画面を開く。
driver.get("https://www.nextcity.jp/36/6/1.html")   #'//div[@class = "areaSearch"]/ul[@id = "koyoSpot"]'


csvlist = []
conditions = []
days = []
places = []
csvlists = []
#結果の出力
def company_info():
    companies = driver.find_element_by_xpath('//div[@id = "wrapper"]/div[@id = "content"]/table[@class = "content kensaku_item zenbu"]')

    
    for n in companies:
        company = n.find_element_by_xpath('//tbody/tr/th/a').text



        csvlist.append(company)
    
    return (csvlist)

result = company_info()
df = pd.DataFrame(result)
df.to_csv('save_csvs_name2.csv')
driver.close()
driver.quit()