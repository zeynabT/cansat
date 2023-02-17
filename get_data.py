import config
import requests
import json
import time

from threading import Thread


def send_request_to_iot_panel(data):
    url = "http://iot.sensifai.com:9090/api/v1/TAO37FyHZEIagFeh1Hb5/telemetry"
    payload = json.dumps(data)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def get_data_from_server():
    # url = "http://192.168.137.83:7418"
    url = "http://127.0.0.1:7418"
    payload = {}
    headers = {}
    for i in range(200):
        time.sleep(1)
        response = requests.request("GET", url, headers=headers, data=payload)
        data_res = json.loads(response.text)
        payloader1 = data_res['payloader1']
        # payloader2=data_res['payloader2']
        for paload in payloader1:
            d = paload.split('_')
            if len(d) < 2:
                continue
            config.time = int(d[0])
            if d[1] == 'Lx':
                config.coordinate_x = float(d[2])
            if d[1] == 'Ly':
                config.coordinate_y = float(d[2])
            if d[1] == 'A':
                acceleration = d[2].split('*')
                config.acceleration_linear_x = float(acceleration[0])
                config.acceleration_linear_y = float(acceleration[1])
                config.acceleration_linear_old_z = config.acceleration_linear_z
                config.acceleration_linear_z = float(acceleration[2])
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
                acceleration = d[2].split('*')
                config.acceleration_angular_x = float(acceleration[0])
                config.acceleration_angular_y = float(acceleration[1])
                config.acceleration_angular_z = float(acceleration[2])
            if d[1] == 'Ti':
                config.in_temp = float(d[2])
            if d[1] == 'To':
                config.out_temp = float(d[2])
            if d[1] == 'U':
                sunlight = d[2].split('*')
                config.sunlight_infrared = sunlight[2]
                config.sunlight_spectrum = sunlight[1]
                config.sunlight_visible = sunlight[0]
            if d[1] == 'H':
                config.hiumidity = float(d[2])
            if d[1] == 'L':
                config.height_x.append(len(config.height_y))
                config.height_y.append(float(d[2]))
            if d[1] == 'P':
                config.pressure_6 = config.pressure_5
                config.pressure_5 = config.pressure_4
                config.pressure_4 = config.pressure_3
                config.pressure_3 = config.pressure_2
                config.pressure_2 = config.pressure_1
                config.pressure_1 = config.pressure
                config.pressure = float(d[2])

            config.log = str(response.text)
            # t = Thread(target=send_request_to_iot_panel, args=(data,))
            # t.start()
        # send_request_to_iot_panel(data)
        # dashboard http://iot.sensifai.com:9090/dashboard/a68e93e0-8c44-11ed-ab34-194fa8ffdeff?publicId=e125ce10-927a-11ed-9ada-194fa8ffdeff
# img_path
