import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class Frequency(Node):

    def __init__(self):
        super().__init__('frequency_publisher')

        # Publishers
        self.fast_pub = self.create_publisher(Int32, '/fast_topic', 10)
        self.medium_pub = self.create_publisher(Int32, '/medium_topic', 10)
        self.slow_pub = self.create_publisher(Int32, '/slow_topic', 10)

        # Data values
        self.fast_value = 10
        self.medium_value = 5
        self.slow_value = 1

        # Timer
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        fast_msg = Int32()
        fast_msg.data = self.fast_value

        medium_msg = Int32()
        medium_msg.data = self.medium_value

        slow_msg = Int32()
        slow_msg.data = self.slow_value

        self.fast_pub.publish(fast_msg)
        self.medium_pub.publish(medium_msg)
        self.slow_pub.publish(slow_msg)

        self.get_logger().info(
            f'Frequency values: {fast_msg.data}, {medium_msg.data}, {slow_msg.data}'
        )


def main(args=None):
    rclpy.init(args=args)

    frequency = Frequency()
    rclpy.spin(frequency)

    frequency.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

