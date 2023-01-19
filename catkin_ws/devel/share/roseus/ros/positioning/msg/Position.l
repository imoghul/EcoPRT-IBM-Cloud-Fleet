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
  :slots (_latitude _longitude _altitude _imu ))

(defmethod positioning::Position
  (:init
   (&key
    ((:latitude __latitude) 0.0)
    ((:longitude __longitude) 0.0)
    ((:altitude __altitude) 0.0)
    ((:imu __imu) (instance sensors::IMUData :init))
    )
   (send-super :init)
   (setq _latitude (float __latitude))
   (setq _longitude (float __longitude))
   (setq _altitude (float __altitude))
   (setq _imu __imu)
   self)
  (:latitude
   (&optional __latitude)
   (if __latitude (setq _latitude __latitude)) _latitude)
  (:longitude
   (&optional __longitude)
   (if __longitude (setq _longitude __longitude)) _longitude)
  (:altitude
   (&optional __altitude)
   (if __altitude (setq _altitude __altitude)) _altitude)
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
    ;; float64 _latitude
    8
    ;; float64 _longitude
    8
    ;; float64 _altitude
    8
    ;; sensors/IMUData _imu
    (send _imu :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _latitude
       (sys::poke _latitude (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _longitude
       (sys::poke _longitude (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _altitude
       (sys::poke _altitude (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; sensors/IMUData _imu
       (send _imu :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _latitude
     (setq _latitude (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _longitude
     (setq _longitude (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _altitude
     (setq _altitude (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; sensors/IMUData _imu
     (send _imu :deserialize buf ptr-) (incf ptr- (send _imu :serialization-length))
   ;;
   self)
  )

(setf (get positioning::Position :md5sum-) "26972fc25ce21b0631b32a2b006a1bf4")
(setf (get positioning::Position :datatype-) "positioning/Position")
(setf (get positioning::Position :definition-)
      "float64 latitude
float64 longitude
float64 altitude
sensors/IMUData imu

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



(provide :positioning/Position "26972fc25ce21b0631b32a2b006a1bf4")


