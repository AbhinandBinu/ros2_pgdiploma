from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='palindrome_service',
            executable='palindrome_server',
            output='screen'
        ),
        Node(
            package='palindrome_service',
            executable='palindrome_client',
            output='screen'
        ),
    ])

