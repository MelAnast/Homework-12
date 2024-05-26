import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    # pre-condition
    driver = webdriver.Chrome()
    # return driver
    yield driver
    # post-conditions / teardown
    driver.close()
