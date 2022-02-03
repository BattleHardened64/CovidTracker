import mysql.connector

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

#ODBC drivers will need to be downloaded 

#---------------------------------#
#Eli Williams
#Creating Tables for the Database
#Last Worked on by E. Williams
#2/3/2022
#---------------------------------#

