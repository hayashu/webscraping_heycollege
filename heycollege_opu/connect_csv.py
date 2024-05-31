import os
import glob
import csv
import pandas as pd

DATA_PATH = "./data/"
All_Files = glob.glob('{}*.csv'.format(DATA_PATH))
print(All_Files)
# フォルダ中の全csvをマージ
list = []
for file in All_Files:
    list.append(pd.read_csv(file))
df = pd.concat(list, sort=False)
del df['Unnamed: 0']
# csv出力
df.to_csv('connect_datas.csv', encoding='utf_8_sig')