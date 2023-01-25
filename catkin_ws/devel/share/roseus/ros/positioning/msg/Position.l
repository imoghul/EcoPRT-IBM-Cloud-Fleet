;; Auto-generated. Do not edit!


(when (boundp 'positioning::Position)
  (if (not (find-package "POSITIONING"))
    (make-package "POSITIONING"))
  (shadow 'Position (find-package "POSITIONING")))
(unless (find-package "POSITIONING::POSITION")
  (make-package "POSITIONING::POSITION"))

(in-package "ROS")
;;//! \htmlinclude Position.msg.html
(if (not (find-package "SENSORS"))
  (ros::roseus-add-msgs "sensors"))


(defclass positioning::Position
  :super ros::object
  :slots (_gps _imu ))

(defmethod positioning::Position
  (:init
   (&key
    ((:gps __gps) (instance sensors::GPSData :init))
    ((:imu __imu) (instance sensors::IMUData :init))
    )
   (send-super :init)
   (setq _gps __gps)
   (setq _imu __imu)
   self)
  (:gps
   (&rest __gps)
   (if (keywordp (car __gps))
       (send* _gps __gps)
     (progn
       (if __gps (setq _gps (car __gps)))
       _gps)))
  (:imu
   (&rest __imu)
   (if (keywordp (car __imu))
       (send* _imu __imu)
     (progn
       (if __imu (setq _imu (car __imu)))
       _imu)))
  (:serialization-length
   ()
   (+
    ;; sensors/GPSData _gps
    (send _gps :serialization-length)
    ;; sensors/IMUData _imu
    (send _imu :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; sensors/GPSData _gps
       (send _gps :serialize s)
     ;; sensors/IMUData _imu
       (send _imu :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; sensors/GPSData _gps
     (send _gps :deserialize buf ptr-) (incf ptr- (send _gps :serialization-length))
   ;; sensors/IMUData _imu
     (send _imu :deserialize buf ptr-) (incf ptr- (send _imu :serialization-length))
   ;;
   self)
  )

(setf (get positioning::Position :md5sum-) "6fb7f457c11907847ca6763dd0bb7aad")
(setf (get positioning::Position :datatype-) "positioning/Position")
(setf (get positioning::Position :definition-)
      "sensors/GPSData gps
sensors/IMUData imu

================================================================================
MSG: sensors/GPSData
string time
float64 lat
float64 long

================================================================================
MSG: sensors/IMUData
float64 AxCalib
float64 AyCalib
float64 AzCalib
float64 Ax
float64 Ay
float64 Az
float64 AxRaw
float64 AyRaw
float64 AzRaw
float64 Vx
float64 Vy
float64 Vz
float64 Gx
float64 Gy
float64 Gz
float64 GxCalib
float64 GyCalib
float64 GzCalib
float64 GxRaw
float64 GyRaw
float64 GzRaw
float64 currTime

")



(provide :positioning/Position "6fb7f457c11907847ca6763dd0bb7aad")


