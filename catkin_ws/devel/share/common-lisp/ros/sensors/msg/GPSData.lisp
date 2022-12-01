; Auto-generated. Do not edit!


(cl:in-package sensors-msg)


;//! \htmlinclude GPSData.msg.html

(cl:defclass <GPSData> (roslisp-msg-protocol:ros-message)
  ((time
    :reader time
    :initarg :time
    :type cl:string
    :initform "")
   (lat
    :reader lat
    :initarg :lat
    :type cl:float
    :initform 0.0)
   (long
    :reader long
    :initarg :long
    :type cl:float
    :initform 0.0))
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
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'time))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'time))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'lat))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'long))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GPSData>) istream)
  "Deserializes a message object of type '<GPSData>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'time) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'time) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'lat) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'long) (roslisp-utils:decode-double-float-bits bits)))
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
  "6be0f4d623467dbac7ec64212189b37c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GPSData)))
  "Returns md5sum for a message object of type 'GPSData"
  "6be0f4d623467dbac7ec64212189b37c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GPSData>)))
  "Returns full string definition for message of type '<GPSData>"
  (cl:format cl:nil "string time~%float64 lat~%float64 long~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GPSData)))
  "Returns full string definition for message of type 'GPSData"
  (cl:format cl:nil "string time~%float64 lat~%float64 long~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GPSData>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'time))
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GPSData>))
  "Converts a ROS message object to a list"
  (cl:list 'GPSData
    (cl:cons ':time (time msg))
    (cl:cons ':lat (lat msg))
    (cl:cons ':long (long msg))
))
