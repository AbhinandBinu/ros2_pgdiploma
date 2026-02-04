ROS 2 Service (Server–Client) Practice Packages

This folder contains ROS 2 (Humble, Python) service-based examples developed as part of my ROS 2 learning series, focusing on understanding client–server communication in ROS 2.

Unlike topics (which stream data continuously), services are used for on-demand, request–response interactions, and these packages are designed to practice that concept clearly.

📌 Purpose of This Folder

The main objectives of these packages are to:

Understand the ROS 2 service model

Design and use custom .srv interfaces

Implement service servers and service clients

Practice deterministic communication in ROS 2

Learn clean separation between interface packages and node packages

📦 Packages Included

This folder includes multiple service-based packages such as:

Simple arithmetic service (add, subtract, etc.)

String processing services (e.g., reverse string)

Practice services using custom request and response fields

Client nodes that send user input and display service responses

Each service setup typically includes:

A service server node

A service client node

A custom service interface package (where applicable)

🛠️ Technologies Used

ROS 2 Humble

Python (rclpy)

Custom ROS 2 service definitions (.srv)

ament_python and ament_cmake build systems

▶️ How to Build & Run

Source ROS 2:

source /opt/ros/humble/setup.bash


Build the workspace:

colcon build
source install/setup.bash


Run the service server:

ros2 run <service_package> <server_node>


Run the service client (in another terminal):

ros2 run <service_package> <client_node>


To inspect available services:

ros2 service list

🎯 Learning Outcomes

By working through these packages, I practiced:

Writing and using custom .srv files

Understanding how request and response data is exchanged

Debugging service communication issues

Structuring ROS 2 service-based systems cleanly

Choosing between topics vs services for different use cases

📚 Notes

These packages are learning-oriented examples

Code is intentionally kept simple and readable

Each package focuses on one concept at a time

More advanced concepts like actions and simulations are explored separately

🤖 Author

Abhinand Binu
Robotics & Automation Engineer
ROS 2 | Robotics | Automation
