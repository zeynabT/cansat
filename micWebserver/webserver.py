from flask import Flask
import time
import secrets

app = Flask(__name__)
temp = 30
perssor = 40
data=[]
battery=100 # battray jori set beshe ke 2 saat tamom beshe
height=100
@app.route('/', methods=['GET'])
def data():
    global battery
    battery=battery-1
    if battery==1:
        battery=100

    global height
    height=height-1
    if height==1:
        height=100
    data = {
        "outside_temp": secrets.randbelow(100),
        "inside_temp": secrets.randbelow(100),
        "humidity": secrets.randbelow(100),
        "air_quality": secrets.randbelow(100),
        "linearX": secrets.randbelow(10),
        "linearY": secrets.randbelow(10),
        "linearZ": secrets.randbelow(10),
        "angularX": secrets.randbelow(10),
        "angularY": secrets.randbelow(10),
        "angularZ": secrets.randbelow(10),
        "pressure": secrets.randbelow(100),
        "uv_index": secrets.randbelow(100),
        "height": height,
        "battery":battery,
        "img_path": "https://s-rahmani.ir/me.jpg"
    }
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7418)

