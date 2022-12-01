roscore &
source ~/EcoPRT-IBM-Cloud-Fleet/catkin_ws/devel/setup.bash

rosrun sensors sensorController.py
rosrun positioning localizer.py
