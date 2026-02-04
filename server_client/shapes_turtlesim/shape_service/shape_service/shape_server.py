import math
import rclpy
from rclpy.node import Node
from shape_interfaces.srv import ShapeRequest
from geometry_msgs.msg import Twist


class ShapeServer(Node):

    def __init__(self):
        super().__init__('shape_server')
        self.srv = self.create_service(
            ShapeRequest,
            'shape_service',
            self.handle_shape_request
        )
        self.cmd_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.get_logger().info("Shape Service Server Ready")

    def handle_shape_request(self, request, response):
        shape = request.shape.lower()
        p1 = request.param1
        p2 = request.param2

        if shape == 'square':
            side = p1
            response.area = side * side
            response.perimeter = 4 * side
            response.dimensions = f"Side = {side}"
            self.draw_polygon(4, side)

        elif shape == 'rectangle':
            length = p1
            breadth = p2
            response.area = length * breadth
            response.perimeter = 2 * (length + breadth)
            response.dimensions = f"Length = {length}, Breadth = {breadth}"
            self.draw_rectangle(length, breadth)

        elif shape == 'circle':
            radius = p1
            response.area = math.pi * radius * radius
            response.perimeter = 2 * math.pi * radius
            response.dimensions = f"Radius = {radius}"
            self.draw_circle(radius)

        elif shape == 'triangle':
            side = p1
            response.area = (math.sqrt(3) / 4) * side * side
            response.perimeter = 3 * side
            response.dimensions = f"Side = {side}"
            self.draw_polygon(3, side)

        else:
            response.dimensions = "Invalid shape"
            response.area = 0.0
            response.perimeter = 0.0

        return response

    def draw_polygon(self, sides, side_length):
        twist = Twist()
        angle = 2 * math.pi / sides
        for _ in range(sides):
            twist.linear.x = side_length
            twist.angular.z = 0.0
            self.cmd_pub.publish(twist)
            self.sleep(1)

            twist.linear.x = 0.0
            twist.angular.z = angle
            self.cmd_pub.publish(twist)
            self.sleep(1)

    def draw_rectangle(self, l, b):
        self.draw_polygon(4, l)
        self.draw_polygon(4, b)

    def draw_circle(self, radius):
        twist = Twist()
        twist.linear.x = radius
        twist.angular.z = 1.0
        for _ in range(30):
            self.cmd_pub.publish(twist)
            self.sleep(0.1)

    def sleep(self, sec):
        self.get_clock().sleep_for(rclpy.duration.Duration(seconds=sec))


def main():
    rclpy.init()
    node = ShapeServer()
    rclpy.spin(node)
    rclpy.shutdown()

