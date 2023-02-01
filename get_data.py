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
            if d[1] == 'Lx':
                config.CoordinateX = float(d[2])
            if d[1] == 'Ly':
                config.CoordinateY = float(d[2])
            if d[1] == 'A':
                acceleration = d[2].split('*')
                config.A_linearX = float(acceleration[0])
                config.A_linearY = float(acceleration[1])
                config.A_linearZ = float(acceleration[2])
            if d[1] == 'Z':
                acceleration = d[2].split('*')
                config.A_angularX = float(acceleration[0])
                config.A_angularY = float(acceleration[1])
                config.A_angularZ = float(acceleration[2])
            if d[1] == 'Ti':
                config.InTemp_6 = config.InTemp_5
                config.InTemp_5 = config.InTemp_4
                config.InTemp_4 = config.InTemp_3
                config.InTemp_3 = config.InTemp_2
                config.InTemp_2 = config.InTemp_1
                config.InTemp_1 = config.InTemp
                config.InTemp = float(d[2])
            if d[1] == 'To':
                config.OutTemp_6 = config.OutTemp_5
                config.OutTemp_5 = config.OutTemp_4
                config.OutTemp_4 = config.OutTemp_3
                config.OutTemp_3 = config.OutTemp_2
                config.OutTemp_2 = config.OutTemp_1
                config.OutTemp_1 = config.OutTemp
                config.OutTemp = float(d[2])
            if d[1] == 'U':
                config.UVIndex = float(d[2])
            if d[1] == 'H':
                config.Hiumidity_6 = config.Hiumidity_5
                config.Hiumidity_5 = config.Hiumidity_4
                config.Hiumidity_4 = config.Hiumidity_3
                config.Hiumidity_3 = config.Hiumidity_2
                config.Hiumidity_2 = config.Hiumidity_1
                config.Hiumidity_1 = config.Hiumidity
                config.Hiumidity = float(d[2])
            if d[1] == 'L':
                config.x_height.append(len(config.x_height))
                config.y_height.append(float(d[2]))
            if d[1]=='P':
                config.Pressure_6 = config.Pressure_5
                config.Pressure_5 = config.Pressure_4
                config.Pressure_4 = config.Pressure_3
                config.Pressure_3 = config.Pressure_2
                config.Pressure_2 = config.Pressure_1
                config.Pressure_1 = config.Pressure
                config.Pressure=float(d[2])

            config.log = str(response.text)
            # t = Thread(target=send_request_to_iot_panel, args=(data,))
            # t.start()
        # send_request_to_iot_panel(data)
        # dashboard http://iot.sensifai.com:9090/dashboard/a68e93e0-8c44-11ed-ab34-194fa8ffdeff?publicId=e125ce10-927a-11ed-9ada-194fa8ffdeff
# img_path
