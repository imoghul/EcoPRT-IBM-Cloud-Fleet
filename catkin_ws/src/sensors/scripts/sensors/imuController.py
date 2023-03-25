import time
import threading
import rospy
from sensors.msg import IMUData
from sensor_msgs.msg import *
from geometry_msgs.msg import *
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
        self.pub = rospy.Publisher("imu_data",IMUData,queue_size=10)
        #MPU_Init()
        self.imuSub = rospy.Subscriber("raw_imu",Imu,self.calc)
        self.imuRaw = None
        
        
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
        self.calibrateCounter = 0

        #self.calibrate()
        #self.refereshIMUData()
        #self.calc()
    

        #self.running = True
        #self.thread = threading.Thread(target = self.run)
        self.sumAx = []
        self.sumAy = []
        self.sumAz = []
        self.sumGx = []
        self.sumGy = []
        self.sumGz = []


    def calibrate(self, newRaw,samples):
        rospy.loginfo("CALIBRATNG IMU..."+str(100*self.calibrateCounter/samples)+"%")
        #sumAx = []
        #sumAy = []
        #sumAz = []
        #sumGx = []
        #sumGy = []
        #sumGz = []
        
        #for i in range(samples):
        Ax,Ay,Az,Gx,Gy,Gz = (newRaw.linear_acceleration.x,newRaw.linear_acceleration.y,newRaw.linear_acceleration.z,newRaw.angular_velocity.x,newRaw.angular_velocity.y,newRaw.angular_velocity.z)
        self.sumAx.append(Ax)
        self.sumAy.append(Ay)
        self.sumAz.append(Az)
        self.sumGx.append(Gx)
        self.sumGy.append(Gy)
        self.sumGz.append(Gz)
            
        self.data.AxCalib = sum(self.sumAx)/len(self.sumAx)
        self.data.AyCalib = sum(self.sumAy)/len(self.sumAy)
        self.data.AzCalib = sum(self.sumAz)/len(self.sumAz)
        self.data.GxCalib = sum(self.sumGx)/len(self.sumGx)
        self.data.GyCalib = sum(self.sumGy)/len(self.sumGy)
        self.data.GzCalib = sum(self.sumGz)/len(self.sumGz)
        #if(self.calibrateCounter<samples-1): return
        #print(len(self.sumAx))
        try:
            self.AxBuffer = Buffer(self.BUFFER_LEN,self.sumAx[-self.BUFFER_LEN:])
            self.AyBuffer = Buffer(self.BUFFER_LEN,self.sumAy[-self.BUFFER_LEN:])
            self.AzBuffer = Buffer(self.BUFFER_LEN,self.sumAz[-self.BUFFER_LEN:])
            self.GxBuffer = Buffer(self.BUFFER_LEN,self.sumGx[-self.BUFFER_LEN:])
            self.GyBuffer = Buffer(self.BUFFER_LEN,self.sumGy[-self.BUFFER_LEN:])
            self.GzBuffer = Buffer(self.BUFFER_LEN,self.sumGz[-self.BUFFER_LEN:])

            #rospy.loginfo("Ax: %f\tAy: %f\tAz: %f\tGx: %f\tGy: %f\tGz: %f"%(self.data.AxCalib,self.data.AyCalib, self.data.AzCalib, self.data.GxCalib, self.data.GyCalib, self.data.GzCalib))
        except:pass

    def refereshIMUData(self, newRaw,calibSamples=100):
        #Ax,Ay,Az,Gx,Gy,Gz = getIMUData()
        #print(type(self.AxBuffer))
        if(newRaw==None):return
        if(self.calibrateCounter<calibSamples):
            self.calibrateCounter +=1
            self.calibrate(newRaw,calibSamples)
            return False
        Ax = newRaw.linear_acceleration.x
        Ay = newRaw.linear_acceleration.y
        Az = newRaw.linear_acceleration.z
        Gx = newRaw.angular_velocity.x
        Gy = newRaw.angular_velocity.y
        Gz = newRaw.angular_velocity.z
        
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

    def calc(self, newRaw):
        origAx,origAy,origAz,origGx,origGy,origGz,origTime = self.data.Ax,self.data.Ay,self.data.Az,self.data.Gx,self.data.Gy,self.data.Gz,self.data.currTime

        if self.refereshIMUData(newRaw)==False: return
        if(self.data.Ax==origAx and self.data.Ay==origAy and self.data.Az==origAz and self.data.Gx == origGx and self.data.Gy==origGy and self.data.Gz==origGz): 
            #print("double imu reading discarded")
            return
        
        timeDiff = self.data.currTime-origTime
        self.data.Vx = self.data.Vx+timeDiff*(origAx+self.data.Ax)/2
        self.data.Vy = self.data.Vy+timeDiff*(origAy+self.data.Ay)/2
        self.data.Vz = self.data.Vz+timeDiff*(origAz+self.data.Az)/2

        try:self.pub.publish(self.data)
        except rospy.exceptions.ROSException: pass
    #def run(self):
    #    while self.running and not rospy.is_shutdown():
    #        self.calc(self.imuRaw)

    #def start(self):
    #    self.running = True
    #    self.thread.start()

    #def end(self):
    #    self.running = False
    #    self.thread.join()
