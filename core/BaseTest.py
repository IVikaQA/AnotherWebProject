import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    driver = webdriver.Safari()
    yield driver
    if driver:
        driver.quit()