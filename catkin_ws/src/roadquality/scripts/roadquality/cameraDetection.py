import cv2 as cv
import rospy
import numpy as np
import argparse
from config.config import *
import sys
import os.path
import random
import os
import glob
import operator
import time
from std_msgs.msg import Int32
from cv_bridge import CvBridge
import tensorflow._api.v2.compat.v1 as tf
from tqdm import tqdm
from sensor_msgs.msg import Image
tf.disable_v2_behavior()
image_size = 128
num_channels = 3

width = round(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
newHeight = int(round(height / 2))
graph = tf.Graph()
graphAQ = tf.Graph()
graphPQ = tf.Graph()
graphUQ = tf.Graph()
# 设置默认 TensorFlow 图
default_graph = tf.get_default_graph()
# 创建一个新的 TensorFlow 会话并恢复模型
with graph.as_default():
    saver = tf.train.import_meta_graph(surfaceTypeModel)#('roadsurfaceType-model.meta')
    y_pred = graph.get_tensor_by_name("y_pred:0")
    x = graph.get_tensor_by_name("x:0")
    y_true = graph.get_tensor_by_name("y_true:0")
    y_test_images = np.zeros((1, 3))

sess = tf.Session(graph=graph)
saver.restore(sess, tf.train.latest_checkpoint('typeCheckpoint/'))
# 加载沥青质量模型
with graphAQ.as_default():
    saverAQ = tf.train.import_meta_graph(asphaltQualityModel)#('roadsurfaceAsphaltQuality-model.meta')
    y_predAQ = graphAQ.get_tensor_by_name("y_pred:0")
    xAQ = graphAQ.get_tensor_by_name("x:0")
    y_trueAQ = graphAQ.get_tensor_by_name("y_true:0")
    y_test_imagesAQ = np.zeros((1, 3))

# 创建一个新的 TensorFlow 会话并恢复模型
sessAQ = tf.Session(graph=graphAQ)
saverAQ.restore(sessAQ, tf.train.latest_checkpoint('asphaltCheckpoint/'))
# 加载铺装道路质量模型
with graphPQ.as_default():
    saverPQ = tf.train.import_meta_graph(pavedQualityModel)#('roadsurfacePavedQuality-model.meta')
    y_predPQ = graphPQ.get_tensor_by_name("y_pred:0")
    xPQ = graphPQ.get_tensor_by_name("x:0")
    y_truePQ = graphPQ.get_tensor_by_name("y_true:0")
    y_test_imagesPQ = np.zeros((1, 3))
    # 创建一个新的 TensorFlow 会话并恢复模型
sessPQ = tf.Session(graph=graphPQ)
saverPQ.restore(sessPQ, tf.train.latest_checkpoint('pavedCheckpoint/'))
# 加载未铺装道路质量模型
with graphUQ.as_default():
    saverUQ = tf.train.import_meta_graph(unpavedQualityModel)#('roadsurfaceUnpavedQuality-model.meta')
    y_predUQ = graphUQ.get_tensor_by_name("y_pred:0")
    xUQ = graphUQ.get_tensor_by_name("x:0")
    y_trueUQ = graphUQ.get_tensor_by_name("y_true:0")
    y_test_imagesUQ = np.zeros((1, 2))
    # 创建一个新的 TensorFlow 会话并恢复模型
sessUQ = tf.Session(graph=graphUQ)
saverUQ.restore(sessUQ, tf.train.latest_checkpoint('unpavedCheckpoint/'))
pub = rospy.Publisher(image_prediction_publisher_name, Int32 ,queue_size = 10)
def predict(images):    
        global pub, y_pred, y_test_images, x, y_true, image_size, newHeight, height, width 
        images = CvBridge().imgmsg_to_cv2(images) 
        finalimg = images

        images = images[newHeight - 5:height - 50, 0:width]
        images = cv.resize(images, (image_size, image_size), 0, 0, cv.INTER_LINEAR)
        images = np.array(images, dtype=np.uint8)
        images = images.astype('float32')
        images = np.multiply(images, 1.0 / 255.0)

        x_batch = images.reshape(1, image_size, image_size, num_channels)

        feed_dict_testing = {x: x_batch, y_true: y_test_images}
        result = sess.run(y_pred, feed_dict=feed_dict_testing)

        outputs = [result[0, 0], result[0, 1], result[0, 2]]

        value = max(outputs)
        index = np.argmax(outputs)

        if index == 0:  # Asphalt
            label = 'Asphalt'
            prob = str("{0:.2f}".format(value))
            color = (0, 0, 0)
            x_batchAQ = images.reshape(1, image_size, image_size, num_channels)
            feed_dict_testingAQ = {xAQ: x_batchAQ, y_trueAQ: y_test_imagesAQ}
            resultAQ = sessAQ.run(y_predAQ, feed_dict=feed_dict_testingAQ)
            outputsQ = [resultAQ[0, 0], resultAQ[0, 1], resultAQ[0, 2]]
            valueQ = max(outputsQ)
            indexQ = np.argmax(outputsQ)
            if indexQ == 0:
                quality = 'Good'
            elif indexQ == 1:
                quality = 'Normal'
            else:
                quality = 'Poor'

        elif index == 1:  # Paved
            label = 'Paved'
            prob = str("{0:.2f}".format(value))
            color = (0, 255, 0)
            x_batchPQ = images.reshape(1, image_size, image_size, num_channels)
            feed_dict_testingPQ = {xPQ: x_batchPQ, y_truePQ: y_test_imagesPQ}
            resultPQ = sessPQ.run(y_predPQ, feed_dict=feed_dict_testingPQ)
            outputsQ = [resultPQ[0, 0], resultPQ[0, 1], resultPQ[0, 2]]
            valueQ = max(outputsQ)
            indexQ = np.argmax(outputsQ)
            if indexQ == 0:
                quality = 'Good'
            elif indexQ == 1:
                quality = 'Normal'
            else:
                quality = 'Poor'

        else:  # Unpaved
            label = 'Unpaved'
            prob = str("{0:.2f}".format(value))
            color = (255, 0, 0)
            x_batchUQ = images.reshape(1, image_size, image_size, num_channels)
            feed_dict_testingUQ = {xUQ: x_batchUQ, y_trueUQ: y_test_imagesUQ}
            resultUQ = sessUQ.run(y_predUQ, feed_dict=feed_dict_testingUQ)
            outputsQ = [resultUQ[0, 0], resultUQ[0, 1]]
            valueQ = max(outputsQ)
            indexQ = np.argmax(outputsQ)
            if indexQ == 0:
                quality = 'Good'
            else:
                quality = 'Poor'

        pub.publish(int(index*3 + indexQ))


sub  = rospy.Subscriber(raw_image_publisher_name, Image, predict )

rospy.spin()

sess.close()
sessAQ.close()
sessPQ.close()
sessUQ.close()


