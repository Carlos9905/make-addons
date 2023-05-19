#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name='scaffold',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'tqdm==4.65.0',
    ],
    entry_points={
        'console_scripts': [
            'make_addons = scaffold_custom.cli:main'
        ]
    }
)
