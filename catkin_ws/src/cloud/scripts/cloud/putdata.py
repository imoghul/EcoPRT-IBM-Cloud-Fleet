#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from roadquality.msg import RoadDefect 
from cloud.Queue import *
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "\nPosition:\n%s\n", str(data))

def runLocalizer():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('cloud_communication', anonymous=True)

    rospy.Subscriber("road_quality", RoadDefect, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    runLocalizer()
