
#################
#This file makes periodic GET requests (every 10 seconds) to the Arduino webpage to grab the current temperature, then writes it to the MySQL database. 
#################

import mysql.connector
import datetime

#imports for test data
import random
import decimal
import time

#requests library for http request
import requests as req

#currentdatetime = datetime.datetime.now()

#random temperature value for testing
#randomtesttemp = float(decimal.Decimal(random.randrange(800, 2800))/100)

import db_config

mydb = mysql.connector.connect(
  host=db_config.login['host'],
  port=db_config.login['port'],
  user=db_config.login['user'],
  password=db_config.login['password'],
  database=db_config.login['database']
)


def reqtempandwrite():
        currentdatetime = datetime.datetime.now()

        resp = req.request(method='GET', url="http://192.168.0.44")

        print(resp.text)

        respfloat = float(resp.text)
        print("respfloat= ")
        print(respfloat)

        mycursor = mydb.cursor()

#originally to testtemplog table
        sql = "INSERT INTO brewtemplog (Time, Temperature) VALUES (%s, %s)"
        val = (currentdatetime, respfloat)
        mycursor.execute(sql,val)

        mycursor = mydb.cursor()

#originally to testtemplog table
        sql = "INSERT INTO brewtemplog (Time, Temperature) VALUES (%s, %s)"
        val = (currentdatetime, respfloat)
        mycursor.execute(sql,val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.") 


#loop to write to db, set to 10000 times
#approx 55.5hrs for a reading every 20 secs for 10000
#possible row size estimated at 4+4+8 bytes + 4 contingency ~20bytes per row?
for x in range (100000):

        reqtempandwrite()

#       mycursor = mydb.cursor()

#       sql = "INSERT INTO testtemplog (Time, Temperature) VALUES (%s, %s)"
#       val = (currentdatetime, randomtesttemp)
#       mycursor.execute(sql,val)

#       mydb.commit()

#       print(mycursor.rowcount, "record inserted.") 

        #delay every 10 secs
        time.sleep(10) 