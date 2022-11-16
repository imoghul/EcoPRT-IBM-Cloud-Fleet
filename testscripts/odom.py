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
Ax = []
AxRaw  =[]
Vx = []
for t in range(samples):
    #plt.stem(t,controller.Vx,color="red")
    #plt.stem(t,controller.Ax)#,color="blue")
    #plt.pause(.000005)
    time.append(t)
    Ax.append(controller.Ax)
    AxRaw.append(controller.AxRaw)
    Vx.append(controller.Vx)
    print(controller.Ax)
    average += controller.Ax
plt.plot(time,Ax,color="blue")
plt.plot(time,Vx,color="red")
plt.show()
print(average/samples)
