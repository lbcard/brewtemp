# Brewtemp Readme

This code is to monitor homebrew fermentation temperatures via an Arduino (using a DS18B20 temperature sensor), save to a MySQL database (in my case on a Raspberry Pi) and then visualise the temperatures on a graph over time.

At the moment due to time constraints, data extraction and prep for the UI is done manually (it isn't yet a stream) when you want to view it.

## Key Files

ds18b20probe_eth.ino - Arduino Sketch

brewtemp_datawrite.py - leave running, makes GET requests to the Arduino to grab temperature & writes to the DB

brewtemp_dataread.py - Run to extract and format/process data from the MySQL DB to save in a json file for the UI to pickup and use.

index.html - UI, to be completed.


## Roadmap

- Finish the Graph UI
- Convert UI to ReactJS 
- Install ExpressJS & add APIs for stuff (data export/query)