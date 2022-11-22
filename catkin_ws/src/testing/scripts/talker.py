#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
import test #from test import Test 
t = test.Test()
def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10) # chatter is the topic
    rospy.init_node('talker', anonymous=True) # talker is the node
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
