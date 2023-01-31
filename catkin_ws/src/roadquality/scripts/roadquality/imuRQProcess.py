import rospy
import time
import numpy as np
import collections, itertools
from positioning.msg import Position
from sensors.msg import *
from roadquality.msg import RoadQualityScore 
# this function will determine the number of additional elements needed before
# sending the data to the cloud after processing
#~~~~~~~~~
# CHECK UNITS ON VELOCITY FROM IMU DATA!!!~~~!!!
#~~~~~~~~~
publisher = rospy.Publisher("road_quality_score",RoadQualityScore,queue_size=10)
# This function will compare current and previous speed to determine how the queue needs to scale
# it returns a value by which to delete entries from the queue
def queueScaling(prevSpeed, _speed, delete, dataQueue):
    speed = _speed * 2.23694 # convert speed from m/s to mph
    oldLength = len(dataQueue)
    newLength = 0

    # for debugging
    # print("Speed of IMU: " + str(speed))
    max_speed = 0.018

    #sets the speed value for comparison with the previous speed
    if abs(speed) < max_speed * 0.25:
        speed = 0
        newLength = 300 # this should be 3 full seconds of data
    elif abs(speed) < max_speed * 0.5:
        speed = 1
        newLength = 234 # this should be 2.33 seconds of data
    elif abs(speed) < max_speed * 0.75:
        speed = 2
        newLength = 166 # this should be 1.67 seconds of data
    else:
        speed = 3
        newLength = 100 # this should be 1 full second of data

    # If the vehicle is going slower we need more data points
    if speed < prevSpeed:
        delete = 0 # stop deleting entries in order to send more data
        return delete, speed
    # if the vehicle is going faster, we need less data points
    elif speed > prevSpeed:
        delete = (speed - prevSpeed) * 2 # delete 2 times the entries per speed level over the previous speed
        return delete, speed
    # if the vehicle is going the same speed as before, check here
    else:
        # if the queue's are the same size, then we just need to maintain it, pop an old point, add a new one
        # the first if statement should catch the array length so it doesn't miss the fact that if we were adding ones
        # and got to an odd number, if we start going back an even amount we won't miss the correct comparison
        if newLength > oldLength - 7 and newLength <= oldLength + 7:
            delete = 1
            return delete, speed
        # if the lengths are different, maintain whatever previous course the program was on until the lengths match
        else:
            return delete, speed

def roadQualityScore(accelData, gyroData1, gyroData2):
    if len(accelData) != 0:
        # normalize the data
        accelData = [i/0.3 for i in accelData]
        gyroData1 = [i/0.3 for i in gyroData1]
        gyroData2 = [i/0.3 for i in gyroData2]
        #print(accelData[:10])
        # compute the average acceleration and rotation for the given period
        averageAccel = sum(accelData) / len(accelData)
        averageGyro1 = sum(gyroData1) / len(gyroData1)
        averageGyro2 = sum(gyroData2) / len(gyroData2)
        #print("Accel score: " + str(averageAccel))
        #print("Gyro1 score: " + str(averageGyro1))
        #print("Gyro2 score: " + str(averageGyro2))
        # road quality score
        roadScore = (0.8 * averageAccel + 0.1 * averageGyro1 + 0.1 * averageGyro2)
        return roadScore
    else:
        #print("accel array has no entries")
        return 0

#print("controller started")
drift = [[0.0000060728,0.0013608],[0.0000031578,-0.00030711],[-0.000012169,0.00021297]]
absAz = []
absGx = []
absGy = []
pointCounter = 50
roadScore = 0
previousSpeed = 0
del_value = 0
startingUp = True
data = None #Position(GPSData(0,0,0),IMUData(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))

def getData(d):
    global data
    data = d


def process():
    while not rospy.is_shutdown():runProcess()
def runProcess():
    global imuData,absAz,absGx,absGy, pointCounter, roadScore, previousSpeed,del_value,startingUp,data,drift
    # populate the queue
    if(data==None):
        #print("waiting")
        return
    #determine how to dynamically scale the queue
    del_value, previousSpeed = queueScaling(previousSpeed, data.imu.Vx, del_value, absAz)
    # print("Current rate of management: " + str(del_value)) # debug line

    # just get the first 300 data points at start up, then dynamically scale the queue
    if startingUp:
        # populate the acceleration and rotation magnitude arrays
        absAz.append(abs(data.imu.Az))
        absGx.append(abs(data.imu.Gx))
        absGy.append(abs(data.imu.Gy))
        # print("Current length of Arrays: " + str(len(absAz)))

        if len(absAz) >= 300:
            startingUp = False
            #print("Done starting up: " + str(not startingUp)) # debug line
    else:
        # delete values in the arrays according to scaled queue
        del absAz[0:del_value]
        del absGx[0:del_value]
        del absGy[0:del_value]

        # add new acceleration and rotation data points
        absAz.append(abs(data.imu.Az))
        absGx.append(abs(data.imu.Gx))
        absGy.append(abs(data.imu.Gy))
        # print("Current length of Arrays: " + str(len(absAz)))

    # count down to next transmission
    if pointCounter != 0:
        pointCounter -= 1
    # half a second has gone by send the data
    else:
        pointCounter = 50
        roadScore = roadQualityScore(absAz[-50:], absGx[-50:], absGy[-50:])
        # putDataToCloud({"road quality score":roadScore,"IMU Data":Az})
        # uncomment the above line when ready to send data to the cloud
        #print("Fake sent the data!\nRoad quality score: " + str(roadScore))
        if roadScore>=1:publisher.publish(RoadQualityScore(data,roadScore))
