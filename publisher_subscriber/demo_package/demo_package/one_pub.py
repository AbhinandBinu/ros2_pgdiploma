import rclpy
from rclpy.node import Node

from std_msgs.msg import String, Int32


class Publisher(Node):

    def __init__(self):
        super().__init__('one_publisher')
        self.name_pub = self.create_publisher(String, '/status', 10)
        self.number_pub = self.create_publisher(Int32, '/numbers', 10)
        timer_period = 0.5  # seconds
        self.name = 'abhinand'
        self.number = '100'
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        name = String()
        name.data = self.name
        number = Int32
        number.data = Int32
        self.name_pub.publish(name)
        self.number_pub.publish(number)
        self.get_logger().info(f'Publishing:{name.data},{number.data}')


def main(args=None):
    rclpy.init(args=args)

    publisher = Publisher()

    rclpy.spin(publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    student_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
    
