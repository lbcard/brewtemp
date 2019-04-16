
The Arduino sketch just reads the temperature from the temperature sensor library (DS18b20) and serves it up on a basic web page.

Just replace the IP addresses to whatever you need them to be & match up the sensor pins on the Arduino.

The delay is set to every 10 seconds but in reality it seemed to take about 20 to update (looking at time differences between database entries).