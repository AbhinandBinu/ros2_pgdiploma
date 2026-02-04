ROS 2 Custom Messages Practice

This folder contains ROS 2 (Humble, Python) packages created as part of my ROS 2 learning series, focused on designing and using custom message types for structured data communication between nodes.

Custom messages allow ROS nodes to exchange application-specific data instead of being limited to standard message types.

📌 Purpose of This Folder

The main goals of these packages are to:

Understand how custom .msg files are created

Learn how message definitions translate into Python message classes

Practice publishing and subscribing to structured data

Separate interface definitions from node implementations (best practice)

📦 Packages Included

This folder includes custom message examples such as:

Student information messages (ID, name, marks, etc.)

Structured data publishing instead of simple integers or strings

Publisher nodes that send custom message data

Subscriber nodes that receive and process custom message fields

Each package demonstrates how custom messages can represent real-world entities in ROS systems.

🛠️ Technologies Used

ROS 2 Humble

Python (rclpy)

Custom ROS message definitions (.msg)

ament_cmake for interface packages

ament_python for node packages

▶️ How to Build & Run

Source ROS 2:

source /opt/ros/humble/setup.bash


Build the workspace:

colcon build
source install/setup.bash


Run a publisher node:

ros2 run <package_name> <publisher_node>


Run a subscriber node (in another terminal):

ros2 run <package_name> <subscriber_node>


To inspect message fields:

ros2 interface show <package_name>/msg/<MessageName>

🎯 Learning Outcomes

Through these exercises, I gained hands-on experience with:

Defining custom message structures

Using custom messages in publisher–subscriber systems

Understanding message generation and imports in ROS 2

Debugging common custom message build and runtime issues

Designing messages that reflect real-world data models

📚 Notes

These examples are learning-focused, not production systems

Messages are intentionally kept simple for clarity

More advanced communication models (services, actions) are explored in separate folders

🤖 Author

Abhinand Binu
Robotics & Automation Engineer
ROS 2 | Robotics | Automation
