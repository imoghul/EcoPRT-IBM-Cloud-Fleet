#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from sensors.gpsController import *
from sensors.imuController import * 



def talker():
    rospy.init_node('Sensor_Node', anonymous=True) # talker is the node
    rate = rospy.Rate(10) # 10hz

    gps = GPSController()
    imu = IMUController()

    #gps.start()
    #imu.start()
    while not rospy.is_shutdown():
        gps.refreshGPSData()
        imu.calc()
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
