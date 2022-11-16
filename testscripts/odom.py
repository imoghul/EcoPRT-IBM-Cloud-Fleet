from MPU6050 import *
from time import *
from imuController import *
import numpy as np
import matplotlib.pyplot as plt

samples = 200

plt.axis([0,samples,-.2,.2])
controller = IMUController()
controller.start()
average = 0

for t in range(samples):
    plt.scatter(t,controller.Vx,color="red")
    #plt.scatter(t,controller.Ax,color="blue")
    #plt.pause(.000005)
    print(controller.Ax)
    average += controller.Ax
plt.show()
print(average/samples)
