#!/usr/bin/env/pyhon3

import rclpy
from rclpy.node import Node

class SimpleNode(Node):
  def __init__(self):
     super().__init__('simple_node')
     self.get_logger().info('SimpleNode has been created')

def main (args=None):
    rclpy.init(args=args)
    node=SimpleNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown() 

if __name__ == '__main__':
   main()
