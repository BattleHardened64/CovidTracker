

import os
import csv
import pandas as pd
import requests
import dateutil
from datetime import timedelta, date
from contextlib import closing
from codecs import iterdecode

def pullCovidData():
    {
#Source: https://github.com/CSSEGISandData/COVID-19

#go through each date sequentially from start to end date
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)



#YYYY MM DD
#hard code start date that data began being recorded. date(2020, 1, 22)
start_date = date(2020, 1, 22) #date(2022, 2, 2) #temporary date for testing
end_date = date.today()

#loop through every date until we get to todays date
for single_date in daterange(start_date, end_date):
    datestr=single_date.strftime("%m-%d-%Y")
    #This is the url to pull data from the github
    url = r'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'+datestr+'.csv' 
    
    #Here is where you would store the data to sql
    print(url)
    
    #downloads data as csv
    with open(os.path.split(url)[1], 'wb') as f, \
            requests.get(url, stream=True) as r:
        for line in r.iter_lines():
            f.write(line+'\n'.encode())
    """ 
    #use this code if you want csv in variable
    with requests.get(url, stream=True) as r:
        lines = (line.decode('utf-8') for line in r.iter_lines())
        for row in csv.reader(lines):
            print(row)
    """
    }

