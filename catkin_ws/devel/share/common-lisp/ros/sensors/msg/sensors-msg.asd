
(cl:in-package :asdf)

(defsystem "sensors-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "GPSData" :depends-on ("_package_GPSData"))
    (:file "_package_GPSData" :depends-on ("_package"))
    (:file "IMUData" :depends-on ("_package_IMUData"))
    (:file "_package_IMUData" :depends-on ("_package"))
  ))