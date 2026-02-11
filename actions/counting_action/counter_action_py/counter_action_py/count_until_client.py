import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from counter_action_interface.action import CountUntil

class CountUntilClient(Node):

    def __init__(self):
        super().__init__('count_until_action_client')
        self._client = ActionClient(self, CountUntil, 'count_until')

    def send_goal(self, number):
        goal = CountUntil.Goal()
        goal.target_number = number
        self._client.wait_for_server()
        self.get_logger().info('Sending goal')
        self._send_goal_future = self._client.send_goal_async(
            goal, feedback_callback=self.feedback_callback)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        self.goal_handle = future.result()
        if not self.goal_handle.accepted:
            self.get_logger().info('Goal rejected')
            return
        self.get_logger().info('Goal accepted')
        self._result_future = self.goal_handle.get_result_async()
        self._result_future.add_done_callback(self.result_callback)

    def feedback_callback(self, feedback_msg):
        self.get_logger().info(f'Feedback: {feedback_msg.feedback.current_count}')

    def result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f'Result: success = {result.success}')
        rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)
    node = CountUntilClient()
    node.send_goal(5)
    rclpy.spin(node)

if __name__ == '__main__':
    main()
