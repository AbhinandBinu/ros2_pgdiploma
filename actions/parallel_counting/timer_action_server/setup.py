from setuptools import find_packages, setup

package_name = 'timer_action_server'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='abhinand',
    maintainer_email='abhinandbinu777@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'timer_server = timer_action_server.timer_server:main',
            'timer_client = timer_action_server.timer_client:main',
        ],
    },
)
