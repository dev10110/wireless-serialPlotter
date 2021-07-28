#include <PacketSerial.h>
// set this to the hardware serial port you wish to use
#define RADIOSERIAL Serial1
#define MOTOR1 Serial2
#define MOTOR2 Serial5
#define MOTOR3 Serial4
#define MOTOR4 Serial3

static const bool DEBUG = true;


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

void parseData4(){
  //
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

void setup() {
  // put your setup code here, to run once:

  pinMode(LED, OUTPUT);

  blink(100,900);
  
  Serial.begin(57600);
  Serial.println("STARTING");
  MOTOR4.begin(19200);

//  blink(900,100);
//  blink(900,100);
//  blink(900,100);
//  blink(900,100);

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

  parseData4();

    

  

}
