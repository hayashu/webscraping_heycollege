# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# ブラウザを開く。
driver = webdriver.Chrome()
# Googleの検索TOP画面を開く。
driver.get("https://www.google.co.jp/")
# 3秒待機
time.sleep(3)
search = driver.find_element_by_name('q') 
search.send_keys('大阪府立大学 学生ポータル')
search.send_keys(Keys.ENTER)
element = driver.find_element_by_partial_link_text("sts.osakafu-u.ac.jp")
element.click()
# ログインボタンをクリックする

# 1秒待機
time.sleep(1)
# ログインIDを入力
login_id = driver.find_element_by_id("input_1")
login_id.send_keys("sdb01121")
# 次へボタンをクリック

# 1秒待機
time.sleep(1)
# パスワードを入力
password = driver.find_element_by_id("input_2")
password.send_keys("H8841aYAeds")
#ログインボタンをクリック
login_btn = driver.find_element_by_class_name("credentials_input_submit")
login_btn.click()

#10秒待機
time.sleep(10)
# ブラウザを終了する。
driver.close()