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
        config.Pressure = str(data['pressure'])

        config.InTemp_6 = config.InTemp_5
        config.InTemp_5 = config.InTemp_4
        config.InTemp_4 = config.InTemp_3
        config.InTemp_3 = config.InTemp_2
        config.InTemp_2 = config.InTemp_1
        config.InTemp_1 = config.InTemp
        config.InTemp = str(data['inside_temp'])

        config.OutTemp_6 = config.OutTemp_5
        config.OutTemp_5 = config.OutTemp_4
        config.OutTemp_4 = config.OutTemp_3
        config.OutTemp_3 = config.OutTemp_2
        config.OutTemp_2 = config.OutTemp_1
        config.OutTemp_1 = config.OutTemp
        config.OutTemp = str(data['outside_temp'])

        config.Hiumidity_6 = config.Hiumidity_5
        config.Hiumidity_5 = config.Hiumidity_4
        config.Hiumidity_4 = config.Hiumidity_3
        config.Hiumidity_3 = config.Hiumidity_2
        config.Hiumidity_2 = config.Hiumidity_1
        config.Hiumidity_1 = config.Hiumidity
        config.Hiumidity = str(data['humidity'])

