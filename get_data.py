import config
import requests
import json
import time


def get_data_from_server():
    url = "http://127.0.0.1:7418"
    payload = {}
    headers = {}
    for i in range(200):
        time.sleep(1)
        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.loads(response.text)
        config.Pressure_6 = config.Pressure_5
        config.Pressure_5 = config.Pressure_4
        config.Pressure_4 = config.Pressure_3
        config.Pressure_3 = config.Pressure_2
        config.Pressure_2 = config.Pressure_1
        config.Pressure_1 = config.Pressure
        config.Pressure = (data['pressure'])  # set new data for pressure

        config.InTemp_6 = config.InTemp_5
        config.InTemp_5 = config.InTemp_4
        config.InTemp_4 = config.InTemp_3
        config.InTemp_3 = config.InTemp_2
        config.InTemp_2 = config.InTemp_1
        config.InTemp_1 = config.InTemp
        config.InTemp = (data['inside_temp'])  # set new data for inside_temp

        config.OutTemp_6 = config.OutTemp_5
        config.OutTemp_5 = config.OutTemp_4
        config.OutTemp_4 = config.OutTemp_3
        config.OutTemp_3 = config.OutTemp_2
        config.OutTemp_2 = config.OutTemp_1
        config.OutTemp_1 = config.OutTemp
        # set new data for outside_temp
        config.OutTemp = (data['outside_temp'])

        config.Hiumidity_6 = config.Hiumidity_5
        config.Hiumidity_5 = config.Hiumidity_4
        config.Hiumidity_4 = config.Hiumidity_3
        config.Hiumidity_3 = config.Hiumidity_2
        config.Hiumidity_2 = config.Hiumidity_1
        config.Hiumidity_1 = config.Hiumidity
        config.Hiumidity = (data['humidity'])  # set new data for humidity

        config.AirQuality = data['air_quality']  # set new data for air_quality

        config.UVIndex = data['uv_index']  # set new data for uv_index

        config.A_linear = data['linear']  # set new data for linear

        config.A_angular = data['angular']  # set new data for angular

        # set new data for x_height
        config.x_height.append(len(config.x_height))
        config.y_height.append(data['height'])

        #Battery
        config.Battery = data['battery']  # set new data for Battery
# img_path
