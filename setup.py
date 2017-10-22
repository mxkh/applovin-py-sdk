from setuptools import setup, find_packages
from os.path import join, dirname

import sdk

setup(
    name='applovin-py-sdk',
    version=sdk.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    install_requires=[
        'requests==2.18.4'
    ],
    test_suite='test_request'
)
