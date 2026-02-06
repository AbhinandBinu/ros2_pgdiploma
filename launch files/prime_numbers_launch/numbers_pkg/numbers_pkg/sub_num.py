import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


class PrimeSubscriber(Node):

    def __init__(self):
        super().__init__('prime_subscriber')
        self.subscription = self.create_subscription(
            Int32,
            'numbers',
            self.callback,
            10
        )

    def callback(self, msg):
        if is_prime(msg.data):
            self.get_logger().info(f'Prime Number: {msg.data}')


def main():
    rclpy.init()
    node = PrimeSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
