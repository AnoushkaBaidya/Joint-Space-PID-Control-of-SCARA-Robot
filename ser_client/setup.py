from setuptools import setup

package_name = 'ser_client'

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
    maintainer='anoushka',
    maintainer_email='baidya.anoushka@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'service1 = ser_client.service_member_function:main',
            'client1 = ser_client.client_member_function:main',
        ],
    },
)
