# 🚀 ROS 2 Autonomous Navigation Simulation

A complete autonomous navigation pipeline built with **ROS 2 Humble** and **Ignition Gazebo (Fortress)** — from a custom-designed simulation environment through SLAM mapping, localization, and autonomous path planning with Nav2.

![ROS2](https://img.shields.io/badge/ROS2-Humble-blue)
![Gazebo](https://img.shields.io/badge/Gazebo-Ignition%20Fortress-orange)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📖 Project Overview

This project implements a full robotics navigation stack in simulation:

- A **custom-designed indoor Gazebo world** (not a stock/default environment) built specifically to test mapping, localization, and navigation
- **SLAM Toolbox** for generating an occupancy grid map of the environment
- **AMCL** for localizing the robot within the saved map
- **Nav2** for planning and executing autonomous navigation to goal poses, including dynamic obstacle avoidance
- **RViz2** for visualizing laser scans, localization, costmaps, and planned paths in real time

The goal was to go beyond a basic tutorial by designing my own environment and validating the entire pipeline end-to-end: simulate → map → localize → navigate.

---

## ✨ Features

- 🗺️ Custom Gazebo world designed from scratch
- 🤖 Robot URDF/SDF description with LiDAR sensor integration
- 🧭 SLAM-based mapping using SLAM Toolbox
- 📍 Map saving and reuse via `map_server`
- 🎯 AMCL-based localization on a pre-built map
- 🚗 Autonomous path planning and execution with Nav2
- 🛑 Real-time obstacle avoidance
- 📊 Full visualization pipeline in RViz2 (TF, laser scans, costmaps, planned paths)

---

## 🧰 Prerequisites

Make sure the following are installed before running this project:

- Ubuntu 22.04 (Jammy)
- [ROS 2 Humble](https://docs.ros.org/en/humble/Installation.html)
- Ignition Gazebo (Fortress) — `ros-humble-ros-ign-gazebo` or `ros-humble-ros-gz`
- Nav2 stack — `ros-humble-navigation2`, `ros-humble-nav2-bringup`
- SLAM Toolbox — `ros-humble-slam-toolbox`
- `colcon` build tools

Install core dependencies:

```bash
sudo apt update
sudo apt install ros-humble-desktop \
  ros-humble-navigation2 \
  ros-humble-nav2-bringup \
  ros-humble-slam-toolbox \
  ros-humble-ros-gz \
  python3-colcon-common-extensions
```

```
caster_wheel_urdf_navigation/
├── my_robot_bringup/
│   ├── my_robot_bringup/
│   │   ├── config/
│   │   │   ├── gazebo_bridge.yaml
│   │   │   ├── mapper_params_online_async.yaml
│   │   │   ├── nav2_params.yaml
│   │   │   └── twist_mux.yaml
│   │   ├── launch/
│   │   │   ├── bringup.launch.py
│   │   │   ├── localization.node.py
│   │   │   ├── my_robot_launch.py
│   │   │   ├── my_robot_launch.xml
│   │   │   ├── nav2_launch.py
│   │   │   └── slam_launch.py
│   │   ├── worlds/
│   │   │   └── simple_world
│   │   └── __init__.py
│   ├── resource/
│   ├── test/
│   ├── CMakeLists.txt
│   ├── package.xml
│   ├── setup.cfg
│   └── setup.py
├── my_robot_description/
│   ├── my_robot_description/
│   │   ├── launch/
│   │   ├── rviz/
│   │   └── urdf/
│   │       ├── common_properties.xacro
│   │       ├── mobile_base_gazebo.xacro
│   │       ├── mobile_base.xacro
│   │       └── my_robot_urdf.xacro
│   ├── resource/
│   ├── CMakeLists.txt
│   ├── package.xml
│   ├── setup.cfg
│   └── setup.py
├── .gitignore
├── LICENSE
└── README.md
---
```

## ⚙️ Installation

1. Create a ROS 2 workspace (if you don't already have one):

```bash
mkdir -p ~/ros2_ws/src
cd ~/imp_ws/src
```

2. Clone this repository:

```bash
git clone https://github.com/tanmaykshirsagar45-cyber/my_robot_navigation.git
```

3. Install dependencies:

```bash
cd ~/imp_ws
rosdep install --from-paths src --ignore-src -r -y
```

---

## 🔨 Build Instructions

```bash
cd ~/imp_ws
colcon build --symlink-install
source install/setup.bash
```


---

## ▶️ Launch Commands

### 1. Launch the custom Gazebo world and spawn the robot

```bash
 ros2 launch my_robot_bringup my_robot.launch.py
```

### 2. Run SLAM to build the map

```bash
ros2 launch slam_toolbox online_async_launch.py params_file:=~/imp_ws/src/my_robot_bringup/my_robot_bringup/config/mapper_params_online_async.yaml
```

Drive the robot around the environment (via teleop or a scripted path) to build the full map, then save it:

```bash
ros2 run nav2_map_server map_saver_cli -f ~/my_map
```

### 3. Now kill all the nodes and start following for using my_robot_launch, localization and nav2 by one file.

```bash
ros2 launch my_robot_bringup bringup.launch.py
```
after this use pose estimate in the direction of urdf.

### 4. Send a navigation goal

Before sending goal outiside the room make sure ti navigate once inside the room so that amcl gets converged to an accurate pose. if not robot may get stuck at one point for longer goal pose initially.
Use RViz2's **Nav2 Goal** tool.


> ⚠️ Adjust launch file names/paths above to match your actual package — update this section once your repo is finalized.

---

## 🎬 Demo

![Demo GIF](docs/demo.gif)

▶️ Full video: *(link to LinkedIn post / YouTube)*

---

## 🚧 Future Improvements

- Add dynamic/moving obstacles to test reactive navigation
- Expand to a larger, multi-room environment
- Tune Nav2 costmap and controller parameters for smoother trajectories
- Add multi-robot navigation support
- Integrate a real robot (hardware-in-the-loop) for sim-to-real transfer
- Add automated tests for navigation success rate

---

## 🛠️ Tech Stack

`ROS 2 Humble` · `Ignition Gazebo (Fortress)` · `Nav2` · `SLAM Toolbox` · `AMCL` · `RViz2` · `URDF` · `SDF` · `TF2` · `LiDAR`

---


## 🙌 Feedback

Feedback, suggestions, and contributions are welcome! Feel free to open an issue or submit a pull request.
