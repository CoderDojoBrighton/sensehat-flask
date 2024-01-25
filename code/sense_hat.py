import random

class SenseHat():
    def get_temperature(self):
        return random.uniform(-5, 30)

    def get_humidty(self):
        return random.uniform(0, 100)
