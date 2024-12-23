from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    laser_fusion_share_dir = get_package_share_directory('laser_fusion')
    rviz_file_path = os.path.join(laser_fusion_share_dir, 'rviz', 'main_Rviz.rviz')

    if not os.path.exists(rviz_file_path):
        raise FileNotFoundError(f"RViz file not found: {rviz_file_path}")

    return LaunchDescription([
        DeclareLaunchArgument(
            'rviz_config',
            default_value=rviz_file_path,
            description='Path to the RViz configuration file'
        ),

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

        # RViz2 node with custom configuration
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', LaunchConfiguration('rviz_config')]
        ),
    ])
