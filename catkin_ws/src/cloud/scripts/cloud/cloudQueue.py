import requests
import time
import rospy

class CloudQueue:
    queue = []
    timeDiff = 1
    def addToQueue(data):
        CloudQueue.queue.append(data)

    def main():
        lastTime = time.time()
        counter=0

        while not rospy.is_shutdown():
            counter+=1
            if (time.time() >= lastTime):
                if (len(CloudQueue.queue) > 0):
                    CloudQueue.putDataToCloud(CloudQueue.queue.pop(0))
                    lastTime = time.time() + CloudQueue.timeDiff
    
    def rqScoreToJson(data):
        return {
                    "Latitude" : data.pos.gps.lat,
                    "Longitude" : data.pos.gps.long,
                    "road_quality_score": data.score
        }

    def putDataToCloud(data):
        print("Sent") 
        return requests.post("https://us-east.functions.appdomain.cloud/api/v1/web/535cf9b8-a592-4110-989b-2c01dc321176/default/Put-Data",json=CloudQueue.rqScoreToJson(data)) 

