// Analog input pin that the Velostat is connected to
const velostatPin = A0;
float sensorValue = 0;        

void setup() {
  Serial.begin(9600);
  digitalWrite(velostatPin, HIGH);
}

void loop() {
  sensorValue = analogRead(analogInPin);
  Serial.print("sensor = " );
  Serial.println(sensorValue);
}