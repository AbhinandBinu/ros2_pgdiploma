import rclpy
from rclpy.node import Node
from msg_interface.msg import Student

class StudentSubscriber(Node):
    def __init__(self):
        super().__init__('student_subscriber')
        self.subscription = self.create_subscription(
            Student,
            'student_info',
            self.callback,
            10
        )

    def callback(self, msg):
        self.get_logger().info(
            f"ID: {msg.id}, Name: {msg.name}, Marks: {msg.marks}"
        )

def main():
    rclpy.init()
    node = StudentSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
