import requests
import time
import rospy
import json
import atexit
import threading
import cloud.confidential
from datetime import datetime
import roadquality.msg

queueFile = (
    "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/src/cloud/scripts/cloud/queue.json"
)


def rqScoreToJson(data: roadquality.msg.RoadQualityScore):
    return {
        "latitude": data.pos.gps.lat,
        "longitude": data.pos.gps.long,
        "road_quality_score": data.score,
        "time": str(datetime.now()),
    }


class CloudQueue:
    def __init__(self, name, tDiff=0.5, url=cloud.confidential.url):
        self.name = name
        self.timeDiff = tDiff
        self.url = url
        self.queue = self.getFileQueue()[self.name]
        self.thread = threading.Thread(target=self.main)
        self.__del__ = self.updateFile
        atexit.register(self.updateFile)

    def getFileQueue(self):
        try:
            open(queueFile,"r").close()
        except: open(queueFile,"w").close()
        with open(queueFile, "r") as rfile:
            try:
                return json.load(rfile)
            except Exception as e:
                try:
                    rfile.read()
                    return {self.name: []}
                except Exception as e:
                    raise Exception(
                        "corrupt queue file"
                    )

    def updateFile(self):
        f = self.getFileQueue()
        with open(queueFile, "w") as ofile:
            f[self.name] = self.queue.copy()
            json.dump(f, ofile, indent=4)

    def addToQueue(self, data: roadquality.msg.RoadQualityScore):
        self.queue.append(rqScoreToJson(data))
        self.updateFile()
        print("Added")

    def popFromQueue(self):
        ret = self.queue.pop(0)
        self.updateFile()
        return ret

    def main(self):
        targetTime = time.time()

        while not rospy.is_shutdown():
            if time.time() >= targetTime:
                if len(self.queue) > 0:
                    self.putDataToCloud(self.popFromQueue())
                    targetTime = time.time() + self.timeDiff

    def putDataToCloud(self, data: dict):
        rospy.loginfo("Sent to cloud")
        data["__passcode__"] = cloud.confidential.passcode
        return requests.post(self.url, json=data)
