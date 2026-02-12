import time
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from timer_action_interfaces.action import Timer


class TimerActionServer(Node):

    def __init__(self):
        super().__init__('timer_action_server')

        self._action_server = ActionServer(
            self,
            Timer,
            'timer',
            self.execute_callback
        )

        self.get_logger().info("Timer Action Server Started")

    def execute_callback(self, goal_handle):

        duration = goal_handle.request.duration
        feedback_msg = Timer.Feedback()
        result = Timer.Result()

        self.get_logger().info(f"Counting forward to {duration}")

        for i in range(0, duration + 1):

            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                result.result_message = "Canceled"
                return result

            feedback_msg.current_value = i
            goal_handle.publish_feedback(feedback_msg)

            self.get_logger().info(f"Server Count: {i}")
            time.sleep(1)

        goal_handle.succeed()
        result.result_message = "Completed"

        return result


def main():
    rclpy.init()
    node = TimerActionServer()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
