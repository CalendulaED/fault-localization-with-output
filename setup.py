from setuptools import setup
import sys
import os

VERSION = '0.0.1'
DESCRIPTION = 'fault localization with output indication'


setup(
    name='fault-localization-output',
    packages=['fault_localization_output'],
    platforms='any',
    version='0.0.1',
    description='A fault localization tool for Python\'s pytest testing framework with output.',
    author='Yuxuan Wu',
    author_email='edmundwuyuxuan@gmail.com',
    url='https://github.com/CalendulaED/fault-localization-output',
    license='MIT',
    install_requires=[
        'pytest>=3.1.2',
    ],
    entry_points={
        'pytest11': [
            'fault-localization-output = fault_localization_output.plugin',
        ]
    },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ]
)
