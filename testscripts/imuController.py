from MPU6050 import *
import time
import threading

class IMUController():
    AxCalib = 0
    AyCalib = 0
    AzCalib = 0
    def __init__(self):
        MPU_Init()
        self.calibrate()
        self.refereshIMUData()
        self.Vx = 0
        self.Vy = 0
        self.Vz = 0


        self.thread = threading.Thread(target = self.run)

    def calibrate(self,samples=1000):
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
        print("X: %f\tY: %f\tZ: %f"%(self.AxCalib,self.AyCalib, self.AzCalib))
    def refereshIMUData(self):
        Ax,Ay,Az,Gx,Gy,Gz = getIMUData()

        self.currTime = time.time()
        self.Ax = Ax-self.AxCalib
        self.Ay = Ay-self.AyCalib
        self.Az = Az-self.AzCalib
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
