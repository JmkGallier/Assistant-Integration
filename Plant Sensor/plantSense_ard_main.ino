int IRpin = 1; //Infrared sensor pin
int MSpin = 0; //moisture sensor pin
char receivedChar;  //variable to store info from Rasp Pi
boolean newData = false;
const unsigned int MAX_INPUT = 50;

void setup() {  
  Serial.begin(9600);
}

void process_data (const char * data) {
  Serial.println("hit process_data");
}

void processIncomingByte (const byte inByte) {
  static char input_line [MAX_INPUT];
  static unsigned int input_pos = 0;

  switch (inByte) {

    case '\n':
      input_line [input_pos] = 0;
      process_data (input_line);
      input_pos = 0;  
      break;

    case '\r':
      break;

    default:
      if (input_pos < (MAX_INPUT - 1))
        input_line [input_pos++] = inByte;
      break;
  }
}

// Serial check
void recvInfo() {
  while (Serial.available() > 0) {
    processIncomingByte(Serial.read());
//    receivedChar = Serial.read();
    newData = true;
  }
}

// Send sensor readings to RPi
void RPi_Serial(float a, int b) {
  if (newData == false) {
    Serial.print(a);
    Serial.print(" ");
    Serial.println(b);
  } else {
    int distance = GetDistance();
    newData = false;
    Serial.print(receivedChar, DEC);
    Serial.print(" ");
    Serial.println(distance);
  }
}

float GetMoisture() {
  float dry = (analogRead(MSpin));
  float reading_min = 300;
  dry = (dry-reading_min)/reading_min;
  float moist = 1.00 - dry;   
  return moist;
}

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

void loop() {
  recvInfo();
  float moisture = GetMoisture();
  int distance = GetDistance();
  RPi_Serial(moisture, distance);
  delay(500);
}
