from datetime import datetime
def rqScoreToJson(msg):
    return {
        "latitude":msg.pos.gps.lat,
        "longitude":msg.pos.gps.long,
        "road_quality_score":msg.score,
        "time":str(datetime.now())
    }
def heartBeatToJson(msg):
    return {
        "latitude":msg.gps.lat,
        "longitude":msg.gps.long,
        "time":str(datetime.now())
    }
