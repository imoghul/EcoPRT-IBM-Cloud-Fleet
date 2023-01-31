import requests
import time
import rospy
from cloud.confidential import *
class CloudQueue:
    queue = []
    timeDiff = .5
    def addToQueue(self,data):
        self.queue.append(data)

    def main(self):
        lastTime = time.time()
        counter=0

        while not rospy.is_shutdown():
            counter+=1
            if (time.time() >= lastTime):
                if (len(self.queue) > 0):
                    self.putDataToCloud(self.queue.pop(0))
                    lastTime = time.time() + self.timeDiff
    
    def rqScoreToJson(self,data):
        return {
                    "__passcode__": passcode,
                    "Latitude" : data.pos.gps.lat,
                    "Longitude" : data.pos.gps.long,
                    "road_quality_score": data.score
        }

    def putDataToCloud(self,data):
        print("Sent") 
        return requests.post(url,json=self.rqScoreToJson(data)) 

