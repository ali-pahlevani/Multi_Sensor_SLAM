cmake_minimum_required(VERSION 3.5)
project(linorobot2_gazebo)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclpy REQUIRED)

execute_process(
  COMMAND python3 ${CMAKE_CURRENT_SOURCE_DIR}/scripts/map2gazebo.py
  --map_dir ${CMAKE_CURRENT_SOURCE_DIR}/../linorobot2_navigation/maps
  --model_dir ${CMAKE_INSTALL_PREFIX}/share/${PROJECT_NAME}/models
  --world_dir ${CMAKE_INSTALL_PREFIX}/share/${PROJECT_NAME}/worlds
  RESULT_VARIABLE SCRIPT_RESULT
  OUTPUT_VARIABLE SCRIPT_OUTPUT
)

if(NOT SCRIPT_RESULT EQUAL 0)
  message(WARNING "Python script execution failed with error code: ${SCRIPT_RESULT}")
  message(WARNING "Script output: ${SCRIPT_OUTPUT}")
endif()

install(
  DIRECTORY launch rviz worlds
  DESTINATION share/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/command_timeout.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_environment_hooks("${CMAKE_CURRENT_SOURCE_DIR}/env-hooks/linorobot2_gazebo.sh.in")
ament_package()