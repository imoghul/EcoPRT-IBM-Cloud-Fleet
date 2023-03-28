#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from roadquality.msg import RoadQualityScore
from cloud.cloudQueue import *
import threading
from config.config import *
from cloud.toJson import *

def run():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('cloud_communication', anonymous=True)

    eventIMU = CloudQueue("eventIMU",True,rqScoreToJson,putDataUrl,tDiff=.5)

    rospy.Subscriber("road_quality_score", RoadQualityScore, eventIMU.addToQueue)
    
    #thread = threading.Thread(target = eventIMU.main)
    eventIMU.start()#thread.start()
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    run()
