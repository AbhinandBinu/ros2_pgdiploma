import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class TopicNode(Node):

    def __init__(self):
        super().__init__('topic_node')

        self.subscription = self.create_subscription(
            String,
            '/chat_input',
            self.callback,
            10
        )

        self.publisher = self.create_publisher(
            String,
            '/chat_response',
            10
        )

    def callback(self, msg):

        text = msg.data.lower()

        response = String()

        if "hello" in text or "hi" in text:
            response.data = "Hello! How can I assist you?"
        elif "ros2" in text:
            response.data = "ROS 2 is a robotics middleware framework."
        elif "robot" in text:
            response.data = "Robots are intelligent machines."
        else:
            response.data = "I did not understand that."

        self.publisher.publish(response)


def main():
    rclpy.init()
    node = TopicNode()
    rclpy.spin(node)
    rclpy.shutdown()
