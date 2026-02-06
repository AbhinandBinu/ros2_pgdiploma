import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class AlphaPublisher(Node):

    def __init__(self):
        super().__init__('alpha_publisher')
        self.publisher_ = self.create_publisher(String, 'letters', 10)

        self.current_char = ord('A')   # ASCII value of 'A'
        self.timer = self.create_timer(0.5, self.publish_letter)

    def publish_letter(self):
        if self.current_char > ord('Z'):
            self.get_logger().info('Finished publishing A to Z')
            self.timer.cancel()
            return

        msg = String()
        msg.data = chr(self.current_char)
        self.publisher_.publish(msg)

        self.get_logger().info(f'Published: {msg.data}')
        self.current_char += 1


def main():
    rclpy.init()
    node = AlphaPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()


