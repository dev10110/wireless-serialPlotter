#include <PacketSerial.h>
// set this to the hardware serial port you wish to use
#define RADIOSERIAL Serial1
#define MOTOR1 Serial2
#define MOTOR2 Serial5
#define MOTOR3 Serial4
#define MOTOR4 Serial3

static const bool DEBUG = false;


PacketSerial myPacketSerial;

// for every received data packet, we will publish the data.

const int LED = 13;

static const uint8_t dataLen = 6; // when publishing, it will prepend the motor ID
static const uint8_t STARTCHAR = 255;

// actual data packets to be sent
uint8_t motor1Packet[dataLen+1];
uint8_t motor2Packet[dataLen+1];
uint8_t motor3Packet[dataLen+1];
uint8_t motor4Packet[dataLen+1];

// position indicators
uint8_t bufferPos1 = 0;
uint8_t bufferPos2 = 0;
uint8_t bufferPos3 = 0;
uint8_t bufferPos4 = 0;


void blink(float on, float off){
  digitalWrite(LED, HIGH);
  delay(on);
  digitalWrite(LED, LOW);
  delay(off);
}

//
void onRadioPacketReceived(const uint8_t* buffer, size_t size){
  Serial.print("Recieved packet of size: ");
  Serial.println(size);
}

void printBuffer1(){
  // only print if not in debug mode.
  if (!DEBUG){ return;}
  
  Serial.print("Motor 1 Buffer: ");
  for (uint8_t i=1; i < dataLen+1; i++){
    Serial.print(motor1Packet[i]);
    Serial.print(" ");
  }
  Serial.println();
  
}

void printBuffer2(){
  // only print if not in debug mode.
  if (!DEBUG){ return;}
  
  Serial.print("Motor 2 Buffer: ");
  for (uint8_t i=1; i < dataLen+1; i++){
    Serial.print(motor2Packet[i]);
    Serial.print(" ");
  }
  Serial.println();
  
}
void printBuffer3(){
  // only print if not in debug mode.
  if (!DEBUG){ return;}
  
  Serial.print("Motor 3 Buffer: ");
  for (uint8_t i=1; i < dataLen+1; i++){
    Serial.print(motor3Packet[i]);
    Serial.print(" ");
  }
  Serial.println();
  
}
void printBuffer4(){
  // only print if not in debug mode.
  if (!DEBUG){ return;}
  
  Serial.print("Motor 4 Buffer: ");
  for (uint8_t i=1; i < dataLen+1; i++){
    Serial.print(motor4Packet[i]);
    Serial.print(" ");
  }
  Serial.println();
  
}

void parseData1(){
  int availBytes = MOTOR1.available();
  if (availBytes > 0){

    for (uint8_t i=0; i < availBytes; i++){
      
        uint8_t incomingByte = MOTOR1.read();
        
        if (incomingByte== STARTCHAR){
          bufferPos1 = 0;
          continue;
        }
        motor1Packet[bufferPos1+1] = incomingByte;
        bufferPos1 = (bufferPos1 + 1) % (dataLen+1);
    }

    
    myPacketSerial.send(motor1Packet, dataLen + 1);
    blink(10, 0);
    printBuffer1();
  }
}

void parseData2(){
  int availBytes = MOTOR2.available();
  if (availBytes > 0){

    for (uint8_t i=0; i < availBytes; i++){
      
        uint8_t incomingByte = MOTOR2.read();
        
        if (incomingByte== STARTCHAR){
          bufferPos2 = 0;
          continue;
        }
        motor2Packet[bufferPos2+1] = incomingByte;
        bufferPos2 = (bufferPos2 + 1) % (dataLen+1);
    }

    
    myPacketSerial.send(motor2Packet, dataLen + 1);
    blink(10, 0);
    printBuffer2();
  }
}


void parseData3(){
  int availBytes = MOTOR3.available();
  if (availBytes > 0){

    for (uint8_t i=0; i < availBytes; i++){
      
        uint8_t incomingByte = MOTOR3.read();
        
        if (incomingByte== STARTCHAR){
          bufferPos3 = 0;
          continue;
        }
        motor3Packet[bufferPos3+1] = incomingByte;
        bufferPos3 = (bufferPos3 + 1) % (dataLen+1);
    }

    
    myPacketSerial.send(motor3Packet, dataLen + 1);
    blink(10, 0);
    printBuffer3();
  }
}


void parseData4(){
  int availBytes = MOTOR4.available();
  if (availBytes > 0){

    for (uint8_t i=0; i < availBytes; i++){
      
        uint8_t incomingByte = MOTOR4.read();
        
        if (incomingByte== STARTCHAR){
          bufferPos4 = 0;
          continue;
        }
        motor4Packet[bufferPos4+1] = incomingByte;
        bufferPos4 = (bufferPos4 + 1) % (dataLen+1);
    }

    
    myPacketSerial.send(motor4Packet, dataLen + 1);
    blink(10, 0);
    printBuffer4();
  }
}

void testSendData(){
  for (uint8_t i=1; i<dataLen+1; i++){
    motor1Packet[i] = i;
    motor2Packet[i] = i;
    motor3Packet[i] = i;
    motor4Packet[i] = i;
  }
  myPacketSerial.send(motor1Packet, dataLen + 1);
  blink(10, 0);
  myPacketSerial.send(motor2Packet, dataLen + 1);
  blink(10, 0);
  myPacketSerial.send(motor3Packet, dataLen + 1);
  blink(10, 0);
  myPacketSerial.send(motor4Packet, dataLen + 1);
  blink(10, 0);
  
  
}

void setup() {
  // put your setup code here, to run once:

  pinMode(LED, OUTPUT);

  blink(100,900);
  
  Serial.begin(57600);
  Serial.println("STARTING");
  MOTOR4.begin(19200);

  // initialize the radio
  RADIOSERIAL.begin(57600);
  myPacketSerial.setStream(&RADIOSERIAL);
  myPacketSerial.setPacketHandler(&onRadioPacketReceived);

  blink(100, 100);
  blink(100, 100);
  blink(100, 100);
  blink(100, 100);

  // assign the motor ID
  motor1Packet[0] = 1;
  motor2Packet[0] = 2;
  motor3Packet[0] = 3;
  motor4Packet[0] = 4;
}

void loop() {
  // put your main code here, to run repeatedly:
  myPacketSerial.update();

  parseData1();
  parseData2();
  parseData3();
  parseData4();


//  // for testing send data:
//  testSendData();
//  delay(500);
  

}
