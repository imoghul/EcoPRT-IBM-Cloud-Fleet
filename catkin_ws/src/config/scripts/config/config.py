import rospy


# cloud
putDataUrl = "https://us-east.functions.appdomain.cloud/api/v1/web/535cf9b8-a592-4110-989b-2c01dc321176/default/Put-Data"
heartbeatUrl = "https://us-east.functions.appdomain.cloud/api/v1/web/535cf9b8-a592-4110-989b-2c01dc321176/default/heartBeat"
passcode = "ncsuECE_sdproject37"
sensorDbName = "sensor-data"
mlDbName = "ml-data"


# hardware
gpsSerPort = "/dev/ttyACM0"

# sensors
raw_imu_publisher_name = "raw_imu"
raw_gps_publisher_name = "raw_gps"
raw_image_publisher_name = "raw_image"

# positioning
waitForGPS = False

#roadquality
modelAbsPath = "/home/pi/EcoPRT-IBM-Cloud-Fleet/model/rq_ml_model.h5"
