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

browser = webdriver.Chrome()

# getting sunrises
l_sunrise = []
l_sunset = []
date_list = []


# list needs to be in REVERSE order of the way you ordered cities in noaa scrape, I think because the other folders will list in order of last modified and we want to join in the future by the right city and year

#place_list = ['boone', 'raleigh', 'salt-lake-city', 'fresno']
place_list = ['fresno', 'salt-lake-city', 'raleigh', 'boone']


# this script goes out to timeanddate.com and grabs the sunrise and sunset times for each day, mo and yr
# variables are sometimes not descriptive, sorry about that
i = 0
while i in range(len(place_list)):
    yy = 1
    while yy < 6:
        yx = str(2020 - yy)
        mo = 1
        while mo < 13:
            month = str(mo)
            city = str(place_list[i])
            browser.get('https://www.timeanddate.com/sun/usa/' + city + '?month=' + month + '&year=' + yx)

            n = 1
            while n < 33:

                # this was very frutstating.. when I go out to the site, there is a green notifitication bar for when our times change twice a year and this is the only way I could handle it, not pretty.. but it works

                if city == 'fresno' and yx == '2019':
                    if mo == 3 and n == 10:
                        n += 1
                elif city == 'fresno' and yx == '2018':
                    if mo == 3 and n == 11:
                        n += 1
                elif city == 'fresno' and yx == '2017':
                    if mo == 3 and n == 12:
                        n += 1
                elif city == 'fresno' and yx == '2016':
                    if mo == 3 and n == 13:
                        n += 1
                elif city == 'fresno' and yx == '2015':
                    if mo == 3 and n == 8:
                        n += 1
                    else:
                        pass

                if city == 'salt-lake-city' and yx == '2019':
                    if mo == 3 and n == 10:
                        n += 1
                elif city == 'salt-lake-city' and yx == '2018':
                    if mo == 3 and n == 11:
                        n += 1
                elif city == 'salt-lake-city' and yx == '2017':
                    if mo == 3 and n == 12:
                        n += 1
                elif city == 'salt-lake-city' and yx == '2016':
                    if mo == 3 and n == 13:
                        n += 1
                elif city == 'salt-lake-city' and yx == '2015':
                    if mo == 3 and n == 8:
                        n += 1
                    else:
                        pass

                if city == 'raleigh' and yx == '2019':
                    if mo == 3 and n == 10:
                        n += 1
                elif city == 'raleigh' and yx == '2018':
                    if mo == 3 and n == 11:
                        n += 1
                elif city == 'raleigh' and yx == '2017':
                    if mo == 3 and n == 12:
                        n += 1
                elif city == 'raleigh' and yx == '2016':
                    if mo == 3 and n == 13:
                        n += 1
                elif city == 'raleigh' and yx == '2015':
                    if mo == 3 and n == 8:
                        n += 1
                    else:
                        pass

                if city == 'boone' and yx == '2019':
                    if mo == 3 and n == 10:
                        n += 1
                elif city == 'boone' and yx == '2018':
                    if mo == 3 and n == 11:
                        n += 1
                elif city == 'boone' and yx == '2017':
                    if mo == 3 and n == 12:
                        n += 1
                elif city == 'boone' and yx == '2016':
                    if mo == 3 and n == 13:
                        n += 1
                elif city == 'boone' and yx == '2015':
                    if mo == 3 and n == 8:
                        n += 1
                    else:
                        pass

                if city == 'fresno' and yx == '2019':
                    if mo == 11 and n == 3:
                        n += 1
                elif city == 'fresno' and yx == '2018':
                    if mo == 11 and n == 4:
                        n += 1
                elif city == 'fresno' and yx == '2017':
                    if mo == 11 and n == 5:
                        n += 1
                elif city == 'fresno' and yx == '2016':
                    if mo == 11 and n == 6:
                        n += 1
                elif city == 'fresno' and yx == '2015':
                    if mo == 11 and n == 1:
                        n += 1
                    else:
                        pass

                if city == 'salt-lake-city' and yx == '2019':
                    if mo == 11 and n == 3:
                        n += 1
                elif city == 'salt-lake-city' and yx == '2018':
                    if mo == 11 and n == 4:
                        n += 1
                elif city == 'salt-lake-city' and yx == '2017':
                    if mo == 11 and n == 5:
                        n += 1
                elif city == 'salt-lake-city' and yx == '2016':
                    if mo == 11 and n == 6:
                        n += 1
                elif city == 'salt-lake-city' and yx == '2015':
                    if mo == 11 and n == 1:
                        n += 1
                    else:
                        pass

                if city == 'raleigh' and yx == '2019':
                    if mo == 11 and n == 3:
                        n += 1
                elif city == 'raleigh' and yx == '2018':
                    if mo == 11 and n == 4:
                        n += 1
                elif city == 'raleigh' and yx == '2017':
                    if mo == 11 and n == 5:
                        n += 1
                elif city == 'raleigh' and yx == '2016':
                    if mo == 11 and n == 6:
                        n += 1
                elif city == 'raleigh' and yx == '2015':
                    if mo == 11 and n == 1:
                        n += 1
                    else:
                        pass

                if city == 'boone' and yx == '2019':
                    if mo == 11 and n == 3:
                        n += 1
                elif city == 'boone' and yx == '2018':
                    if mo == 11 and n == 4:
                        n += 1
                elif city == 'boone' and yx == '2017':
                    if mo == 11 and n == 5:
                        n += 1
                elif city == 'boone' and yx == '2016':
                    if mo == 11 and n == 6:
                        n += 1
                elif city == 'boone' and yx == '2015':
                    if mo == 11 and n == 1:
                        n += 1
                    else:
                        pass

                # html elements
                date = str(n)
                rise_link = '/html/body/div[1]/div[7]/section[3]/div/div[2]/div/table/tbody/tr[' + date + ']/td[1]'
                set_link = '/html/body/div[1]/div[7]/section[3]/div/div[2]/div/table/tbody/tr[' + date + ']/td[2]'

                year_link = '/html/body/div[1]/div[7]/section[3]/div/div[2]/div/table/thead/tr[1]/th[1]'

                month_link = '/html/body/div[1]/div[7]/section[3]/div/div[2]/div/table/thead/tr[2]/th[1]'

                day_link = '/html/body/div[1]/div[7]/section[3]/div/div[2]/div/table/tbody/tr[' + date + ']/th'

                # try to scrape until there are no more days in the month
                try:
                    # innerhtml just grabs the string value
                    sunrise = browser.find_element_by_xpath(rise_link).get_attribute("innerHTML").split(' ')[0]

                    # sunrise comes back as string 7:23, I want to convert to 7.23 so I can subtract later on
                    r = sunrise[0]
                    sun_rise = r + '.' + sunrise[2] + sunrise[3]

                    # same thing, only add 12 to the float value so it is 'converted' to military time
                    sunset = browser.find_element_by_xpath(set_link).get_attribute("innerHTML").split(' ')[0]
                    test = int(sunset[0]) + 12
                    t1 = str(test)
                    sun_set = t1 + '.' + sunset[2] + sunset[3]

                    yr = browser.find_element_by_xpath(year_link).get_attribute("innerHTML").split(' ')[0]
                    mon = browser.find_element_by_xpath(month_link).get_attribute("innerHTML").split(' ')[0]
                    dy = browser.find_element_by_xpath(day_link).get_attribute("innerHTML").split(' ')[0]

                   # handles 2 weird outputs in the inner html that I got, not sure if I even still need the note and div conditions now that I think about it

                    if sunrise == 'Note':  # need to handle <div on june 5 - 6.09
                        pass
                    elif sun_rise == '<div':
                        pass
                    else:
                        l_sunrise.append(sun_rise)
                    if sun_set == 'Note:' and sun_set == '<div':
                        pass
                    else:
                        l_sunset.append(sun_set)

                    # string concat for hours, we'll need this later when we create a df that needs to be merged on the scraped noaa data
                    concat = yx + mon + dy
                    full_date = str(concat)
                    # print(full_date)

                    date_list.append(full_date)

                except Exception as e:
                    break
                n += 1
            mo += 1

        df1 = pd.DataFrame({'concat': date_list})
        df2 = pd.DataFrame({'sunrise': l_sunrise})
        df3 = pd.DataFrame({'sunset': l_sunset})

        result = pd.concat([df1, df2, df3], axis=1, sort=False)

        result_path = r"C:\\Users\\MG\\Desktop\\Daylight\\" + city + yx + '.csv'
        # print(result_path)
        result.to_csv(result_path, index=False)

        date_list.clear()
        l_sunrise.clear()
        l_sunset.clear()

        yy += 1
    i += 1

browser.close()
browser.quit()

# works
