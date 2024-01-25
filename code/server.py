from flask import Flask
from sense_hat import SenseHat
import json

app = Flask(__name__)

sense = SenseHat()
sense.colour.gain = 4
sense.colour.integration_cycles = 64

@app.route('/temperature')
def get_temperature():
    temp = sense.get_temperature()
    data={'temp': temp}
    return json.dumps(data)

@app.route('/humidty')
def get_humidty():
    humidty = sense.get_humidty()
    data={'temp': humidty}
    return json.dumps(data)

@app.route('/colour')
def get_colour():
    red,green,blue,clear = sense.colour.colour
    data={'red': red, 'green': green, 'blue': blue, 'clear': clear}
    return json.dumps(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

