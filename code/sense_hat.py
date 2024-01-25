import random

class Colour():
    def __init__(self, gain=1, integration_cycles=1):
        self._gain = gain
        self._integration_cycles = integration_cycles
        self._enabled = 1

    GAIN_VALUES = (1, 4, 16, 64)

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, status):
        self._enabled = status

    @property
    def gain(self):
        return self._gain

    @gain.setter
    def gain(self, gain):
        if gain in self.GAIN_VALUES:
            self._gain = gain
        else:
            raise Exception(f"cannot set gain to '{gain}. Values: {self.GAIN_VALUES}")

    @property
    def integration_cycles(self):
        return self._integration_cycles

    @integration_cycles.setter
    def integration_cycles(self, integration_cycles):
        if 1 <= integration_cycles <= 256:
            self._integration_cycles = integration_cycles
        else:
            raise Exception(f"Cannot set integration cycles to {integration_cycles} (1-256)")

    @property
    def colour(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)
        return (r,g,b,c)
    

class SenseHat():
    colour = Colour()
    def get_temperature(self):
        return random.uniform(-5, 30)

    def get_temperature_from_humidty(self):
        return random.uniform(-5, 30)

    def get_temperature_from_pressure(self):
        return random.uniform(-5, 30)

    def get_humidty(self):
        return random.uniform(0, 100)

    def show_message(self, text_string, scroll_speed=.1,text_colour=[255, 255, 255],back_colour=[0, 0, 0]):
        print(f"Showing message on pi: {text_string}")
