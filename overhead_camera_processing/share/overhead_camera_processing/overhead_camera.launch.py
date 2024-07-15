from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    launch_descript = []
    for camera_id in range(1, 5):  # Launch for cameras 1 to 4
        node = Node(
            package='overhead_camera_processing',
            executable='overhead_camera_node',
            name=f'overhead_camera_{camera_id}',
            parameters=[{'camera_id': camera_id}],
            output='screen',
        )
        launch_descript.append(node)
    return LaunchDescription(launch_descript)

