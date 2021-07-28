// this file is for the leaf teensys which will be sending test data

#define HWSERIAL Serial1

//static const bool DEBUG = false;

#define DEBUG

int counter = 0;

const int LED = 13;
const uint8_t STARTCHAR = 255;

void blink(float on, float off){
  digitalWrite(LED, HIGH);
  delay(on);
  digitalWrite(LED, LOW);
  delay(off);
}

void setup() {
  // put your setup code here, to run once:

  pinMode(LED, OUTPUT);
  Serial.begin(57600);
  HWSERIAL.begin(19200);

  blink(50, 150);
  blink(50, 150);
  blink(50, 150);

  Serial.println("READY TO SEND DATA");
  
}

void loop() {

  // data format:
    // 1. STARTCHAR
    // 2. RPM
    // 3. RPM_COMMAND
    // 4. CURRENT
    // 5. CURRENT_COMMAND
    // 6. VOLTAGE
    // 7. TEMPERATURE

  uint8_t data[7] = {STARTCHAR, counter, counter/2, 4, 5, 6, 7};

  counter = counter + 1;
  if (counter == 255){
    counter = 0;
  }

  HWSERIAL.write(data, 7);

//  if (DEBUG){
    #ifdef DEBUG

    Serial.print("SENDING ");
    for (int i=0; i<7; i++){
      Serial.print(data[i]);
      Serial.print(" ");
    }
    Serial.println(";");
//  }

  #endif

  blink(10, 50); //has been tested down to blink(10, 3);

}
