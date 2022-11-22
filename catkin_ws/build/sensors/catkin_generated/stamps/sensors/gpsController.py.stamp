from sensors.GT_U7 import *
import time
import threading

class GPSController():
    def __init__(self):
        self.refreshGPSData()
        self.thread = threading.Thread(target = self.run)

    def refreshGPSData(self):
        satTime, lat, lon = getGPSData()

        self.satTime = satTime
        self.lat = lat
        self.lon = lon

    def run(self):
        while True:
            self.refreshGPSData()

    def start(self):
        self.thread.start()

    def end(self):
        self.thread.terminate()
