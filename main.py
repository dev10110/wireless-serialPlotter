"""
Reads data from a serial port and plots it using the dashboard I made.

## Usage:

    python3 -i main.py --port PORT

and the PORT must be the address of the serial port to read. 

Example:

    python3 -i main.py --port /dev/ttyUSB0

the `-i` puts python into interactive mode, so the plots can be seen.

"""


import serial
import argparse
from cobs import cobs
import time
import signal

# import PySide2
import pyqtgraph as pg
import numpy as np
from dashboard import Dashboard


startTime = time.time();


read_buf = [None]*256
read_buf_pos = 0


# test function to send some bytes
# returns number of bytes written
def testSend(ser):
    encoded = cobs.encode(bytes([255,255]));
    print("sending: ", encoded)
    return ser.write(encoded);


# def mainReadLoop(ser, dash):

def motorMap(num):
    if num == 1:
        return "DL"
    if num == 2:
        return "DR"
    if num == 3: 
        return "WL"
    if num == 4:
        return "WR"


def insertData(dash, data):
   
    if len(data) != 7:
        print("Data is of wrong length - ignoring")
        return

    t = time.time() - startTime
    motor_id = motorMap(data[0])
    dash.insertMotorData(motor_id, t, data[1],data[2],data[3],data[4],data[5],data[6])




if __name__ == "__main__":

    # make Control C the key to press to exit and kill all windows
    signal.signal(signal.SIGINT, signal.SIG_DFL)


    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=str, default='/dev/ttyUSB0', help="Specify the port to use. To find all available ports run `python -m serial.tools.list_ports`")
    args = parser.parse_args()

    print("Selecting USB port: " + args.port)

    # open the serial port
    ser = serial.Serial(args.port, baudrate= 57600, timeout=0.5)

    # test sending data
    n = testSend(ser)
    if n == 0:
        print("Could not send data!")
        exit()

    print(f"Successfully sent {n} bytes of data")


    # Create the dashboard
    dash = Dashboard()

    # dash.test_getData()
    # dash.update()

    # timer = pg.Qt.QtCore.QTimer()
    # timer.timeout.connect(dash.testUpdate)
    # timer.start(0) 

    # start the main plotting loop
    while True: 

        try:
            # print("In Waiting: ", ser.in_waiting)
            if ser.in_waiting == 0:
            # print("no data to read..")
            # time.sleep(0.01)
                continue;
            c = ser.read(1)
            if not c:
                print("no data to read..")
                continue
            # else:
            #     # print("Received: ", c, " = int: ", c[0])
            #     pass
        
        except Exception as e:
            print("Read Error: ", e)
            continue
        
        if c[0] == 0:
            # message end received
            # print("decoding")
            # grab all the data
            data = [s[0] for s in read_buf[0:read_buf_pos]]
            
            #reset buffer
            read_buf = [None]*256
            read_buf_pos = 0

            # print("BUFFER DATA: ", data)

            try:
                decoded = cobs.decode(bytes(data))
            except Exception as e:
                print("Decoding failed: ", e)
                continue

            decoded_data = [d for d in decoded]

            # print("Decoded Data: ", decoded_data)

            insertData(dash, decoded_data)
            dash.update()
            
        else:
            # still need to keep reading
            read_buf[read_buf_pos] = c
            read_buf_pos += 1

        if read_buf_pos > 255:
            print("read buf > 255")
            read_buf_pos = 0
            read_buf = [None]*256






