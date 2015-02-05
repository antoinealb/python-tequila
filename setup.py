#!/usr/bin/env python

from distutils.core import setup

setup(name='tequila-sessions',
      version='1.0.1',
      description='Requests session for Tequila (EPFL login manager)',
      author='Antoine Albertelli',
      author_email='antoine.albertelli+github@gmail.com',
      url='https://github.com/antoinealb/python-tequila',
      py_modules=['tequila'],
      install_requires=['requests', 'beautifulsoup4'],
      )
