import rclpy
from rclpy.node import Node
from string_reverse.srv import Reverse


class ReverseStringClient(Node):

    def __init__(self):
        super().__init__('reverse_string_client')
        self.client = self.create_client(Reverse, 'reverse_string')

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service...')

        self.request = Reverse.Request()

    def send_request(self, text):
        self.request.input = text
        return self.client.call_async(self.request)


def main(args=None):
    rclpy.init(args=args)

    client = ReverseStringClient()
    future = client.send_request("hello ROS2")

    rclpy.spin_until_future_complete(client, future)

    if future.result() is not None:
        client.get_logger().info(
            f"Reversed string: {future.result().output}"
        )
    else:
        client.get_logger().error("Service call failed")

    client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

