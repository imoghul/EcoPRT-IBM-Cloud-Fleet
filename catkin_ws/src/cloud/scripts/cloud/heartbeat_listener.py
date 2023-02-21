#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from cloud.msg import Heartbeat
from roadquality.msg import RoadQualityScore
from cloud.cloudQueue import *
import threading
from cloud.confidential import *
from cloud.toJson import *


def callback(data):
    rospy.loginfo("Scores In Range:\n"+str(data))
def run():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('heartbeat_listener', anonymous=True)

    rospy.Subscriber("heartbeat_rx", RoadQualityScore, callback)
    
    rospy.spin()

if __name__ == '__main__':
    run()
