from flask import Flask
import time
import secrets

app = Flask(__name__)
temp = 30
perssor = 40
data=[]

@app.route('/', methods=['GET'])
def data():
    data = {
        "outside_temp": secrets.randbelow(100),
        "inside_temp": secrets.randbelow(100),
        "humidity": secrets.randbelow(100),
        "air_quality": secrets.randbelow(100),
        "linear": secrets.randbelow(10),
        "angular": secrets.randbelow(10),
        "pressure": secrets.randbelow(100),
        "uv_index": secrets.randbelow(100),
        "height": secrets.randbelow(100),
        "battery":80,
        "img_path": "https://s-rahmani.ir/me.jpg"
    }
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7418)

