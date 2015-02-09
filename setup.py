from setuptools import setup, find_packages

setup(
    name='test-pypi-deploy',
    version='0.1',
    packages=find_packages(),

    test_suite='test',

    license='Apache 2',
    description='Test configuration for deployment to PyPi by Travis CI',
    url='https://github.com/2m/test-pypi-deploy',
)
