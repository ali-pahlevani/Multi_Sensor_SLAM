from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    first_package  = 'linorobot2_gazebo'
    second_package = 'laser_fusion'
    third_package  = 'kinematic_icp'
    fourth_package = 'rtabmap_launch'

    first_launch_file  = FindPackageShare(first_package).find(first_package) +   '/launch/gazebo_laser.launch.py'
    second_launch_file = FindPackageShare(second_package).find(second_package) + '/launch/laser_fusion.launch.py'
    third_launch_file  = FindPackageShare(third_package).find(third_package) +   '/launch/online_node.launch.py'
    fourth_launch_file = FindPackageShare(fourth_package).find(fourth_package) + '/launch/rtabmap.launch.py'

    first_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(first_launch_file)
    )
    
    second_launch = TimerAction(
        period=5.0,
        actions=[IncludeLaunchDescription(PythonLaunchDescriptionSource(second_launch_file))]
    )

    third_launch = TimerAction(
        period=5.0,
        actions=[IncludeLaunchDescription(PythonLaunchDescriptionSource(third_launch_file))]
    )

    fourth_launch = TimerAction(
        period=5.0,
        actions=[IncludeLaunchDescription(PythonLaunchDescriptionSource(fourth_launch_file))]
    )
    
    return LaunchDescription([
        first_launch,
        second_launch,
        #third_launch,
        fourth_launch,
    ])
