// PINS
const int relayOn = 4; // D2
const int relayOff = 2; //D4
const int analogInPin = A2;  // Analog input pin that the potentiometer is attached to

// analog read
int sensorValue = 0;        // value read from the pot

// timer
const int MAX_TIME_SHORT = 15;
const int MAX_TIME_LONG = 500;
int maxTime = 0;
int countTime = 0;

// comunication
String inputString = "";         // a String to hold incoming data
boolean stringComplete = false;  // data arrived