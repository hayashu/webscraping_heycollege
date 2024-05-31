from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www0.osakafu-u.ac.jp/syllabus/Detail.aspx?CD=5956")
time.sleep(1)

def get_class_item():
  items = ['科目名','配当年次','開講期間','科目分類','曜日コマ','教員']
  print(items)
  class_name = driver.find_element_by_xpath('//*[@id="lbl_KAMOKU_NM"]').text
  student_grade = driver.find_element_by_xpath('//*[@id="lbl_HAITO"]').text
  term = driver.find_element_by_xpath('//*[@id="lbl_GAKKI_NM"]').text
  class_group = driver.find_element_by_xpath('//*[@id="lbl_KAMOKU_BUNRUI"]').text
  class_time = driver.find_element_by_xpath('//*[@id="lbl_WJ_NM"]').text
  teacher = driver.find_element_by_xpath('//*[@id="lbl_KYOIN_NM"]').text

  items = [class_name,student_grade,term,class_group,class_time,teacher.replace('\u3000','')]



driver.close()
driver.quit()