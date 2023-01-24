import requests
import time


class Queue:
    queue = []
    timeDiff = 1
    def addToQueue(data):
        Queue.queue.append(data)

    def main():
        lastTime = time.time()
        counter=0

        while(True):
            counter+=1
            if (time.time() >= lastTime):
                if (len(Queue.queue) > 0):
                    Queue.putDataToCloud(Queue.queue.pop(0))
                    lastTime = time.time() + Queue.timeDiff
                
    def putDataToCloud(data):
        return requests.post("https://us-east.functions.appdomain.cloud/api/v1/web/535cf9b8-a592-4110-989b-2c01dc321176/default/helloworld",json=data) 

if __name__ == "__main__":
    Queue.main()
