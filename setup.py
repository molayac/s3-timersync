#!/usr/bin/env python

from distutils.core import setup

setup(name='s3-timersync',
      version='1.0',
      description='Run every x seconds the aws s3 sync command until a y minutes timer.',
      author='Marlon Olaya',
      author_email='marlon.olaya.ac@gmail.com',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['s3timersync'],
      install_requires=['argparser', 'time', 'subprocess'],
      scripts=['s3-timersync']
     )
