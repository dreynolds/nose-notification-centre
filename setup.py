import os
from setuptools import setup


setup(name='NCPlugin',
    version='0.3',
    author='David Reynolds',
    author_email='david@reynoldsfamily.org.uk',
    description=('Nose plugin to raise an OS X Notification'
        ' Center alert when a test run has finished'),
    long_description=open(
        os.path.join(
            os.path.dirname(__file__),
            'README.md',
        ), 'r').read(),
    url='https://github.com/dreynolds/nose-notification-centre',
    license='GNU LGPL',
    py_modules=['ncplugin'],
    platforms='MacOS X',
    install_requires=[
        'pync == 1.1',
    ],
    entry_points = {
        'nose.plugins.0.10': [
            'ncplugin = ncplugin:NCPlugin'
            ]
        },
    )