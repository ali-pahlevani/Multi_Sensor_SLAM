from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    laser_fusion_share_dir = get_package_share_directory('laser_fusion')

    return LaunchDescription([

        # Static transform publisher node
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher',
            output='screen',
            arguments=['0', '0', '-0.09', '0', '0', '0', 'base_link', 'all_laser_link']
        ),

        # Laser fusion node
        Node(
            package='laser_fusion',
            executable='combine_laser_measurements',
            name='laser_fusion_node',
            output='screen',
            parameters=[]
        ),
    ])
