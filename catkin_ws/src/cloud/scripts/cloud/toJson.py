from datetime import datetime
from roadquality.msg import RoadQualityScore
from positioning.msg import Position
from sensors.msg import GPSData


def rqScoreToJson(msg):
    return {
        "latitude": msg.pos.gps.lat,
        "longitude": msg.pos.gps.long,
        "road_quality_score": msg.score,
        "time": str(datetime.now()),
    }

def mlScoreToJson(msg):
    return {
        "latitude": msg.pos.gps.lat,
        "longitude": msg.pos.pgs.long,
        "machine_learning_score": msg.score,
        "terraint_type": msg.type,
        "time": str(datetime.now()),
    }


def jsonToRqScore(json):
    return RoadQualityScore(
        Position(
            GPSData(json["time"], json["latitude"], json["longitude"], 0, 0), None
        ),
        json["road_quality_score"],
    )


def heartBeatToJson(msg):
    return {
        "latitude": msg.pos.gps.lat,
        "longitude": msg.pos.gps.long,
        "time": msg.time,
        "distance": msg.distance,
    }
