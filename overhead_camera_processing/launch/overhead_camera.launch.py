from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='overhead_camera_processing',
            executable='overhead_camera_node',
            name='overhead_camera_node',
            output='screen',
            parameters=[{
                'use_sim_time': True  # Set to True if you are using simulation time
            }]
        ),
    ])
