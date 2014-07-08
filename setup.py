from distutils.core import setup
from setuptools import find_packages

INSTALL_REQUIRES = ['lxml>=2.3.4']

setup(
    name='django-geo-world',
    version='1.2',
    packages=find_packages(),
    url='https://github.com/jbonfante/django-geo-world',
    license='FreeBSD',
    author='juanrbonfante',
    author_email='juan@juanbonfante.com',
    description='Django Geo Starter Pack inlcuding World cities, states, and us zip codes.',
    install_requires=INSTALL_REQUIRES
)
