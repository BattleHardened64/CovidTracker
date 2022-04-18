import sys
import logging
import pymysql
import csv
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


