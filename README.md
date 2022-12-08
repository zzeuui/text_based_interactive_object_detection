# text_based_interactive_object_detection

## realsense camera
```
$ sudo apt-get install ros-$ROS_DISTRO-realsense2-camera
$ sudo apt-get install ros-$ROS_DISTRO-realsense2-description
```

## darknet_ros
```
$ git clone --recursive https://github.com/leggedrobotics/darknet_ros.git
$ catkin_make -DCMAKE_BUILD_TYPE=Release
```

## docker
```
$ xhost +local:docker
$ docker run -it --gpus all --privileged -e DISPLAY=unix$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -e "QT_X11_NO_MITSHM=1" <image>
```
* -it
* --gpus all : use gpu
* --privileged : connect device
* -e DISPLAY=unix$DISPLAY : allow display
* -v /tmp/.X11-unix:/tmp/.X11-unix : allow display
* -e "QT_X11_NO_MITSHM=1" : use opencv
