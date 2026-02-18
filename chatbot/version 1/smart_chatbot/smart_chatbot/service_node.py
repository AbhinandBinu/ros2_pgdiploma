import rclpy
from rclpy.node import Node
from smart_chatbot_interfaces.srv import ChatService


class ServiceNode(Node):

    def __init__(self):
        super().__init__('service_node')

        self.srv = self.create_service(
            ChatService,
            'chat_service',
            self.callback
        )

        self.get_logger().info("Service Node Ready")

    # =====================================================
    # SERVICE CALLBACK
    # =====================================================
    def callback(self, request, response):

        question = request.question.lower()

        # -------------------------
        # Known Robotics Answers
        # -------------------------
        if "ros2" in question or "ros 2" in question:
            response.answer = (
                "ROS 2 is an open-source robotics middleware framework "
                "developed by Open Robotics. It enables communication "
                "between different parts of a robotic system."
            )

        elif "slam" in question:
            response.answer = (
                "SLAM stands for Simultaneous Localization and Mapping. "
                "It allows a robot to build a map of an unknown environment "
                "while tracking its own position within that map."
            )

        elif "action" in question:
            response.answer = (
                "In ROS 2, an Action is used for long-running tasks that "
                "provide feedback during execution and return a result when finished."
            )

        elif "service" in question:
            response.answer = (
                "A Service in ROS 2 follows a request-response pattern. "
                "A client sends a request, and the server returns a response."
            )

        elif "topic" in question:
            response.answer = (
                "A Topic in ROS 2 enables asynchronous communication "
                "between nodes using publishers and subscribers."
            )

        # -------------------------
        # Unknown → Trigger LLM
        # -------------------------
        else:
            response.answer = "UNKNOWN"

        return response


# =====================================================
# MAIN
# =====================================================
def main():
    rclpy.init()
    node = ServiceNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
