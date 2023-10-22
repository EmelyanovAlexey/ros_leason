import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node
from launch_ros.actions import SetParameter

# Этот файл запуска импортирует необходимые пакеты, а затем создает demo_nodesпеременную, 
# в которой будут храниться узлы, которые мы создали в файле запуска предыдущего руководства.

def generate_launch_description():
    demo_nodes = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('maniac'), 'launch'),
            '/turtle_tf2_demo.launch.py']),
            # launch_arguments={'target_frame': 'carrot1'}.items()
        )

    # Последняя часть кода добавит наш фиксированный carrot1кадр в мир черепах, 
    # используя наш fixed_frame_tf2_broadcasterузел.
    return LaunchDescription([
        SetParameter(name='radius', value=4),
        SetParameter(name='direction_of_rotation', value=1),
        demo_nodes,
        Node(
            package='maniac',
            executable='fixed_frame_tf2_broadcaster',
            name='fixed_broadcaster',
        ),
    ])