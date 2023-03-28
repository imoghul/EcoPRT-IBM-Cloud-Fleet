# EcoPRT-IBM-Cloud-Fleet
EcoPRT fleet management system with IBM Cloud



## Setup
``` bash
cd catkin_ws # enter the catkin worksapce directory
catkin_make # make the project
```

## Usage
``` bash
./catkin_ws/launch.sh
```

## Software Infrastructure
The infrastrucre is defined by ROS, for better modularity. The rqt_graph is shown below
![alt text](https://github.com/imoghul/EcoPRT-IBM-Cloud-Fleet/blob/main/ros%20infrastructure.png)
### Graph Explanation
`sensor_io` is part of the `hardware` package (which will be unnecessary for different hardware) will publish `raw_gps` and `raw_imu` which are of type `geometry_msgs/Pose2D` and `sensor_msgs/Imu` respectively. `Pose2D.x` is latitude and `Pose2D.y` is longitude. `Imu.linear_acceleration` will hold Ax, Ay, Az while `Imu.angular_velocity` will hold Gx, Gy, Gz.\
`Sensor_Node` is part of the `sensors` package. This package will subscribe to the `raw_gps` and `raw_imu` publishers (currently in hardware package, but doesn't need to be). It mainly does IMU data smoothing, and converts gps data to custom message types. It also makes sure the same data isn't published twice.\
`localization` is part of the `positioning` package. This will convert sensor data into one message type, so other packages can know sensor data.\
The localization data is subscribed to by the road_quality and cloud packages, which will do road quality calculation and cloud communication respectively. Cloud communication will subscribe to road_quality, in order to post data to the database


## Configuration
The configuration file is in the config package in the ```config.py``` file.\
`putDataUrl` will contain the url to IBM Cloud function that posts data in the database\
`heartbeatURL` will contain the url to the IBM Cloud function that handles heartbeat requeusts\
`passcode` will contain the passcode that is defined in the IBM Cloud functions\
`gpsSerPort` will contain the usb port name for the gps

## Integration
To integrate this project into existing code, complete the following:
1. Make sure to not launch existing hardware nodes that are provided
2. Create `raw_gps` and `raw_imu` publishers as described before in your pre-existing hardware package. Or alternatively, edit the 2 publisher names in the config file to match existing publishers in your code
