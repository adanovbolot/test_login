import pytest
from selenium import webdriver


@pytest.fixture
def get_webdriver(request):
    driver = webdriver.Firefox()
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://www.saucedemo.com/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()
