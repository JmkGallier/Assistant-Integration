const int velostatPin = A0;
float sensorValue = 0;

void setup() {
  Serial.begin(9600);
  digitalWrite(velostatPin, HIGH);
}

void loop() {
  sensorValue = analogRead(velostatPin);
  
  String sensorState = "Not Pressed";
  if (sensorValue < 60) {
    sensorState = "Pressed";
  } else if (sensorValue > 300) {
    sensorState = "Disconnected";
  }

  Serial.println(sensorState);
  delay(500);
}