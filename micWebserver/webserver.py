from flask import Flask
import time
import secrets

app = Flask(__name__)
temp = 30
perssor = 40
data = []
battery = 100  # battray jori set beshe ke 2 saat tamom beshe
height = 100
time = 1


@app.route('/', methods=['GET'])
def data():
    global height, time
    height = height-1
    if height == 1:
        height = 100
    time = time+1
    # payloader1 = {
    #     "outside_temp": secrets.randbelow(100),
    #     "inside_temp": secrets.randbelow(100),
    #     "humidity": secrets.randbelow(100),
    #     "air_quality": secrets.randbelow(100),
    #     "linearX": secrets.randbelow(10),
    #     "linearY": secrets.randbelow(10),
    #     "linearZ": secrets.randbelow(10),
    #     "angularX": secrets.randbelow(10),
    #     "angularY": secrets.randbelow(10),
    #     "angularZ": secrets.randbelow(10),
    #     "pressure": secrets.randbelow(100),
    #     "uv_index": secrets.randbelow(100),
    #     "height": height,
    #     "battery":battery,
    #     "img_path": "https://s-rahmani.ir/me.jpg"
    # }
    str_time = str(time)
    rand = str(secrets.randbelow(100))
    payloader1 = [
        '{}_Lx_36.308314'.format(str_time),
        '{}_Ly_59.529174'.format(str_time),
        '{}_A_{}*{}*{}'.format(str_time, rand, rand, rand),
        '{}_Z_{}*{}*{}'.format(str_time, rand, rand, rand),
        '{}_Ti_{}'.format(str_time, rand),
        '{}_To_{}'.format(str_time, rand),
        '{}_U_{}*{}*{}'.format(str_time, rand, rand, rand),
        '{}_H_{}'.format(str_time, rand),
        '{}_L_{}'.format(str_time, height),
        '{}_P_{}'.format(str_time, rand),
    ]
    return {'payloader1': payloader1, 'payloader2': 2}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7418)
