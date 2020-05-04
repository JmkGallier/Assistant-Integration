int IRpin = 1; //Infrared sensor pin
int MSpin = 0; //moisture sensor pin
char receivedChar;  //variable to store info from Rasp Pi
boolean newData = false;

//If Arduino is used for LED output
//int greenLED = 13;
//int redLED = 12; 

void setup() {  
  Serial.begin(9600); // open serial port, set the baud rate as 9600 bps
  // If arduino is used for LED output
  //pinMode(greenLED, OUTPUT);
  //pinMode(redLED, OUTPUT);
}

float GetMoisture() {
  float dry = (analogRead(MSpin));  // connect sensor to Analog 0
  float reading_min = 300;          // Minimum value of sensor
  dry = (dry-reading_min)/reading_min;      // Set dry to be a percentage of dryness
  float moist = 1.00 - dry;         // Moisture is the inverse of dryness
  return moist;
}

int GetDistance() {
  int dist_val = 0;
  float IR_Reading = 0;
  int sensor_count = 25;
  for (int i = 0; i < sensor_count; i++){
    IR_Reading = IR_Reading + analogRead(IRpin);
    delay(50);
  }
  IR_Reading = IR_Reading / sensor_count;
  IR_Reading = IR_Reading - 36;
  if (IR_Reading < 160) {
    dist_val = 0;
  } else {
    dist_val = 1;
  }
  return dist_val;
}

void loop() {
  float moisture = GetMoisture();
  int distance = GetDistance();
  Serial.print(moisture);
  Serial.print(" ");
  Serial.println(distance);
  delay(1000);

  //recvInfo(); // If arduino is used for LED output
  //lightLED(); // If arduino is used for LED output
}

// // If arduino is used for LED output
//void recvInfo() {

  //if (Serial.available() > 0) {
    //receivedChar = Serial.read();
    //newData = true;
  //}
//}

// If arduino is used for LED output
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