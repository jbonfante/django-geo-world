# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import django_geo_world
version = django_geo_world.__version__

setup(
    name='Django Geo World',
    version=version,
    author='Juan Bonfante',
    author_email='juan.bonfante@gmail.com',
    packages=[
        'django_geo_world',
        ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
        ],
    zip_safe=False,
    scripts=['django_geo_world/manage.py'],
    description='Django Geo Starter Pack inlcuding World cities, states, and us zip codes.',
    )