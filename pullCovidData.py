import os
import csv
import requests
from datetime import timedelta, date
from contextlib import closing
import json



def pullCovidData_old():
        #Source: https://github.com/CSSEGISandData/COVID-19

        #go through each date sequentially from start to end date
        def daterange(start_date, end_date):
            for n in range(int ((end_date - start_date).days)):
                yield start_date + timedelta(n)


        #Code for testing date ranges:
        #print("Enter the date you wish to start at in the following format: YYYY MM DD")
        #date = input()
        #start_date_y = int(date[0:4])
        #start_date_m = int(date[5:8])
        #start_date_d = int(date[8:10])

        #date = (start_date_y, start_date_m, start_date_d)
        

        #YYYY MM DD
        #hard code start date that data began being recorded. date(2020, 1, 22)
        start_date = date(2022, 2, 13) #date(2022, 2, 2) #temporary date for testing
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
   

def pullCovidData():
    
    fileName = "covid-data.json"

    url_date = input("Enter the date in the following format: YYYY-MM-DD\n")

    url = ("https://api.covid19tracking.narrativa.com/api/"+url_date)
    myfile = requests.get(url)
    
    text = myfile.text

    data = json.loads(text)

    #key = data['dates']
    #key2 = key[url_date]
    #key3 = key2['countries']
    #key4 = key3['Poland']
    #print(key4['today_new_open_cases'])

    date = url_date
    key = data['total']
    today_confirmed = key['today_confirmed']
    today_deaths = key['today_deaths']
    today_new_confirmed = key['today_new_confirmed']
    today_new_deaths = key['today_new_deaths']
    today_new_open_cases = key['today_new_open_cases']
    today_new_recovered = key['today_new_recovered']
    today_open_cases = key['today_open_cases']
    today_recovered = key['today_recovered']
    yesterday_confirmed = key['yesterday_confirmed']
    yesterday_deaths = key['yesterday_deaths']
    yesterday_open_cases = key['yesterday_open_cases']
    yesterday_recovered = key['yesterday_recovered']

    diff_open = ( today_open_cases - yesterday_open_cases)


    today_confirmed = str(today_confirmed)
    today_deaths =str(today_deaths)
    today_new_confirmed = str(today_new_confirmed)
    today_new_deaths = str(today_new_deaths)
    today_new_open_cases =str(today_new_open_cases)
    today_new_recovered = str(today_new_recovered)
    today_open_cases = str(today_open_cases)
    today_recovered = str(today_recovered)
    yesterday_confirmed = str(yesterday_confirmed)
    yesterday_deaths =str(yesterday_deaths)
    yesterday_open_cases =str(yesterday_open_cases)
    yesterday_recovered =str(yesterday_recovered)

   

    print("Today's World Total Information:\n")
    print("Date: " + url_date +'\n')
    print("Total Confirmed Cases:"+ today_confirmed +'\n')
    print("Today's New Confirmmed Cases: "+today_new_confirmed+'\n')
    print("Total Deaths: "+today_deaths+'\n')
    print("Today's Death Count: "+today_new_deaths+'\n')
    print("Total Current Cases: "+today_open_cases+'\n')
    print("Today's Current Cases: "+today_new_open_cases+'\n')
    print("Total Recovered Cases: "+today_recovered+'\n')
    print("Today's Recovered Cases: "+today_new_recovered+'\n')
    print("\Yesterady's Data\n\n")

    print("Yesterday's Confirmed Cases: "+yesterday_confirmed+'\n')
    print("Yesterday's Deaths: "+yesterday_deaths+'\n')
    print("Yesterday's Open Cases: "+yesterday_open_cases+'\n')
    print("Yesterday's Recovered Cases: "+yesterday_recovered+'\n')
    
    print("\nAnalysis:\n\n")
    
    if(diff_open < 0):
        diff_open = diff_open * -1
        diff_open = str(diff_open)
        print("There has been a net gain of " + diff_open + " cases\n")


    else:
        diff_open = str(diff_open)
        print("There has been a net decrease of " + diff_open + " cases\n")

    '''file = open(fileName, "w")
    json.dump(data,file)
    file.close()'''
   
    
    



pullCovidData()