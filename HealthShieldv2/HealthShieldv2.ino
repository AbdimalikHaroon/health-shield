/*
HealthSheild - IoT implementation to get the BPM reading from the patient
*/

#include <PulseSensorPlayground.h> // the PulseSensorPlayground library to create the pulseSensor object

// Project variables
const int sensorPin = A0;  // Signal pin connected to the analog pin A0
const int ledPin = 13;     // Digital pin 13 for the LED
int threshold = 550;       // Necessary to determine what input counts as a beat and that which to ignore
const int arraySize = 5;   // Size of the array for the readings
int sensorReadings[arraySize]; // Array to store the array readings
int readingSum = 0;        // Sum of the readings in the array
int validReadings = 0;     // Count of valid readings

PulseSensorPlayground pulseSensor;  // Creating an instance of the PulseSensorPlayground object "pulseSensor"

// Timing variables
unsigned long lastBeatTime = 0;
unsigned long readingInterval = 2000; // Interval between readings
unsigned long lastLoopTime = 0;
unsigned long loopDelay = 3000; // Delay before the next set of readings

void setup() {
  pinMode(ledPin, OUTPUT);  // Define the ledPin as an OUTPUT
  Serial.begin(115200);     // Baud rate for the serial monitor

  // PulseSensor variables and configurations
  pulseSensor.analogInput(sensorPin);
  pulseSensor.setThreshold(threshold);

  // Ensure the pulseSensor object is successfully created and is reading the expected data
  if (pulseSensor.begin()) {
    Serial.println("The PulseSensor object has successfully been created!!");
  } else {
    for (;;) { // LED blinks infinitely
      digitalWrite(ledPin, LOW);
      delay(50);
      digitalWrite(ledPin, HIGH);
      delay(50);
    }
  }

  lastLoopTime = millis();
}

void loop() {
  readingSum = 0; // Reset the sum at the beginning of each loop
  validReadings = 0; // Reset the count of valid readings

  while (validReadings < arraySize) {
    if (pulseSensor.sawStartOfBeat()) {  // Test whether a beat occurred and was recorded
      int BPM = pulseSensor.getBeatsPerMinute();  // Calculate the BPM and store the variable

      // Check if BPM value is within a valid range
      if (BPM > 40 && BPM < 100) {
        sensorReadings[validReadings] = BPM;  // Store the valid BPM value in the array
        Serial.println("Heartbeat Recorded!!");
        Serial.print("BPM: ");
        Serial.println(sensorReadings[validReadings]); // Print the BPM value
        readingSum += sensorReadings[validReadings];  // Get the sum of the readings
        validReadings++; // Increment the count of valid readings

        // Manually blink the LED
        digitalWrite(ledPin, HIGH);
        delay(1000);
        digitalWrite(ledPin, LOW);
      }
      lastBeatTime = millis();
    }

    // Use non-blocking delay to allow continuous checking for beats
    if (millis() - lastBeatTime >= readingInterval) {
      lastBeatTime = millis(); // Reset last beat time
    }
  }

  // Calculate and print the average BPM if there are valid readings
  if (validReadings > 0) {
    int averageBPM = readingSum / validReadings;
    Serial.print("The average BPM is: ");
    Serial.println(averageBPM);
  } else {
    Serial.println("No valid BPM readings.");
  }

  lastLoopTime = millis(); // Reset loop start time
  delay(loopDelay); // Add a delay before starting the next set of readings
}
