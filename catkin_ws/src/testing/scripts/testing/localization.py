#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensors.gpsController import *
from sensors.imuController import *
from testing.localizer import *

#localizer = Localizer()

def gpsCallback(data):
    #global localizer
    rospy.loginfo(rospy.get_caller_id() + "\nGPS:\n%s", str(data))
    #localizer.updateIMU(imu)
def imuCallback(data):
    #global localizer
    rospy.loginfo(rospy.get_caller_id() + "\nIMU:\n%s", str(data))
    #localizer.updateGPS(data)
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('localization', anonymous=True)

    rospy.Subscriber("gps_data", GPSData, gpsCallback)
    rospy.Subscriber("imu_data", IMUData, imuCallback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
