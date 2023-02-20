import config
import requests
import json
import time


def send_request_to_iot_panel():
    url = "http://iot.sensifai.com:9090/api/v1/TAO37FyHZEIagFeh1Hb5/telemetry"
    data = {
        "pressure": 950,
        "acceleration_angular": 5,
        "acceleration_linear": 4,
        "speed": 3,
        "outside_temp": 40,
        "inside_temp": 55,
        "sunlight_infrared": 52,
        "sunlight_spectrum": 22,
        "sunlight_visible": 11,
        "humidity": 55,
        "height": 200,
        "img_path": "https://s-rahmani.ir/me.jpg",
        "image_text": 'Shape Circle and number 65'
    }
    payload = json.dumps(data)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


pic_number = 1
def get_picture_from_server():
    print ('get picture ##################################')
    global pic_number
    url = "http://192.168.137.33:7418"
    # url = "http://127.0.0.1:7418"
    r = requests.get(
        url+'/static/final_pic{}.jpg'.format(pic_number), allow_redirects=True)
    if (r.status_code == 200):
        open('final.jpg', 'wb').write(r.content)
        pic_number += 1
    else:
        print('there is no picture')


def get_data_from_server():
    url = "http://192.168.137.33:7418"
    # url = "http://127.0.0.1:7418"
    payload = {}
    headers = {}
    # picture = []
    # empty_pic_time = 0
    while (True):
        time.sleep(1)
        print("starting get data **************************************************")
        response = requests.request("GET", url, headers=headers, data=payload)
        data_res = json.loads(response.text)
        print ('i got data **********************************' , str(data_res))
        payloader1 = data_res['payloader1']
        get_picture_from_server()
        print('picture recived')
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
                if d[0] == '0':
                    config.sensor_acceleration = False
                    continue
                config.sensor_acceleration = True
                acceleration = d[2].split('*')
                config.acceleration_angular_x = float(acceleration[0])
                config.acceleration_angular_y = float(acceleration[1])
                config.acceleration_angular_z = float(acceleration[2])
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
            # t = Thread(target=send_request_to_iot_panel, args=(data,))
            # t.start()
        # send_request_to_iot_panel(data)
        # dashboard http://iot.sensifai.com:9090/dashboard/a68e93e0-8c44-11ed-ab34-194fa8ffdeff?publicId=e125ce10-927a-11ed-9ada-194fa8ffdeff
# img_path
