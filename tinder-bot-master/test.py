from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://tinder.com/app/login')
sleep(3)


sleep(3)
driver.close()