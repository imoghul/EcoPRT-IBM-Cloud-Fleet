import rospy


# cloud
putDataUrl = "https://us-east.functions.appdomain.cloud/api/v1/web/535cf9b8-a592-4110-989b-2c01dc321176/default/Put-Data"
heartbeatUrl = "https://us-east.functions.appdomain.cloud/api/v1/web/535cf9b8-a592-4110-989b-2c01dc321176/default/heartBeat"
passcode = "ncsuECE_sdproject37"
sensorDbName = "sensor-data"
mlDbName = "ml-data"
heartbeat_rx_publisher_name = "heartbeat_rx"

# hardware
gpsSerPort = "/dev/ttyACM0"

# sensors
raw_imu_publisher_name = "raw_imu"
raw_gps_publisher_name = "raw_gps"
raw_image_publisher_name = "raw_image"

# positioning
waitForGPS = False

#roadquality
modelAbsPath = "/home/pi/EcoPRT-IBM-Cloud-Fleet/model/rq_ml_model_0418231326.h5"
modelInputLen = 160 # This is NOT to be changed unless you change the model you are using
modelRate = 2*(1/60) # Hz
image_prediction_publisher_name = "image_predictions"
surfaceTypeModel = ""
asphaltQualityModel = ""
pavedQualityModel = ""
unpavedQualityModel = ""
