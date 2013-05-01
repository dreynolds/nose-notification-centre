from setuptools import setup


setup(name='NCPlugin',
    version='0.2',
    author='David Reynolds',
    author_email='david@reynoldsfamily.org.uk',
    description=('Plugin to raise an OS X Notification'
        ' Center alert when a test run has finished'),
    license='GNU LGPL',
    py_modules=['ncplugin'],
    install_requires=[
        'pync == 1.1',
    ],
    entry_points = {
        'nose.plugins.0.10': [
            'ncplugin = ncplugin:NCPlugin'
            ]
        },
    )