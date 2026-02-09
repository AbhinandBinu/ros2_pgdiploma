import rclpy
from rclpy.node import Node
from palindrome_interfaces.srv import CheckPalindrome


class PalindromeClient(Node):

    def __init__(self):
        super().__init__('palindrome_client')
        self.client = self.create_client(CheckPalindrome, 'check_palindrome')

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for palindrome service...')

        self.req = CheckPalindrome.Request()
        self.req.input = 'madam'

        self.future = self.client.call_async(self.req)


def main():
    rclpy.init()
    node = PalindromeClient()

    rclpy.spin_until_future_complete(node, node.future)

    if node.future.result() is not None:
        result = node.future.result().is_palindrome
        node.get_logger().info(f'Is palindrome: {result}')
    else:
        node.get_logger().error('Service call failed')

    rclpy.shutdown()


if __name__ == '__main__':
    main()

