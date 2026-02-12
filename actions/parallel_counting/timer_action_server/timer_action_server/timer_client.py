import time
import threading
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from timer_action_interfaces.action import Timer


class TimerActionClient(Node):

    def __init__(self):
        super().__init__('timer_action_client')

        self._client = ActionClient(
            self,
            Timer,
            'timer'
        )

        self.duration = 0
        self.server_finished = False

    def send_goal(self, duration):

        self.duration = duration

        self._client.wait_for_server()

        goal_msg = Timer.Goal()
        goal_msg.duration = duration

        self.get_logger().info(f"Sending goal: {duration}")

        self._send_goal_future = self._client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )

        self._send_goal_future.add_done_callback(
            self.goal_response_callback
        )

    # 🔹 Server Feedback
    def feedback_callback(self, feedback_msg):
        value = feedback_msg.feedback.current_value
        self.get_logger().info(f"Server Feedback: {value}")

    # 🔹 Goal Accepted
    def goal_response_callback(self, future):

        goal_handle = future.result()

        if not goal_handle.accepted:
            self.get_logger().info("Goal Rejected")
            return

        self.get_logger().info("Goal Accepted")

        # Start reverse counting in parallel
        reverse_thread = threading.Thread(
            target=self.reverse_count
        )
        reverse_thread.start()

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(
            self.get_result_callback
        )

    # 🔹 Client Reverse Counting
    def reverse_count(self):

        for i in range(self.duration, -1, -1):
            self.get_logger().info(f"Client Reverse Count: {i}")
            time.sleep(1)

        self.get_logger().info("Client Reverse Finished")

    # 🔹 Final Result from Server
    def get_result_callback(self, future):

        result = future.result().result
        self.get_logger().info(f"Server Result: {result.result_message}")

        self.get_logger().info("Both Tasks Completed")
        rclpy.shutdown()


def main():
    rclpy.init()
    node = TimerActionClient()

    node.send_goal(25)  # 👈 Duration here

    rclpy.spin(node)


if __name__ == '__main__':
    main()
