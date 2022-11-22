# Install script for directory: /home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/src/sensors

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  include("/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/build/sensors/catkin_generated/safe_execute_install.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/build/sensors/catkin_generated/installspace/sensors.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/sensors/cmake" TYPE FILE FILES
    "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/build/sensors/catkin_generated/installspace/sensorsConfig.cmake"
    "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/build/sensors/catkin_generated/installspace/sensorsConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/sensors" TYPE FILE FILES "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/src/sensors/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/sensors" TYPE PROGRAM FILES "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/build/sensors/catkin_generated/installspace/gpsController.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/sensors" TYPE PROGRAM FILES "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/build/sensors/catkin_generated/installspace/GT_U7.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/sensors" TYPE PROGRAM FILES "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/build/sensors/catkin_generated/installspace/imuController.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/sensors" TYPE PROGRAM FILES "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/build/sensors/catkin_generated/installspace/listener.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/sensors" TYPE PROGRAM FILES "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/build/sensors/catkin_generated/installspace/MPU6050.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/sensors" TYPE PROGRAM FILES "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/build/sensors/catkin_generated/installspace/sensorController.py")
endif()

