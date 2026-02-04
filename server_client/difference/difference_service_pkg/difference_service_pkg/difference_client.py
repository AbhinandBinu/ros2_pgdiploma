import rclpy
from rclpy.node import Node
from difference_interfaces.srv import Difference
import sys

class DifferenceClient(Node):

    def __init__(self):
        super().__init__('difference_client')
        self.client = self.create_client(Difference, 'difference_service')

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service...')

        self.req = Difference.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        self.future = self.client.call_async(self.req)

def main(args=None):
    rclpy.init(args=args)

    if len(sys.argv) != 3:
        print("Usage: ros2 run difference_service_pkg difference_client a b")
        return

    node = DifferenceClient()
    node.send_request(int(sys.argv[1]), int(sys.argv[2]))

    while rclpy.ok():
        rclpy.spin_once(node)
        if node.future.done():
            response = node.future.result()
            node.get_logger().info(f"Difference = {response.difference}")
            break

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

