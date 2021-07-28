# Listener: read char from USB Serial
import serial
from cobs import cobs
import time

ser = serial.Serial('/dev/ttyUSB0', baudrate= 57600, timeout=0.5)


read_buf = [None]*256
read_buf_pos = 0

encoded = cobs.encode(bytes([255,9]));
print("sending: ", encoded)
ser.write(encoded);
time.sleep(2);


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
        else:
            # print("Received: ", c, " = int: ", c[0])
            pass
    
    except Exception as e:
        print("ERROR ", e)
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
            print("decoding failed: ", e)
            continue

        decoded_data = [d for d in decoded]
        print("Decoded Data: ", decoded_data)
        
    else:
        # still need to keep reading
        read_buf[read_buf_pos] = c
        read_buf_pos += 1

    if read_buf_pos > 255:
        print("read buf > 255")
        read_buf_pos = 0
        read_buf = [None]*256



    # try:
    #     ret = ser.read(10)
    #     print(ret, ", ", ret.hex())
    #     print(cobs.decode(ret))
    # except Exception as e:
    #     print(e)
