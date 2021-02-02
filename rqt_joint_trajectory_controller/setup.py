from setuptools import setup

package_name = 'rqt_joint_trajectory_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['plugin.xml']),
        ('share/' + package_name + '/resource', ['resource/joint_trajectory_controller.ui',
                                                 'resource/on.svg',
                                                 'resource/off.svg',
                                                 'resource/scope.png',
                                                 'resource/scope.svg',
                                                 'resource/double_editor.ui']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Kevin DeMarco',
    maintainer_email='kevin@kevindemarco.com',
    description='Graphical frontend for interacting with joint_trajectory_controller instances',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'rqt_joint_trajectory_controller=rqt_joint_trajectory_controller.rqt_joint_trajectory_controller:main'
        ],
    },
)
