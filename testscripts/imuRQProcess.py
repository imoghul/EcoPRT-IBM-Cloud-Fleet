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
def queueScaling(speed):
	if speed * 2.23694 < 5:    # send the full 3 seconds of data
		return 1500
	elif speed * 2.23694 < 10: # send 2.25 seconds of data
		return 1125
	elif speed * 2.23694 < 15: # send 1.5 seconds of data
		return 750
	else:			   # send 1 second of data
		return 500

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
	severity = magnitude / duration

	# Determine quality score based on threshold values
	if thresh == "high":
		qualityScore = (1000 * severity + 500 * duration + 100 * max)/1600
	elif thres == "low for time":
		qualityScore = (500 * severity + 1000 * duration + 100 * max)/1600

	# more testing will need to be done here to know how best to
	# normalize the road score data
	qualityScore = round(qualityScore / 0.01,0)

	return qualityScore

controller = IMUController()
controller.start()
print("controller started")
run = True
drift = [[0.0000060728,0.0013608],[0.0000031578,-0.00030711],[-0.000012169,0.00021297]]
Az = collections.deque()
Gx = collections.deque()
Gy = collections.deque()
absAz = collections.deque()
absGx = collections.deque()
absGy = collections.deque()
duration = 0.0
pointSend = 0
pointCounter = 0
roadScore = 0
sumAz = 0
sumGx = 0
sumGy = 0
logging = False
sendData = False
checkDuration = False
threshold = None

while run:
	# populate the queue
	if len(Az) < 3000:
		Az.append(controller.Az)
		Gx.append(controller.Gx)
		Gy.append(controller.Gy)
		absAz.append(abs(controller.Az))
		absGx.append(abs(controller.Gx))
		absGy.append(abs(controller.Gy))
		print("queue smaller than 3000")
		print(len(Az))
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
