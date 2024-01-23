from flask import Flask
from sense_hat import SenseHat
import json

app = Flask(__name__)

sense = SenseHat()

@app.route('/temperature')
def get_temperature():
    temp = sense.get_temperature()
    data={'temp': temp}
    return json.dumps(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

