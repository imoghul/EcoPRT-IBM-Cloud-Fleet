import time
import threading
import datetime
import rospy
from sensor_msgs.msg import Image
import math
from config.config import raw_image_publisher_name


class ImageController:
    def __init__(self):
        self.pub = rospy.Publisher("image_data", Image, queue_size=10)
        self.sub = rospy.Subscriber(
            raw_image_publisher_name, Image, self.refreshImageData
        )

    def refreshImageData(self, newImage):
        self.pub.publish(newImage)
