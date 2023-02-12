# import serial

# ser = serial.Serial('COM5', 9600, timeout=0.050)

# while 1:
#     while ser.in_waiting:
#         data_in = ser.readline()
#         print (data_in)

import serial
from time import sleep

ser = serial.Serial ("COM5", 9600)    #Open port with baud rate
while True:
    received_data = ser.read()              #read serial port
    sleep(0.03)
    data_left = ser.inWaiting()             #check for remaining byte
    received_data += ser.read(data_left)
    print (received_data)                   #print received data
    # ser.write(received_data)    