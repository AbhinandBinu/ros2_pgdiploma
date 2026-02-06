import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import time


class NumberPublisher(Node):

    def __init__(self):
        super().__init__('number_publisher')
        self.publisher_ = self.create_publisher(Int32, 'numbers', 10)

        for i in range(1, 101):
            msg = Int32()
            msg.data = i
            self.publisher_.publish(msg)
            self.get_logger().info(f'Published: {i}')
            time.sleep(0.5)


def main():
    rclpy.init()
    node = NumberPublisher()
    rclpy.spin_once(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

