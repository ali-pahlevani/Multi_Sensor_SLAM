from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, TimerAction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Declare a launch argument for simulation time
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation time if true'
        ),

        # Start the radar fusion node first
        Node(
            package='radar_fusion',
            executable='combine_radar_measurements',
            name='radar_fusion_node',
            output='screen',
            parameters=[{
                'use_sim_time': LaunchConfiguration('use_sim_time'),
            }],
        ),

        # Delay starting the SLAM node by 3 seconds
        TimerAction(
            period=3.0,  # Wait for 3 seconds
            actions=[
                Node(
                    package='slam_toolbox',
                    executable='sync_slam_toolbox_node',
                    name='slam_toolbox',
                    output='screen',
                    parameters=[{
                        'use_sim_time': LaunchConfiguration('use_sim_time'),
                        'slam_params': '/home/alip22/mobileRadar_ws/src/linorobot2/linorobot2_navigation/config/pure_slam.yaml',  # Path to the config file
                    }],
                    remappings=[('/scan', '/radar/combined_scan')]  # Remap the scan topic
                ),
            ]
        ),
    ])
