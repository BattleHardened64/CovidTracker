import sys
import logging
import requests
import shutil
import pymysql
import csv
from datetime import date
#rds settings

rds_host  = "coviddata.c0hduqczxapy.us-east-1.rds.amazonaws.com"
username = "admin"
password = "5^Qf6qW%&B5O5bz$"
db_name = "coviddata"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect( host='coviddata-1.c0hduqczxapy.us-east-1.rds.amazonaws.com', user='admin',password='5^Qf6qW%&B5O5bz$', port=3306, database="coviddata")
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")


today = str(date.today())
url_date = (today[5:10] + "-" + today[0:4])
print(url_date)

url = ("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"+url_date+".csv")

with requests.Session() as s:
    download = s.get(url)
    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    covid_data_list = list(cr)


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))
#ignore this line cause we dont really need it since the database already has column names
"""1048575"""
val = []
count = 0
with conn:
    with conn.cursor() as cursor:
        #for i in range(5921)
        for dater_chunk in chunker(covid_data_list,500):
            for line in my dater_chunk:
                if len(line) != 14:
                    raise NameError("u stoopid, line = {}".format(line))
                val.append(tuple(line))    
            sql = "INSERT INTO data (FIPS, County, State_Province, Country_Region, Last_Updated, Latitude, Longitude, Confirmed_Cases, Deaths, Recovered, Active_Cases, Location, Incident_Rate, Fatality_Rate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "
            cursor.executemany(sql,val)
            conn.commit()
            val = []
                
            count+=500
            print("\r>> You have finished {}".format(count/datalength), end='')

