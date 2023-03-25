'''
        Read Gyro and Accelerometer by Interfacing Raspberry Pi with MPU6050 using Python
        http://www.electronicwings.com
'''
import smbus                    #import SMBus module of I2C
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Quaternion, Vector3
from std_msgs.msg import Header
#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47
Device_Address = 0x68

bus = None

last = None
def MPU_Init():
    global bus
    bus = smbus.SMBus(1)
    #write to sample rate register
    bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)

    #Write to power management register
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)

    #Write to Configuration register
    bus.write_byte_data(Device_Address, CONFIG, 0)

    #Write to Gyro configuration register
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)

    #Write to interrupt enable register
    bus.write_byte_data(Device_Address, INT_ENABLE, 1)
    return bus

def read_raw_data(bus,addr):
    #Accelero and Gyro value are 16-bit
    high = bus.read_byte_data(Device_Address, addr)
    low = bus.read_byte_data(Device_Address, addr+1)

    #concatenate higher and lower value
    value = ((high << 8) | low)

    #to get signed value from mpu6050
    if(value > 32768):
        value = value - 65536
    return value


def getIMUData():
    global last
    if(bus==None):
        raise Exception("IMU not initialized")
    #Read Accelerometer raw value
    acc_x = read_raw_data(bus,ACCEL_XOUT_H)
    acc_y = read_raw_data(bus,ACCEL_YOUT_H)
    acc_z = read_raw_data(bus,ACCEL_ZOUT_H)

    #Read Gyroscope raw value
    gyro_x = read_raw_data(bus,GYRO_XOUT_H)
    gyro_y = read_raw_data(bus,GYRO_YOUT_H)
    gyro_z = read_raw_data(bus,GYRO_ZOUT_H)

    #Full scale range +/- 250 degree/C as per sensitivity scale factor
    Ax = acc_x/16384.0
    Ay = acc_y/16384.0
    Az = acc_z/16384.0

    Gx = gyro_x/131.0
    Gy = gyro_y/131.0
    Gz = gyro_z/131.0

    imuVal=Imu()
    imuVal.angular_velocity = Vector3(Gx,Gy,Gz)
    imuVal.linear_acceleration = Vector3(Ax,Ay,Az)
    if imuVal==last:
        print("discarded double reading")
        return
    last = imuVal
    return imuVal#(Ax,Ay,Az,Gx,Gy,Gz)
if __name__ == "__main__":
    MPU_Init()
    while(True):print(getIMUData())
