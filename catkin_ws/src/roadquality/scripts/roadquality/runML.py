#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from positioning.msg import Position
import threading
from config.config import modelAbsPath
from tensorflow import keras#from keras.models import load_model
from tensorflow.keras.optimizers import Adam
import numpy as np
from roadquality.msg import MachineLearningScore
import tensorflow as tf
buff = []#Buffer(240,[[[[0]]*6]*240])
model = None
lastPos = None
def feedML(x):
    global buff, lastPos
    data = [[x.imu.Ax],[x.imu.Ay],[x.imu.Az],[x.imu.Gx],[x.imu.Gy],[x.imu.Gz]]
    buff.append(data) 
    lastPos = x
@tf.autograph.experimental.do_not_convert
def runML():
    global model,buff,lastPos
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node("ml_calculation", anonymous=True)

    rospy.Subscriber("position", Position, feedML)
    pub = rospy.Publisher("ml_score", MachineLearningScore, queue_size = 10)

    model = keras.models.load_model(modelAbsPath, compile=False)
    print("model loaded")#(model)
    model.compile(optimizer=Adam(learning_rate = 0.001), loss = 'categorical_crossentropy', metrics = ['accuracy'])
    print("model compiled")
    
    
    while not rospy.is_shutdown():
        if(len(buff)>=240):
            mlbuff = np.array([buff.copy()[0:240]])
            prediction = None
            if(model!=None):
                prediction = list(model.predict(mlbuff))
            
                mlScore = MachineLearningScore()
                mlScore.pos = lastPos
                mlScore.score = prediction.index(max(prediction))
                mlScore.type = ""
                print(mlScore)
                pub.publish(mlScore) 
            buff = []




    # spin() simply keeps python from exiting until this node is stopped


if __name__ == "__main__":
    runML()
