#!/usr/bin/env/pyhon3

import rclpy
from rclpy.node import Node
import time

class SimpleNode(Node):
  def __init__(self):
     super().__init__('num_node')
  def print_numbers(self):
     for i in range(1,11):
        self.get_logger().info(f'Number:{i}')
        rclpy.spin_once(self,timeout_sec=0.1)
        time.sleep(1)

def main (args=None):
    rclpy.init(args=args)
    node=SimpleNode()
    node.print_numbers()
    node.destroy_node()
    rclpy.shutdown() 

if __name__ == '__main__':
   main()
