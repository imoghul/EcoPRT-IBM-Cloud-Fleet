# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "positioning: 1 messages, 0 services")

set(MSG_I_FLAGS "-Ipositioning:/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/src/positioning/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg;-Isensors:/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/src/sensors/msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(positioning_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/src/positioning/msg/Position.msg" NAME_WE)
add_custom_target(_positioning_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "positioning" "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/src/positioning/msg/Position.msg" "sensors/IMUData"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(positioning
  "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/src/positioning/msg/Position.msg"
  "${MSG_I_FLAGS}"
  "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/src/sensors/msg/IMUData.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/positioning
)

### Generating Services

### Generating Module File
_generate_module_cpp(positioning
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/positioning
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(positioning_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(positioning_generate_messages positioning_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/src/positioning/msg/Position.msg" NAME_WE)
add_dependencies(positioning_generate_messages_cpp _positioning_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(positioning_gencpp)
add_dependencies(positioning_gencpp positioning_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS positioning_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(positioning
  "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/src/positioning/msg/Position.msg"
  "${MSG_I_FLAGS}"
  "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/src/sensors/msg/IMUData.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/positioning
)

### Generating Services

### Generating Module File
_generate_module_eus(positioning
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/positioning
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(positioning_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(positioning_generate_messages positioning_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/src/positioning/msg/Position.msg" NAME_WE)
add_dependencies(positioning_generate_messages_eus _positioning_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(positioning_geneus)
add_dependencies(positioning_geneus positioning_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS positioning_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(positioning
  "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/src/positioning/msg/Position.msg"
  "${MSG_I_FLAGS}"
  "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/src/sensors/msg/IMUData.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/positioning
)

### Generating Services

### Generating Module File
_generate_module_lisp(positioning
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/positioning
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(positioning_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(positioning_generate_messages positioning_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/src/positioning/msg/Position.msg" NAME_WE)
add_dependencies(positioning_generate_messages_lisp _positioning_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(positioning_genlisp)
add_dependencies(positioning_genlisp positioning_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS positioning_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(positioning
  "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/src/positioning/msg/Position.msg"
  "${MSG_I_FLAGS}"
  "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/src/sensors/msg/IMUData.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/positioning
)

### Generating Services

### Generating Module File
_generate_module_nodejs(positioning
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/positioning
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(positioning_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(positioning_generate_messages positioning_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/src/positioning/msg/Position.msg" NAME_WE)
add_dependencies(positioning_generate_messages_nodejs _positioning_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(positioning_gennodejs)
add_dependencies(positioning_gennodejs positioning_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS positioning_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(positioning
  "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/src/positioning/msg/Position.msg"
  "${MSG_I_FLAGS}"
  "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/src/sensors/msg/IMUData.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/positioning
)

### Generating Services

### Generating Module File
_generate_module_py(positioning
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/positioning
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(positioning_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(positioning_generate_messages positioning_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/src/positioning/msg/Position.msg" NAME_WE)
add_dependencies(positioning_generate_messages_py _positioning_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(positioning_genpy)
add_dependencies(positioning_genpy positioning_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS positioning_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/positioning)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/positioning
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(positioning_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET sensors_generate_messages_cpp)
  add_dependencies(positioning_generate_messages_cpp sensors_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/positioning)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/positioning
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(positioning_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET sensors_generate_messages_eus)
  add_dependencies(positioning_generate_messages_eus sensors_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/positioning)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/positioning
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(positioning_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET sensors_generate_messages_lisp)
  add_dependencies(positioning_generate_messages_lisp sensors_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/positioning)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/positioning
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(positioning_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET sensors_generate_messages_nodejs)
  add_dependencies(positioning_generate_messages_nodejs sensors_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/positioning)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/positioning\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/positioning
    DESTINATION ${genpy_INSTALL_DIR}
    # skip all init files
    PATTERN "__init__.py" EXCLUDE
    PATTERN "__init__.pyc" EXCLUDE
  )
  # install init files which are not in the root folder of the generated code
  string(REGEX REPLACE "([][+.*()^])" "\\\\\\1" ESCAPED_PATH "${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/positioning")
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/positioning
    DESTINATION ${genpy_INSTALL_DIR}
    FILES_MATCHING
    REGEX "${ESCAPED_PATH}/.+/__init__.pyc?$"
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(positioning_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET sensors_generate_messages_py)
  add_dependencies(positioning_generate_messages_py sensors_generate_messages_py)
endif()
