#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from cloud.msg import Heartbeat
from roadquality.msg import RoadQualityScore
from cloud.cloudQueue import *
import threading
from config.config import *
from cloud.toJson import *
import json

heartBeatPub = rospy.Publisher("heartbeat_rx",String,queue_size=10)#rospy.Publisher("heartbeat_rx",RoadQualityScore,queue_size = 10)

def callback(data):
    global heartBeatPub
    try:
        #for i in data.json()["Scores In Range"]:
            d = json.dumps(data.json()["Scores In Range"])
            heartBeatPub.publish(d)
        #rqScoresInRange = [jsonToRqScore(i) for i in data.json()["Scores In Range"]
        #heartBeatPub.publish(rqScoresInRange)
    except : print("fail")
def run():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('heartbeat', anonymous=True)

    heartbeat = CloudQueue("heartbeat",False,heartBeatToJson,heartbeatUrl,tDiff=.5,callback=callback)

    rospy.Subscriber("heartbeat_tx", Heartbeat, heartbeat.addToQueue)
    
    heartbeat.start()# spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    run()
