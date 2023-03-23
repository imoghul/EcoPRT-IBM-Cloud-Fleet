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
    thread = threading.Thread(target=run,args=(gpsPub,imuPub))
    thread.start()
    #while not rospy.is_shutdown():
        #print(getIMUData())
        #imuPub.publish(getIMUData())
        #gpsPub.publish(getGPSData())
        #rate.sleep()

def run(gpsPub,imuPub):
    while not rospy.is_shutdown():
        imuPub.publish(getIMUData())
        gpsPub.publish(getGPSData())

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
