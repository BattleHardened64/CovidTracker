import os
import csv
import pandas as pd
import dateutil
import requests
import string
import urllib
import datetime
#######################################################################
# Eli Williams
# This file is for organizing data in the CSV file for the covid map.
# Last Edited: 2 - 18 - 2022
#######################################################################

# Eli Williams
# This function pulls in all past data files from the github repository and saves them into the CovidTracker github
# This function needs to be called once upon initialization
# Last Edited: 2/16/22
def readPreviousCSVs():
    url = "https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports"
    date = "01-22-2020"
    date_temp = datetime.datetime.strptime(date, "%m-%d-%y")
    for i in range (1, 755):  #all the days between 1/22/20 and 2/16/22
        new_date = date_temp + datetime.timedelta(days=1)
        #filename = new_date + ".csv" # This line might break; not sure if dates can be treated as strings.
        filename, headers = urllib.urlretrieve(url, filename = "https://github.com/BattleHardened64/CovidTracker/tree/CovidMap/mapData") #ADD TO GITHUB (WE NEED A FILE)
        filename += date_temp + ".csv"  # This line may break? Unsure.  Need to write a test.
        parseFile(filename)




# Eli Williams
# readCSV, this function pulls the file from the github. 
# This needs to be called daily to pull the latest file from the github.
# Last Edited: 2/17/22
def readCSV(date):
    date += '.csv'
    url = "https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports"
    #We need to add a file to the github for all old files...
    filename, headers = urllib.urlretrieve(url, filename = "https://github.com/BattleHardened64/CovidTracker/tree/CovidMap/mapData")
    parseFile(filename)




# Eli Williams
# parseFile, this function organizes data from . 
# This needs to be called multiple times to organize the csv files.
# This code is modified from https://stackoverflow.com/questions/16306819/python-edit-csv-headers
# Last Edited: 2/18/22
def parseFile(File):
    outputFileName = "https://github.com/BattleHardened64/CovidTracker/tree/CovidMap/mapData" + File + ".csv"  # NEED TO CREATE A FOLDER IN GITHUB FOR THESE FILES.
    with open(File, newline='') as inFile, open(outputFileName, 'w', newline='') as outfile:
         r = csv.reader(inFile)
    w = csv.writer(outfile)

    next(r, None)  # skip the first row from the reader, the old header
    # write new header
    w.writerow(['FIPS', 'County', 'State/Province', 'Country/Region','Last Updated', 'Latitude', 'Longitude', 'Confirmed Cases', 'Deaths', 'Recovered', 'Active Cases', 'Location', 'Incident Rate', 'Fatality Rate'])

    # copy the rest
    for row in r:
        w.writerow(row)


# Eli Williams
# pullData, this function pulls all the previous files from the github. 
# This needs to be called once.
# Last Edited: 2/14/22
def pullData():
    stuff = ""
