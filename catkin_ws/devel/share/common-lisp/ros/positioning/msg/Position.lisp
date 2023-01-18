; Auto-generated. Do not edit!


(cl:in-package positioning-msg)


;//! \htmlinclude Position.msg.html

(cl:defclass <Position> (roslisp-msg-protocol:ros-message)
  ((latitude
    :reader latitude
    :initarg :latitude
    :type cl:float
    :initform 0.0)
   (longitude
    :reader longitude
    :initarg :longitude
    :type cl:float
    :initform 0.0)
   (altitude
    :reader altitude
    :initarg :altitude
    :type cl:float
    :initform 0.0)
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

(cl:ensure-generic-function 'latitude-val :lambda-list '(m))
(cl:defmethod latitude-val ((m <Position>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader positioning-msg:latitude-val is deprecated.  Use positioning-msg:latitude instead.")
  (latitude m))

(cl:ensure-generic-function 'longitude-val :lambda-list '(m))
(cl:defmethod longitude-val ((m <Position>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader positioning-msg:longitude-val is deprecated.  Use positioning-msg:longitude instead.")
  (longitude m))

(cl:ensure-generic-function 'altitude-val :lambda-list '(m))
(cl:defmethod altitude-val ((m <Position>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader positioning-msg:altitude-val is deprecated.  Use positioning-msg:altitude instead.")
  (altitude m))

(cl:ensure-generic-function 'imu-val :lambda-list '(m))
(cl:defmethod imu-val ((m <Position>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader positioning-msg:imu-val is deprecated.  Use positioning-msg:imu instead.")
  (imu m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Position>) ostream)
  "Serializes a message object of type '<Position>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'latitude))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'longitude))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'altitude))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'imu) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Position>) istream)
  "Deserializes a message object of type '<Position>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'latitude) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'longitude) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'altitude) (roslisp-utils:decode-double-float-bits bits)))
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
  "26972fc25ce21b0631b32a2b006a1bf4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Position)))
  "Returns md5sum for a message object of type 'Position"
  "26972fc25ce21b0631b32a2b006a1bf4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Position>)))
  "Returns full string definition for message of type '<Position>"
  (cl:format cl:nil "float64 latitude~%float64 longitude~%float64 altitude~%sensors/IMUData imu~%~%================================================================================~%MSG: sensors/IMUData~%float64 AxCalib~%float64 AyCalib~%float64 AzCalib~%float64 Ax~%float64 Ay~%float64 Az~%float64 AxRaw~%float64 AyRaw~%float64 AzRaw~%float64 Vx~%float64 Vy~%float64 Vz~%float64 Gx~%float64 Gy~%float64 Gz~%float64 GxCalib~%float64 GyCalib~%float64 GzCalib~%float64 GxRaw~%float64 GyRaw~%float64 GzRaw~%float64 currTime~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Position)))
  "Returns full string definition for message of type 'Position"
  (cl:format cl:nil "float64 latitude~%float64 longitude~%float64 altitude~%sensors/IMUData imu~%~%================================================================================~%MSG: sensors/IMUData~%float64 AxCalib~%float64 AyCalib~%float64 AzCalib~%float64 Ax~%float64 Ay~%float64 Az~%float64 AxRaw~%float64 AyRaw~%float64 AzRaw~%float64 Vx~%float64 Vy~%float64 Vz~%float64 Gx~%float64 Gy~%float64 Gz~%float64 GxCalib~%float64 GyCalib~%float64 GzCalib~%float64 GxRaw~%float64 GyRaw~%float64 GzRaw~%float64 currTime~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Position>))
  (cl:+ 0
     8
     8
     8
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'imu))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Position>))
  "Converts a ROS message object to a list"
  (cl:list 'Position
    (cl:cons ':latitude (latitude msg))
    (cl:cons ':longitude (longitude msg))
    (cl:cons ':altitude (altitude msg))
    (cl:cons ':imu (imu msg))
))
