;; Auto-generated. Do not edit!


(when (boundp 'sensors::IMUData)
  (if (not (find-package "SENSORS"))
    (make-package "SENSORS"))
  (shadow 'IMUData (find-package "SENSORS")))
(unless (find-package "SENSORS::IMUDATA")
  (make-package "SENSORS::IMUDATA"))

(in-package "ROS")
;;//! \htmlinclude IMUData.msg.html


(defclass sensors::IMUData
  :super ros::object
  :slots (_AxCalib _AyCalib _AzCalib _Ax _Ay _Az _AxRaw _AyRaw _AzRaw _Vx _Vy _Vz _Gx _Gy _Gz _currTime ))

(defmethod sensors::IMUData
  (:init
   (&key
    ((:AxCalib __AxCalib) 0.0)
    ((:AyCalib __AyCalib) 0.0)
    ((:AzCalib __AzCalib) 0.0)
    ((:Ax __Ax) 0.0)
    ((:Ay __Ay) 0.0)
    ((:Az __Az) 0.0)
    ((:AxRaw __AxRaw) 0.0)
    ((:AyRaw __AyRaw) 0.0)
    ((:AzRaw __AzRaw) 0.0)
    ((:Vx __Vx) 0.0)
    ((:Vy __Vy) 0.0)
    ((:Vz __Vz) 0.0)
    ((:Gx __Gx) 0.0)
    ((:Gy __Gy) 0.0)
    ((:Gz __Gz) 0.0)
    ((:currTime __currTime) 0.0)
    )
   (send-super :init)
   (setq _AxCalib (float __AxCalib))
   (setq _AyCalib (float __AyCalib))
   (setq _AzCalib (float __AzCalib))
   (setq _Ax (float __Ax))
   (setq _Ay (float __Ay))
   (setq _Az (float __Az))
   (setq _AxRaw (float __AxRaw))
   (setq _AyRaw (float __AyRaw))
   (setq _AzRaw (float __AzRaw))
   (setq _Vx (float __Vx))
   (setq _Vy (float __Vy))
   (setq _Vz (float __Vz))
   (setq _Gx (float __Gx))
   (setq _Gy (float __Gy))
   (setq _Gz (float __Gz))
   (setq _currTime (float __currTime))
   self)
  (:AxCalib
   (&optional __AxCalib)
   (if __AxCalib (setq _AxCalib __AxCalib)) _AxCalib)
  (:AyCalib
   (&optional __AyCalib)
   (if __AyCalib (setq _AyCalib __AyCalib)) _AyCalib)
  (:AzCalib
   (&optional __AzCalib)
   (if __AzCalib (setq _AzCalib __AzCalib)) _AzCalib)
  (:Ax
   (&optional __Ax)
   (if __Ax (setq _Ax __Ax)) _Ax)
  (:Ay
   (&optional __Ay)
   (if __Ay (setq _Ay __Ay)) _Ay)
  (:Az
   (&optional __Az)
   (if __Az (setq _Az __Az)) _Az)
  (:AxRaw
   (&optional __AxRaw)
   (if __AxRaw (setq _AxRaw __AxRaw)) _AxRaw)
  (:AyRaw
   (&optional __AyRaw)
   (if __AyRaw (setq _AyRaw __AyRaw)) _AyRaw)
  (:AzRaw
   (&optional __AzRaw)
   (if __AzRaw (setq _AzRaw __AzRaw)) _AzRaw)
  (:Vx
   (&optional __Vx)
   (if __Vx (setq _Vx __Vx)) _Vx)
  (:Vy
   (&optional __Vy)
   (if __Vy (setq _Vy __Vy)) _Vy)
  (:Vz
   (&optional __Vz)
   (if __Vz (setq _Vz __Vz)) _Vz)
  (:Gx
   (&optional __Gx)
   (if __Gx (setq _Gx __Gx)) _Gx)
  (:Gy
   (&optional __Gy)
   (if __Gy (setq _Gy __Gy)) _Gy)
  (:Gz
   (&optional __Gz)
   (if __Gz (setq _Gz __Gz)) _Gz)
  (:currTime
   (&optional __currTime)
   (if __currTime (setq _currTime __currTime)) _currTime)
  (:serialization-length
   ()
   (+
    ;; float64 _AxCalib
    8
    ;; float64 _AyCalib
    8
    ;; float64 _AzCalib
    8
    ;; float64 _Ax
    8
    ;; float64 _Ay
    8
    ;; float64 _Az
    8
    ;; float64 _AxRaw
    8
    ;; float64 _AyRaw
    8
    ;; float64 _AzRaw
    8
    ;; float64 _Vx
    8
    ;; float64 _Vy
    8
    ;; float64 _Vz
    8
    ;; float64 _Gx
    8
    ;; float64 _Gy
    8
    ;; float64 _Gz
    8
    ;; float64 _currTime
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _AxCalib
       (sys::poke _AxCalib (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _AyCalib
       (sys::poke _AyCalib (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _AzCalib
       (sys::poke _AzCalib (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _Ax
       (sys::poke _Ax (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _Ay
       (sys::poke _Ay (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _Az
       (sys::poke _Az (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _AxRaw
       (sys::poke _AxRaw (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _AyRaw
       (sys::poke _AyRaw (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _AzRaw
       (sys::poke _AzRaw (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _Vx
       (sys::poke _Vx (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _Vy
       (sys::poke _Vy (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _Vz
       (sys::poke _Vz (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _Gx
       (sys::poke _Gx (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _Gy
       (sys::poke _Gy (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _Gz
       (sys::poke _Gz (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _currTime
       (sys::poke _currTime (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _AxCalib
     (setq _AxCalib (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _AyCalib
     (setq _AyCalib (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _AzCalib
     (setq _AzCalib (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _Ax
     (setq _Ax (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _Ay
     (setq _Ay (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _Az
     (setq _Az (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _AxRaw
     (setq _AxRaw (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _AyRaw
     (setq _AyRaw (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _AzRaw
     (setq _AzRaw (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _Vx
     (setq _Vx (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _Vy
     (setq _Vy (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _Vz
     (setq _Vz (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _Gx
     (setq _Gx (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _Gy
     (setq _Gy (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _Gz
     (setq _Gz (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _currTime
     (setq _currTime (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get sensors::IMUData :md5sum-) "34b732ae811cee8c11c282e3af23a7b1")
(setf (get sensors::IMUData :datatype-) "sensors/IMUData")
(setf (get sensors::IMUData :definition-)
      "float64 AxCalib
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
float64 currTime

")



(provide :sensors/IMUData "34b732ae811cee8c11c282e3af23a7b1")


