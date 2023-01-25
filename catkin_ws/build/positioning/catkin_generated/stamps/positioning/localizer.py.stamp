import rospy
from sensors.msg import IMUData, GPSData 
from positioning.msg import Position
class Localizer():
    def __init__(self):
        self.imuData = IMUData() 
        self.gpsData = GPSData()
        self.position = Position()
        self.pub = rospy.Publisher("position",Position,queue_size=10)
    def updateIMU(self,imuData):
        self.imuData = imuData
    def updateGPS(self,gpsData):
        self.gpsData = gpsData
    def run(self):
        origPos = Position(self.position.gps, self.position.imu)
        self.position.gps = self.gpsData
        self.position.imu = self.imuData
        if(origPos == self.position):
            return
        self.pub.publish(self.position)
