;; Auto-generated. Do not edit!


(when (boundp 'sensors::GPSData)
  (if (not (find-package "SENSORS"))
    (make-package "SENSORS"))
  (shadow 'GPSData (find-package "SENSORS")))
(unless (find-package "SENSORS::GPSDATA")
  (make-package "SENSORS::GPSDATA"))

(in-package "ROS")
;;//! \htmlinclude GPSData.msg.html


(defclass sensors::GPSData
  :super ros::object
  :slots (_time _lat _long ))

(defmethod sensors::GPSData
  (:init
   (&key
    ((:time __time) "")
    ((:lat __lat) 0.0)
    ((:long __long) 0.0)
    )
   (send-super :init)
   (setq _time (string __time))
   (setq _lat (float __lat))
   (setq _long (float __long))
   self)
  (:time
   (&optional __time)
   (if __time (setq _time __time)) _time)
  (:lat
   (&optional __lat)
   (if __lat (setq _lat __lat)) _lat)
  (:long
   (&optional __long)
   (if __long (setq _long __long)) _long)
  (:serialization-length
   ()
   (+
    ;; string _time
    4 (length _time)
    ;; float64 _lat
    8
    ;; float64 _long
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _time
       (write-long (length _time) s) (princ _time s)
     ;; float64 _lat
       (sys::poke _lat (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _long
       (sys::poke _long (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _time
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _time (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float64 _lat
     (setq _lat (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _long
     (setq _long (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get sensors::GPSData :md5sum-) "6be0f4d623467dbac7ec64212189b37c")
(setf (get sensors::GPSData :datatype-) "sensors/GPSData")
(setf (get sensors::GPSData :definition-)
      "string time
float64 lat
float64 long

")



(provide :sensors/GPSData "6be0f4d623467dbac7ec64212189b37c")


