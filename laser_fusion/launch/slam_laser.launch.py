#How to save the map  -->  ros2 run nav2_map_server map_saver_cli -f <map_name>

from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    laser_fusion_share_dir = get_package_share_directory('laser_fusion')
    maps_folder_path = os.path.join(laser_fusion_share_dir, 'maps')

    if not os.path.exists(maps_folder_path):
        os.makedirs(maps_folder_path)

    map_filename = os.path.join(maps_folder_path, 'company_map.yaml')

    return LaunchDescription([
        Node(
            package='slam_toolbox',
            executable='async_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[
                {'use_sim_time': True},
                {'map_resolution': 0.05},
                {'map_size': 512},
                {'minimum_time_between_scans': 0.1},
                {'maximum_range': 10.0},
                {'sensor_frame': 'all_laser_link'},
                {'base_frame': 'base_footprint'},
                {'odom_frame': 'odom'},
                {'map_frame': 'map'},
                {'scan_topic': '/laser/all_laser'},
                {'odom_topic': '/odom'},
                {'save_map': True},
                {'map_filename': map_filename},
            ],
        ),
    ])
