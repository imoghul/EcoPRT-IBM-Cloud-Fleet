#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String
from sensors.gpsController import *
from sensors.imuController import * 



def talker():
    gpsTopic = rospy.Publisher('gps', String, queue_size=10) # chatter is the topic
    imuTopic = rospy.Publisher('imu', String, queue_size=10)

    rospy.init_node('Sensor_Node', anonymous=True) # talker is the node
    rate = rospy.Rate(10) # 10hz

    gps = GPSController()
    imu = IMUController()

    gps.start()
    imu.start()
    while not rospy.is_shutdown():
        gps_str = "%s\n%d\n%d" % (gps.satTime,gps.lat,gps.lon)
        imu_str = "%d\n%d\n%d" % (imu.Ax,imu.Ay,imu.Az)
        rospy.loginfo(gps_str)
        rospy.loginfo(imu_str)
        gpsTopic.publish(gps_str)
        imuTopic.publish(imu_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
