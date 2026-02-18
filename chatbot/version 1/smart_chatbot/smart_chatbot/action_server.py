import time
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from smart_chatbot_interfaces.srv import ChatService
from smart_chatbot_interfaces.action import SystemCheck
from smart_chatbot_interfaces.srv import ChatService
from smart_chatbot_interfaces.action import SystemCheck



class SystemCheckServer(Node):

    def __init__(self):
        super().__init__('system_check_server')

        self._action_server = ActionServer(
            self,
            SystemCheck,
            'system_check',
            self.execute_callback
        )

    def execute_callback(self, goal_handle):

        duration = goal_handle.request.duration

        feedback_msg = SystemCheck.Feedback()
        result = SystemCheck.Result()

        for i in range(duration):

            feedback_msg.feedback = f"Checking... {i+1}/{duration}"
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1)

        goal_handle.succeed()
        result.result = "System Check Completed Successfully"

        return result


def main():
    rclpy.init()
    node = SystemCheckServer()
    rclpy.spin(node)
    rclpy.shutdown()
