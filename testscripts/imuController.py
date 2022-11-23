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
    #AxCalib = 0
    #AyCalib = 0
    #AzCalib = 0
    def __init__(self):
        MPU_Init()

        self.BUFFER_LEN = 25

        self.AxCalib = 0
        self.AyCalib = 0
        self.AzCalib = 0
        self.Vx = 0
        self.Vy = 0
        self.Vz = 0

        self.AxBuffer = None
        self.AyBuffer = None
        self.AzBuffer = None

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
        self.AxCalib = sum(sumAx)/len(sumAx)
        self.AyCalib = sum(sumAy)/len(sumAy)
        self.AzCalib = sum(sumAz)/len(sumAz)

        self.AxBuffer = Buffer(self.BUFFER_LEN,sumAx[-self.BUFFER_LEN:])
        self.AyBuffer = Buffer(self.BUFFER_LEN,sumAy[-self.BUFFER_LEN:])
        self.AzBuffer = Buffer(self.BUFFER_LEN,sumAz[-self.BUFFER_LEN:])


        print("X: %f\tY: %f\tZ: %f"%(self.AxCalib,self.AyCalib, self.AzCalib))
    def refereshIMUData(self):
        Ax,Ay,Az,Gx,Gy,Gz = getIMUData()


        self.currTime = time.time()

        self.AxRaw = Ax-self.AxCalib
        self.AyRaw = Ay-self.AyCalib
        self.AzRaw = Az-self.AzCalib

        self.AxBuffer.push(self.AxRaw)
        self.AyBuffer.push(self.AyRaw)
        self.AzBuffer.push(self.AzRaw)

        self.Ax = self.AxBuffer.average()#Ax-self.AxCalib
        self.Ay = self.AyBuffer.average()#Ay-self.AyCalib
        self.Az = self.AzBuffer.average()#Az-self.AzCalib
        self.Gx = Gx
        self.Gy = Gy
        self.Gz = Gz

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
