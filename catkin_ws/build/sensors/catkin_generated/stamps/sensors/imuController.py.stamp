from sensors.MPU6050 import *
import time
import threading
import rospy
from sensors.msg import IMUData
#class IMUData():
#    def __init__(self,AxCalib,AyCalib,AzCalib,Ax,Ay,Az,AxRaw,AyRaw,AzRaw,Vx,Vy,Vz,Gx,Gy,Gz,currTime):
#        self.AxCalib = AxCalib
#        self.AyCalib = AyCalib
#        self.AzCalib = AzCalib
#        self.Ax = Ax
#        self.Ay = Ay
#        self.Az = Az
#        self.AxRaw = AxRaw
#        self.AyRaw = AyRaw
#        self.AzRaw = AzRaw
#        self.Vx = Vx
#        self.Vy = Vy
#        self.Vz = Vz
#        self.Gx = Gx
#        self.Gy = Gy
#        self.Gz = Gz
#        self.currTime = currTime
class Buffer():
    vals = []
    def __init__(self, nums, preload):
        if(nums!=len(preload)):
            raise Exception("length of preload doesn't match")
        self.vals = preload
    def push(self,val):
        self.vals = [val]+self.vals[0:-1]
    def average(self):
        return sum(self.vals)/len(self.vals)

class IMUController():
    def __init__(self):
        #rospy.init_node("IMU_Data",anonymous=False)
        self.pub = rospy.Publisher("imu_data",IMUData,queue_size=10)
        MPU_Init()

        self.data = IMUData()#(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
       
        self.data.AxCalib = 0
        self.data.AyCalib = 0
        self.data.AzCalib = 0
        self.data.Ax = 0
        self.data.Ay = 0
        self.data.Az = 0
        self.data.AxRaw = 0
        self.data.AyRaw = 0
        self.data.AzRaw = 0
        self.data.Vx = 0
        self.data.Vy = 0
        self.data.Vz = 0
        self.data.Gx = 0
        self.data.Gy = 0
        self.data.Gz = 0
        self.data.currTime = 0

        self.AxBuffer = None
        self.AyBuffer = None
        self.AzBuffer = None

        self.BUFFER_LEN = 25

        self.calibrate()
        self.refereshIMUData()



        self.thread = threading.Thread(target = self.run)

    def calibrate(self,samples=100):
        print("CALIBRATNG...")
        sumAx = []
        sumAy = []
        sumAz = []
        for i in range(samples):
            Ax, Ay,Az,Gx,Gy,Gz = getIMUData()
            sumAx.append(Ax)
            sumAy.append(Ay)
            sumAz.append(Az)
        self.data.AxCalib = sum(sumAx)/len(sumAx)
        self.data.AyCalib = sum(sumAy)/len(sumAy)
        self.data.AzCalib = sum(sumAz)/len(sumAz)

        self.AxBuffer = Buffer(self.BUFFER_LEN,sumAx[-self.BUFFER_LEN:])
        self.AyBuffer = Buffer(self.BUFFER_LEN,sumAy[-self.BUFFER_LEN:])
        self.AzBuffer = Buffer(self.BUFFER_LEN,sumAz[-self.BUFFER_LEN:])


        print("X: %f\tY: %f\tZ: %f"%(self.data.AxCalib,self.data.AyCalib, self.data.AzCalib))
    def refereshIMUData(self):
        Ax,Ay,Az,Gx,Gy,Gz = getIMUData()


        self.data.currTime = time.time()

        self.data.AxRaw = Ax-self.data.AxCalib
        self.data.AyRaw = Ay-self.data.AyCalib
        self.data.AzRaw = Az-self.data.AzCalib

        self.AxBuffer.push(self.data.AxRaw)
        self.AyBuffer.push(self.data.AyRaw)
        self.AzBuffer.push(self.data.AzRaw)

        self.data.Ax = self.AxBuffer.average()#Ax-self.AxCalib
        self.data.Ay = self.AyBuffer.average()#Ay-self.AyCalib
        self.data.Az = self.AzBuffer.average()#Az-self.AzCalib
        self.data.Gx = Gx
        self.data.Gy = Gy
        self.data.Gz = Gz

    def calc(self):
        origAx,origAy,origAz,origGx,origGy,origGz,origTime = self.data.Ax,self.data.Ay,self.data.Az,self.data.Gx,self.data.Gy,self.data.Gz,self.data.currTime

        self.refereshIMUData()

        timeDiff = self.data.currTime-origTime
        self.data.Vx = self.data.Vx+timeDiff*(origAx+self.data.Ax)/2
        self.data.Vy = self.data.Vy+timeDiff*(origAy+self.data.Ay)/2
        self.data.Vz = self.data.Vz+timeDiff*(origAz+self.data.Az)/2

        self.pub.publish(self.data)
    def run(self):
        while True:
            self.calc()

    def start(self):
        self.thread.start()

    def end(self):
        self.thread.terminate()
