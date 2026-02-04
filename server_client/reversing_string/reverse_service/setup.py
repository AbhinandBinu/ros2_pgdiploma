from setuptools import find_packages, setup

package_name = 'reverse_service'

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
        'reverse_server = reverse_service.reverse_server:main',
        'reverse_client = reverse_service.reverse_client:main',
        ],
    },
)
