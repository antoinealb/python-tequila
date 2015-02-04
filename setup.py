#!/usr/bin/env python

from distutils.core import setup

setup(name='tequila session',
      version='1.0',
      description='requests session for tequila, epfl login manager',
      author='Antoine Albertelli',
      author_email='antoine.albertelli+github@gmail.com',
      url='https://github.com/antoinealb/python-tequila',
      py_modules=['tequila'],
      install_requires=['requests', 'BeautifulSoup'],
      )
