import time
import threading
import datetime
import rospy
from geometry_msgs.msg import Pose2D
from sensors.msg import GPSData
import math
from config.config import raw_gps_publisher_name
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
        self.sub = rospy.Subscriber(raw_gps_publisher_name,Pose2D,self.refreshGPSData)
        self.data = GPSData()
        #self.refreshGPSData()
        #self.running = True
        #self.thread = threading.Thread(target = self.run)


    def refreshGPSData(self,newRaw):
        try:
            self.prevData.time = self.data.time+"" if self.data.time!=None else None
            self.prevData.lat = self.data.lat+0 if self.data.lat!=None else None
            self.prevData.long = self.data.long+0 if self.data.long!=None else None
            self.prevData.currTime = self.data.currTime+0 if self.data.currTime!=None else None
        except: pass
        
        lat, long = (newRaw.x, newRaw.y)#getGPSData()
        
        if(lat==None and long==None):return
       

        self.data.currTime = time.time()
        self.data.time = datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%d %H:%M:%S")# satTime
        self.data.lat = lat
        self.data.long = long
        try:self.data.speed = dist(self.data,self.prevData)/(self.data.currTime-self.prevData.currTime) 
        except:pass
        self.pub.publish(self.data)
        

    #def run(self):
    #    while self.running and not rospy.is_shutdown():
    #        self.refreshGPSData()

    #def start(self):
    #    self.running = True
    #    self.thread.start()

    #def end(self):
    #    self.running = False
    #    self.thread.join()
