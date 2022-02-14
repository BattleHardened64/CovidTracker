import os
import csv
import pandas as pd
import dateutil
import string
import urllib
#######################################################################
# Eli Williams
# This file is for organizing data in the CSV file for the covid map.
# Last Edited: 2 - 14 - 2022
#######################################################################







# Eli Williams
# readCSV, this function pulls the file from the github. 
# This needs to be called daily to pull the latest file from the github.
# Last Edited: 2/14/22
def readCSV(date):
    date += '.csv'
    url = "https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports"
    filename, headers = urllib.request.urlretrieve(url, filename = "https://github.com/BattleHardened64/CovidTracker/tree/CovidMap")


