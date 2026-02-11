# ROS 2 Action Example – Count Until

This repository contains a **ROS 2 (Humble, Python) Action-based application** developed as part of my ROS 2 learning journey.

The example demonstrates how to implement a **long-running task** using ROS 2 Actions, including:

- Goal handling
- Continuous feedback
- Final result reporting
- Clean interface separation

---

## 📌 Concept Overview

ROS 2 provides three primary communication mechanisms:

| Communication Type | Use Case |
|-------------------|----------|
| Topics            | Continuous data streaming |
| Services          | Request–response (short tasks) |
| Actions           | Long-running tasks with feedback |

This project focuses on **Actions**, which are ideal for:
- Navigation
- Motion execution
- Counting or iterative tasks
- Any process that requires feedback during execution

---

## 🧩 System Architecture

### 1️⃣ Interface Package
- `counter_action_interface`
- Defines the custom action file:
