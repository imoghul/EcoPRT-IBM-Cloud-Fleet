import rospy
from sensors.msg import IMUData, GPSData 
from positioning.msg import Position
class Localizer():
    def __init__(self):
        self.imuData = None
        self.gpsData = None
        self.position = Position()
        self.pub = rospy.Publisher("position",Position,queue_size=10)
    def updateIMU(self,imuData):
        self.imuData = imuData
    def updateGPS(self,gpsdata):
        self.gpsData = gpsData
    def run(self):
        self.position.longitude = self.gpsData.long
        self.position.latitude = self.gpsData.lat
        self.pub.publish(self.position)
