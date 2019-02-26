import pytest

@pytest.yield_fixture()
def setUp():
    print('Once before every method')
    yield
    print('Once after every method')



@pytest.yield_fixture(scope='class')
def OneTimeSetUp(request, browser):
    print('Once before every method monkey runs')
    if browser == "firefox":
        value = 10
        print("run on ff")
    else:
        value = 20
        print("run on chrome")

    if request.cls is not None:
        request.cls.value = value

    yield value
    print('Once after every method monkey runs')


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--ostype", help ="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--ostype")