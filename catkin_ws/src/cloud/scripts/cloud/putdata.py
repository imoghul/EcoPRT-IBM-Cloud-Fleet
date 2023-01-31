#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from roadquality.msg import RoadQualityScore
from cloud.cloudQueue import *
import threading
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "\nRoad Defect:\n%s\n", str(data))

def run():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('cloud_communication', anonymous=True)

    rospy.Subscriber("road_quality_score", RoadQualityScore, CloudQueue.addToQueue)
    thread = threading.Thread(target = CloudQueue.main)
    thread.start()
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    run()
