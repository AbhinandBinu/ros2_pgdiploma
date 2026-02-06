from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='alphabet_pkg',
            executable='alpha_pub',
            name='alpha_publisher',
            output='screen'
        ),
        Node(
            package='alphabet_pkg',
            executable='alpha_sub',
            name='alpha_subscriber',
            output='screen'
        ),
    ])

