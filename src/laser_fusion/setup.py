from setuptools import find_packages, setup

package_name = 'laser_fusion'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/fusion_rviz.launch.py', 'launch/slam_laser.launch.py', 'launch/laser_fusion.launch.py']),
        ('share/' + package_name + '/rviz', ['rviz/main_Rviz.rviz']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='alip22',
    maintainer_email='alip22@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'combine_laser_measurements = laser_fusion.combine_laser_measurements:main',
        ],
    },
)
