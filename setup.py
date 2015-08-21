import sys
from setuptools.command.test import test as TestCommand
from setuptools import setup, find_packages

class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initalize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(
    name='whoisxmlapi',
    version='0.1',
    description='Wrapper for whoisxmlapi web service',
    author='Kyle Richardson',
    author_email='kylerichardson2@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['requests'],
    tests_require=['pytest'],
    cmdclass={'test':PyTest},
)

