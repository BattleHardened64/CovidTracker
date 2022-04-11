import os
import csv
import requests
import datetime
import sqlite3




def pullCovidData():

    url_date = str(datetime.date.isoformat(datetime.date.today()))
    url_date = "04-10-2022"

    connection = sqlite3.connect("coviddata.db")
    cursor = connection.cursor()



    url = ("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"+url_date+".csv")

    with requests.Session() as s:
        download = s.get(url)

        decoded_content = download.content.decode('utf-8')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        for row in my_list:
            insert = ("""
            INSERT INTO coviddata (FIPS, County, State_Province, Country_Region, Last_updated, Latitude, Longitude, Confirmed_Cases, Deaths, Recovered, Active_Cases, Location, Incident_rate, Fatality_Rate)
            VALUES (%d, %s, %s, %s, %s, %f, %f, %d, %d, %d, %d, %s, %f , %f)""")

            cursor.execute(insert,row)
            
        connection.close()
                           
pullCovidData()


