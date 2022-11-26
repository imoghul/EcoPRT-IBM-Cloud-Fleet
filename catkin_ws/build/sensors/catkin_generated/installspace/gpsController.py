from sensors.GT_U7 import *
import time
import threading
import datetime
import rospy
from sensors.msg import GPSData

#class GPSData():
#    def __init__(self,t,lat,lon):
#        self.time = t
#        self.lat = lat
#        self.long = lon

class GPSController():
    def __init__(self):
        #rospy.init_node("GPS_Data",anonymous=False)
        self.data = GPSData()
        self.refreshGPSData()
        self.pub = rospy.Publisher("gps_data",GPSData,queue_size=10)
        self.thread = threading.Thread(target = self.run)

    def refreshGPSData(self):
        satTime, lat, long = getGPSData()
        
        if(satTime==None and lat==None and long==None):return

        self.data.time = satTime#datetime.datetime.strptime(satTime,"%Y-%m-%d %H:%M:%S")
        self.data.lat = lat
        self.data.long = long
        

        self.pub.publish(self.data)
        

    def run(self):
        while True:
            self.refreshGPSData()

    def start(self):
        self.thread.start()

    def end(self):
        self.thread.terminate()
