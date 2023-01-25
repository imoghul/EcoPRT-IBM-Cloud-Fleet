; Auto-generated. Do not edit!


(cl:in-package positioning-msg)


;//! \htmlinclude Position.msg.html

(cl:defclass <Position> (roslisp-msg-protocol:ros-message)
  ((gps
    :reader gps
    :initarg :gps
    :type sensors-msg:GPSData
    :initform (cl:make-instance 'sensors-msg:GPSData))
   (imu
    :reader imu
    :initarg :imu
    :type sensors-msg:IMUData
    :initform (cl:make-instance 'sensors-msg:IMUData)))
)

(cl:defclass Position (<Position>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Position>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Position)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name positioning-msg:<Position> is deprecated: use positioning-msg:Position instead.")))

(cl:ensure-generic-function 'gps-val :lambda-list '(m))
(cl:defmethod gps-val ((m <Position>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader positioning-msg:gps-val is deprecated.  Use positioning-msg:gps instead.")
  (gps m))

(cl:ensure-generic-function 'imu-val :lambda-list '(m))
(cl:defmethod imu-val ((m <Position>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader positioning-msg:imu-val is deprecated.  Use positioning-msg:imu instead.")
  (imu m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Position>) ostream)
  "Serializes a message object of type '<Position>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'gps) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'imu) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Position>) istream)
  "Deserializes a message object of type '<Position>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'gps) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'imu) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Position>)))
  "Returns string type for a message object of type '<Position>"
  "positioning/Position")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Position)))
  "Returns string type for a message object of type 'Position"
  "positioning/Position")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Position>)))
  "Returns md5sum for a message object of type '<Position>"
  "6fb7f457c11907847ca6763dd0bb7aad")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Position)))
  "Returns md5sum for a message object of type 'Position"
  "6fb7f457c11907847ca6763dd0bb7aad")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Position>)))
  "Returns full string definition for message of type '<Position>"
  (cl:format cl:nil "sensors/GPSData gps~%sensors/IMUData imu~%~%================================================================================~%MSG: sensors/GPSData~%string time~%float64 lat~%float64 long~%~%================================================================================~%MSG: sensors/IMUData~%float64 AxCalib~%float64 AyCalib~%float64 AzCalib~%float64 Ax~%float64 Ay~%float64 Az~%float64 AxRaw~%float64 AyRaw~%float64 AzRaw~%float64 Vx~%float64 Vy~%float64 Vz~%float64 Gx~%float64 Gy~%float64 Gz~%float64 GxCalib~%float64 GyCalib~%float64 GzCalib~%float64 GxRaw~%float64 GyRaw~%float64 GzRaw~%float64 currTime~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Position)))
  "Returns full string definition for message of type 'Position"
  (cl:format cl:nil "sensors/GPSData gps~%sensors/IMUData imu~%~%================================================================================~%MSG: sensors/GPSData~%string time~%float64 lat~%float64 long~%~%================================================================================~%MSG: sensors/IMUData~%float64 AxCalib~%float64 AyCalib~%float64 AzCalib~%float64 Ax~%float64 Ay~%float64 Az~%float64 AxRaw~%float64 AyRaw~%float64 AzRaw~%float64 Vx~%float64 Vy~%float64 Vz~%float64 Gx~%float64 Gy~%float64 Gz~%float64 GxCalib~%float64 GyCalib~%float64 GzCalib~%float64 GxRaw~%float64 GyRaw~%float64 GzRaw~%float64 currTime~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Position>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'gps))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'imu))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Position>))
  "Converts a ROS message object to a list"
  (cl:list 'Position
    (cl:cons ':gps (gps msg))
    (cl:cons ':imu (imu msg))
))
