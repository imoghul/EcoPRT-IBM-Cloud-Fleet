#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensors.gpsController import *
from sensors.imuController import *
from sensors.imageController import *
import atexit
import sys
from config.config import *


def talker():
    rospy.init_node('Sensor_Node', anonymous=True) # talker is the node
    rate = rospy.Rate(100) # 10hz
    
    gps = GPSController()
    imu = IMUController()
    image = ImageController()
    #gps.start()
    #imu.start()
    while not rospy.is_shutdown():
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
