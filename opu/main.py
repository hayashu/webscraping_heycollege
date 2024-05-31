from selenium import webdriver
import pandas as pd
import time
import faculty_index

department = faculty_index.Faculty()
department.open_window()
department.faculty_list()


time.sleep(3)

for url in department.faculties:
  department.driver.get(url)
  time.sleep(1)
  #授業一覧
  department.lecture_list()
  break


department.output_csv()
department.close_window()
