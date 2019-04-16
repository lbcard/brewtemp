#include <SPI.h>


#include <Ethernet.h>
//#include <EthernetClient.h>
//#include <EthernetServer.h>
//#include <EthernetUdp.h>



#include <OneWire.h>
#include <DallasTemperature.h>

byte mac[] = {
  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED
};
IPAddress ip(192,168,0,44);
IPAddress gateway(192,168,0,1);
IPAddress subnet(255,255,255,0);

// Initialize the Ethernet server library
// with the IP address and port you want to use
// (port 80 is default for HTTP):
EthernetServer server(80);

 
// Data wire is plugged into pin 2 on the Arduino
#define ONE_WIRE_BUS 2
 
// Setup a oneWire instance to communicate with any OneWire devices 
// (not just Maxim/Dallas temperature ICs)
OneWire oneWire(ONE_WIRE_BUS);
 
// Pass our oneWire reference to Dallas Temperature.
DallasTemperature sensors(&oneWire);
 
void setup(void)
{
  //start ethernet
  Ethernet.begin(mac, ip, gateway, subnet);
  
  // start serial port
  Serial.begin(9600);

  // Start up the library
  sensors.begin();
  
  server.begin();
  Serial.print("server is at ");
  Serial.println(Ethernet.localIP());

}
 
 
void loop(void)
{

// listen for incoming clients
  EthernetClient client = server.available();
  if (client) {
    Serial.println("new client");
    // an http request ends with a blank line
    boolean currentLineIsBlank = true;
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        Serial.write(c);
        // if you've gotten to the end of the line (received a newline
        // character) and the line is blank, the http request has ended,
        // so you can send a reply
        if (c == '\n' && currentLineIsBlank) {
          // send a standard http response header
          client.println("HTTP/1.1 200 OK");
          client.println("Content-Type: text/html");
          client.println("Connection: close");  // the connection will be closed after completion of the response
          client.println("Refresh: 5");  // refresh the page automatically every 5 sec
          client.println();
//          client.println("<!DOCTYPE HTML>");
//          client.println("<html>");
          
          // output the value of each analog input pin
                // call sensors.requestTemperatures() to issue a global temperature
                // request to all devices on the bus
                sensors.requestTemperatures(); // Send the command to get temperatures
                
                Serial.println(sensors.getTempCByIndex(0)); // Why "byIndex"? 
                  // You can have more than one IC on the same bus. 
                  // 0 refers to the first IC on the wire
               
                float tempdata = sensors.getTempCByIndex(0) ; 
                //Serial.println(tempdata);  
                
//            client.print("tempdata ");
            client.print(tempdata);
//            client.println("<br />");
     
//          client.println("</html>");
          break;
        }
        if (c == '\n') {
          // you're starting a new line
          currentLineIsBlank = true;
        } else if (c != '\r') {
          // you've gotten a character on the current line
          currentLineIsBlank = false;
        }
      }
    }
    // give the web browser time to receive the data
    delay(1);
    // close the connection:
    client.stop();
    Serial.println("client disconnected");
  }


    
    delay(10000);

}

