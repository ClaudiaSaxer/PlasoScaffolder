#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This is the setup file for the project."""
from setuptools import find_packages
from setuptools import setup

setup(name='plasoscaffolder',
      version='0.1',
      packages=find_packages(),
      include_package_data=True,
      package_data={'plasoscaffolder.bll.templates': ['*.jinja2'], },
      install_requires=['Click', 'setuptools', 'jinja2', 'colorama'],
      entry_points='''
        [console_scripts]
        plasoscaffolder=plasoscaffolder.frontend.main:entry_point
      ''')
