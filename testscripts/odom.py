from MPU6050 import *
from time import *
from imuController import *
import numpy as np
import matplotlib.pyplot as plt

samples = 1000

plt.axis([0,samples,-2,2])
controller = IMUController()
controller.start()
average = 0

time = []
A = []
ARaw  =[]
V = []
for t in range(samples):
    #plt.stem(t,controller.Vx,color="red")
    #plt.stem(t,controller.Ax)#,color="blue")
    #plt.pause(.000005)
    time.append(t)
    A.append(controller.Az)
    ARaw.append(controller.AzRaw)
    V.append(controller.Vz)
    print(controller.Az)
    average += controller.Az
plt.plot(time,A,color="blue")
plt.plot(time,V,color="red")
plt.show()
print(average/samples)
