import pytest

@pytest.yield_fixture()
def setUp():
    print('Once before every method')
    yield
    print('Once after every method')



@pytest.yield_fixture()
def OneTimeSetUp():
    print('Once before every method monkey runs')
    yield
    print('Once after every method monkey runs')
