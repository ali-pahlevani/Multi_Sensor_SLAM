# Multi Sensor SLAM

**A framework to work with Industrial AMRs and perform SLAM using various sensors in challenging environments**

In this repository, I have combined different frameworks to create a functional AMR that performs **Robust SLAM** in smart factories and similar environments:

![rtab](https://github.com/user-attachments/assets/36dca959-9468-4c7c-ad9a-43100fb4f004)


For my AMR development, I’ve selected the following **Open-Source Repositories**:
1. **[Linorobot2](https://github.com/linorobot/linorobot2?tab=readme-ov-file)** as the base repository for **creating my AMR**,
2. **[RTAB-Map](https://github.com/introlab/rtabmap)** as the main framework for **sensor fusion and SLAM**,
3. **[Kinematic-ICP](https://github.com/PRBonn/kinematic-icp)** for future work on **enhancing ICP-based odometry**,

Additionally, there are two more packages I created:
1. **amr_main** as the base package for running **everything together**,
2. **laser_fusion** which contains the necessary **2D-LiDAR fusion node** (to fuse measurements from different 2D LiDARs).

* I’m still working on enhancing this project. It works well, but still needs some improvements to incorporate additional features (e.g., using **Kinematic-ICP** alongside **RTAB-Map**).

---
## Main Files (To adapt the work to your needs)
1. **RTAB-Map parameter file**: In this file, you can change the RTAB-Map parameters. You can also set **which** 2D LiDAR you want to use (**front, back, all**) and **which** Stereo Camera (**front, back, both** -> (Not available yet)).
   
   ```bash
   code ~/Multi_Sensor_SLAM/src/rtabmap_ros/rtabmap_launch/launch/rtabmap.launch.py

2. Change the Robot and Sensors' **parameters** or **Add/Remove** them:
   ```bash
   code ~/Multi_Sensor_SLAM/src/linorobot2/linorobot2_description/urdf/4wd_properties.urdf.xacro
   code ~/Multi_Sensor_SLAM/src/linorobot2/linorobot2_description/urdf/robots/4wd.urdf.xacro
   code ~/Multi_Sensor_SLAM/src/linorobot2/linorobot2_description/urdf/sensors/laser_new.urdf.xacro
   code ~/Multi_Sensor_SLAM/src/linorobot2/linorobot2_description/urdf/sensors/stereo_camera.urdf.xacro
   code ~/Multi_Sensor_SLAM/src/linorobot2/linorobot2_description/urdf/sensors/imu.urdf.xacro

3. 2D-LiDAR **fusion** algorithm:
   ```bash
   code ~/Multi_Sensor_SLAM/src/laser_fusion/laser_fusion/combine_laser_measurements.py

---
## Demo
![amr_rtab_gif_2](https://github.com/user-attachments/assets/d0d5b713-1a9e-42c4-9ad8-94e54d0f8753)

* In this demo, I have used only the **front LiDAR** (not both). I have also used the **front stereo camera**. Here, I'm performing **VIO** and **ICP odometry**, as well as **visual** and **laser** **loop closures** to create a **2D map**. Additionally, RTAB-Map uses **graph-based SLAM**.

---
## Installation and Usage

- This project requires **ROS 2** (**Recommended: ROS 2 Humble**):

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
