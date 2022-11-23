from MPU6050 import *
from time import sleep
import numpy as np
from invoke import *

MPU_Init()
print("initialize")
sendingToCloud = dataStruct()
print("finished")
controller.end()
#while True:
 #   sendingToCloud = dataStruct()
 #   #Ax, Ay, Az, Gx, Gy, Gz = getIMUData()
 #   print(sendingToCloud)
 #   sleep(1)
