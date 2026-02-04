ROS 2 Publisher–Subscriber Practice Packages

This folder contains a collection of ROS 2 (Humble, Python) packages created as part of my ROS 2 learning series, focused specifically on mastering publisher–subscriber communication.

Each package in this folder is a small, self-contained exercise designed to understand how data flows between nodes using ROS 2 topics.

📌 Purpose of This Folder

The main goal of this folder is to:

Practice topic-based communication in ROS 2

Understand how publishers and subscribers interact

Learn how data can be processed, filtered, or transformed by subscribers

Build confidence in ROS 2 Python package structure

These examples progress from very basic nodes to slightly more logic-oriented subscribers.

📦 Packages Included

This folder contains multiple ROS 2 packages such as:

Basic publisher and subscriber examples

Packages that publish numeric or textual data

Subscribers that perform filtering or processing (e.g., prime number filtering)

Experiments using standard ROS messages (std_msgs)

Practice with timers, callbacks, and node lifecycle basics

Each package can be built and run independently.

🛠️ Technologies Used

ROS 2 Humble

Python (rclpy)

Standard ROS message types (std_msgs)

ament_python build system

▶️ How to Build & Run

Source ROS 2:

source /opt/ros/humble/setup.bash


Build the workspace:

colcon build
source install/setup.bash


Run a specific package:

ros2 run <package_name> <node_name>


To observe topic data:

ros2 topic echo <topic_name>

🎯 Learning Outcomes

Through these packages, I gained hands-on experience with:

ROS 2 node creation and execution

Publisher–subscriber architecture

Topic naming and message flow

Writing clean and modular ROS 2 Python code

Debugging common ROS 2 Python package issues

📚 Notes

These packages are learning-focused, not production projects

Code is kept simple and readable for clarity

More advanced ROS 2 concepts (services, actions, turtlesim, launch files) are maintained in separate folders

🤖 Author

Abhinand Binu
Robotics & Automation Engineer
ROS 2 | Robotics | Automation
