import rclpy
from rclpy.node import Node
from palindrome_interfaces.srv import CheckPalindrome


class PalindromeServer(Node):

    def __init__(self):
        super().__init__('palindrome_server')
        self.srv = self.create_service(
            CheckPalindrome,
            'check_palindrome',
            self.check_callback
        )
        self.get_logger().info('Palindrome Server Started')

    def check_callback(self, request, response):
        text = request.input

        if text == text[::-1]:
            response.is_palindrome = True
        else:
            response.is_palindrome = False

        self.get_logger().info(
            f"Received: '{text}' | Palindrome: {response.is_palindrome}"
        )

        return response


def main():
    rclpy.init()
    node = PalindromeServer()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()

