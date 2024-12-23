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

   
## If you have any question about any part, please feel free to ask! ## 
