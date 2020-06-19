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


browser = webdriver.Chrome()
# boone, raleigh, salt-lake, fresno''
# hope to get user input later
stationIDs = ['722198-63819-', '723060-13722-', '725720-24127-', '723890-93193-']
x = 0

# changing for naming file later
while x in range(len(stationIDs)):
    city = 'blank'
    station = str(stationIDs[x])
    # print(station)
    if station == '722198-63819-':
        city = 'boone'
    elif station == '723060-13722-':
        city = 'raleigh'
    elif station == '725720-24127-':
        city = 'salt-lake-city'
    else:
        city = 'fresno'
    # print(city)

    # selenium loop to grab each year starting from '19
    i = 1
    while i < 6:
        start_year = 2020 - i
        year = str(start_year)

        # noaa isd link
        link = 'ftp://ftp.ncdc.noaa.gov/pub/data/noaa/isd-lite/' + year + '/'

        # file download link
        url = '/pub/data/noaa/isd-lite/' + year + '/' + station + year + '.gz'

        # handles browser load timeout, will retry until it loads - helps when my wifi is slow
        load = False
        while load != True:
            try:
                browser.get(link)

                # clicks download
                browser.find_element_by_xpath('//a[@href="' + url + '"]').click()
            except Exception as e:
                load = False
            else:
                load = True

        # setting naming schema to search for when we loop through our recently downloaded files
        file = station + year + '.gz'
        sfile = str(file)

        # setting naming schema to export to so its easier to read city instead of stationID when working with csvs
        dfile = city + year + '.csv'
        download_file = str(dfile)

        time.sleep(1)
        # change to your path
        download = os.path.join(r'C:\Users\MG\Downloads', sfile)

        # change to your path
        dest = os.path.join(r'C:\Users\MG\Desktop\Raw_Wx', download_file)

        # using gzip to read in files, then slap onto a df with field names for each variable
        with gzip.open(download, 'rb') as wxfile:
            df = pd.read_csv(wxfile, sep='\s+', header=None)
            df.columns = ['year', 'month', 'day', 'hour', 'temp', 'dew_point', 'sea_level_pressure', 'wind_dir', 'wind_speed', 'coverage', 'precip_1', 'precip_6']
            df.loc[:, 'year'] = year

            df.to_csv(dest, index=False)

        i += 1
    x += 1
browser.close()
browser.quit()

# works
