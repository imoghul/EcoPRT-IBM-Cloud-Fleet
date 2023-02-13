import requests
import time
import rospy
import json
from cloud.confidential import *
class CloudQueue:
    def __init__(self,name,tDiff=.5,_url = url):
        self.name = name
        self.timeDiff = tDiff
        self.url = _url
    def addToQueue(self,data):
        rfile = open("/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/src/cloud/scripts/cloud/queue.json", 'r')
        try:
            f = json.load(rfile)
        except Exception as e:
            f = {self.name:[]}
        rfile.close()

        ofile = open("/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/src/cloud/scripts/cloud/queue.json",'w')
        f[self.name].append(self.rqScoreToJson(data))
        json.dump(f,ofile,indent=4)
        ofile.close()
    def main(self):
        lastTime = time.time()
        counter=0
        while not rospy.is_shutdown():
            counter+=1
            if (time.time() >= lastTime):
                try:
                    readfile = open("/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/src/cloud/scripts/cloud/queue.json",'r')
                    f = json.load(readfile)

                    readfile.close()
                except Exception as e:pass
                if (len(f[self.name]) > 0):
                    self.putDataToCloud(f[self.name].pop(0))
                    lastTime = time.time() + self.timeDiff
                
                outfile = open("/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/src/cloud/scripts/cloud/queue.json",'w')
                json.dump(f,outfile,indent=4)
                outfile.close()
    def rqScoreToJson(self,data):
        return {
                    "Latitude" : data.pos.gps.lat,
                    "Longitude" : data.pos.gps.long,
                    "road_quality_score": data.score
        }

    def putDataToCloud(self,data):
        print("Sent")
        return
        data["__passcode__"] = passcode 
        return requests.post(self.url,json=data) 

