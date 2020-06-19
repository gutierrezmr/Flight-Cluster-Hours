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
import statistics

user_in = str(input('Enter location: '))

file = user_in + '*.csv'

path = os.path.join(r'C:\Users\MG\Desktop\cluster_final', file)

#path = r"C:\Users\MG\Desktop\cluster_final\*.csv"
AHBCD_list = []
AHBFD_list = []

AHBFH_list = []
AHBCH_list = []

yr_list = []
for fname in glob.glob(path):
    i = str(fname)
    df = pd.read_csv(i)
    AHBCD = df.iloc[1, 27]
    AHBFD = df.iloc[1, 24]

    AHBFH = df.iloc[1, 23]
    AHBCH = df.iloc[1, 26]
    yr = df.iloc[1, 0]

    AHBCD_list.append(AHBCD)
    AHBFD_list.append(AHBFD)
    AHBFH_list.append(AHBFH)
    AHBCH_list.append(AHBCH)
    yr_list.append(yr)


#print(day_list, yr_list)
avg_AHBCD = statistics.mean(AHBCD_list)
avg_AHBFD = statistics.mean(AHBFD_list)

last_val_cluster = float(AHBCD_list[-1])
last_val_flight = float(AHBFD_list[-1])

second_last_cluster = float(AHBCD_list[-2])
second_last_flight = float(AHBFD_list[-2])

dif_cluster = round(((last_val_cluster - second_last_cluster) / second_last_cluster) * 100, 2)
dif_cluster_avg = round(((last_val_cluster - avg_AHBCD) / avg_AHBCD) * 100, 2)

dif_flight = round(((last_val_flight - second_last_flight) / second_last_flight) * 100, 2)
dif_flight_avg = round(((avg_AHBFD - last_val_flight) / last_val_flight) * 100, 2)


if dif_flight > 0:
    dif_flight_str = str(dif_flight)
    test = '*This years accumulated flight days are ' + dif_flight_str + ' percent higher than last years accumulated flight days. Here is what that could mean for you: '

elif dif_flight < 0:
    dif_flight1 = str(dif_flight)
    dif_flight_str = dif_flight1.replace('-', ' ')

    test = '*This years accumulated flight days are' + dif_flight_str + ' percent lower than last years accumulated flight days. Here is what that could mean for you: '
else:
    test = '*This years accumulated flight days are the same as last years accumulated flight days. Here is what that could mean for you:'
x_index = np.arange(len(yr_list))

plt.style.use('seaborn-whitegrid')

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

#indx = np.arange(5)
width = 0.5
plt.gcf().text(0.12, 0.03, test, fontsize=10, wrap=True, style='italic')
# plt.text(min(yr_list), max(AHBCD_list) + 10, test, wrap=True, style='italic',
# fontsize=10, bbox={'facecolor': 'grey', 'alpha': 0.5, 'pad': 10})

ax1.plot(yr_list, AHBCD_list, marker='o', label=str(user_in + ' AHBCD'))
ax1.plot(yr_list, AHBFD_list, marker='o', label=str(user_in + ' AHBFD'))
ax1.legend()


ax1.set_xlabel('Year', fontsize=12)
# Labeling the Y-axis
ax1.set_ylabel('Accumulated Number of Days per Year', fontsize=12)
ax1.set_title('Accumulated Number of Flight and Cluster Days over 5 Years', fontsize=14)

ax1.set_xticks(np.arange(min(yr_list), max(yr_list) + 1, 1.0))


ax2.bar(x_index - width / 3.5, AHBCH_list, width=0.4, label=str(user_in + ' AHBCH'))
ax2.bar(x_index + width / 2, AHBFH_list, width=0.4, label=str(user_in + ' AHBFH'))
ax2.legend()


ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylim(0, max(AHBCH_list + AHBFH_list) + 500)
# Labeling the Y-axis
ax2.set_ylabel('Accumulated Number of Hours per Year', fontsize=12)
ax2.set_title('Accumulated Number of Flight and Cluster Hours over 5 Years', fontsize=14)

ax2.set_xticks(ticks=x_index)
ax2.set_xticklabels(yr_list)

#plot scale = 100, adjsut scale accordingly, change 1st chart to bar

#120 - 140 cluster days / 30 = 3 mo of winter, boone / 30 = 7 mo of clustering

#clear up labels to more human readable types
plt.show()

# plt.show()
# works
