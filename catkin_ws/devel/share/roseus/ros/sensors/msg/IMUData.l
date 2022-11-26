;; Auto-generated. Do not edit!


(when (boundp 'sensors::IMUData)
  (if (not (find-package "SENSORS"))
    (make-package "SENSORS"))
  (shadow 'IMUData (find-package "SENSORS")))
(unless (find-package "SENSORS::IMUDATA")
  (make-package "SENSORS::IMUDATA"))

(in-package "ROS")
;;//! \htmlinclude IMUData.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass sensors::IMUData
  :super ros::object
  :slots (_AxCalib _AyCalib _AzCalib _Ax _Ay _Az _AxRaw _AyRaw _AzRaw _Vx _Vy _Vz _Gx _Gy _Gz _currTime ))

(defmethod sensors::IMUData
  (:init
   (&key
    ((:AxCalib __AxCalib) (instance std_msgs::Float64 :init))
    ((:AyCalib __AyCalib) (instance std_msgs::Float64 :init))
    ((:AzCalib __AzCalib) (instance std_msgs::Float64 :init))
    ((:Ax __Ax) (instance std_msgs::Float64 :init))
    ((:Ay __Ay) (instance std_msgs::Float64 :init))
    ((:Az __Az) (instance std_msgs::Float64 :init))
    ((:AxRaw __AxRaw) (instance std_msgs::Float64 :init))
    ((:AyRaw __AyRaw) (instance std_msgs::Float64 :init))
    ((:AzRaw __AzRaw) (instance std_msgs::Float64 :init))
    ((:Vx __Vx) (instance std_msgs::Float64 :init))
    ((:Vy __Vy) (instance std_msgs::Float64 :init))
    ((:Vz __Vz) (instance std_msgs::Float64 :init))
    ((:Gx __Gx) (instance std_msgs::Float64 :init))
    ((:Gy __Gy) (instance std_msgs::Float64 :init))
    ((:Gz __Gz) (instance std_msgs::Float64 :init))
    ((:currTime __currTime) (instance std_msgs::Float64 :init))
    )
   (send-super :init)
   (setq _AxCalib __AxCalib)
   (setq _AyCalib __AyCalib)
   (setq _AzCalib __AzCalib)
   (setq _Ax __Ax)
   (setq _Ay __Ay)
   (setq _Az __Az)
   (setq _AxRaw __AxRaw)
   (setq _AyRaw __AyRaw)
   (setq _AzRaw __AzRaw)
   (setq _Vx __Vx)
   (setq _Vy __Vy)
   (setq _Vz __Vz)
   (setq _Gx __Gx)
   (setq _Gy __Gy)
   (setq _Gz __Gz)
   (setq _currTime __currTime)
   self)
  (:AxCalib
   (&rest __AxCalib)
   (if (keywordp (car __AxCalib))
       (send* _AxCalib __AxCalib)
     (progn
       (if __AxCalib (setq _AxCalib (car __AxCalib)))
       _AxCalib)))
  (:AyCalib
   (&rest __AyCalib)
   (if (keywordp (car __AyCalib))
       (send* _AyCalib __AyCalib)
     (progn
       (if __AyCalib (setq _AyCalib (car __AyCalib)))
       _AyCalib)))
  (:AzCalib
   (&rest __AzCalib)
   (if (keywordp (car __AzCalib))
       (send* _AzCalib __AzCalib)
     (progn
       (if __AzCalib (setq _AzCalib (car __AzCalib)))
       _AzCalib)))
  (:Ax
   (&rest __Ax)
   (if (keywordp (car __Ax))
       (send* _Ax __Ax)
     (progn
       (if __Ax (setq _Ax (car __Ax)))
       _Ax)))
  (:Ay
   (&rest __Ay)
   (if (keywordp (car __Ay))
       (send* _Ay __Ay)
     (progn
       (if __Ay (setq _Ay (car __Ay)))
       _Ay)))
  (:Az
   (&rest __Az)
   (if (keywordp (car __Az))
       (send* _Az __Az)
     (progn
       (if __Az (setq _Az (car __Az)))
       _Az)))
  (:AxRaw
   (&rest __AxRaw)
   (if (keywordp (car __AxRaw))
       (send* _AxRaw __AxRaw)
     (progn
       (if __AxRaw (setq _AxRaw (car __AxRaw)))
       _AxRaw)))
  (:AyRaw
   (&rest __AyRaw)
   (if (keywordp (car __AyRaw))
       (send* _AyRaw __AyRaw)
     (progn
       (if __AyRaw (setq _AyRaw (car __AyRaw)))
       _AyRaw)))
  (:AzRaw
   (&rest __AzRaw)
   (if (keywordp (car __AzRaw))
       (send* _AzRaw __AzRaw)
     (progn
       (if __AzRaw (setq _AzRaw (car __AzRaw)))
       _AzRaw)))
  (:Vx
   (&rest __Vx)
   (if (keywordp (car __Vx))
       (send* _Vx __Vx)
     (progn
       (if __Vx (setq _Vx (car __Vx)))
       _Vx)))
  (:Vy
   (&rest __Vy)
   (if (keywordp (car __Vy))
       (send* _Vy __Vy)
     (progn
       (if __Vy (setq _Vy (car __Vy)))
       _Vy)))
  (:Vz
   (&rest __Vz)
   (if (keywordp (car __Vz))
       (send* _Vz __Vz)
     (progn
       (if __Vz (setq _Vz (car __Vz)))
       _Vz)))
  (:Gx
   (&rest __Gx)
   (if (keywordp (car __Gx))
       (send* _Gx __Gx)
     (progn
       (if __Gx (setq _Gx (car __Gx)))
       _Gx)))
  (:Gy
   (&rest __Gy)
   (if (keywordp (car __Gy))
       (send* _Gy __Gy)
     (progn
       (if __Gy (setq _Gy (car __Gy)))
       _Gy)))
  (:Gz
   (&rest __Gz)
   (if (keywordp (car __Gz))
       (send* _Gz __Gz)
     (progn
       (if __Gz (setq _Gz (car __Gz)))
       _Gz)))
  (:currTime
   (&rest __currTime)
   (if (keywordp (car __currTime))
       (send* _currTime __currTime)
     (progn
       (if __currTime (setq _currTime (car __currTime)))
       _currTime)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Float64 _AxCalib
    (send _AxCalib :serialization-length)
    ;; std_msgs/Float64 _AyCalib
    (send _AyCalib :serialization-length)
    ;; std_msgs/Float64 _AzCalib
    (send _AzCalib :serialization-length)
    ;; std_msgs/Float64 _Ax
    (send _Ax :serialization-length)
    ;; std_msgs/Float64 _Ay
    (send _Ay :serialization-length)
    ;; std_msgs/Float64 _Az
    (send _Az :serialization-length)
    ;; std_msgs/Float64 _AxRaw
    (send _AxRaw :serialization-length)
    ;; std_msgs/Float64 _AyRaw
    (send _AyRaw :serialization-length)
    ;; std_msgs/Float64 _AzRaw
    (send _AzRaw :serialization-length)
    ;; std_msgs/Float64 _Vx
    (send _Vx :serialization-length)
    ;; std_msgs/Float64 _Vy
    (send _Vy :serialization-length)
    ;; std_msgs/Float64 _Vz
    (send _Vz :serialization-length)
    ;; std_msgs/Float64 _Gx
    (send _Gx :serialization-length)
    ;; std_msgs/Float64 _Gy
    (send _Gy :serialization-length)
    ;; std_msgs/Float64 _Gz
    (send _Gz :serialization-length)
    ;; std_msgs/Float64 _currTime
    (send _currTime :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Float64 _AxCalib
       (send _AxCalib :serialize s)
     ;; std_msgs/Float64 _AyCalib
       (send _AyCalib :serialize s)
     ;; std_msgs/Float64 _AzCalib
       (send _AzCalib :serialize s)
     ;; std_msgs/Float64 _Ax
       (send _Ax :serialize s)
     ;; std_msgs/Float64 _Ay
       (send _Ay :serialize s)
     ;; std_msgs/Float64 _Az
       (send _Az :serialize s)
     ;; std_msgs/Float64 _AxRaw
       (send _AxRaw :serialize s)
     ;; std_msgs/Float64 _AyRaw
       (send _AyRaw :serialize s)
     ;; std_msgs/Float64 _AzRaw
       (send _AzRaw :serialize s)
     ;; std_msgs/Float64 _Vx
       (send _Vx :serialize s)
     ;; std_msgs/Float64 _Vy
       (send _Vy :serialize s)
     ;; std_msgs/Float64 _Vz
       (send _Vz :serialize s)
     ;; std_msgs/Float64 _Gx
       (send _Gx :serialize s)
     ;; std_msgs/Float64 _Gy
       (send _Gy :serialize s)
     ;; std_msgs/Float64 _Gz
       (send _Gz :serialize s)
     ;; std_msgs/Float64 _currTime
       (send _currTime :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Float64 _AxCalib
     (send _AxCalib :deserialize buf ptr-) (incf ptr- (send _AxCalib :serialization-length))
   ;; std_msgs/Float64 _AyCalib
     (send _AyCalib :deserialize buf ptr-) (incf ptr- (send _AyCalib :serialization-length))
   ;; std_msgs/Float64 _AzCalib
     (send _AzCalib :deserialize buf ptr-) (incf ptr- (send _AzCalib :serialization-length))
   ;; std_msgs/Float64 _Ax
     (send _Ax :deserialize buf ptr-) (incf ptr- (send _Ax :serialization-length))
   ;; std_msgs/Float64 _Ay
     (send _Ay :deserialize buf ptr-) (incf ptr- (send _Ay :serialization-length))
   ;; std_msgs/Float64 _Az
     (send _Az :deserialize buf ptr-) (incf ptr- (send _Az :serialization-length))
   ;; std_msgs/Float64 _AxRaw
     (send _AxRaw :deserialize buf ptr-) (incf ptr- (send _AxRaw :serialization-length))
   ;; std_msgs/Float64 _AyRaw
     (send _AyRaw :deserialize buf ptr-) (incf ptr- (send _AyRaw :serialization-length))
   ;; std_msgs/Float64 _AzRaw
     (send _AzRaw :deserialize buf ptr-) (incf ptr- (send _AzRaw :serialization-length))
   ;; std_msgs/Float64 _Vx
     (send _Vx :deserialize buf ptr-) (incf ptr- (send _Vx :serialization-length))
   ;; std_msgs/Float64 _Vy
     (send _Vy :deserialize buf ptr-) (incf ptr- (send _Vy :serialization-length))
   ;; std_msgs/Float64 _Vz
     (send _Vz :deserialize buf ptr-) (incf ptr- (send _Vz :serialization-length))
   ;; std_msgs/Float64 _Gx
     (send _Gx :deserialize buf ptr-) (incf ptr- (send _Gx :serialization-length))
   ;; std_msgs/Float64 _Gy
     (send _Gy :deserialize buf ptr-) (incf ptr- (send _Gy :serialization-length))
   ;; std_msgs/Float64 _Gz
     (send _Gz :deserialize buf ptr-) (incf ptr- (send _Gz :serialization-length))
   ;; std_msgs/Float64 _currTime
     (send _currTime :deserialize buf ptr-) (incf ptr- (send _currTime :serialization-length))
   ;;
   self)
  )

(setf (get sensors::IMUData :md5sum-) "e854ee703c7cc2b23f6a5df92872cf41")
(setf (get sensors::IMUData :datatype-) "sensors/IMUData")
(setf (get sensors::IMUData :definition-)
      "std_msgs/Float64 AxCalib
std_msgs/Float64 AyCalib
std_msgs/Float64 AzCalib
std_msgs/Float64 Ax
std_msgs/Float64 Ay
std_msgs/Float64 Az
std_msgs/Float64 AxRaw
std_msgs/Float64 AyRaw
std_msgs/Float64 AzRaw
std_msgs/Float64 Vx
std_msgs/Float64 Vy
std_msgs/Float64 Vz
std_msgs/Float64 Gx
std_msgs/Float64 Gy
std_msgs/Float64 Gz
std_msgs/Float64 currTime

================================================================================
MSG: std_msgs/Float64
float64 data
")



(provide :sensors/IMUData "e854ee703c7cc2b23f6a5df92872cf41")


