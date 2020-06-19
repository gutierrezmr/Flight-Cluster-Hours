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
path = r"C:\Users\MG\Desktop\merged\*.csv"


#df = pd.read_csv(r"C:\Users\MG\Desktop\merged\boone2015.csv")

for fname in glob.glob(path):
    i = str(fname)
    df = pd.read_csv(i)

    # print(i)

    # determine whether or not hour is in range of sunrise to sunset

    df.loc[(df['hour'] >= (df['sunrise']) + 1) & (df['hour'] <= (df['sunset']) - 1), 'is_day'] = '1'
    df.loc[(df['hour'] < (df['sunrise']) + 1), 'is_day'] = '0'
    df.loc[(df['hour'] > (df['sunset']) - 1), 'is_day'] = '0'

    # temp check
    # switch to metric - most of the world (possible limitation if others in the world have to convert C- F) -

    # 3 line graphs, yr to date, for locations
    # zip for locations, plug in, convert to weather station (don't WORRY about about automation!)

    # user input of zip, location etc, map to weather station, pulls hourly weather, sunrise sunset, X line graphs overlayed, compare to prior year,
    # adjust for cluster hours, sister side tab
    # zip for location, compare to previous 3yr

    # are we getting + or - flight hours than previous years, if condition, do X with hives

    df.loc[(df['temp_converted'] > 55), 'warm_enough'] = '1'
    df.loc[(df['temp_converted'] <= 55), 'warm_enough'] = '0'

    # rain check
    df.loc[(df['precip_1'] != -9999), 'dry'] = '0'
    df.loc[(df['precip_1'] == -9999), 'dry'] = '1'

    # if all three columns in row are true, store a 1 in new column 'flight hour'
    df.loc[(df['is_day'] == '1') & (df['warm_enough'] == '1'), 'flight_hour'] = '1'

    # wind speed, - watch for certain threshhold, isd data has this
    # - until threshholds are known, we're guessing - dewpoint (in isd) pressure (in isd)
    # need evidence of these factors, experiments?

    # correlation with iot sensors - could be good to test on these locations for these factors and thresholds

    # capture everything, but first test temp - then see how other factors affect

    # measure when they are flying vs when they are not - bee flight counters, portable LIDAR? unit (),  activity sensors (digital hives - infrared flight detector) - link in this project

    ##phase 2 ^##

    # daily hours of daytime flight temps, 1hr after sunrise and 1hr before sunset, above 55F - DHBFH
    #df.loc[(df['warm_enough'] == '1') & (df['is_day'] == '1'), 'max_potential'] = round((df['sunset'] - df['sunrise']), 0)

    # Cluster - DHBCH count
    df.loc[(df['temp_converted'] <= 55), 'cold_enough'] = '1'
    df.loc[(df['temp_converted'] > 55), 'cold_enough'] = '0'

    #df.loc[(df['is_day'] == '1') & (df['cold_enough'] == '1'), 'DHBCH_count'] = '1 **'


#% of max number of potential daily flight hours - %MDFH

    df['accum_day'] = df['concat'].astype(str) + df['flight_hour'].astype(str)
    df['concat3'] = df['concat'].astype(str) + df['cold_enough'].astype(str)
    df['concat_hour'] = df['concat'].astype(str) + df['hour'].astype(str) + df['temp_converted'].astype(str)

    #df['num_month'] = '0'

    df.loc[(df['month'] == 'Jan'), 'num_month'] = '1'
    df.loc[(df['month'] == 'Feb'), 'num_month'] = '2'
    df.loc[(df['month'] == 'Mar'), 'num_month'] = '3'
    df.loc[(df['month'] == 'Apr'), 'num_month'] = '4'
    df.loc[(df['month'] == 'May'), 'num_month'] = '5'
    df.loc[(df['month'] == 'Jun'), 'num_month'] = '6'
    df.loc[(df['month'] == 'Jul'), 'num_month'] = '7'
    df.loc[(df['month'] == 'Aug'), 'num_month'] = '8'
    df.loc[(df['month'] == 'Sep'), 'num_month'] = '9'
    df.loc[(df['month'] == 'Oct'), 'num_month'] = '10'
    df.loc[(df['month'] == 'Nov'), 'num_month'] = '11'
    df.loc[(df['month'] == 'Dec'), 'num_month'] = '12'

    df['month_concat'] = df['year'].astype(str) + df['num_month'].astype(str) + df['day'].astype(str) + df['hour'].astype(str)

    sum_csv = df.groupby(['accum_day']).size().reset_index(name='DHBFH')

    sum_path = i.replace('merged', 'sum')
    sum_csv.to_csv(sum_path, index=False)

    data = pd.read_csv(sum_path)
    # data[~df.accum_day.str.contains('nan')]

    data.loc[(data['accum_day'].str.contains('nan')), 'DHBFH'] = '0'

    # still need AHBFD**

    data.to_csv(sum_path, index=False)

    flight_path = i.replace('merged', 'final')

    # print(flight_path)

    df.to_csv(flight_path, index=False)

    z = 0
    i = []
    for z in glob.glob(flight_path):
        o = str(z)
        i.append(o)

    j = 0
    l = []
    for j in glob.glob(sum_path):
        q = str(j)
        l.append(q)

    m = 0
    while m in range(len(i)) and m in range(len(l)):

        df1 = pd.read_csv(i[m])
        df2 = pd.read_csv(l[m])

        merge = pd.merge(df1, df2, how='left', left_on='accum_day', right_on='accum_day')

        merge1 = merge.drop('accum_day', axis=1)
        merge2 = merge1.drop_duplicates(subset=['concat_hour'], keep='first', inplace=True)
        merge_path = str(l[m])
        merge_path_new = merge_path.replace('sum', 'total')

        # print(merge_path_new)
        merge1.to_csv(merge_path_new, index=False)
        # max = 1hr post sunrise, and 1hr pre sunset
        m += 1

        # elevation can also come into play

    # for s in glob.glob(merge_path_new):
     #   percent = pd.read_csv(s)

    #% of max number of potential daily flight hours - %MDFH
      #  percent.loc[(df['flight_hour'] == '1'), 'pMDFH'] = (percent['DHBFH'] / percent['max_potential']) * 100

       # percent.to_csv(merge_path_new, index=False)

    # works
