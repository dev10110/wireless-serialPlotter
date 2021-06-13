#include <PacketSerial.h>
// set this to the hardware serial port you wish to use
#define HWSERIAL Serial1

PacketSerial myPacketSerial;

int data = 0;

void onPacketReceived(const uint8_t* buffer, size_t size){
  Serial.print("Recieved packet of size: ");
  Serial.println(size);
}


void setup() {
  // put your setup code here, to run once:
  Serial.begin(57600);
  HWSERIAL.begin(57600);
  myPacketSerial.setStream(&HWSERIAL);
  myPacketSerial.setPacketHandler(&onPacketReceived);
}

void loop() {
  // put your main code here, to run repeatedly:
  myPacketSerial.update();
//  Serial.println(".");

uint8_t myPacket[4] = { 255, (uint8_t)data , 0, 1};

data = data + 1;
if(data == 256){
  data = 0;
}

myPacketSerial.send(myPacket, 4);
Serial.print("Sending: ");
Serial.println(data);

delay(1000);

}
