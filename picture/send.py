"""
Simple example of using the RF24 class.
"""
import spidev
from circuitpython_nrf24l01.rf24 import RF24
import time
import struct
import board
from digitalio import DigitalInOut, Direction
from picamera import PiCamera
import PIL
import os
import io
import glob
import digitalio
from threading import Thread
import secrets

led_mpl = digitalio.DigitalInOut(board.D7)
led_mpl.direction = digitalio.Direction.OUTPUT

led_UV = digitalio.DigitalInOut(board.D16)
led_UV.direction = digitalio.Direction.OUTPUT

led_gps = digitalio.DigitalInOut(board.D18)
led_gps.direction = digitalio.Direction.OUTPUT

led_Gy = digitalio.DigitalInOut(board.D26)
led_Gy.direction = digitalio.Direction.OUTPUT

led_Nrf = digitalio.DigitalInOut(board.D12)
led_Nrf.direction = digitalio.Direction.OUTPUT

led_Aht = digitalio.DigitalInOut(board.D25)
led_Aht.direction = digitalio.Direction.OUTPUT

start_timer = time.time()  # start timer

# make camera ready
"""camera = PiCamera()
camera.resolution = (1920,1080)
camera.start_preview()"""

# invalid default values for scoping
# invalid default values for scoping
SPI_BUS, CSN_PIN, CE_PIN = (None, None, None)

SPI_BUS = spidev.SpiDev()  # for a faster interface on linux
CSN_PIN = 0  # use CE0 on default bus (even faster than using any pin)
CE_PIN = DigitalInOut(board.D22)  # using pin gpio22 (BCM numbering)

# initialize the nRF24L01 on the spi bus object
nrf = RF24(SPI_BUS, CSN_PIN, CE_PIN)

nrf.pa_level = 0

# addresses needs to be in a buffer protocol object (bytearray)
address = [b"\xe1\xf0\xf0\xf0\xf0", b"\xd2\xf0\xf0\xf0\xf0"]

pipe1 = address[0]  # using pipe 1 for sensordatas
pipe2 = address[1]  # using pipe 2 for pic

# uncomment the following 3 lines for compatibility with TMRh20 library
nrf.allow_ask_no_ack = False
nrf.dynamic_payloads = True
nrf.data_rate = 250
nrf.channel = 22
nrf.arc = 6
nrf.auto_ack = True
nrf.listen = False

pic_time = -15
# using the python keyword global is bad practice. Instead we'll use a 1 item
# list to store our float number for the payloads sent


def master1():  # count = 5 will only transmit 5 packets
    """Transmits sensor data to master"""
    # set TX address of RX node into the TX pipe
    nrf.open_tx_pipe(pipe1)  # using pipe2 for sensordatas
    # use struct.pack to structure your data
    # into a usable payload
    print("sending data...")
    for item in payloader:

        encoded_string = [bytearray(x.encode()) for sets in item for x in sets]
        buffer = struct.pack(
            ''.join('s' for item in encoded_string), *encoded_string)

        # sending data
        result = nrf.send(buffer)
        end_timer = time.time()
        if not result:
            print("send{} failed or timed out".format(buffer))
        else:
            print(
                "Transmission successful! Time to Transmit:",
                "{} s. Sent: {}".format(round((end_timer - start_timer), 3), item))


def master2(pic_data):
    """Transmits pic data to master"""
    master1()
    compressed_file_name = ('/home/pi/Desktop/nrf/handv.jpg')
    im= open(compressed_file_name, 'rb')
    pic_data = im.read()
    nrf.open_tx_pipe(pipe2)  # using pipe 0 for pic
    print("sending Picture...")
    payloading = 32
    pic_start_timer = time.time()

    for item in range(int(len(pic_data)/payloading)+1):
        buffer = pic_data[(item*payloading): (item+1)*payloading]
        nrf.send(buffer)

        # if (item+1) % 200 == 0:
        #   master1()

    print('pic send time : ', pic_start_timer-time.time())
    time.sleep(3)


def make_data():

    global payloader

    global pic_data, pic_time

    while True:
        # data make to send
        send_time = ("%s_" % round(time.time() - start_timer, 1))
        locationX = "%sLx_36.31130898586006" % send_time
        locationY = "%sLy_59.526375931025" % send_time
        Acceleration = "%sA_{}*{}*{}".format(secrets.randbelow(
            5), secrets.randbelow(5), secrets.randbelow(5)) % send_time
        Angular_acceleration = "%sZ_{}*{}*{}".format(secrets.randbelow(
            5), secrets.randbelow(5), secrets.randbelow(5)) % send_time
        intemp = "%sTi_{}".format(secrets.randbelow(50)) % send_time
        outtemp = "%sTo_{}".format(secrets.randbelow(50)) % send_time
        humedity = "%sH_{}".format(secrets.randbelow(100)) % send_time
        hight = "%sL_{}".format(secrets.randbelow(300)) % send_time
        presure = "%sP_{}".format(900+secrets.randbelow(1000)) % send_time
        uv = "%sU_{}".format(secrets.randbelow(250)) % send_time

        payloader = [locationX, locationY, Acceleration, hight, presure,
                     Angular_acceleration, intemp, outtemp, humedity, uv]

        """
        # 1. take a shot
        sleep(1)
        file_name = ('/home/pi/Desktop/images/image%s.jpg' % i)
        camera.capture(file_name)
        # camera.stop_preview()
        
        #2. optmazition
        picture = Image.open('image.jpg')
        compressed_file_name = 'compressed' + file_name
        picture.save(compressed_file_name ,optimize=True , quality=30 )
        """
        compressed_file_name = ('/home/pi/Desktop/nrf/handv.jpg')

        # 3. encoding
        with open(compressed_file_name, 'rb') as im:
            pic_data1 = im.read()

        if time.time()-pic_time >= 15:
            pic_time = time.time()
            pic_data = pic_data1

    return payloader, pic_data

    time.sleep(3)
    # start loop


print("sending message...")

# master1()
t1 = Thread(target=make_data)
t1.start()

time.sleep(1)
i = 0

while True:
    if payloader:
        master2(pic_data)
    time.sleep(1)


# t2=Thread(target=master2)
# t2.start()

print(" finished nRF24L01 Simple test")
