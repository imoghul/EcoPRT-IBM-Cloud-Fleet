from MPU6050 import *
import time
from imuController import *
import numpy as np
import matplotlib.pyplot as plt

samples = 1000

#plt.axis([0,samples,-2,2])
controller = IMUController()
controller.start()
average = 0

_time = []
A = []
ARaw  =[]
V = []
origTime = time.time()
for t in range(samples):
    #plt.stem(t,controller.Vx,color="red")
    #plt.stem(t,controller.Ax)#,color="blue")
    #plt.pause(.000005)
    _time.append(controller.currTime)
    A.append(controller.Az)
    ARaw.append(controller.AzRaw)
    V.append(controller.Vz)
    print("diff: ",time.time()-origTime)
    origTime=time.time()
    average += controller.Az
plt.plot(_time,A,color="blue")
plt.plot(_time,V,color="red")
plt.show()
print(average/samples)

