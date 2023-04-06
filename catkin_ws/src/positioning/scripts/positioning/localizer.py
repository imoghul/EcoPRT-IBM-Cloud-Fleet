import rospy
from sensors.msg import IMUData, GPSData 
from positioning.msg import Position
from config.config import waitForGPS
from sensor_msgs.msg import Image
class Localizer():
    def __init__(self):

        # set imuData and gpsData if you don't want to publish values with zeros, that would cause the system to think that those garbage values are valid
        if(not waitForGPS):
            self.imuData = IMUData() 
            self.gpsData = GPSData()
            self.image = Image()
        self.position = Position()
        self.pub = rospy.Publisher("position",Position,queue_size=10)
    def updateIMU(self,imuData):
        self.imuData = imuData
        self.run()
    def updateGPS(self,gpsData):
        self.gpsData = gpsData
        self.run()
    def updateImage(self,image):
        self.image = image
        self.run()
    def run(self):
        try:
            origPos = Position(self.position.gps, self.position.imu, self.position.frame)
            try:
                self.position.gps = self.gpsData
                self.position.imu = self.imuData
                self.position.frame = self.image
            except: pass
            if(origPos == self.position):
                return
            self.pub.publish(self.position)
        except: pass
