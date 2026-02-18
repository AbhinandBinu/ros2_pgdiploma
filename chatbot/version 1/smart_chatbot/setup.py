from setuptools import find_packages, setup
import os
from glob import glob


package_name = 'smart_chatbot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
    ('share/ament_index/resource_index/packages',
        ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
    (os.path.join('share', package_name, 'launch'),
        glob('launch/*.py')),
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
             'topic_node = smart_chatbot.topic_node:main',
        'service_node = smart_chatbot.service_node:main',
        'action_server = smart_chatbot.action_server:main',
        'chat_manager = smart_chatbot.chat_manager:main',
        'chat_ui = smart_chatbot.chat_ui:main',
        ],
    },
)
