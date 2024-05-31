from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("http://www0.osakafu-u.ac.jp/syllabus/list01.aspx?CD1=2B11&CD2=01")
time.sleep(1)

def lecture_list():
  for div in range(3,12):
    if div >= 4 and div <=6:
      pass
    else:
      lecture_title = driver.find_element_by_xpath('//*[@id="contents"]/div/div['+str(div)+']/h3/span/strong')
      print(lecture_title.text)
      lecture = []
      for ol in range(1,4):
        for li in range(1,70):
          try:
            index = driver.find_element_by_xpath('//*[@id="contents"]/div/div['+str(div)+']/div/ol['+str(ol)+']/li['+str(li)+']/a')
            lecture.append(index)
          except :
            pass

lecture_list()


driver.close()
driver.quit()