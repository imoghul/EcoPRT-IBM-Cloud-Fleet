from MPU6050 import *
from time import sleep
import numpy as np

MPU_Init()
Ax, Ay, Az, Gx, Gy, Gz = getIMUData()

while True:
    Ax, Ay, Az, Gx, Gy, Gz = getIMUData()
    print(Ax)
    sleep(1)
