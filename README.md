
# Gesture Car
Gesture Car is a ROS-based simulation of a four-wheeler car controlled by hand gestures. Using computer vision techniques and ROS nodes, the system reads hand gestures captured by your machine's camera. These gestures are then translated into commands that drive the car within a simulated environment in Gazebo. Gesture Car provides an interactive and intuitive way to navigate the virtual world, making it a fun and engaging project for robotics enthusiasts and anyone looking to explore ROS capabilities.



## Deployment

Follow these steps to install and set up Gesture car]:

1. [Make sure you have a working ROS installation. If not, refer to the official ROS documentation for installation instructions.](http://wiki.ros.org/noetic/Installation)

2. Clone this repository into your catkin workspace:


```bash
  cd ~/catkin_ws/src
  git clone https://github.com/yuvimehta/ROS.git

```
3. Build the Package
```bash
  cd ~/catkin_ws
  catkin_make
```
4. Launch the nodes:
```bash
  roslaunch gesture_car base_gazebo_control.launch
```
## Configuration
To configure for your specific setup

-> Install these dependencies:
```bash
        pip3 install opencv-python
        pip3 install mediapipe
  ```

-> `VideoCapture(0)`: The index of the camera feed. Adjust this parameter if your camera index differs from the default


