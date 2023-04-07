import requests
import time
import rospy
import json
import atexit
import threading
import config.config
from datetime import datetime
import roadquality.msg
import os


queuePath = os.path.abspath(
    __file__
) 
queuePath = "/".join(queuePath.split("/")[:-1]) + "/queues/"
# TODO: change this to cross platform function call
os.system(f"mkdir -p {queuePath}")


class CloudQueue:
    def __init__(self, name, requiresFile, msgToJson, url, tDiff=0.5, callback=None, dbName=None):
        self.name = name
        self.timeDiff = tDiff
        self.url = url
        self.requiresFile = requiresFile
        self.callback = callback
        self.msgToJson = msgToJson
        self.dbName = dbName
        if self.requiresFile:
            self.queueFile = queuePath + self.name + ".json"
            f = self.getFileQueue()
            self.queue = f[self.name] if self.name in f else []
            self.__del__ = self.updateFile
            atexit.register(self.updateFile)
        else:
            self.queue = []
        self.thread = threading.Thread(target=self.main)

    def getFileQueue(self):
        try:
            open(self.queueFile, "r").close()
        except:
            open(self.queueFile, "w").close()
        with open(self.queueFile, "r") as rfile:
            try:
                return json.load(rfile)
            except Exception as e:
                try:
                    rfile.read()
                    return {}
                except Exception as e:
                    return {} #raise Exception("corrupt queue file, please fix or delete the file")

    def updateFile(self):
        try: f = self.getFileQueue()
        except: f = {} 
        with open(self.queueFile, "w") as ofile:
            f[self.name] = self.queue.copy()
            json.dump(f, ofile, indent=4)

    def addToQueue(self, data: roadquality.msg.RoadQualityScore):
        self.queue.append(self.msgToJson(data))
        if self.requiresFile:
            self.updateFile()

    def popFromQueue(self):
        ret = self.queue.pop(0)
        if self.requiresFile:
            self.updateFile()
        return ret

    def main(self):
        targetTime = time.time()

        while not rospy.is_shutdown():
            if time.time() >= targetTime:
                if len(self.queue) > 0:
                    self.putDataToCloud(self.popFromQueue())
                    targetTime = time.time() + self.timeDiff

    def start(self):
        self.thread.start()

    def putDataToCloud(self, data: dict):
        rospy.loginfo("Sent to %s cloud" % self.name)
        data["__passcode__"] = config.config.passcode
        if(self.dbName!=None):data["__database__"] = self.dbName
        return (
            requests.post(self.url, json=data)
            if self.callback == None
            else self.callback(requests.post(self.url, json=data))
        )
