#!/usr/bin/env python3

# SAM
# Copyright © 2017 Arkena S.A

import computor

from setuptools import setup, find_packages


setup(
    name='computorv2',
    version=computor.__version__,
    description='ComputorV2 Mega FUN',
    long_description="""
    Awesome calc tool
    """,
    author='Robinson.bernand',
    author_email='robinson.bernand@student.42.com',
    packages=find_packages(),
    include_package_data=True,
    setup_requires=[
        'pytest-runner'
    ],
    install_requires=[
        'prompt-toolkit',
        'docopt',
    ],
    tests_require=[
        'pytest',
    ],
    classifiers=[
        'Operating System :: *',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': ['computorv2=computor.__main__:main']
    }
)
