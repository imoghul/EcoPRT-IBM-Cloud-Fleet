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
def queueScaling(prevSpeed, speed, deleting, dataQueue):
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
		return delete
	# if the vehicle is going faster, we need less data points
	elif speed > prevSpeed:
		delete = (speed - prevSpeed) * 2 # delete 2 times the entries per speed level over the previous speed
		return delete
	# if the vehicle is going the same speed as before, check here
	else:
		# if the queue's are the same size, then we just need to maintain it, pop an old point, add a new one
		# the first if statement should catch the array length so it doesn't miss the fact that if we were adding ones
		# and got to an odd number, if we start going back an even amount we won't miss the correct comparison
		if newLength > oldLength - delete && newLength =< oldLength + delete:
			delete = 1
			return delete
		# if the lengths are different, maintain whatever previous course the program was on until the lengths match
		else:
			return delete


def processIMU(thresh,accelData):
	duration = 0
	magnitude = 0.0
	max = 0.0
	qualityScore = 0

	# Determine the severity, duration, and max values
	for point in accelData:
		if point > 0.01:
			duration += 1
			magnitude += abs(accelData[point])
			if abs(accelData[point]) > max:
				max = abs(accelData[point])
		#code might be missing here for the else statement
		####insert code
	severity = magnitude / duration

	# Determine quality score based on threshold values
	if thresh == "high":
		qualityScore = (1000 * severity + 400 * duration + 100 * max)/1500
	elif thres == "low for time":
		qualityScore = (400 * severity + 1000 * duration + 100 * max)/1500

	# more testing will need to be done here to know how best to
	# normalize the road score data
	qualityScore = round(qualityScore * 100,0)

	return qualityScore

controller = IMUController()
controller.start()
print("controller started")
drift = [[0.0000060728,0.0013608],[0.0000031578,-0.00030711],[-0.000012169,0.00021297]]
Az = []
Gx = []
Gy = []
absAz = []
absGx = []
absGy = []
duration = 0.0
pointSend = 0
pointCounter = 0
roadScore = 0
sumAz = 0
sumGx = 0
sumGy = 0
perviousSpeed = 0
logging = False
sendData = False
checkDuration = False
threshold = None

while True:
	# populate the queue
	# need to check how frequently the ros nod is publishing data
	if len(Az) < 300:
		Az.append(controller.Az)
		Gx.append(controller.Gx)
		Gy.append(controller.Gy)
		absAz.append(abs(controller.Az))
		absGx.append(abs(controller.Gx))
		absGy.append(abs(controller.Gy))
		#print("queue smaller than 300") # debug line
		#print(len(Az))			 # debug line
	else:
		Az.popleft()
		Gx.popleft()
		Gy.popleft()
		absAz.popleft()
		absGx.popleft()
		absGy.popleft()
		Az.append(controller.Az)
		Gx.append(controller.Gx)
		Gy.append(controller.Gy)
		absAz.append(controller.Az)
		absGx.append(controller.Gx)
		absGy.append(controller.Gy)
		print("queue at 3000")

	# determine the sum of the magnitude of imu data
	if len(absAz)< 500:
		sumAz += abs(controller.Az)
		sumGx += abs(controller.Gx)
		sumGy += abs(controller.Gy)
	else:
		index = len(absAz) - 500
		sumAz = sumAz + abs(controller.Az) - absAz[index]
		sumGx = sumGx + abs(controller.Gx) - absGx[index]
		sumGy = sumGy + abs(controller.Gy) - absGy[index]
	print(sumAz)

	# count down the number of instances
	if pointCounter != 0:
		pointCounter -= 1
	# if the number of data points is done being logged,
	# set the flag to send the data
	elif pointCounter == 0 and logging:
		sendData = True
		logging = False

	# Check for rough road
	# Need to account for gyroscope measurements in the if statements.
	if abs(controller.Az) > 0.03 and pointCounter == 0:
		threshold = "high"
		pointCounter = queueScaling(controller.Vx)
		pointSend = 2 * pointCounter
		logging = True
		print("big bump")
	elif abs(controller.Az) > 0.01 and duration >= 0.5 and pointCounter == 0:
		threshold = "low for time"
		pointCounter = queueScaling(controller.Vx)
		pointSend = 2 * pointCounter
		logging = True
		print("rough road")
	elif sumAz/500 > 0.008 and len(Az) > 500:
		durration += 0.001
		print("counting")
	else:
		durration = 0
		print("not counting")

	# Check if data needs to be sent
	if sendData:
		roadScore = processIMU(threshold,Az[-pointSend:])
#		putDataToCloud({"road quality score":roadScore,"IMU Data":Az})
# uncomment the above line when ready to send data to the cloud
		sendData = False
		run = False
		print("Fake sent the data!")

print("Completed task.")
controller.end()
