cmake_minimum_required(VERSION 3.8)
project(my_robot_bringup)

find_package(ament_cmake REQUIRED)

cmake_minimum_required(VERSION 3.8)
project(my_robot_bringup)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY my_robot_bringup/launch/
  DESTINATION share/${PROJECT_NAME}/launch
)

install(
  DIRECTORY my_robot_bringup/config/
  DESTINATION share/${PROJECT_NAME}/config
)

install(
  DIRECTORY my_robot_bringup/worlds/
  DESTINATION share/${PROJECT_NAME}/worlds
)

ament_package()
