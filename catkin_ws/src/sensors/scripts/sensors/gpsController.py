from sensors.GT_U7 import *
import time
import threading
import datetime
import rospy
from sensors.msg import GPSData
import math
#class GPSData():
#    def __init__(self,t,lat,lon):
#        self.time = t
#        self.lat = lat
#        self.long = lon

class GPSController():
    def __init__(self):
        #rospy.init_node("GPS_Data",anonymous=False)
        self.pub = rospy.Publisher("gps_data",GPSData,queue_size=10)
        self.prevData = GPSData()
        self.data = GPSData()
        self.refreshGPSData()
        self.running = True
        self.thread = threading.Thread(target = self.run)


    def refreshGPSData(self):
        self.prevData.time = self.data.time+"" if self.data.time!=None else None
        self.prevData.lat = self.data.lat+0 if self.data.lat!=None else None
        self.prevData.long = self.data.long+0 if self.data.long!=None else None
        self.prevData.currTime = self.data.currTime+0 if self.data.currTime!=None else None
        satTime, lat, long = getGPSData()
        self.data.currTime = time.time()

        if(satTime==None and lat==None and long==None):return

        self.data.time = datetime.datetime.strftime(satTime,"%Y-%m-%d %H:%M:%S")
        self.data.lat = lat
        self.data.long = long
        try:self.data.speed = dist(self.data,self.prevData)/(self.data.currTime-self.prevData.currTime) 
        except:pass
        self.pub.publish(self.data)
        

    def run(self):
        while self.running and not rospy.is_shutdown():
            self.refreshGPSData()

    def start(self):
        self.running = True
        self.thread.start()

    def end(self):
        self.running = False
        self.thread.join()
