# Multi Sensor SLAM

**A framework to work with Industrial AMR and perform SLAM using various sensors in challenging environments**

In this repository, I have combined different frameworks to come up with a functional AMR, performing Robust SLAM in smart factories and similar environment:

![rtab](https://github.com/user-attachments/assets/36dca959-9468-4c7c-ad9a-43100fb4f004)

1. Linorobot2 as the base repo for creating my AMR,
2. RTAB-Map as the main framework for sensor fusion and SLAM,
3. Kinematic-ICP for the future works on enhancing ICP-Based odometry,

Also, there are two more packages involved (which I made them):
1. amr_main as the base package for running everything together,
2. laser_fusion which contains necessary 2D-LiDAR fusion code (to fuse the measurements of different 2D-LiDARs).

* I'm still working on enhancing it. It needs some corrections yet. Also, some of the parts may go into problem which will be solved in the near future (e.g., using Kinematic-ICP algorithm).

---
## Main Files (To adapt the work to your own needs)
1. RTAB-Map parameter file: In this file, not only can you change the RTAB-Map parameters, also you can set which 2D-LiDAR you want to use (**front**, **back**, **all**) and also, which Stereo Camera (**front**, **back**, **both** (Not available yet))
   
   ```bash
   code ~/Multi_Sensor_SLAM/src/rtabmap_ros/rtabmap_launch/launch/rtabmap.launch.py

2. Change the Robot and Sensors' parameters or Add/Remove them:
   ```bash
   code ~/Multi_Sensor_SLAM/src/linorobot2/linorobot2_description/urdf/4wd_properties.urdf.xacro
   code ~/Multi_Sensor_SLAM/src/linorobot2/linorobot2_description/urdf/robots/4wd.urdf.xacro
   code ~/Multi_Sensor_SLAM/src/linorobot2/linorobot2_description/urdf/sensors/laser_new.urdf.xacro
   code ~/Multi_Sensor_SLAM/src/linorobot2/linorobot2_description/urdf/sensors/stereo_camera.urdf.xacro
   code ~/Multi_Sensor_SLAM/src/linorobot2/linorobot2_description/urdf/sensors/imu.urdf.xacro

3. 2D-LiDAR fusion algorithm:
   ```bash
   code ~/Multi_Sensor_SLAM/src/laser_fusion/laser_fusion/combine_laser_measurements.py

---
## Demo
![amr_rtab_gif_2](https://github.com/user-attachments/assets/d0d5b713-1a9e-42c4-9ad8-94e54d0f8753)


---
## Installation and Usage

- This project needs **ROS 2** (Recommended: **ROS 2 Humble**)

1. **Clone the Repository**:
   ```bash
   git https://github.com/ali-pahlevani/Multi_Sensor_SLAM.git
   cd Multi_Sensor_SLAM

2. **Install the required Dependencies**:
   ```bash
   rosdep update && rosdep install --from-path src --ignore-src -y

3. **Build the Workspace**:
   ```bash
   colcon build
   source install/setup.bash

4. **Launch the Simulation**: 
   ```bash
   ros2 launch amr_main launch_all.launch.py

## If you have any question about any part, please feel free to ask! ## 
