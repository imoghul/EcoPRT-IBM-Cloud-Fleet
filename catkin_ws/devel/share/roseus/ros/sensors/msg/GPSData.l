;; Auto-generated. Do not edit!


(when (boundp 'sensors::GPSData)
  (if (not (find-package "SENSORS"))
    (make-package "SENSORS"))
  (shadow 'GPSData (find-package "SENSORS")))
(unless (find-package "SENSORS::GPSDATA")
  (make-package "SENSORS::GPSDATA"))

(in-package "ROS")
;;//! \htmlinclude GPSData.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass sensors::GPSData
  :super ros::object
  :slots (_time _lat _long ))

(defmethod sensors::GPSData
  (:init
   (&key
    ((:time __time) (instance std_msgs::String :init))
    ((:lat __lat) (instance std_msgs::Float64 :init))
    ((:long __long) (instance std_msgs::Float64 :init))
    )
   (send-super :init)
   (setq _time __time)
   (setq _lat __lat)
   (setq _long __long)
   self)
  (:time
   (&rest __time)
   (if (keywordp (car __time))
       (send* _time __time)
     (progn
       (if __time (setq _time (car __time)))
       _time)))
  (:lat
   (&rest __lat)
   (if (keywordp (car __lat))
       (send* _lat __lat)
     (progn
       (if __lat (setq _lat (car __lat)))
       _lat)))
  (:long
   (&rest __long)
   (if (keywordp (car __long))
       (send* _long __long)
     (progn
       (if __long (setq _long (car __long)))
       _long)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/String _time
    (send _time :serialization-length)
    ;; std_msgs/Float64 _lat
    (send _lat :serialization-length)
    ;; std_msgs/Float64 _long
    (send _long :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/String _time
       (send _time :serialize s)
     ;; std_msgs/Float64 _lat
       (send _lat :serialize s)
     ;; std_msgs/Float64 _long
       (send _long :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/String _time
     (send _time :deserialize buf ptr-) (incf ptr- (send _time :serialization-length))
   ;; std_msgs/Float64 _lat
     (send _lat :deserialize buf ptr-) (incf ptr- (send _lat :serialization-length))
   ;; std_msgs/Float64 _long
     (send _long :deserialize buf ptr-) (incf ptr- (send _long :serialization-length))
   ;;
   self)
  )

(setf (get sensors::GPSData :md5sum-) "127d8146da420293b29d277551a452ba")
(setf (get sensors::GPSData :datatype-) "sensors/GPSData")
(setf (get sensors::GPSData :definition-)
      "std_msgs/String time
std_msgs/Float64 lat
std_msgs/Float64 long

================================================================================
MSG: std_msgs/String
string data

================================================================================
MSG: std_msgs/Float64
float64 data
")



(provide :sensors/GPSData "127d8146da420293b29d277551a452ba")


