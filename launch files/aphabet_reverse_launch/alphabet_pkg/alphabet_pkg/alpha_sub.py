import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class AlphaReverseSubscriber(Node):

    def __init__(self):
        super().__init__('alpha_reverse_subscriber')
        self.subscription = self.create_subscription(
            String,
            'letters',
            self.listener_callback,
            10
        )
        self.letters = []

    def listener_callback(self, msg):
        letter = msg.data
        self.letters.append(letter)
        self.get_logger().info(f'Received: {letter}')

        # When Z is received, reverse and display
        if letter == 'Z':
            self.get_logger().info('All letters received. Printing in reverse order:')
            for ch in reversed(self.letters):
                self.get_logger().info(ch)


def main():
    rclpy.init()
    node = AlphaReverseSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
