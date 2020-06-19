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
import plotly
import plotly.graph_objects as go

loc_input = str(input("Enter your city: "))
yr_input = str(input("Enter the year you want to view: "))



file = loc_input + yr_input + '.csv'

path = os.path.join(r'C:\Users\MG\Desktop\cluster_final', file)

month_list = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

df = pd.read_csv(path)

monthly_sum_flight = df.groupby('month')['DHBFH'].sum().reindex(month_list, axis=0)

monthly_sum_cluster = df.groupby('month')['DHBCH'].sum().reindex(month_list, axis=0)

plt.style.use('seaborn-whitegrid')

fig, ax1 = plt.subplots(nrows=1, ncols=1)


ax1.plot(df['month'].unique(), monthly_sum_cluster, marker='o', label=str(loc_input + 'Monthly DHBCH'))
ax1.legend()

ax1.plot(df['month'].unique(), monthly_sum_flight, marker='o', label=str(loc_input + 'Monthly DHBFH'))
ax1.legend()


ax1.set_xlabel('Month', fontsize=12)
# Labeling the Y-axis
ax1.set_ylabel('Accumulated Hours per Month', fontsize=12)
ax1.set_title('Accumulated Daily Flight and Cluster Hours Per Month over ' + yr_input, fontsize=14)

plt.show()



### grab 1 location of each state - elevation data also associated - must be scaled

#different climates in different states


# NC Beekeepers association - reach out and see if they want to work with us, and if you still have those scales, we could use them to validate this - problem w scale data is that its gross weight, doesn't account for when people touch the hives, but if we could clean that and flag a time when the hive is touched. How many of htese events that we can detect statistically. Non-flight data could be used also. we're interested in the change of weight.

# pull capital from each county in NC, pull 5 yr, graph that has this year, and a graph that shows the historical average, and show if we are early or late. Take capital of each county. Compare day to day graph with historical graphs. Line graph - here's the average of the primary average to the previous years, are we early or are we late?

#if we can get scale data clean and used consistently over the years

#Lit says, do this based on when spring is this year

#color code each county and how it changes vs how it changes related to elevation ***

#plot elevation of different location, with accumulated flight and cluster hours

#took center of county and took nearest station, plot as heatmap, with FChours, per each county

#capital of county, airport usually would be near the capital, beekeeper would be familiar with the county and capital

#get location, then find closest airport, then plot

#do this^

#focused on nc, enter zip or city, here's the nearest weather staion, here's the data from this

#if we have 5 yrs of data in chart form, at least we could say that this is the affect of climate chnage on honeybee FChours

#climate change would need much more data in years

#do calc by each year, by month, take those sets of data, avg, we could come up with a long term avg when we see a certain cross over with FChours for given location, and then plot current year against this and see if we can see if it is early or late for this year

#study would be, 100 yrs, break down by decade, here's avg for 20's 30's etc, we could map those and see if there is stat difference between, and we can say if climate change is affecting it or not

#baby step list and then I take some and see which are most doable

#traking global warming from the bees perspective - hypothesis is that it will change over the decades for different parts of the state

#drill down by location and give differnet time increments

#but start with decade data

#north carolina first

#elevation for each reporting station, and then plot against sort data by increasing elevation, and FChour data point associated with each, see change in FH with increasing or CH with increasing elevation- 2 lines on chart, x = elevation, y axis = accum hours

#windy.com & darksky

#end prod viz = like windy.com or darksky or awad's link:
#https://en.wikipedia.org/wiki/K%C3%B6ppen_climate_classification

#climate change from bee weather over 100 years per decade - for NC

#group by decade, let's just look at it, visually, if it's different, then we want to prove statistically. Is each decade different from the preceding decade. Avg FH and CH for decade, for each year of decade, simple t test from each of the decades, we expect it to be different, one tail really, we have more flight hours every decade than in 1920/10, and few cluster hours each one

#f hours reducing to global warming it could mean more radical events / radical events. opposite is that the are going to have more flight hours because of rising temps

#climate change implications
#delete temp files after using them

#del command to manage resources

