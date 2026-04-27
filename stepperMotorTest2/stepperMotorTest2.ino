#define STEP_PIN 9   // connected to PUL-
#define DIR_PIN 8    // connected to DIR-
#define ENA_PIN 7    // connected to ENA- (optional)

void setup() {
  pinMode(STEP_PIN, OUTPUT);
  pinMode(DIR_PIN, OUTPUT);
  pinMode(ENA_PIN, OUTPUT);

  // Enable driver (LOW usually = enabled in common-anode)
  digitalWrite(ENA_PIN, HIGH);
}

void loop() {
  // Reverse direction
  digitalWrite(DIR_PIN, LOW);

  for (int i = 0; i < 1600; i++) {
    digitalWrite(STEP_PIN, LOW);
    delayMicroseconds(500);

    digitalWrite(STEP_PIN, HIGH);
    delayMicroseconds(500);
  }

  delay(1000);
}