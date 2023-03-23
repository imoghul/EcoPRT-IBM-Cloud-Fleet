#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from hardware.MPU6050 import *
from hardware.GT_U7 import * 
from sensor_msgs.msg import *
from geometry_msgs.msg import *
import atexit
import sys
import threading


def talker():
    rospy.init_node('sensor_io', anonymous=True) # talker is the node
    MPU_Init()
    #rate = rospy.Rate(100) # 10hz
    gpsPub = rospy.Publisher("raw_gps",Pose2D,queue_size=100000000000)
    imuPub = rospy.Publisher("raw_imu",Imu,queue_size=1000000000000000)
    imuthread = threading.Thread(target=run,args=(imuPub,getIMUData))
    gpsthread = threading.Thread(target=run,args=(gpsPub,getGPSData))
    imuthread.start()
    gpsthread.start()
    #while not rospy.is_shutdown():
        #print(getIMUData())
        #imuPub.publish(getIMUData())
        #gpsPub.publish(getGPSData())
        #rate.sleep()

def run(pub,func):
    while not rospy.is_shutdown():
        pub.publish(func())

if __name__ == '__main__':
    try:
        MPU_Init()
        talker()
    except rospy.ROSInterruptException:
        pass
