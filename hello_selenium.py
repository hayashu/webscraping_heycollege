import time
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
op = Options()
# --headlessだけではOSによって動かない、プロキシが弾かれる、
# CUI用の省略されたHTMLが帰ってくるなどの障害が出ます。
# 長いですが、これら6行あって最強かつどんな環境でも動きますので、必ず抜かさないようにしてください。
op.add_argument("--disable-gpu")
op.add_argument("--disable-extensions")
op.add_argument("--proxy-server='direct://'")
op.add_argument("--proxy-bypass-list=*")
op.add_argument("--start-maximized")
op.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=op)
driver.get('https://www.google.com')
time.sleep(2)

el = driver.find_element_by_name('q')
el.send_keys('Qiitaで検索楽しいぞ!!!')
time.sleep(2)

el.submit()

from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source, features='html.parser')
print(soup.title.string)