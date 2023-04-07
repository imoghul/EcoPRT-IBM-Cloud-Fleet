#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from roadquality.msg import RoadQualityScore, MachineLearningScore
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
    rospy.init_node("cloud_communication", anonymous=True)

    eventIMU = CloudQueue("eventIMU", True, rqScoreToJson, putDataUrl,  tDiff=0.5, dbName = "sensor-data")
    mlStream = CloudQueue("mlStream", True, mlScoreToJson, putDataUrl, tDiff=0.5, dbName = "ml-data")
    rospy.Subscriber("road_quality_score", RoadQualityScore, eventIMU.addToQueue)
    rospy.Subscriber("machine_learning_score", MachineLearningScore, mlStream.addToQueue)

    # thread = threading.Thread(target = eventIMU.main)
    eventIMU.start()  # thread.start()
    mlStream.start()
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == "__main__":
    run()
