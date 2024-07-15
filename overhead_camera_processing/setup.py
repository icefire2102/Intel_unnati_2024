from setuptools import setup

package_name = 'overhead_camera_processing'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='riyanshi',
    maintainer_email='riyanshi.mathur2102@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'overhead_camera_node = overhead_camera_processing.overhead_camera_node:main',
        ],
    },
)

