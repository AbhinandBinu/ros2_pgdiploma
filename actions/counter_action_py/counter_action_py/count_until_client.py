import rclpy #import the rclpy module, which is the ROS client library for Python, to create and manage ROS nodes and communication
from rclpy.node import Node  #import the Node class from the rclpy.node module to create a ROS node
from rclpy.action import ActionClient  #import the ActionClient class from the rclpy.action module to create an action client that can communicate with the action server
from counter_action_interface.action import CountUntil #import the CountUntil action definition from the counter_action_interface package

class CountUntilClient(Node): #define the CountUntilClient class, which is a subclass of Node

    def __init__(self):  #initialize the CountUntilClient class, which is a subclass of Node
        super().__init__('count_until_action_client')   #initialize the node with the name 'count_until_action_client'
        self._client = ActionClient(self, CountUntil, 'count_until')  #first argument is the node, second is the action type, third is the action name

    def send_goal(self, number):
        goal = CountUntil.Goal() #create a goal message
        goal.target_number = number #set the target number in the goal message
        self._client.wait_for_server() #wait for the action server to be available
        self.get_logger().info('Sending goal') #log that we are sending the goal
        self._send_goal_future = self._client.send_goal_async( 
            goal, feedback_callback=self.feedback_callback) #send the goal asynchronously and set the feedback callback
        self._send_goal_future.add_done_callback(self.goal_response_callback) #add a callback to handle the response from the action server when the goal is accepted or rejected

    def goal_response_callback(self, future): #callback to handle the response from the action server when the goal is accepted or rejected
        self.goal_handle = future.result() #get the goal handle from the future result
        if not self.goal_handle.accepted: #check if the goal was accepted
            self.get_logger().info('Goal rejected')#log that the goal was rejected
            return
        self.get_logger().info('Goal accepted') #log that the goal was accepted
        self._result_future = self.goal_handle.get_result_async()  #get the result asynchronously from the goal handle
        self._result_future.add_done_callback(self.result_callback) #add a callback to handle the result when it is available

    def feedback_callback(self, feedback_msg): #callback to handle feedback from the action server
        self.get_logger().info(f'Feedback: {feedback_msg.feedback.current_count}') #log the current count from the feedback message

    def result_callback(self, future): #callback to handle the result when it is available
        result = future.result().result #get the result from the future result
        self.get_logger().info(f'Result: success = {result.success}') #log the success value from the result message
        rclpy.shutdown() #shutdown the ROS client library after receiving the result


def main(args=None): #main function to initialize the ROS client library, create an instance of the CountUntilClient, send a goal, and spin the node to process callbacks
    rclpy.init(args=args) #initialize the ROS client library
    node = CountUntilClient() #create an instance of the CountUntilClient
    node.send_goal(5) #send a goal to count until 5
    rclpy.spin(node) #spin the node to process callbacks until the result is received and the node is shutdown

if __name__ == '__main__': #check if the script is being run directly
    main()   #call the main function to start the client node and send the goal
