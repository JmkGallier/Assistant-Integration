#include <TFT.h>
#include <SPI.h>

int IRpin = 1; //Infrared sensor pin
int MSpin = 0; //moisture sensor pin
char receivedChar;  //variable to store info from Rasp Pi
boolean newData = false;
//int greenLED = 13; if using Arudino for LED O/P
//int redLED = 12; 

void setup() {  
  Serial.begin(9600); // open serial port, set the baud rate as 9600 bps
  //pinMode(greenLED, OUTPUT); If choosing Ardunio for OP
  //pinMode(redLED, OUTPUT);
}

float GetMoisture() {
  float dry = (analogRead(MSpin));  // connect sensor to Analog 0
  float reading_min = 300;          // Minimum value of sensor
  dry = (dry-reading_min)/reading_min;      // Set dry to be a percentage of dryness
  float moist = 1.00 - dry;         // Moisture is the inverse of dryness
  return moist;
}

// Needs work
int GetDistance() {
  int i;
  int dist_val = 0;
  for (i = 0; i < 1; i++){
    dist_val = dist_val + analogRead(IRpin);    // sensor on analog pin 0
  }
  dist_val = dist_val / 5;
  return dist_val;
}

void loop() {
//  float moisture = GetMoisture();
  int distance = GetDistance();
//  Serial.print(moisture);
//  Serial.print(" ");
  Serial.println(distance);
  delay(1000);

  //recvInfo(); If Raspb Pi is triggering Arduino to turn on lights
  //lightLED();  
}




//this was for Arduino connecting to LEDs
//void recvInfo() {

  //if (Serial.available() > 0) {

    //receivedChar = Serial.read();
    //newData = true;
    
  //}
  
//}

//void lightLED() {

  //int led = (receivedChar - '0');

  //while(newData == true) {
    
    //digitalWrite(led, HIGH);
    //delay(1000);
    //digitalWrite(led, LOW);
    //delay(1000);
    //digitalWrite(led, HIGH);
    //delay(1000);
    //digitalWrite(led, LOW);
    //delay(1000);

    //newData = false;
  //}
  
  
//}
