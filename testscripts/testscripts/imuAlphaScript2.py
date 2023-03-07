# this script will gather data from the road test on 11/23/22
# Updating script for ML Model data collection on 3/3/2023
from imuController import *
import numpy as np
import time
import copy
import sys

controller = IMUController()
controller.start()

while True:
    accelBuffer = controller.AzBuffer.vals.copy()
    gyroxBuffer = controller.GxBuffer.vals.copy()
    gyroyBuffer = controller.GyBuffer.vals.copy()

    # normalize the data
    accelData = [i / 0.3 for i in accelBuffer]
    gyroxData = [i / 0.3 for i in gyroxBuffer]
    gyroyData = [i / 0.3 for i in gyroyBuffer]

    # compute the RMS value of the data
    accelS = np.square(accelData)
    gyroxS = np.square(gyroxData)
    gyroyS = np.square(gyroyData)

    accelMS = np.average(accelS)
    gyroxMS = np.average(gyroxS)
    gyroyMS = np.average(gyroyS)

    accelRMS = np.sqrt(accelMS)
    gyroxRMS = np.sqrt(gyroxMS)
    gyroyRMS = np.sqrt(gyroyMS)

    # value of road score
    roadQualityScore = 0.8 * accelRMS + 0.1 * gyroxRMS + 0.1 * gyroyRMS

    print(f"Z Accel Score: {accelRMS:.4f}    X Rot Score: {gyroxRMS:.4f}    Y Rot Score: {gyroxRMS:.4f}    RQ Score: {roadQualityScore:.4f}")

    if roadQualityScore > 0.95:
        print("This data would get sent to the cloud.")

    orig_time = time.time()

    time.sleep(0.01) # taking readings every frame

file.close()
print("File closed.\nPlease exit.\n\n")
controller.end()
