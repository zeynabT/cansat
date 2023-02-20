import config
import requests
import json
import time
import logging
from threading import Thread

logger = ''


def send_request_to_iot_panel():
    url = "http://iot.sensifai.com:9090/api/v1/TAO37FyHZEIagFeh1Hb5/telemetry"
    data = {
        "pressure": config.pressure,
        "acceleration_angular": ((config.acceleration_angular_x**2) + (config.acceleration_angular_y**2) + (config.acceleration_angular_z)**2)**0.5,
        "acceleration_linear": ((config.acceleration_linear_x**2) + (config.acceleration_linear_y**2) + (config.acceleration_linear_z)**2)**0.5,
        "speed": config.speed,
        "outside_temp": config.out_temp,
        "inside_temp": config.in_temp,
        "sunlight_infrared": config.sunlight_infrared,
        "sunlight_spectrum": config.sunlight_spectrum,
        "sunlight_visible": config.sunlight_visible,
        "humidity": config.hiumidity,
        "height": config.height_y,
        "img_path": "http://secure-iot.ir/cansat/1.jpg",
        "image_text": config.image_text
    }
    payload = json.dumps(data)
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        requests.request("POST", url, headers=headers, data=payload)
        logger.info('data sent to server')
    except:
        logger.error('some error in sending data to server')


pic_number = 1


def get_picture_from_server():
    logger.info('try to get picture')
    global pic_number
    url = "http://192.168.137.33:7418"
    # url = "http://127.0.0.1:7418"
    try:
        r = requests.get(
            url+'/static/final_pic{}.jpg'.format(pic_number), allow_redirects=True)
        if (r.status_code == 200):
            open('final.jpg', 'wb').write(r.content)
            pic_number += 1
        else:
            print('there is no picture')
    except:
        logger.error('rasbery not respose')


def get_data_from_server():
    logging.basicConfig(filename='log/getdata.log',
                        format='%(asctime)s - %(levelname)s - %(message)s', filemode='a')
    # Creating an object logger
    global logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    url = "http://192.168.137.33:7418"
    # url = "http://127.0.0.1:7418"
    al_init = 0
    aa_init = 0
    payload = {}
    headers = {}
    # picture = []
    # empty_pic_time = 0
    logger.info('start logging ...')
    while (True):
        time.sleep(1)
        logger.info("try to get data")
        try:
            response = requests.request(
                "GET", url, headers=headers, data=payload)
            data_res = json.loads(response.text)
        except:
            logger.error('rasbery not respose')
            config.ground_station_connection = False
            continue
        payloader1 = data_res['payloader1']
        logger.info('data recived : ' + str(data_res))
        get_picture_from_server()
        for paload in payloader1:
            d = paload.split('_')
            if len(d) < 2:
                continue
            config.time = int(d[0])
            if d[1] == 'Lx':
                if d[0] == '0':
                    config.sensor_gps = False
                    continue
                config.coordinate_x = float(d[2])
                config.sensor_gps = True
            if d[1] == 'Ly':
                if d[0] == '0':
                    config.sensor_gps = False
                    continue
                config.coordinate_y = float(d[2])
                config.sensor_gps = True
            if d[1] == 'A':
                if d[0] == '0':
                    config.sensor_acceleration = False
                    continue
                config.sensor_acceleration = True
                acceleration = d[2].split('*')
                if al_init == 0:
                    config.acceleration_linear_x_init = float(acceleration[0])
                    config.acceleration_linear_y_init = float(acceleration[1])
                    config.acceleration_linear_z_init = float(acceleration[2])
                    al_init = 1
                config.acceleration_linear_x = float(
                    acceleration[0]) - config.acceleration_linear_x_init
                config.acceleration_linear_y = float(
                    acceleration[1])-config.acceleration_linear_y_init
                config.acceleration_linear_old_z = config.acceleration_linear_z
                config.acceleration_linear_z = float(
                    acceleration[2])-config.acceleration_linear_z_init
                config.acceleration_linear_old_time = config.acceleration_linear_time
                config.acceleration_linear_time = config.time
                config.speed_6 = config.speed_5
                config.speed_5 = config.speed_4
                config.speed_4 = config.speed_3
                config.speed_3 = config.speed_2
                config.speed_2 = config.speed_1
                config.speed_1 = config.speed
                config.speed = ((config.acceleration_linear_z-config.acceleration_linear_old_z)*(
                    config.acceleration_linear_old_time-config.time))/2

            if d[1] == 'Z':
                if d[0] == '0':
                    config.sensor_acceleration = False
                    continue
                config.sensor_acceleration = True
                acceleration = d[2].split('*')
                if aa_init == 0:
                    config.acceleration_angular_x_init = float(acceleration[0])
                    config.acceleration_angular_y_init = float(acceleration[1])
                    config.acceleration_angular_z_init = float(acceleration[2])
                    aa_init = 1
                config.acceleration_angular_x = float(
                    acceleration[0])-config.acceleration_angular_x_init
                config.acceleration_angular_y = float(
                    acceleration[1])-config.acceleration_angular_y_init
                config.acceleration_angular_z = float(
                    acceleration[2])-config.acceleration_angular_z_init
            if d[1] == 'Ti':
                if d[0] == '0':
                    config.sensor_temp_in = False
                    continue
                config.sensor_temp_in = True
                config.in_temp = float(d[2])
            if d[1] == 'To':
                if d[0] == '0':
                    config.sensor_temp_out = False
                    continue
                config.sensor_temp_out = True
                config.out_temp = float(d[2])
            if d[1] == 'U':
                if d[0] == '0':
                    config.sensor_sunlight = False
                    continue
                config.sensor_sunlight = True
                sunlight = d[2].split('*')
                config.sunlight_infrared = sunlight[2]
                config.sunlight_spectrum = sunlight[1]
                config.sunlight_visible = sunlight[0]
            if d[1] == 'H':
                if d[0] == '0':
                    config.sensor_humidity = False
                    continue
                config.sensor_humidity = True
                config.hiumidity = float(d[2])
            if d[1] == 'L':
                if d[0] == '0':
                    config.sensor_pressure = False
                    continue
                config.sensor_pressure = True
                config.height_x.append(len(config.height_y))
                config.height_y.append(float(d[2]))
            if d[1] == 'P':
                if d[0] == '0':
                    config.sensor_pressure = False
                    continue
                config.sensor_pressure = True
                config.pressure_6 = config.pressure_5
                config.pressure_5 = config.pressure_4
                config.pressure_4 = config.pressure_3
                config.pressure_3 = config.pressure_2
                config.pressure_2 = config.pressure_1
                config.pressure_1 = config.pressure
                config.pressure = float(d[2])

            config.log = str(response.text)
        # t = Thread(target=send_request_to_iot_panel)
        # t.start()
        # dashboard http://iot.sensifai.com/cansat/fumcan/
