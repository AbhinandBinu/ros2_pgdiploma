# ROS 2 Action – Parallel Forward & Reverse Counter

This project demonstrates an advanced ROS 2 Action implementation using Python (Humble).

The system performs two parallel counting operations:

- The Action Server counts forward from 0 → duration.
- The Action Client simultaneously counts backward from duration → 0.
- Once the server completes execution, it returns "Completed".

---

## 📌 Objective

Create an Action-based system that:

- Accepts a duration in seconds
- Publishes feedback during execution
- Executes forward counting on the server
- Executes reverse counting on the client concurrently
- Returns a final result upon completion

---

## 🧩 Action Definition

Timer.action

int32 duration
string result_message

int32 current_value


### Structure:
- Goal: duration
- Feedback: current_value (server counter)
- Result: completion message

---

## ⚙️ System Architecture

### Action Server
- Receives duration as goal
- Counts forward from 0 to duration
- Publishes feedback at each step
- Returns "Completed" when finished

### Action Client
- Sends duration goal
- Receives feedback asynchronously
- Starts reverse counting in a separate thread
- Prints final result after server completes

---

## ▶️ Build Instructions

```bash
source /opt/ros/humble/setup.bash
colcon build
source install/setup.bash

▶️ Run

Start Server:

ros2 run timer_action_server timer_server


Start Client:

ros2 run timer_action_server timer_client

🧠 Learning Outcomes

Understanding ROS 2 Action lifecycle

Implementing Goal–Feedback–Result pattern

Asynchronous client handling

Parallel execution using Python threading

Concurrency concepts in robotics software

Clean separation between interface and implementation

📚 Why This Matters

In real robotics systems:

Navigation runs while localization updates

Motion control executes while sensors stream data

Tasks run concurrently

This project simulates similar concurrent behavior using ROS 2 Actions.

🤖 Author

Abhinand Binu
Robotics & Automation Engineer
ROS 2 | Robotics | Automation
