# wireless-serialPlotter
I needed a method to send data from a teensy to a computer wirelessly, and plot it live. This is my solution.


## Overview

```
Teensy 4.0 publishes data on Serial1  
     ^
     |
  (wired serial comm at 57600 baud)
     |
     v
Wireless Telemetry Module 1
     ^
     |
  (wireless radio comm)
     |
     v
Wireless Telemetry Module 2
     ^
     |
  (usb connection)
     |
     v
Linux machine, running python script
```

## Details
 
The messages to be sent are encoded and decoded using COBS.
In the teensy, I used the package PacketSerial, (https://github.com/bakercp/PacketSerial)
In the ubuntu, the messages were received using a python script. The `pySerial` library (https://pyserial.readthedocs.io/en/latest/index.html) was used to read each byte, and then the messages were decoded using `cobs` (https://github.com/cmcqueen/cobs-python). 

A very useful reference was (https://github.com/igor47/spaceboard/blob/master/spaceteam/microcontroller.py)
 
The wireless communication happens at 915MHz, using commercial products like http://www.holybro.com/product/transceiver-telemetry-radio-v3-915mhz/
These essentially act as a wireless cable, replacing a physical wire with radio comms. As such, every byte sent from the teensy reaches the ubuntu. While it may be possible to change the baud rate, the default seems to 57600, and I wasnt bothered enough.

Note, while the radio module has 5V and GND connections, the RX TX signals operate at 3.3V. They can also draw a significant amount of current - supposedly 100mA (through the 5V line), but in a few experiments it seems to draw about 30-40mA when not sending too much data, and using the smaller antenna.

## Folder Org:  
each folder contains a pair of files - a file to be run on the teensy, and a file to be run in the ubuntu machine. Sometimes a readme might be available to describe whats happening.
