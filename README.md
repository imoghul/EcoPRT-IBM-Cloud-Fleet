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
![alt text](http://url/to/img.png) 

`sensor_io` is part of the hardware package (which will be unnecessary for different hardware) will publish `raw_gps` and `raw_imu` which are of type `geometry_msgs/Pose2D` and `sensor_msgs/Imu` respectively. `Pose2D.x` is latitude and `Pose2D.y` is longitude. `Imu.linear_acceleration` will hold Ax, Ay, Az while `Imu.angular_velocity` will hold Gx, Gy, Gz.



## Configuration
The configuration file is in the config package in the ```config.py``` file.
