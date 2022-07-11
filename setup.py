from tkinter.ttk import setup_master
from setuptools import find_packages, setup

setup(
    name='mcdevtools',
    packages=find_packages(include=['mcdevtools']),
    version='0.0.1',
    description='my personal dev tools loaded into a python package',
    author='Luke McConnell',
    author_email='luke.mcconnell@gmail.com',
    url='https://github.com/lmcconnell1665/mcdevtools',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)