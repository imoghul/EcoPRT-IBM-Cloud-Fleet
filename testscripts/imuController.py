from MPU6050 import *
import time
import threading

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
        MPU_Init()

        self.BUFFER_LEN = 25

        self.AxCalib = 0
        self.AyCalib = 0
        self.AzCalib = 0
        self.GxCalib = 0
        self.GyCalib = 0
        self.GzCalib = 0
        self.Vx = 0
        self.Vy = 0
        self.Vz = 0

        self.AxBuffer = None
        self.AyBuffer = None
        self.AzBuffer = None
        self.GxBuffer = None
        self.GyBuffer = None
        self.GzBuffer = None

        self.calibrate()
        self.refereshIMUData()

        self.thread = threading.Thread(target = self.run)

    def calibrate(self,samples=100):
        print("CALIBRATNG...")
        sumAx = []
        sumAy = []
        sumAz = []
        sumGx = []
        sumGy = []
        sumGz = []

        for i in range(samples):
            Ax,Ay,Az,Gx,Gy,Gz = getIMUData()
            sumAx.append(Ax)
            sumAy.append(Ay)
            sumAz.append(Az)
            sumGx.append(Gx)
            sumGy.append(Gy)
            sumGz.append(Gz)

        self.AxCalib = sum(sumAx)/len(sumAx)
        self.AyCalib = sum(sumAy)/len(sumAy)
        self.AzCalib = sum(sumAz)/len(sumAz)
        self.GxCalib = sum(sumGx)/len(sumGx)
        self.GyCalib = sum(sumGy)/len(sumGy)
        self.GzCalib = sum(sumGz)/len(sumGz)

        self.AxBuffer = Buffer(self.BUFFER_LEN,sumAx[-self.BUFFER_LEN:])
        self.AyBuffer = Buffer(self.BUFFER_LEN,sumAy[-self.BUFFER_LEN:])
        self.AzBuffer = Buffer(self.BUFFER_LEN,sumAz[-self.BUFFER_LEN:])
        self.GxBuffer = Buffer(self.BUFFER_LEN,sumGx[-self.BUFFER_LEN:])
        self.GyBuffer = Buffer(self.BUFFER_LEN,sumGy[-self.BUFFER_LEN:])
        self.GzBuffer = Buffer(self.BUFFER_LEN,sumGz[-self.BUFFER_LEN:])

        print("X: %f\tY: %f\tZ: %f"%(self.AxCalib,self.AyCalib, self.AzCalib))

    def refereshIMUData(self):
        Ax,Ay,Az,Gx,Gy,Gz = getIMUData()

        self.currTime = time.time()

        self.AxRaw = (Ax-self.AxCalib)/9.81
        self.AyRaw = (Ay-self.AyCalib)/9.81
        self.AzRaw = (Az-self.AzCalib)/9.81
        self.GxRaw = (Gx-self.GxCalib)/9.81
        self.GyRaw = (Gy-self.GyCalib)/9.81
        self.GzRaw = (Gz-self.GzCalib)/9.81

        self.AxBuffer.push(self.AxRaw)
        self.AyBuffer.push(self.AyRaw)
        self.AzBuffer.push(self.AzRaw)
        self.GxBuffer.push(self.GxRaw)
        self.GyBuffer.push(self.GyRaw)
        self.GzBuffer.push(self.GzRaw)

        self.Ax = self.AxBuffer.average()
        self.Ay = self.AyBuffer.average()
        self.Az = self.AzBuffer.average()
        self.Gx = self.GxBuffer.average()
        self.Gy = self.GyBuffer.average()
        self.Gz = self.GzBuffer.average()

    def calc(self):
        origAx,origAy,origAz,origGx,origGy,origGz,origTime = self.Ax,self.Ay,self.Az,self.Gx,self.Gy,self.Gz,self.currTime

        self.refereshIMUData()

        timeDiff = self.currTime-origTime
        self.Vx = self.Vx+timeDiff*(origAx+self.Ax)/2
        self.Vy = self.Vy+timeDiff*(origAy+self.Ay)/2
        self.Vz = self.Vz+timeDiff*(origAz+self.Az)/2

    def run(self):
        while True:
            self.calc()

    def start(self):
        self.thread.start()

    def end(self):
        self.thread.terminate()

#if(__name__=="__main__"):
#    controller = IMUController()
#    controller.start()
#    while(True):
#        print(controller.Ax)
