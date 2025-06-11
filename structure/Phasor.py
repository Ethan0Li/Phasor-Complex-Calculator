class Phasor:
    def __init__(self, mag, deg):
        self.mag = mag
        self.deg = deg

    def print(self):
        print(str(self.mag) +"\u2220"+ str(self.deg) + "\u00B0")