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


path = r"C:\Users\MG\Desktop\cluster\*.csv"
for fname in glob.glob(path):
    i = str(fname)
    df = pd.read_csv(i)
    #df.drop_duplicates(subset=['year', 'month', 'day'], keep='first')

    #df = pd.read_csv(test)

    #df2['DHBFH_keep'] = df['DHBFH']

    #df.drop_duplicates(subset=['concat'], keep='first', inplace=True)
    df['flight_concat'] = df['year'].astype(str) + df['month'].astype(str) + df['day'].astype(str) + df['flight_hour'].astype(str)

    #df.loc[(df['flight_concat'].str.contains('nan')), 'DHBCH'] = 0
    df2 = df.drop_duplicates(subset=['flight_concat'], keep='first')
    df3 = df2.drop_duplicates(subset=['concat3'], keep='last')

    df3['cluster_concat'] = df3['concat'].astype(str) + df3['DHBCH'].astype(str)
    df3.loc[(df3['cluster_concat'].str.contains('nan')), 'DHBCH'] = 0

    df3 = df3.drop_duplicates(subset=['concat'], keep='last')

    # AHBFH = sum of all daily hours
    # df2['DHBFH_keep'] =

    count = sum(df3['DHBCH'])
    df3['AHBCH'] = count

    seriesObj = df3.apply(lambda x: True if x['DHBCH'] >= 1 else False, axis=1)
    numOfRows = len(seriesObj[seriesObj == True].index)

    df3['AHBCD'] = numOfRows

    count2 = sum(df3['DHBFH'])
    df3['AHBFH'] = count2

    seriesObj2 = df3.apply(lambda x: True if x['DHBFH'] >= 1 else False, axis=1)
    numOfRows2 = len(seriesObj2[seriesObj2 == True].index)

    df3['AHBFD'] = numOfRows2

    df3.drop(df3.columns[[1, 17, 25, 26, 27, 28, 30, 31]], axis=1, inplace=True)

    df_final = df3[['year', 'month', 'day', 'hour', 'temp', 'dew_point', 'sea_level_pressure', 'wind_dir', 'wind_speed', 'coverage', 'precip_1', 'precip_6', 'in_season', 'temp_converted', 'sunrise', 'sunset', 'is_day', 'warm_enough', 'dry', 'cold_enough', 'flight_hour', 'cold_enough', 'DHBFH', 'AHBFH', 'AHBFD', 'DHBCH', 'AHBCH', 'AHBCD']]

    #drop1 = df3.drop('concat', axis=1)
    #drop2 = df3.drop('concat3', axis=1)
    #drop3 = df3.drop('concat_hour', axis=1)
    #drop4 = df3.drop('index', axis=1)
    #drop5 = df3.drop('num_month', axis=1)
    #drop6 = df3.drop('month_concat', axis=1)
    #drop7 = df3.drop('cluster_concat', axis=1)

    #df2 = df.drop_duplicates(subset=['flight_concat'], keep='first')
    #df2['newish_concat'] = df2['concat'].astype(str) + df2['DHBCH'].astype(str)

    #df2.loc[(df2['newish_concat'].str.contains('nan')), 'DHBCH'] = 0

    #df3 = df2.drop_duplicates(subset=['concat3'], keep='last')

    #df2['slice'] = df2['flight_concat'].str[:-3].astype(str)

    #df2['strip_concat'] = df['concat'].astype(str) + df['DHBCH'].astype(str)

    #df2.loc[(df2['strip_concat'].str.contains('nan')), 'DHBCH'] = 0

    #df3 = df2.drop_duplicates(subset=['slice'], keep='first')

    #count2 = sum(df3['DHBCH'])
    #df3['AHBCH'] = count2

    #seriesObj2 = df3.apply(lambda x: True if x['DHBCH'] >= 1 else False, axis=1)
    #numOfRows2 = len(seriesObj2[seriesObj2 == True].index)

    #df3['AHBCD'] = numOfRows2

    # print(count2)

    path_new = i.replace('cluster', 'cluster_final')
    df_final.to_csv(path_new, index=False)
# works
