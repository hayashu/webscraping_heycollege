# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import chromedriver_binary
from bs4 import BeautifulSoup

# ブラウザを開く。
driver = webdriver.Chrome()
# Googleの検索TOP画面を開く。
driver.get("https://souda-kyoto.jp/travel/koyo/")   #'//div[@class = "areaSearch"]/ul[@id = "koyoSpot"]'

csvlist = []
conditions = []
days = []
places = []
csvlists = []
#結果の出力
def koyo_info():
    for n in range(6):
        elem = driver.find_element_by_xpath('//div[@class = "areaSearch"]/ul[@id = "koyoSpot'+str(n)+'"]')
        all_li = elem.find_elements_by_tag_name('li')

        for li in all_li:
            place = li.find_elements_by_tag_name('strong')
            images = li.find_elements_by_tag_name('img')
            dates = li.find_elements_by_tag_name('em')

            

            for date in dates:
                day = date.text
                days.append(day)

            for image in images:
                condition = image.get_attribute('src')
                conditions.append(condition)

            for p in place:
                places.append(p.text)

        
    return {'place':places,'date':days,'image':conditions}

result = koyo_info()
print(result)

driver.close()
driver.quit()