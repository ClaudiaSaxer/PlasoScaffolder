#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This is the setup file for the project."""
from setuptools import find_packages
from setuptools import setup

setup(name='plasoscaffolder',
      version='0.1',
      packages=find_packages(),
      include_package_data=True,
      install_requires=['Click'],
      entry_points='''
        [console_scripts]
        plasoscaffolder=plasoscaffolder.frontend.argumentparser.main:entry_point
      ''')
