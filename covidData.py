import json
#import csv
#import os
import pandas as pd
import requests

# Source: https://www.askpython.com/python/examples/pull-data-from-an-api

website = requests.get("https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/01-01-2022.csv") # connects to the API
data = website.content #gets the data from the API
#if(data):
#    print("yee, data!")

dataframe1 = pd.read_csv(data)
#print(type(data))
dataframe1.to_csv('/Users/djtol/Downloads/CovidData.csv', encoding='utf-8', index=False)
