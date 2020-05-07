#include <stdio.h>
#include <stdlib.h>

int IRpin = 1; //Infrared sensor pin
int MSpin = 0; //moisture sensor pin
int receivedChar;  //variable to store info from Rasp Pi
boolean newData = false;

void setup() {  
  Serial.begin(9600);
}

// Check Incoming Serial Data
void recvInfo() {
  while (Serial.available() > 0) {
    receivedChar = Serial.read();
    newData = true;
  }
}

// Get Moisture Value
int GetMoisture() {
  float sensorRead = (analogRead(MSpin));
  float sensorWet = 274.00;
  float sensorDry = 325.00;
  sensorRead = (1.00-(sensorRead-sensorWet)/sensorDry)*100.00;
  int moist = sensorRead;
  return moist;
}

// Get IR Sensor Distance Value
int GetDistance() {
  float IR_read = 0;
  float IR_read_offset = -36;
  int sensor_count = 25;
  for (int i = 0; i < sensor_count; i++){
    IR_read = IR_read + analogRead(IRpin);
    delay(50);
  }
  IR_read = (IR_read / sensor_count) + IR_read_offset;
  if (IR_read < 160) {
    return 0;
  } else {
    return 1;
  }
}

// Send Serial data to RPi
void RPi_Serial(int a, int b) {
  if (newData == false) {
    Serial.print(a);
    Serial.print(" ");
    Serial.println(b);
  } 
//  else {
//    // HERE
//    if (a < receivedChar) {
//    }
//    newData = false;
//  }
}

void loop() {
  recvInfo();
  int moisture = GetMoisture();
  int distance = GetDistance();
  RPi_Serial(moisture, distance);
  //delay(500);
}
