import json
import csv
import os
import pandas as pd
import requests

response_API = requests.get("https://bamatracker.com/api") # connects to the API
data = response_API.text #gets the data from the API
if(data):
    print("yee, data!")
json.loads(data) # parses the data into a JSON format


#data.to_csv('/Users/kt/Documents/JSON Project/CovidData.csv', encoding='utf-8', index=False)