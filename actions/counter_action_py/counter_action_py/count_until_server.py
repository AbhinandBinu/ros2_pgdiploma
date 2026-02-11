import time #import the time module to use the sleep function for simulating counting delay
import rclpy  #import the rclpy module, which is the ROS client library for Python, to create and manage ROS nodes and communication
from rclpy.node import Node  #import the Node class from the rclpy.node module to create a ROS node
from rclpy.action import ActionServer #import the ActionServer class from the rclpy.action module to create an action server that can communicate with action clients
from counter_action_interface.action import CountUntil #import the CountUntil action definition from the counter_action_interface package to define the action type for the server

class CountUntilServer(Node):  #define the CountUntilServer class, which is a subclass of Node, to implement the action server for counting until a target number

    def __init__(self): #initialize the CountUntilServer class, which is a subclass of Node, and set up the action server to handle CountUntil action requests
        super().__init__('count_until_action_server') #initialize the node with the name 'count_until_action_server'
        self._action_server = ActionServer(
            self,
            CountUntil,
            'count_until',
            self.execute_callback
        )
        self.get_logger().info('Action Server started') #log that the action server has started and is ready to receive goals

    def execute_callback(self, goal_handle): #callback function that is called when a new goal is received by the action server, which will execute the counting logic and provide feedback and result to the client
        self.get_logger().info(f'Received goal: {goal_handle.request.target_number}') #log the target number received in the goal request

        feedback = CountUntil.Feedback() #create a feedback message to send updates to the client during the counting process
        result = CountUntil.Result() #create a result message to send the final result to the client after counting is complete
 
        for i in range(1, goal_handle.request.target_number + 1):  #loop from 1 to the target number specified in the goal request, simulating the counting process
            feedback.current_count = i  #update the current count in the feedback message
            goal_handle.publish_feedback(feedback)  #publish the feedback message to the client to provide updates on the counting progress
            self.get_logger().info(f'Counting: {i}') #log the current count during the counting process
            time.sleep(1) #sleep for 1 second to simulate a delay in counting, making it more realistic for demonstration purposes

        goal_handle.succeed() #mark the goal as succeeded after counting is complete
        result.success = True #set the success value in the result message to True to indicate that the counting was successful
        self.get_logger().info('Goal completed') #log that the goal has been completed and the result is being sent to the client
        return result 


def main(args=None): #main function to initialize the ROS client library, create an instance of the CountUntilServer, and spin the node to process action requests
    rclpy.init(args=args) #initialize the ROS client library
    node = CountUntilServer() #create an instance of the CountUntilServer to start the action server
    rclpy.spin(node) #spin the node to keep it running and able to process incoming action requests until the node is shutdown
    rclpy.shutdown() #shutdown the ROS client library after the node is shutdown and no longer needs to process action requests

if __name__ == '__main__': #check if the script is being run directly, and if so, call the main function to start the action server node
    main() #call the main function to start the action server node and begin processing action requests from clients