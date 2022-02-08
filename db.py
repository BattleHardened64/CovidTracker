import mysql.connector
import csv
import pandas as pd
##############################################################
#Eli Williams
#Database File
#Last worked on by E. Williams
#2/7/22
#ODBC drivers will need to be downloaded.
#This file needs to be run everytime the server goes online.
##############################################################

#-------------------------------#
#Eli Williams
#Database Initialization
#Last Worked on by E. Williams
#2/3/2022
#-------------------------------#
mydb = mysql.connector.connect(
    host="localhost",
    user="sampleuser",
    password="samplepassword"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)


#---------------------------------#
#Eli Williams
#Creating Tables for the Database
#Last Worked on by E. Williams
#2/3/2022
#---------------------------------#
#Further Comments: Does this code run on the creation of the instance of the website? 
#or does this run once something has been clicked? 
#
#Currently there are 3 tables, Country, State, County
mycursor.execute("CREATE TABLE Country (Cases INT, Deaths INT, Recovered INT, Fatality Rate DOUBLE, Recovery Rate, DOUBLE)")
mycursor.execute("CREATE TABLE State (Cases INT, Deaths INT, Recovered INT, Fatality Rate DOUBLE, Recovery Rate, DOUBLE)")
mycursor.execute("CREATE TABLE County (Cases INT, Deaths INT, Recovered INT, Fatality Rate DOUBLE, Recovery Rate, DOUBLE)")


#---------------------------------#
#Eli Williams
#Data Parsing before database input
#Last Worked on by E. Williams
#2/7/2022
#---------------------------------#
def data_parser():
    #pull data from csv file. keyword usecols(pandas) only reads explicitly named columns, all others are ignored.
    data = pd.read_csv("data.csv", usecols = 'Admin2' 'Province_State' 'Country_Region' 'Lat' 'Long_' 'Confirmed' 'Deaths' 'Recovered' 'Active' 'Incident_Rate' 'Case_Fatality_Ratio')
    #admin2 is county, province_state is state, country is country
    #if admin2 and province state are null, we are looking at the country
    #if province_state has a value, we are looking at a state within a country.
    #if admin2 is filled we are looking at a county within a state/province
    #State data must be calculated using the county data
    #country data must be calculated using the state data.
    #insert into database.
    sql_insert = "INSERT INTO "
