int IRpin = 1; //Infrared sensor pin
int MSpin = 0; //moisture sensor pin
// int greenLED = 13; if using Arudino for LED O/P
// int redLED = 12; 

char receivedChar;  //variable to store info from Rasp Pi
boolean newData = false; 

void setup() {
  
  Serial.begin(9600); // open serial port, set the baud rate as 9600 bps

  //pinMode(greenLED, OUTPUT); If choosing Ardunio for OP
 // pinMode(redLED, OUTPUT);
  
}

void loop() {

  float distance = (analogRead(IRpin)-40.0)/500;  
  float moist_range = 288; //custom value based on readings
  float dry_val = (analogRead(MSpin)-295)/moist_range; //connect sensor to Analog 0
  float moist_val = 1.00 - dry_val;
 
  // 
  Serial.print(moist_val);
  Serial.print(" ");
  Serial.println(distance);//print the value to serial port
  delay(1200); //to delay the looping again

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