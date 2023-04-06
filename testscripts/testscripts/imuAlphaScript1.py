# this script will gather data from the road test on 11/23/22
# Updating script for ML Model data collection on 3/3/2023
from imuController import *
import csv
import time
import signal
import sys

controller = IMUController()
controller.start()
file = open('ml_data_collect2.csv','w')
writer = csv.writer(file)

writer.writerow(["Beginning Data Collection"," "," "," "," "," "," "])

while True:
    data = [controller.Ax, controller.Ay, controller.Az, controller.Gx, controller.Gy, controller.Gz, time.time()]
    writer.writerow(data)

    orig_time = time.time()
    print(f"Current Accel Reading\nAx:  {controller.Ax} Ay: {controller.Ay} Az: {controller.Az} Gx: {controller.Gx} Gy: {controller.Gy} Gz: {controller.Gz} Time: {orig_time}")

    time.sleep(0.00833333) # taking 2 readings every frame

file.close()
print("File closed.\nPlease exit.\n\n")
controller.end()
