#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from positioning.msg import Position
from positioning.localizer import Localizer
from cloud.msg import Heartbeat
from datetime import datetime

currHb = Heartbeat(Position(), str(datetime.now()), 0.5)


def callback(data):
    global currHb
    currHb.pos = data
    currHb.time = str(datetime.now())
    currHb.distance = 0.5


def runLocalizer():
    global currHb
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.

    rospy.init_node("localization_listener", anonymous=True)
    rate = rospy.Rate(.5)#(0.2)
    rospy.Subscriber("position", Position, callback)
    pub = rospy.Publisher("heartbeat_tx", Heartbeat, queue_size=10)
    # spin() simply keeps python from exiting until this node is stopped
    while not rospy.is_shutdown():
        pub.publish(currHb)
        rate.sleep()
    # rospy.spin()


if __name__ == "__main__":
    runLocalizer()
