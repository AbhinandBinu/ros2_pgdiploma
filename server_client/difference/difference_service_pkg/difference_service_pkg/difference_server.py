import rclpy
from rclpy.node import Node
from difference_interfaces.srv import Difference

class DifferenceServer(Node):

    def __init__(self):
        super().__init__('difference_server')
        self.srv = self.create_service(Difference, 'difference_service', self.callback)
        self.get_logger().info('Difference Server Ready')

    def callback(self, request, response):
        response.difference = request.a - request.b
        self.get_logger().info(f"{request.a} - {request.b} = {response.difference}")
        return response

def main(args=None):
    rclpy.init(args=args)
    node = DifferenceServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
