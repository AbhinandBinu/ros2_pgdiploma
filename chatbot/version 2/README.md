🤖 ROS 2 Hybrid Smart Chatbot
📌 Overview

This project demonstrates a Hybrid Smart Chatbot built using ROS 2 Humble (Python).

The system combines:

ROS Topics

ROS Services

ROS Actions

Local LLM (Ollama)

The goal is to simulate a real robotic middleware architecture where deterministic logic and AI reasoning coexist.

🏗 System Architecture
GUI
   ↓
Chat Manager (Decision Layer)
   ↓
------------------------------------------------
| Topics | Services | Actions | Local LLM |
------------------------------------------------

🔹 Communication Models
📡 Topics

Used for simple conversational responses using Publisher–Subscriber communication.

🔁 Services

Handles deterministic knowledge queries via Request–Response pattern.

⚡ Actions

Used for long-running operations with feedback and final result.

🧠 Local LLM

When service layer returns UNKNOWN, the system calls a local LLM (Ollama) for intelligent response generation.

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

🚀 Build & Run
1️⃣ Build Workspace
cd ~/chatbot_ws
colcon build
source install/setup.bash

2️⃣ Launch System
ros2 launch smart_chatbot chatbot_launch.py

🧠 How It Works

User sends message via GUI.

ChatManager routes request:

Greeting → Topic

Known question → Service

Command → Action

Unknown → LLM fallback

Response is returned to GUI.

⚡ Performance Optimization

Lightweight LLM model (phi / mistral)

Limited token generation

Deterministic layer reduces LLM calls

Hybrid routing improves response speed

🎯 Learning Objectives

Understand ROS 2 communication models

Design layered distributed systems

Integrate AI modules into middleware

Optimize local LLM performance

Implement modular scalable architecture

🔮 Future Improvements

Conversation memory

Streaming LLM responses

Voice input/output

Confidence-based routing

Embedded deployment (Jetson / Raspberry Pi)

👨‍💻 Author

Abhinand Binu
Robotics & Automation Engineer
ROS 2 | Robotics Software | AI Integration
