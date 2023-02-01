import spidev
import time
import struct
import board
from digitalio import DigitalInOut
import os
import io
import PIL.Image as Image
from circuitpython_nrf24l01.rf24 import RF24


from flask import Flask
from threading import Thread
app = Flask(__name__)
data = {
    'payloader1': [],
    'payloader2': []
}

# invalid default values for scoping
SPI_BUS, CSN_PIN, CE_PIN = (None, None, None)

# try:  # on Linux
SPI_BUS = spidev.SpiDev()  # for a faster interface on linux
CSN_PIN = 0  # use CE0 on default bus (even faster than using any pin)
CE_PIN = DigitalInOut(board.D22)  # using pin gpio22 (BCM numbering)

# initialize the nRF24L01 on the spi bus object
nrf = RF24(SPI_BUS, CSN_PIN, CE_PIN)

nrf.pa_level = 0

# addresses needs to be in a buffer protocol object (bytearray)
address = [b"\xe1\xf0\xf0\xf0\xf0", b"\xd2\xf0\xf0\xf0\xf0"]

# set RX address of TX node into an RX pipe

nrf.open_rx_pipe(1, address[0])  # using pipe 1 for sensordatas
nrf.open_rx_pipe(2, address[1])  # using pipe 2 for pic

# uncomment the following 3 lines for compatibility with TMRh20 library
nrf.allow_ask_no_ack = False
nrf.dynamic_payloads = True

RF24.data_rate = 250
RF24.channel = 22
RF24.arc = 2
RF24.auto_ack = True

timeout = 3*3600
i = 1

start0 = time.monotonic()


def slave(timeout):
    nrf.listen = True  # put radio into RX mode and power up
    global data
    payloader1 = bytearray()
    payloader2 = bytearray()
    start = start0
    while (time.monotonic() - start) < timeout:

        if nrf.available():

            start = time.monotonic()
            # grab information about the received payload
            payload_size, pipe_number = (nrf.any(), nrf.pipe)
            # fetch 1 payload from RX FIFO
            buffer = nrf.read()  # also clears nrf.irq_dr status flag
            print(buffer)
            if pipe_number == 1:
                data['payloader1'].append(buffer.decode())
            else:
                data['payloader2'].append(buffer.decode())

    return payloader2, payloader1


@app.route('/', methods=['GET'])
def data_api():
    global data
    tmp = data
    data = {
        'payloader1': [],
        'payloader2': []
    }
    return tmp


def run_webserver():
    app.run(host='0.0.0.0', port=7418)


t = Thread(target=run_webserver)
t.start()

print("start listenning...")


while True:
    # save :
    try:
        payloader2, payloader1 = slave(timeout)

        if payloader1:
            with open("final_data.bin", "ab") as f:
                f.write(payloader1 + "\n".encode())
            print('data saved...')

        if payloader2:
            final_pic = "final_pic%s.bin" % i
            with open(final_pic, "wb") as file:
                file.write(payloader1)
        #             image = Image.open(io.BytesIO(payloader1))
        #             image.save("final_pic%s.jpg" %i)
            print(time.monotonic() - start0)
            print('pic saved...')
            i += 1
    except:
        time.sleep(0.01)
        pass
