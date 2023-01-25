#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensors.msg import IMUData
from sensors.msg import GPSData
def imu_callback(data):
    pass#rospy.loginfo(rospy.get_caller_id() + "\nIMU:\n%s\n", str(data))
def gps_callback(data):
    rospy.loginfo(rospy.get_caller_id() + "\nGPS:\n%s\n", str(data))

def runLocalizer():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('sensors_listener', anonymous=True)

    rospy.Subscriber("imu_data", IMUData, imu_callback)
    rospy.Subscriber("gps_data", GPSData, gps_callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    runLocalizer()
