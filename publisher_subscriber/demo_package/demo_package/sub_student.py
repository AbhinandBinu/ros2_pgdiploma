import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class StudentSubscriber(Node):

    def __init__(self):
        super().__init__('student_subscriber')
        self.subscription = self.create_subscription(
            String,
            'student_name',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        uppercase_name = msg.data.upper()
        self.get_logger().info(f'student name is: {uppercase_name}')


def main(args=None):
    rclpy.init(args=args)

    student_subscriber = StudentSubscriber()

    rclpy.spin(student_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    student_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
