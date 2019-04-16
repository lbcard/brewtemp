# Brewtemp Readme

This code is to monitor homebrew fermentation temperatures via an Arduino (using a .... temperature sensor), save to a MySQL database (in my case on a Raspberry Pi) and then visualise the temperatures on a graph over time.

At the moment due to time constraints, data extraction and prep for the UI is done manually (it isn't yet a stream) when you want to view it.

## Roadmap

- Finish the Graph
- Convert UI to ReactJS 
- Install ExpressJS & add APIs for stuff (data export/query)