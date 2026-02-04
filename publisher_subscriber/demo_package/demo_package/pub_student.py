import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class StudentPublisher(Node):

    def __init__(self):
        super().__init__('student_publisher')
        self.publisher_ = self.create_publisher(String, 'student_name', 10)
        timer_period = 0.5  # seconds
        self.student = 'abhinand'
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = self.student
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing:{msg.data}')


def main(args=None):
    rclpy.init(args=args)

    student_publisher = StudentPublisher()

    rclpy.spin(student_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    student_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
    
