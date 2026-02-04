import rclpy
from rclpy.node import Node

from std_msgs.msg import String, Int32



class Frequency(Node):

    def __init__(self):
        super().__init__('frequency_subscriber')
        self.subscription = self.create_subscription(Int32,'fast_topic',self.listener_callback,10)
        self.subscription = self.create_subscription(Int32,'medium_topic',self.listener_callback,10)
        self.subscription = self.create_subscription(String,'slow_topic',self.listener_callback,10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('frequency is: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    frequency = Frequency()

    rclpy.spin(frequency)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
