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

    def callback(self, request, response):

        question = request.question.lower()

        if "ros2" in question or "ros 2" in question:
            response.answer = (
                "ROS 2 is an open-source robotics middleware "
                "developed by Open Robotics."
            )

        elif "slam" in question:
            response.answer = (
                "SLAM stands for Simultaneous Localization "
                "and Mapping."
            )

        elif "action" in question:
            response.answer = (
                "In ROS 2, Actions are used for long-running "
                "tasks with feedback."
            )

        elif "service" in question:
            response.answer = (
                "Services follow a request-response model."
            )

        elif "topic" in question:
            response.answer = (
                "Topics use publisher-subscriber communication."
            )

        else:
            response.answer = "UNKNOWN"

        return response


def main():
    rclpy.init()
    node = ServiceNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
