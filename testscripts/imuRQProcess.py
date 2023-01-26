from imuController import *
import time
import numpy as np
from invoke import *
import collections, itertools

# this function will determine the number of additional elements needed before
# sending the data to the cloud after processing
#~~~~~~~~~
# CHECK UNITS ON VELOCITY FROM IMU DATA!!!~~~!!!
#~~~~~~~~~

# This function will compare current and previous speed to determine how the queue needs to scale
# it returns a value by which to delete entries from the queue
def queueScaling(prevSpeed, speed, delete, dataQueue):
	speed *= 2.23694 # convert speed from m/s to mph
	oldLength = len(dataQueue)
	newLength = 0
	
	#sets the speed value for comparison with the previous speed
	if speed < 5:
		speed = 0
		newLength = 150 # this should be 3 full seconds of data
	elif speed < 10:
		speed = 1
		newLength = 117 # this should be 2.33 seconds of data
	elif speed < 15: 
		speed = 2
		newLength = 83 # this should be 1.67 seconds of data
	else:
		speed = 3
		newLength = 50 # this should be 1 full second of data
	
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
		if newLength > oldLength - delete and newLength <= oldLength + delete:
			delete = 1
			return delete, speed
		# if the lengths are different, maintain whatever previous course the program was on until the lengths match
		else:
			return delete, speed

def roadQualityScore(accelData, gyroData1, gyroData2):
	# compute the average acceleration and rotation for the given period
	averageAccel = sum(accelData) / len(accelData)
	averageGyro1 = sum(gyroData1) / len(gyroData1)
	averageGyro2 = sum(gyroData2) / len(gyroData2)

	# road quality score
	roadScore = (0.8 * averageAccel + 0.1 * averageGyro1 + 0.1 * averageGyro2) * 100
	return roadScore

controller = IMUController()
controller.start()
print("controller started")
drift = [[0.0000060728,0.0013608],[0.0000031578,-0.00030711],[-0.000012169,0.00021297]]
# Az = []
# Gx = []
# Gy = []
absAz = []
absGx = []
absGy = []
pointCounter = 0
roadScore = 0
# sumAz = 0
# sumGx = 0
# sumGy = 0
previousSpeed = 0
del_value = 0
startingUp = True

while True:
	# populate the queue
	# need to check how frequently the ros node is publishing data

	#determine how to dynamically scale the queue
	del_value, previousSpeed = queueScaling(previousSpeed, controller.Vx, del_value, absAz)

	# just get the first 300 data points at start up, then dynamically scale the queue
	if startingUp:
		# populate the acceleration and rotation arrays
		# Az.append(controller.Az)
		# Gx.append(controller.Gx)
		# Gy.append(controller.Gy)

		# populate the acceleration and rotation magnitude arrays
		absAz.append(abs(controller.Az))
		absGx.append(abs(controller.Gx))
		absGy.append(abs(controller.Gy))

		#track the cumulative acceleration and rotation data
		# sumAz += abs(controller.Az)
		# sumGx += abs(controller.Gx)
		# sumGy += abs(controller.Gy)

		#print("queue smaller than 300") # debug line
		#print(len(Az))			 # debug line
		if len(absAz) >= 300:
			startingUp = False
	else:
		# # moving cummulative sum based on scaled queue
		# sumAz = sumAz + abs(controller.Az) - sum(absAz[0:del_value])
		# sumGx = sumGx + abs(controller.Gx) - sum(absAz[0:del_value])
		# sumGy = sumGy + abs(controller.Gy) - sum(absAz[0:del_value])

		# delete values in the arrays according to scaled queue 
		# del Az[0:del_value]
		# del Gx[0:del_value]
		# del Gy[0:del_value]
		del absAz[0:del_value]
		del absGx[0:del_value]
		del absGy[0:del_value]

		# add new acceleration and rotation data points
		# Az.append(controller.Az)
		# Gx.append(controller.Gx)
		# Gy.append(controller.Gy)

		absAz.append(controller.Az)
		absGx.append(controller.Gx)
		absGy.append(controller.Gy)
		# print("queue at 300")

	# count down to next transmission
	if pointCounter != 0:
		pointCounter -= 1
	# half a second has gone by send the data
	else:
		pointCounter = 50
		roadScore = roadQualityScore(absAz[-1:50], absGx[-1:50], absGy[-1:50])
		# putDataToCloud({"road quality score":roadScore,"IMU Data":Az})
		# uncomment the above line when ready to send data to the cloud
		run = False
		print("Fake sent the data!")

print("Completed task.")
controller.end()
