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
1. ...

2. ...

3. ...

4. ...

---
## Demo
![amr_rtab_gif_2](https://github.com/user-attachments/assets/d0d5b713-1a9e-42c4-9ad8-94e54d0f8753)


---
## Installation and Usage
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ali-pahlevani/Versatile_Robot.git
   cd Versatile_Robot

2. **Build the Workspace**:
   ```bash
   catkin_make
   source devel/setup.bash

3. **Launch the Simulation**: 
In one terminal, launch the main simulation:
   ```bash
   roslaunch robot_arm main_Launch.launch
This loads the world in Gazebo, spawns the robot, and initializes the controllers.

## If you have any question about any part, please feel free to ask! ## 
