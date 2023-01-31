from sensors.MPU6050 import *
import time
import threading
import rospy
from sensors.msg import IMUData
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

        self.data = IMUData()#(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
       
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
        self.data.GxCalib = 0
        self.data.GyCalib = 0
        self.data.GzCalib = 0
        self.data.GxRaw = 0
        self.data.GyRaw = 0
        self.data.GzRaw = 0
        self.data.currTime = 0

        self.AxBuffer = None
        self.AyBuffer = None
        self.AzBuffer = None
        self.GxBuffer = None
        self.GyBuffer = None
        self.GzBuffer = None

        self.BUFFER_LEN = 25

        self.calibrate()
        self.refereshIMUData()
        self.calc()
    

        self.running = True
        self.thread = threading.Thread(target = self.run)

    def calibrate(self,samples=100):
        rospy.loginfo("CALIBRATNG...")
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
            
        self.data.AxCalib = sum(sumAx)/len(sumAx)
        self.data.AyCalib = sum(sumAy)/len(sumAy)
        self.data.AzCalib = sum(sumAz)/len(sumAz)
        self.data.GxCalib = sum(sumGx)/len(sumGx)
        self.data.GyCalib = sum(sumGy)/len(sumGy)
        self.data.GzCalib = sum(sumGz)/len(sumGz)

        self.AxBuffer = Buffer(self.BUFFER_LEN,sumAx[-self.BUFFER_LEN:])
        self.AyBuffer = Buffer(self.BUFFER_LEN,sumAy[-self.BUFFER_LEN:])
        self.AzBuffer = Buffer(self.BUFFER_LEN,sumAz[-self.BUFFER_LEN:])
        self.GxBuffer = Buffer(self.BUFFER_LEN,sumGx[-self.BUFFER_LEN:])
        self.GyBuffer = Buffer(self.BUFFER_LEN,sumGy[-self.BUFFER_LEN:])
        self.GzBuffer = Buffer(self.BUFFER_LEN,sumGz[-self.BUFFER_LEN:])


        rospy.loginfo("Ax: %f\tAy: %f\tAz: %f\tGx: %f\tGy: %f\tGz: %f"%(self.data.AxCalib,self.data.AyCalib, self.data.AzCalib, self.data.GxCalib, self.data.GyCalib, self.data.GzCalib))
        
    def refereshIMUData(self):
        Ax,Ay,Az,Gx,Gy,Gz = getIMUData()

        self.data.currTime = time.time()

        self.data.AxRaw = (Ax-self.data.AxCalib)/9.81
        self.data.AyRaw = (Ay-self.data.AyCalib)/9.81
        self.data.AzRaw = (Az-self.data.AzCalib)/9.81
        self.data.GxRaw = (Gx-self.data.GxCalib)/9.81
        self.data.GyRaw = (Gy-self.data.GyCalib)/9.81
        self.data.GzRaw = (Gz-self.data.GzCalib)/9.81

        self.AxBuffer.push(self.data.AxRaw)
        self.AyBuffer.push(self.data.AyRaw)
        self.AzBuffer.push(self.data.AzRaw)
        self.GxBuffer.push(self.data.GxRaw)
        self.GyBuffer.push(self.data.GyRaw)
        self.GzBuffer.push(self.data.GzRaw)

        self.data.Ax = self.AxBuffer.average()
        self.data.Ay = self.AyBuffer.average()
        self.data.Az = self.AzBuffer.average()
        self.data.Gx = self.GxBuffer.average()
        self.data.Gy = self.GyBuffer.average()
        self.data.Gz = self.GzBuffer.average()

    def calc(self):
        origAx,origAy,origAz,origGx,origGy,origGz,origTime = self.data.Ax,self.data.Ay,self.data.Az,self.data.Gx,self.data.Gy,self.data.Gz,self.data.currTime

        self.refereshIMUData()
        if(self.data.Ax==origAx and self.data.Ay==origAy and self.data.Az==origAz and self.data.Gx == origGx and self.data.Gy==origGy and self.data.Gz==origGz): return
        
        timeDiff = self.data.currTime-origTime
        self.data.Vx = self.data.Vx+timeDiff*(origAx+self.data.Ax)/2
        self.data.Vy = self.data.Vy+timeDiff*(origAy+self.data.Ay)/2
        self.data.Vz = self.data.Vz+timeDiff*(origAz+self.data.Az)/2

        self.pub.publish(self.data)
    def run(self):
        while self.running and not rospy.is_shutdown():
            self.calc()

    def start(self):
        self.running = True
        self.thread.start()

    def end(self):
        self.running = False
        self.thread.join()
