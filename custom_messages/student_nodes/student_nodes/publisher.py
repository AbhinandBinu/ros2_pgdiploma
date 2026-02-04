import rclpy
from rclpy.node import Node
from msg_interface.msg import Student


class StudentPublisher(Node):

    def __init__(self):
        super().__init__('student_publisher')
        self.publisher_ = self.create_publisher(Student, 'student_info', 10)
        self.timer = self.create_timer(1.0, self.publish_data)

        # index to control which student to publish
        self.index = 0

        # student data list
        self.students = [
            {'id': 1, 'name': 'Anu', 'marks': 89.5},
            {'id': 2, 'name': 'Rahul', 'marks': 92.0}
        ]

    def publish_data(self):
        msg = Student()

        current_student = self.students[self.index]

        msg.id = current_student['id']
        msg.name = current_student['name']
        msg.marks = current_student['marks']

        self.publisher_.publish(msg)

        self.get_logger().info(
            f"Published -> ID: {msg.id}, Name: {msg.name}, Marks: {msg.marks}"
        )

        # move to next student, repeat
        self.index = (self.index + 1) % len(self.students)


def main():
    rclpy.init()
    node = StudentPublisher()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()

