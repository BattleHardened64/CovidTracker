import os
import csv
import pandas as pd
import requests
import dateutil
from datetime import timedelta, date
from contextlib import closing
from codecs import iterdecode

#Source: https://github.com/CSSEGISandData/COVID-19

#go through each date sequentially from start to end date
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)


#Code for testing date ranges:
#print("Enter the date you wish to start at in the following format: YYYY MM DD")
#date = input()
#start_date = int(date[0:4])
#start_date_m = int(date[5:8])
#start_date_d = int(date[8:10])

#Note: No exception catching implemented since we're just testing direct. 
#We can limit the range the users can put in through front end.


print(start_date, start_date_m, start_date_d)


#YYYY MM DD
#hard code start date that data began being recorded. date(2020, 1, 22)
start_date = date(2020, 1, 22) #date(2022, 2, 2) #temporary date for testing
end_date = date.today()

#loop through every date until we get to todays date
for single_date in daterange(start_date, end_date):
    datestr=single_date.strftime("%m-%d-%Y")
    #This is the url to pull data from the github
    url = r'https://api.covid19tracking.narrativa.com/api/2022-02-09'
    
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


