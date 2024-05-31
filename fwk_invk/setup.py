from setuptools import setup

package_name = 'fwk_invk'

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
    maintainer='rohin',
    maintainer_email='rohin@todo.todo',
    description='SCARA fwk and invk',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ 'listener = fwk_invk.subscriber_member_function:main',
        ],
    },
)
