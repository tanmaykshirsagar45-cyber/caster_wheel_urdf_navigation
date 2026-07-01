from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'my_robot_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),
        (
            os.path.join('share', package_name, 'launch'),
            glob('my_robot_description/launch/*')
        ),
        (
            os.path.join('share', package_name, 'urdf'),
            glob('my_robot_description/urdf/*')
        ),
        (
            os.path.join('share', package_name, 'rviz'),
            glob('my_robot_description/rviz/*')
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tanmay',
    maintainer_email='tanmay@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [],
    },
)