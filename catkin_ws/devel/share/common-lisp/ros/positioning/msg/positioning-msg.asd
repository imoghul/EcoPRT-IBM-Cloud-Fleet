
(cl:in-package :asdf)

(defsystem "positioning-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :sensors-msg
)
  :components ((:file "_package")
    (:file "Position" :depends-on ("_package_Position"))
    (:file "_package_Position" :depends-on ("_package"))
  ))