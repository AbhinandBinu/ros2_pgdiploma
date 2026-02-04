import rclpy
from rclpy.node import Node
from string_reverse.srv import Reverse


class ReverseStringServer(Node):

    def __init__(self):
        super().__init__('reverse_string_server')
        self.srv = self.create_service(
            Reverse,
            'reverse_string',
            self.reverse_callback
        )

    def reverse_callback(self, request, response):
        response.output = request.input[::-1]
        self.get_logger().info(f"Incoming: {request.input} → Outgoing: {response.output}")
        return response



def main(args=None):
    rclpy.init(args=args)
    node = ReverseStringServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

