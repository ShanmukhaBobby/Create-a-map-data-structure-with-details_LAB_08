// Arduino Code: Smart Car Kit -> Send Map Data to Raspberry Pi
#include <Arduino.h>

const int trigPin = A5;  // Trig on A4
const int echoPin = A4;  // Echo on A5

long duration;
int distance;

void setup() {
  Serial.begin(9600);      // Initialize serial communication with Raspberry Pi
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  // Send a 10µs pulse to trigger ultrasonic sensor
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Read the duration of echo
  duration = pulseIn(echoPin, HIGH);

  // Convert duration to distance in cm
  distance = duration * 0.034 / 2;

  // Send distance to Raspberry Pi as JSON-like string
  Serial.print("{\"distance\":");
  Serial.print(distance);
  Serial.println("}");

  delay(500);  // Wait before next reading
}
