import requests
from GT_U7 import *
from imuController import *

vehicleID = 0
controller = IMUController()
controller.start()

def putDataToCloud(data):
    print("sending data")
    return requests.post("https://us-east.functions.appdomain.cloud/api/v1/web/535cf9b8-a592-4110-989b-2c01dc321176/default/helloworld",json=data)

#def heartBeat():
#    return getData()

#def dataStruct():
#    imuDataInstance = controller.Az
#    connection = heartBeat()
#    data = {"vehicleID":vehicleID,"heartBeat":connection if connection!=None else -1}
#    putDataToCloud(data)
