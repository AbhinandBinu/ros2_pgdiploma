🤖 ROS 2 Smart Chatbot (Modular Version)
📌 Overview

This project demonstrates a modular chatbot built using ROS 2 Humble (Python).
The system showcases core ROS communication models:

Topics

Services

Actions

GUI Integration

The goal of this project is to simulate real-world robotic system architecture in a conversational system.

🏗 System Architecture
GUI
   ↓
Chat Manager Node
   ↓
--------------------------------
| Topic | Service | Action |
--------------------------------

🧩 Package Structure
chatbot_ws/src/
│
├── smart_chatbot_interfaces   (ament_cmake)
│   ├── srv/ChatService.srv
│   └── action/SystemCheck.action
│
└── smart_chatbot              (ament_python)
    ├── topic_node.py
    ├── service_node.py
    ├── action_server.py
    ├── chat_manager.py
    ├── chat_ui.py
    └── launch/chatbot_launch.py

🔹 Communication Models Used
📡 Topics

Used for simple real-time conversational responses.

Publisher–Subscriber pattern.

🔁 Services

Used for structured question–answer interactions.

Request–Response model.

⚡ Actions

Used for long-running tasks.

Provides feedback during execution.

Returns final result.

🖥 GUI

Built using Tkinter.

Displays conversation messages.

Connected to ROS backend via ChatManager node.

🚀 Build & Run
1️⃣ Build Workspace
cd ~/chatbot_ws
colcon build
source install/setup.bash

2️⃣ Launch System
ros2 launch smart_chatbot chatbot_launch.py

🎯 Learning Objectives

Understand ROS 2 node communication

Design modular multi-node systems

Implement custom .srv and .action files

Separate interface and implementation packages

Build scalable ROS applications

🧠 Future Improvements

AI integration (Local LLM)

Conversation memory

Speech recognition

Modern UI framework

Deployment on embedded systems

👨‍💻 Author

Abhinand Binu
Robotics & Automation Engineer
ROS 2 | Automation | Robotics Software
