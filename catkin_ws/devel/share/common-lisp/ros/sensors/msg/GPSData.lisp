; Auto-generated. Do not edit!


(cl:in-package sensors-msg)


;//! \htmlinclude GPSData.msg.html

(cl:defclass <GPSData> (roslisp-msg-protocol:ros-message)
  ((time
    :reader time
    :initarg :time
    :type std_msgs-msg:String
    :initform (cl:make-instance 'std_msgs-msg:String))
   (lat
    :reader lat
    :initarg :lat
    :type std_msgs-msg:Float64
    :initform (cl:make-instance 'std_msgs-msg:Float64))
   (long
    :reader long
    :initarg :long
    :type std_msgs-msg:Float64
    :initform (cl:make-instance 'std_msgs-msg:Float64)))
)

(cl:defclass GPSData (<GPSData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GPSData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GPSData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sensors-msg:<GPSData> is deprecated: use sensors-msg:GPSData instead.")))

(cl:ensure-generic-function 'time-val :lambda-list '(m))
(cl:defmethod time-val ((m <GPSData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensors-msg:time-val is deprecated.  Use sensors-msg:time instead.")
  (time m))

(cl:ensure-generic-function 'lat-val :lambda-list '(m))
(cl:defmethod lat-val ((m <GPSData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensors-msg:lat-val is deprecated.  Use sensors-msg:lat instead.")
  (lat m))

(cl:ensure-generic-function 'long-val :lambda-list '(m))
(cl:defmethod long-val ((m <GPSData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensors-msg:long-val is deprecated.  Use sensors-msg:long instead.")
  (long m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GPSData>) ostream)
  "Serializes a message object of type '<GPSData>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'time) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'lat) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'long) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GPSData>) istream)
  "Deserializes a message object of type '<GPSData>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'time) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'lat) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'long) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GPSData>)))
  "Returns string type for a message object of type '<GPSData>"
  "sensors/GPSData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GPSData)))
  "Returns string type for a message object of type 'GPSData"
  "sensors/GPSData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GPSData>)))
  "Returns md5sum for a message object of type '<GPSData>"
  "127d8146da420293b29d277551a452ba")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GPSData)))
  "Returns md5sum for a message object of type 'GPSData"
  "127d8146da420293b29d277551a452ba")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GPSData>)))
  "Returns full string definition for message of type '<GPSData>"
  (cl:format cl:nil "std_msgs/String time~%std_msgs/Float64 lat~%std_msgs/Float64 long~%~%================================================================================~%MSG: std_msgs/String~%string data~%~%================================================================================~%MSG: std_msgs/Float64~%float64 data~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GPSData)))
  "Returns full string definition for message of type 'GPSData"
  (cl:format cl:nil "std_msgs/String time~%std_msgs/Float64 lat~%std_msgs/Float64 long~%~%================================================================================~%MSG: std_msgs/String~%string data~%~%================================================================================~%MSG: std_msgs/Float64~%float64 data~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GPSData>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'time))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'lat))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'long))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GPSData>))
  "Converts a ROS message object to a list"
  (cl:list 'GPSData
    (cl:cons ':time (time msg))
    (cl:cons ':lat (lat msg))
    (cl:cons ':long (long msg))
))
