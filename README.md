# Sensehat Flask API

## Setup

The code for this project can be found in the `code` directory. 
```bash
cd code
```

We recommend using a virtual environment, but this is optional:
```bash
# Optional, but recommended
python -m venv venv --system-site-packages,
source venv/bin/activate
```

Note: `-system-site-packages` ensures that the system packages for the sense hat are used in the virtual environment.
See the sense HAT [installation instructions](https://www.raspberrypi.com/documentation/accessories/sense-hat.html).

The API uses [Flask](https://flask.palletsprojects.com/en/3.0.x/), which can be installed with:
```bash
pip install Flask
```

## Running

If you're running on the Pi, use:
```bash
flask --app server run
```

`--app server` ensures flask knows to use `server.py`.

You can access the API in the browser, e.g. http://localhost:5000/temperature.
Alternatively, you can use `curl`:
```bash
curl http://localhost:5000/temperature
```

If you're not running on the Pi, use:
```bash
flask --app server run --host=0.0.0.0
```

`--host=0.0.0.0` ensures that API is available on other computers than the Pi itself.
Note: This can allow arbitrary Python code to be executed on your Pi!
Use with caution, and read the information [here](https://flask.palletsprojects.com/en/3.0.x/quickstart/) for more details.

You can access the API using the Pi's IP address by going to the browser or using `curl`.
The IP address can be found by running:
```bash
hostname -I
```
