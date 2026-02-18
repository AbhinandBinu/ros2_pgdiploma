from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='smart_chatbot', executable='topic_node'),
        Node(package='smart_chatbot', executable='service_node'),
        Node(package='smart_chatbot', executable='action_server'),
        Node(package='smart_chatbot', executable='chat_manager'),
        Node(package='smart_chatbot', executable='chat_ui'),
    ])
