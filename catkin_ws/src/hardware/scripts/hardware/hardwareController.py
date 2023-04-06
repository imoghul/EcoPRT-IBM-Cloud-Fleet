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
    gpsPub = rospy.Publisher("raw_gps",NavSatFix,queue_size=100000)
    imuPub = rospy.Publisher("raw_imu",Imu,queue_size=10000)
    imuthread = threading.Thread(target=run,args=(imuPub,getIMUData,Imu))
    gpsthread = threading.Thread(target=run,args=(gpsPub,getGPSData,Pose2D))
    imuthread.start()
    gpsthread.start()

def run(pub,func,_type):
    while not rospy.is_shutdown():
        val = func()
        if(type(val)==_type):
            try:pub.publish(val)
            except:pass

if __name__ == '__main__':
    try:
        MPU_Init()
        talker()
    except rospy.ROSInterruptException:
        pass
