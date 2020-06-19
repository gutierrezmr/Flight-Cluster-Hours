import gzip
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import glob
import os
import pandas as pd
import itertools
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import csv
import re
import numpy as np
import glob
import matplotlib.pyplot as plt
import seaborn as sns

path = r"C:\Users\MG\Desktop\total\*.csv"
#test = r"C:\Users\MG\Desktop\total\boone2015.csv"


for fname in glob.glob(path):
    i = str(fname)
    df = pd.read_csv(i)
    #df.drop_duplicates(subset=['year', 'month', 'day'], keep='first')

#df = pd.read_csv(test)

    df["concat2"] = df["year"].astype(str) + df["month"].astype(str) + df['day'].astype(str) + df['DHBFH'].astype(str)

    df["concat3"] = df["year"].astype(str) + df["month"].astype(str) + df['day'].astype(str) + df['cold_enough'].astype(str)

    #df2 = df['concat3']
    #df3 = df['cold_enough']

    #result = pd.concat([df1, df2, df3], axis=1, sort=False)
    #sum_csv = result.groupby(['concat3']).size().reset_index(name='yerr')
    r = df.groupby('concat3').cold_enough.count().reset_index(name='DHBCH')
    #r = result['concat3'].value_counts()
    # print(r)
    #df.loc[(df['concat3'].str[-1:] == '0'), 'drop']

    # drops all rows in column that last piece of string = 0
    r2 = r.drop(r[r['concat3'].str[-1:] == '0'].index)

    r2['concat'] = r2['concat3'].str[:-1].astype(str)

    r3 = r2.drop('concat3', axis=1)
    #r2['concat1'] = r2['concat3'].str[-1:]
    #df.drop_duplicates(subset=['concat2'], keep='first', inplace=True)

    # AHBFH = sum of all daily hours
    #count = sum(df['DHBFH'])
    #df['AHBFH'] = count

    #seriesObj = df.apply(lambda x: True if x['DHBFH'] >= 1 else False, axis=1)
    #numOfRows = len(seriesObj[seriesObj == True].index)

    #df['AHBFD'] = numOfRows

    #df.plot(kind='bar',x='month', y='DHBFH')
    #y = df['DHBFH']

    # plt.plot(y)

    # plt.show()

    flight_path = i.replace('total', 'next')

    # need to add headers
    r3.to_csv(flight_path, index=False)


new_path = r'C:\Users\MG\Desktop\next\*.csv'

z = 0
n = []
for z in glob.glob(new_path):
    o = str(z)
    n.append(o)


j = 0
l = []
for j in glob.glob(path):
    q = str(j)
    l.append(q)


m = 0
while m in range(len(n)) and m in range(len(l)):

    df1 = pd.read_csv(n[m])
    df2 = pd.read_csv(l[m])

    merge = df2.reset_index().merge(df1, how='right', on='concat', sort=True)

    # merge.sort_index()
    merge = pd.merge(df1, df2, how='right', on='concat')
    #merge1 = merge.drop('accum_day', axis=1)

    merge_path = str(n[m])
    merge_path_new = merge_path.replace('next', 'cluster_start')

    merge.to_csv(merge_path_new, index=False)

    m += 1

merge_path_new2 = r"C:\Users\MG\Desktop\cluster_start\*.csv"

for name in glob.glob(merge_path_new2):
    b = str(name)
    df = pd.read_csv(b)
    df.sort_values('index', inplace=True)
    merge_path_new3 = b.replace('cluster_start', 'cluster')
    df.to_csv(merge_path_new3, index=False)
# works
