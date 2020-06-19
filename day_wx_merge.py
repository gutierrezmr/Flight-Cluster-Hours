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


# merges all sunrise and sunset data onto Wx files for each location, and each year, on that column that we created before
import glob
wx_path = r"C:\Users\MG\Desktop\cleaned\*.csv"
day_path = r"C:\Users\MG\Desktop\Daylight\*.csv"

z = 0
i = []
for z in glob.glob(wx_path):
    o = str(z)
    i.append(o)

j = 0
l = []
for j in glob.glob(day_path):
    q = str(j)
    l.append(q)

m = 0
while m in range(len(i)) and m in range(len(l)):
    print(i[m])
    print(l[m])

    df1 = pd.read_csv(i[m])
    df1['index'] = df1.index
    df2 = pd.read_csv(l[m])

    merge = pd.merge(df1, df2, how='left', left_on='concat', right_on='concat')

    merge_path = str(l[m])
    merge_path_new = merge_path.replace('Daylight', 'merged')

    merge.to_csv(merge_path_new, index=False)

    m += 1
    # works
