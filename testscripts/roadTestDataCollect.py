# this script will gather data from the road test on 11/23/22
from imuController import *
import csv
import time

controller = IMUController()
controller.start()

file = open('roadTestData.csv','w')
writer = csv.writer(file)

for i in range(100):
	data = [controller.Ax, controller.Ay, controller.Az, controller.Gx, controller.Gy, controller.Gz]
	writer.writerow(data)
	time.sleep(0.01)

file.close()
