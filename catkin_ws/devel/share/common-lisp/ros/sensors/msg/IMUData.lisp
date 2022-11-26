; Auto-generated. Do not edit!


(cl:in-package sensors-msg)


;//! \htmlinclude IMUData.msg.html

(cl:defclass <IMUData> (roslisp-msg-protocol:ros-message)
  ((AxCalib
    :reader AxCalib
    :initarg :AxCalib
    :type std_msgs-msg:Float64
    :initform (cl:make-instance 'std_msgs-msg:Float64))
   (AyCalib
    :reader AyCalib
    :initarg :AyCalib
    :type std_msgs-msg:Float64
    :initform (cl:make-instance 'std_msgs-msg:Float64))
   (AzCalib
    :reader AzCalib
    :initarg :AzCalib
    :type std_msgs-msg:Float64
    :initform (cl:make-instance 'std_msgs-msg:Float64))
   (Ax
    :reader Ax
    :initarg :Ax
    :type std_msgs-msg:Float64
    :initform (cl:make-instance 'std_msgs-msg:Float64))
   (Ay
    :reader Ay
    :initarg :Ay
    :type std_msgs-msg:Float64
    :initform (cl:make-instance 'std_msgs-msg:Float64))
   (Az
    :reader Az
    :initarg :Az
    :type std_msgs-msg:Float64
    :initform (cl:make-instance 'std_msgs-msg:Float64))
   (AxRaw
    :reader AxRaw
    :initarg :AxRaw
    :type std_msgs-msg:Float64
    :initform (cl:make-instance 'std_msgs-msg:Float64))
   (AyRaw
    :reader AyRaw
    :initarg :AyRaw
    :type std_msgs-msg:Float64
    :initform (cl:make-instance 'std_msgs-msg:Float64))
   (AzRaw
    :reader AzRaw
    :initarg :AzRaw
    :type std_msgs-msg:Float64
    :initform (cl:make-instance 'std_msgs-msg:Float64))
   (Vx
    :reader Vx
    :initarg :Vx
    :type std_msgs-msg:Float64
    :initform (cl:make-instance 'std_msgs-msg:Float64))
   (Vy
    :reader Vy
    :initarg :Vy
    :type std_msgs-msg:Float64
    :initform (cl:make-instance 'std_msgs-msg:Float64))
   (Vz
    :reader Vz
    :initarg :Vz
    :type std_msgs-msg:Float64
    :initform (cl:make-instance 'std_msgs-msg:Float64))
   (Gx
    :reader Gx
    :initarg :Gx
    :type std_msgs-msg:Float64
    :initform (cl:make-instance 'std_msgs-msg:Float64))
   (Gy
    :reader Gy
    :initarg :Gy
    :type std_msgs-msg:Float64
    :initform (cl:make-instance 'std_msgs-msg:Float64))
   (Gz
    :reader Gz
    :initarg :Gz
    :type std_msgs-msg:Float64
    :initform (cl:make-instance 'std_msgs-msg:Float64))
   (currTime
    :reader currTime
    :initarg :currTime
    :type std_msgs-msg:Float64
    :initform (cl:make-instance 'std_msgs-msg:Float64)))
)

(cl:defclass IMUData (<IMUData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <IMUData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'IMUData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sensors-msg:<IMUData> is deprecated: use sensors-msg:IMUData instead.")))

(cl:ensure-generic-function 'AxCalib-val :lambda-list '(m))
(cl:defmethod AxCalib-val ((m <IMUData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensors-msg:AxCalib-val is deprecated.  Use sensors-msg:AxCalib instead.")
  (AxCalib m))

(cl:ensure-generic-function 'AyCalib-val :lambda-list '(m))
(cl:defmethod AyCalib-val ((m <IMUData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensors-msg:AyCalib-val is deprecated.  Use sensors-msg:AyCalib instead.")
  (AyCalib m))

(cl:ensure-generic-function 'AzCalib-val :lambda-list '(m))
(cl:defmethod AzCalib-val ((m <IMUData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensors-msg:AzCalib-val is deprecated.  Use sensors-msg:AzCalib instead.")
  (AzCalib m))

(cl:ensure-generic-function 'Ax-val :lambda-list '(m))
(cl:defmethod Ax-val ((m <IMUData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensors-msg:Ax-val is deprecated.  Use sensors-msg:Ax instead.")
  (Ax m))

(cl:ensure-generic-function 'Ay-val :lambda-list '(m))
(cl:defmethod Ay-val ((m <IMUData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensors-msg:Ay-val is deprecated.  Use sensors-msg:Ay instead.")
  (Ay m))

(cl:ensure-generic-function 'Az-val :lambda-list '(m))
(cl:defmethod Az-val ((m <IMUData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensors-msg:Az-val is deprecated.  Use sensors-msg:Az instead.")
  (Az m))

(cl:ensure-generic-function 'AxRaw-val :lambda-list '(m))
(cl:defmethod AxRaw-val ((m <IMUData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensors-msg:AxRaw-val is deprecated.  Use sensors-msg:AxRaw instead.")
  (AxRaw m))

(cl:ensure-generic-function 'AyRaw-val :lambda-list '(m))
(cl:defmethod AyRaw-val ((m <IMUData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensors-msg:AyRaw-val is deprecated.  Use sensors-msg:AyRaw instead.")
  (AyRaw m))

(cl:ensure-generic-function 'AzRaw-val :lambda-list '(m))
(cl:defmethod AzRaw-val ((m <IMUData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensors-msg:AzRaw-val is deprecated.  Use sensors-msg:AzRaw instead.")
  (AzRaw m))

(cl:ensure-generic-function 'Vx-val :lambda-list '(m))
(cl:defmethod Vx-val ((m <IMUData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensors-msg:Vx-val is deprecated.  Use sensors-msg:Vx instead.")
  (Vx m))

(cl:ensure-generic-function 'Vy-val :lambda-list '(m))
(cl:defmethod Vy-val ((m <IMUData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensors-msg:Vy-val is deprecated.  Use sensors-msg:Vy instead.")
  (Vy m))

(cl:ensure-generic-function 'Vz-val :lambda-list '(m))
(cl:defmethod Vz-val ((m <IMUData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensors-msg:Vz-val is deprecated.  Use sensors-msg:Vz instead.")
  (Vz m))

(cl:ensure-generic-function 'Gx-val :lambda-list '(m))
(cl:defmethod Gx-val ((m <IMUData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensors-msg:Gx-val is deprecated.  Use sensors-msg:Gx instead.")
  (Gx m))

(cl:ensure-generic-function 'Gy-val :lambda-list '(m))
(cl:defmethod Gy-val ((m <IMUData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensors-msg:Gy-val is deprecated.  Use sensors-msg:Gy instead.")
  (Gy m))

(cl:ensure-generic-function 'Gz-val :lambda-list '(m))
(cl:defmethod Gz-val ((m <IMUData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensors-msg:Gz-val is deprecated.  Use sensors-msg:Gz instead.")
  (Gz m))

(cl:ensure-generic-function 'currTime-val :lambda-list '(m))
(cl:defmethod currTime-val ((m <IMUData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensors-msg:currTime-val is deprecated.  Use sensors-msg:currTime instead.")
  (currTime m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <IMUData>) ostream)
  "Serializes a message object of type '<IMUData>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'AxCalib) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'AyCalib) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'AzCalib) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'Ax) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'Ay) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'Az) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'AxRaw) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'AyRaw) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'AzRaw) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'Vx) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'Vy) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'Vz) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'Gx) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'Gy) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'Gz) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'currTime) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <IMUData>) istream)
  "Deserializes a message object of type '<IMUData>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'AxCalib) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'AyCalib) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'AzCalib) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'Ax) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'Ay) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'Az) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'AxRaw) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'AyRaw) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'AzRaw) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'Vx) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'Vy) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'Vz) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'Gx) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'Gy) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'Gz) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'currTime) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<IMUData>)))
  "Returns string type for a message object of type '<IMUData>"
  "sensors/IMUData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'IMUData)))
  "Returns string type for a message object of type 'IMUData"
  "sensors/IMUData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<IMUData>)))
  "Returns md5sum for a message object of type '<IMUData>"
  "e854ee703c7cc2b23f6a5df92872cf41")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'IMUData)))
  "Returns md5sum for a message object of type 'IMUData"
  "e854ee703c7cc2b23f6a5df92872cf41")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<IMUData>)))
  "Returns full string definition for message of type '<IMUData>"
  (cl:format cl:nil "std_msgs/Float64 AxCalib~%std_msgs/Float64 AyCalib~%std_msgs/Float64 AzCalib~%std_msgs/Float64 Ax~%std_msgs/Float64 Ay~%std_msgs/Float64 Az~%std_msgs/Float64 AxRaw~%std_msgs/Float64 AyRaw~%std_msgs/Float64 AzRaw~%std_msgs/Float64 Vx~%std_msgs/Float64 Vy~%std_msgs/Float64 Vz~%std_msgs/Float64 Gx~%std_msgs/Float64 Gy~%std_msgs/Float64 Gz~%std_msgs/Float64 currTime~%~%================================================================================~%MSG: std_msgs/Float64~%float64 data~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'IMUData)))
  "Returns full string definition for message of type 'IMUData"
  (cl:format cl:nil "std_msgs/Float64 AxCalib~%std_msgs/Float64 AyCalib~%std_msgs/Float64 AzCalib~%std_msgs/Float64 Ax~%std_msgs/Float64 Ay~%std_msgs/Float64 Az~%std_msgs/Float64 AxRaw~%std_msgs/Float64 AyRaw~%std_msgs/Float64 AzRaw~%std_msgs/Float64 Vx~%std_msgs/Float64 Vy~%std_msgs/Float64 Vz~%std_msgs/Float64 Gx~%std_msgs/Float64 Gy~%std_msgs/Float64 Gz~%std_msgs/Float64 currTime~%~%================================================================================~%MSG: std_msgs/Float64~%float64 data~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <IMUData>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'AxCalib))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'AyCalib))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'AzCalib))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'Ax))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'Ay))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'Az))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'AxRaw))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'AyRaw))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'AzRaw))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'Vx))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'Vy))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'Vz))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'Gx))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'Gy))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'Gz))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'currTime))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <IMUData>))
  "Converts a ROS message object to a list"
  (cl:list 'IMUData
    (cl:cons ':AxCalib (AxCalib msg))
    (cl:cons ':AyCalib (AyCalib msg))
    (cl:cons ':AzCalib (AzCalib msg))
    (cl:cons ':Ax (Ax msg))
    (cl:cons ':Ay (Ay msg))
    (cl:cons ':Az (Az msg))
    (cl:cons ':AxRaw (AxRaw msg))
    (cl:cons ':AyRaw (AyRaw msg))
    (cl:cons ':AzRaw (AzRaw msg))
    (cl:cons ':Vx (Vx msg))
    (cl:cons ':Vy (Vy msg))
    (cl:cons ':Vz (Vz msg))
    (cl:cons ':Gx (Gx msg))
    (cl:cons ':Gy (Gy msg))
    (cl:cons ':Gz (Gz msg))
    (cl:cons ':currTime (currTime msg))
))
