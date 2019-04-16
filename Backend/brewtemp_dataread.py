############################
#This file reads the data written to the database, formats it and saves it to a json file rady to be picked up by the UI
############################

import mysql.connector
from datetime import datetime
import json
import db_config

mydb = mysql.connector.connect(
  host=db_config.login['host'],
  port=db_config.login['port'],
  user=db_config.login['user'],
  password=db_config.login['password'],
  database=db_config.login['database']
)

print(mydb)

mycursor = mydb.cursor()

#mycursor.execute("SELECT * FROM testtemplog")
mycursor.execute("SELECT ID, Time, Temperature FROM brewtemplog")

myresult = mycursor.fetchall()


#print(myresult)

Results = []

for x in myresult:
#  print(x)
  ID = x[0]

  Ti = x[1]
  Tim = str(Ti).lstrip('(').rstrip(')')
#  Datetime = datetime.strptime(Tim, "%Y %m %d %H %M %S")
  Datetime = Tim
  
  Time = Datetime[-8:] 
  Date = Datetime[0:10]


  T = x[2]
  Temp = str(T).lstrip(').rstrip(')
  Temperature = float(Temp)

  Row = {"ID":ID, "Date":Date, "Time":Time, "Temperature":Temperature} 
  Results.append(Row)

print(Results)

#writes json to file ready for js to pickup. Overwites whole file, not append.
with open('brewdata.json', 'w') as outfile:
  json.dump(Results, outfile, indent=4)


#NEEDED TO ORIGINALLY BREAKUP THIS FORMAT:
# (1, datetime.datetime(2018, 11, 5, 20, 40, 13), Decimal('21.25'))

