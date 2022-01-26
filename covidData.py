import json
#import csv
#import os
import pandas as pd
import requests

# Source: https://www.askpython.com/python/examples/pull-data-from-an-api

response_API = requests.get("https://bamatracker.com/api") # connects to the API
data = response_API.text #gets the data from the API
if(data):
    print("yee, data!")
json.loads(data) # parses the data into a JSON format
# needs to add code to store the json somewhere

#data.to_csv('/Users/kt/Documents/JSON Project/CovidData.csv', encoding='utf-8', index=False)