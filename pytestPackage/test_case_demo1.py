"""
file name should start with test
test method name should start with test

py.test test_mod.py   # run tests in module
py.test somepath      # run all tests below somepath
py.test test_module.py::test_method  # only run test_method in test_module

-s to print statements
-v verbose
"""

import pytest


@pytest.yield_fixture()

def setUp():
    print('Once before every method')
    yield
    print('Once after every method')


def test_demo1_methodA(setUp):
    print('Run A')

def test_demo1_methodB(setUp):
    print('Run B')

