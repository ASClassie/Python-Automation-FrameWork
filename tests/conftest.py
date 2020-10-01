import pytest
from selenium import webdriver
from base.webdriverfactory import WebDriverFactory


# execution order for same file using wildcards pytest -v -s test_conftest_demo*.py

@pytest.yield_fixture()
def setUp():
    print('Running method lvl setUp')
    yield
    print('Running method lvl  tearDown')


@pytest.yield_fixture(scope='class')
def oneTimeSetUp(request, browser):
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print('Running one time tearDown')


def pytest_addoption(parser):
    parser.addoption('--browser')
    parser.addoption('--osType', help='Type of operating system')


@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption('--browser')


@pytest.fixture(scope='session')
def osType(request):
    return request.config.getoption('--osType')
