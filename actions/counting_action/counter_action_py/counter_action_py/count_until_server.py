import time
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from counter_action_interface.action import CountUntil

class CountUntilServer(Node):

    def __init__(self):
        super().__init__('count_until_action_server')
        self._action_server = ActionServer(
            self,
            CountUntil,
            'count_until',
            self.execute_callback
        )
        self.get_logger().info('Action Server started')

    def execute_callback(self, goal_handle):
        self.get_logger().info(f'Received goal: {goal_handle.request.target_number}')

        feedback = CountUntil.Feedback()
        result = CountUntil.Result()

        for i in range(1, goal_handle.request.target_number + 1):
            feedback.current_count = i
            goal_handle.publish_feedback(feedback)
            self.get_logger().info(f'Counting: {i}')
            time.sleep(1)

        goal_handle.succeed()
        result.success = True
        self.get_logger().info('Goal completed')
        return result


def main(args=None):
    rclpy.init(args=args)
    node = CountUntilServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()