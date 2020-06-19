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


# cleans each file in path and exports to csv
import glob
# change to same path you just exported those files as csvs to in the last script
path = r"C:\Users\MG\Desktop\Raw_Wx\*.csv"
for fname in glob.glob(path):
    i = str(fname)
    df = pd.read_csv(i)

    # handling binary variable for within summer - winter solstice or not, can change accordingly
    # can index columns by name by using df.iloc
    # more on df indexing that I reference: https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/

    # if abc columns meet xyz conditions then a new column called 'in_season' gets a certain value
    df.loc[(df['month'] >= 6) & (df['day'] >= 20), 'in_season'] = 1
    df.loc[df['month'] >= 7, 'in_season'] = 1
    df.loc[df['month'] < 6, 'in_season'] = 0
    df.loc[(df['month'] == 6) & (df['day'] < 20), 'in_season'] = 0
    df.loc[(df['month'] == 12) & (df['day'] >= 21), 'in_season'] = 0

    # chaning hour of day numbers to military time

    # I needed to essentially convert these hours to a float because I needed to take the difference of sunrise and sunset and I didn't know how to do that with timestamps and couldn't find a forum that explained it well
    # Need to automate
    df.loc[df['hour'] == 0, 'hour'] = '0.00'
    df.loc[df['hour'] == 1, 'hour'] = '1.00'
    df.loc[df['hour'] == 2, 'hour'] = '2.00'
    df.loc[df['hour'] == 3, 'hour'] = '3.00'
    df.loc[df['hour'] == 4, 'hour'] = '4.00'
    df.loc[df['hour'] == 5, 'hour'] = '5.00'
    df.loc[df['hour'] == 6, 'hour'] = '6.00'
    df.loc[df['hour'] == 7, 'hour'] = '7.00'
    df.loc[df['hour'] == 8, 'hour'] = '8.00'
    df.loc[df['hour'] == 9, 'hour'] = '9.00'
    df.loc[df['hour'] == 10, 'hour'] = '10.00'
    df.loc[df['hour'] == 11, 'hour'] = '11.00'
    df.loc[df['hour'] == 12, 'hour'] = '12.00'
    df.loc[df['hour'] == 13, 'hour'] = '13.00'
    df.loc[df['hour'] == 14, 'hour'] = '14.00'
    df.loc[df['hour'] == 15, 'hour'] = '15.00'
    df.loc[df['hour'] == 16, 'hour'] = '16.00'
    df.loc[df['hour'] == 17, 'hour'] = '17.00'
    df.loc[df['hour'] == 18, 'hour'] = '18.00'
    df.loc[df['hour'] == 19, 'hour'] = '19.00'
    df.loc[df['hour'] == 20, 'hour'] = '20.00'
    df.loc[df['hour'] == 21, 'hour'] = '21.00'
    df.loc[df['hour'] == 22, 'hour'] = '22.00'
    df.loc[df['hour'] == 23, 'hour'] = '23.00'

    df.loc[(df['month'] == 1), 'month'] = 'Jan'
    df.loc[(df['month'] == 2), 'month'] = 'Feb'
    df.loc[(df['month'] == 3), 'month'] = 'Mar'
    df.loc[(df['month'] == 4), 'month'] = 'Apr'
    df.loc[(df['month'] == 5), 'month'] = 'May'
    df.loc[(df['month'] == 6), 'month'] = 'Jun'
    df.loc[(df['month'] == 7), 'month'] = 'Jul'
    df.loc[(df['month'] == 8), 'month'] = 'Aug'
    df.loc[(df['month'] == 9), 'month'] = 'Sep'
    df.loc[(df['month'] == 10), 'month'] = 'Oct'
    df.loc[(df['month'] == 11), 'month'] = 'Nov'
    df.loc[(df['month'] == 12), 'month'] = 'Dec'

    # concat year, month and day col into new column to create join column for sunrises and sunsets. I'll send files of each script output so you can see the differences
    # you can add mathematically if you remove .astype(str)

    df['concat'] = df['year'].astype(str) + df['month'].astype(str) + df['day'].astype(str)

    # convert scaling factor on C temp to F
    df['temp_converted'] = ((df['temp'] / 10) * (9 / 5) + 32)

    # new path, new csvs, gets old after 5 scripts..
    # the second arg is the new folder
    path_new = i.replace('Raw_Wx', 'cleaned')

    df.to_csv(path_new, index=True)
# works
