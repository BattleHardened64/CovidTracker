import pandas as pd
import requests
import dateutil
from datetime import timedelta, date


#go through each date sequentially from start to end date
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)



#YYYY MM DD
#todo: set real date
start_date = date(2020, 1, 1)
end_date = date.today()

#loop through every date until we get to todays date
for single_date in daterange(start_date, end_date):
    datestr=single_date.strftime("%m-%d-%Y")
    #This is the url to pull data from the github
    url = r'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'+datestr+'.csv' 
    #Here is where you would store the data to sql
    print(url)



