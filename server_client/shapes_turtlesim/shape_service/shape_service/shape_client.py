import rclpy
from rclpy.node import Node
from shape_interfaces.srv import ShapeRequest
import sys


class ShapeClient(Node):

    def __init__(self):
        super().__init__('shape_client')
        self.client = self.create_client(ShapeRequest, 'shape_service')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for shape service...")

    def send_request(self, shape, p1, p2):
        req = ShapeRequest.Request()
        req.shape = shape
        req.param1 = p1
        req.param2 = p2
        return self.client.call_async(req)


def main():
    rclpy.init()
    node = ShapeClient()

    shape = input("Enter shape (square/circle/triangle/rectangle): ")
    p1 = float(input("Enter param1: "))
    p2 = float(input("Enter param2 (0 if not needed): "))

    future = node.send_request(shape, p1, p2)
    rclpy.spin_until_future_complete(node, future)

    response = future.result()
    print("\n--- Shape Details ---")
    print("Dimensions:", response.dimensions)
    print("Area:", response.area)
    print("Perimeter:", response.perimeter)

    rclpy.shutdown()

