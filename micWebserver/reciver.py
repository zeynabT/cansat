import spidev
import time
import board
from digitalio import DigitalInOut
from circuitpython_nrf24l01.rf24 import RF24
import logging
from flask import Flask
from threading import Thread
from PIL import Image 
import io
from sim800l import SIM800L
import digitalio


app = Flask(__name__)
data = {
    'payloader1': [],
}
logging.basicConfig(filename='/home/pi/log.log',
                    format='%(asctime)s - %(levelname)s - %(message)s', filemode='a')
# Creating an object
logger = logging.getLogger()
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

def LEDs():
    global led_GSM ,led_recive

    led_recive = digitalio.DigitalInOut(board.D1)
    led_recive.direction = digitalio.Direction.OUTPUT
    led_recive.value = True

    led_GSM = digitalio.DigitalInOut(board.D0)
    led_GSM.direction = digitalio.Direction.OUTPUT
    led_GSM.value = True
    
    time.sleep(10)
    
    led_recive.value = False
    led_GSM.value = False


def GSM():
    try:
        sim800l = SIM800L()
        sim800l.setup()

        while True:
            if sim800l.is_registered():
                led_GSM.value = True
                msg = sim800l.read_next_message(all_msg=True)
                data['payloader1'].append(msg)
            else:
                led_GSM.value = False
            time.sleep(5)
    except:
        logger.error('gsm error')

# invalid default values for scoping
SPI_BUS, CSN_PIN, CE_PIN = (None, None, None)

# try:  # on Linux
SPI_BUS = spidev.SpiDev()  # for a faster interface on linux
CSN_PIN = 0  # use CE0 on default bus (even faster than using any pin)
CE_PIN = DigitalInOut(board.D17)  # using pin gpio22 (BCM numbering)

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

nrf.data_rate = 250
nrf.channel = 22
nrf.arc = 6
nrf.auto_ack = True

timeout = 2
picture_num = 1

start0 = time.monotonic()


def slave(timeout):
    global data
    logger.info('start listening nrf')
    pic_byte = bytearray()
    nrf.listen = True  # put radio into RX mode and power up
    led_recive.value = True
    start = time.monotonic()
    while (time.monotonic() - start) < timeout:
        if nrf.available():
            start = time.monotonic()
            # grab information about the received payload
            pipe_number = nrf.pipe
            # fetch 1 payload from RX FIFO
            buffer = nrf.read()  # also clears nrf.irq_dr status flag
            if pipe_number == 1:
                data['payloader1'].append(buffer.decode())
                # logger.info('output data is: '+str(data))
            else:
                pic_byte += buffer
        else:
            logger.warning('watingig for data')
    return pic_byte


@app.route('/', methods=['GET'])
def data_api():
    global data
    tmp = data
    logger.info('data sent:' + str(data))
    data = {
        'payloader1': []
    }
    return tmp


def run_webserver():
    app.run(host='0.0.0.0', port=7418)


if __name__ == "__main__":
    t1 = Thread(target=LEDs)
    t1.start()
    
    t = Thread(target=run_webserver)
    t.start()
    
    t2 = Thread(target=GSM)
    t2.start()
    logger.info('webserver started')
    while True:
        try:
            pic_pyte = slave(timeout)
            if pic_pyte:
                logger.info('Start convert picture')
                final_pic = "/home/pi/static/final_pic{}.jpg".format(picture_num)
                with open(final_pic, "wb") as file:
                    file.write(pic_pyte)
                #image = Image.open(io.BytesIO(pic_pyte))
                #image.save(final_pic)
                logger.info('End time converting picture . ' + 'picture name: '+final_pic +
                            str(time.monotonic() - start0))
                pic_pyte = bytearray()
                picture_num += 1
        except Exception as e:
            logger.error('error in main function: ')
            time.sleep(0.01)
            pass


# if payloader1:
#   with open("final_data.bin", "ab") as f:
#      f.write(payloader1 + "\n".encode())
#  print('data saved...')

#             image = Image.open(io.BytesIO(payloader1))
#             image.save("final_pic%s.jpg" %i)
