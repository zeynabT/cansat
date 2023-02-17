
import digitalio
import time
import board

led_rsp = ''
led_mpl = ''
led_gps = ''
led_UV = ''
led_Gy = ''
led_Nrf = ''
led_Aht = ''

start_time = time.monotonic()


def LEDs_function():
    # LEDs Submitions
    global led_rsp, led_mpl, led_gps, led_UV, led_Gy, led_Nrf, led_Aht
    try:
        led_rsp = digitalio.DigitalInOut(board.D5)
        led_rsp.direction = digitalio.Direction.OUTPUT
        led_rsp.value = True

        led_mpl = digitalio.DigitalInOut(board.D4)
        led_mpl.direction = digitalio.Direction.OUTPUT
        led_mpl.value = True

        led_UV = digitalio.DigitalInOut(board.D16)
        led_UV.direction = digitalio.Direction.OUTPUT
        led_UV.value = True

        led_gps = digitalio.DigitalInOut(board.D18)
        led_gps.direction = digitalio.Direction.OUTPUT
        led_gps.value = True

        led_Gy = digitalio.DigitalInOut(board.D26)
        led_Gy.direction = digitalio.Direction.OUTPUT
        led_Gy.value = True

        led_Nrf = digitalio.DigitalInOut(board.D12)
        led_Nrf.direction = digitalio.Direction.OUTPUT
        led_Nrf.value = True

        led_Aht = digitalio.DigitalInOut(board.D25)
        led_Aht.direction = digitalio.Direction.OUTPUT
        led_Aht.value = True
        print('LEDs playing')
    except:
        print('LEDs doesn\'t work')

    time.sleep(1)
    #off 
    leds = [led_Aht, led_Gy, led_mpl, led_gps, led_Nrf, led_UV, led_rsp]
    for led in leds:
        led.value=False
    
    time.sleep(1)

    for led in leds:
        led.value=True
        time.sleep(0.3)
        led.value=False

    time.sleep(1)

    for led in leds:
        led.value=True

    time.sleep(1)

    for led in leds:
        led.value=False
        time.sleep(0.3)
        led.value=True

    for led in leds:
        led.value=False
        time.sleep(0.3)

    for led in leds:
        led.value=True
        time.sleep(0.3)