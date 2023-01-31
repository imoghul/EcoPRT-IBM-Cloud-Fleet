from MPU6050 import *
import time
from imuController import *
import numpy as np
import matplotlib.pyplot as plt

samples = 1500

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
	A.append(controller.Ax)
	ARaw.append(controller.AxRaw)
	V.append(controller.Vx)
	print("diff: ",time.time()-origTime)
	origTime=time.time()
	average += controller.Ax

del A[0:4]
del ARaw[0:4]
del V[0:4]
del _time[0:4]
samples -= 5

print(average/samples)
plt.plot(_time,A,color="blue")
plt.plot(_time,V,color="red")
plt.grid()
plt.show()
