import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from smart_chatbot_interfaces.srv import ChatService
from smart_chatbot_interfaces.action import SystemCheck
from rclpy.action import ActionClient
import ollama


class ChatManager(Node):

    def __init__(self):
        super().__init__('chat_manager')

        # Topic
        self.publisher = self.create_publisher(String, '/chat_input', 10)
        self.subscription = self.create_subscription(
            String,
            '/chat_response',
            self.topic_callback,
            10
        )

        # Service
        self.client = self.create_client(ChatService, 'chat_service')

        # Action
        self.action_client = ActionClient(
            self,
            SystemCheck,
            'system_check'
        )

        self.latest_response = ""
        self.get_logger().info("Fast Hybrid ChatManager Started")

    # =====================================================
    # ROUTER
    # =====================================================
    def process_message(self, text):

        text_clean = text.strip().lower()
        self.latest_response = ""

        question_keywords = ["what", "why", "how", "explain", "define", "tell"]

        if text_clean.endswith('?') or any(word in text_clean for word in question_keywords):
            self.call_service(text)
            return

        if "start" in text_clean or "run" in text_clean:
            self.start_action()
            return

        msg = String()
        msg.data = text
        self.publisher.publish(msg)

    # =====================================================
    # TOPIC
    # =====================================================
    def topic_callback(self, msg):
        self.latest_response = msg.data

    # =====================================================
    # SERVICE
    # =====================================================
    def call_service(self, question):

        if not self.client.wait_for_service(timeout_sec=1.0):
            self.latest_response = "Service not available."
            return

        request = ChatService.Request()
        request.question = question

        future = self.client.call_async(request)

        def service_callback(future):
            try:
                response = future.result()

                if response.answer == "UNKNOWN":
                    self.latest_response = self.ask_llm_fast(question)
                else:
                    self.latest_response = response.answer

            except Exception as e:
                self.latest_response = f"Service Error: {str(e)}"

        future.add_done_callback(service_callback)

    # =====================================================
    # ACTION
    # =====================================================
    def start_action(self):

        if not self.action_client.wait_for_server(timeout_sec=1.0):
            self.latest_response = "Action server not available."
            return

        goal_msg = SystemCheck.Goal()
        goal_msg.duration = 5

        send_goal_future = self.action_client.send_goal_async(goal_msg)

        def goal_response_callback(future):
            goal_handle = future.result()

            if not goal_handle.accepted:
                self.latest_response = "Action rejected."
                return

            result_future = goal_handle.get_result_async()

            def result_callback(future):
                result = future.result().result
                self.latest_response = result.result

            result_future.add_done_callback(result_callback)

        send_goal_future.add_done_callback(goal_response_callback)

    # =====================================================
    # FAST LLM (PHI MODEL)
    # =====================================================
    def ask_llm_fast(self, prompt):

        try:
            response = ollama.chat(
                model='phi',  # 🔥 fastest option
                messages=[
                    {'role': 'user', 'content': prompt}
                ],
                options={
                    "num_predict": 120,     # limit response length
                    "temperature": 0.7
                }
            )

            return response['message']['content']

        except Exception as e:
            return f"LLM Error: {str(e)}"


# =====================================================
# MAIN
# =====================================================
def main():
    rclpy.init()
    node = ChatManager()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
