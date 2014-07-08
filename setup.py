from distutils.core import setup

INSTALL_REQUIRES = ['lxml>=2.3.4']

setup(
    name='django-geo-world',
    version='1.2',
    packages=['django_geo_world'],
    url='https://github.com/jbonfante/django-geo-world',
    license='FreeBSD',
    author='juanrbonfante',
    author_email='juan@juanbonfante.com',
    description='Django Geo Starter Pack inlcuding World cities, states, and us zip codes.',
    install_requires=INSTALL_REQUIRES
)
