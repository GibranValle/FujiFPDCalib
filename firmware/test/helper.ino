void relayInit() {
  // RELAY INIT
  pinMode(relayOn, OUTPUT);
  pinMode(relayOff, OUTPUT);
  digitalWrite(relayOn, LOW);
  digitalWrite(relayOff, LOW);
}

void startExposure() {
  digitalWrite(relayOn, HIGH);
  delay(100);
  digitalWrite(relayOn, LOW);
}

void endExposure() {
  digitalWrite(relayOff, HIGH);
  delay(100);
  digitalWrite(relayOff, LOW);
}

void performShortExposure() {
  TIMSK1 = !TIMSK1 & (1 << OCIE1A);  //disable timer
  countTime = 0;
  maxTime = MAX_TIME_SHORT;
  TIMSK1 |= (1 << OCIE1A);  //enable timer
  Serial.println("STARTING EXPOSURE");
  startExposure();
}

void performLongxposure() {
  TIMSK1 = !TIMSK1 & (1 << OCIE1A);  //disable timer
  countTime = 0;
  maxTime = MAX_TIME_LONG;
  TIMSK1 |= (1 << OCIE1A);  //enable timer
  Serial.println("STARTING LONG EXPOSURE");
  startExposure();
}
