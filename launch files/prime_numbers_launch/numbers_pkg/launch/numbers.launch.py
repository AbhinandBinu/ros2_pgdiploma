from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='numbers_pkg',
            executable='number_pub',
            name='number_publisher',
            output='screen'
        ),
        Node(
            package='numbers_pkg',
            executable='number_sub',
            name='number_subscriber',
            output='screen'
        ),
    ])

