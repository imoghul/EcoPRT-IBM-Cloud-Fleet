#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/src/cloud"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/install_isolated/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/install_isolated/lib/python3/dist-packages:/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/build_isolated/cloud/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/build_isolated/cloud" \
    "/usr/bin/python3" \
    "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/src/cloud/setup.py" \
     \
    build --build-base "/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/build_isolated/cloud" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/install_isolated" --install-scripts="/home/pi/EcoPRT-IBM-Cloud-Fleet/catkin_ws/install_isolated/bin"
