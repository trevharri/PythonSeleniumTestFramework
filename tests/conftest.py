import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service('/Users/trevorharrington/Downloads/chrome-mac-x64/Google Chrome for Testing.app')
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        pass
    elif browser_name == "edge":
        pass
    driver.implicitly_wait(2)
    driver.get('https://www.rahulshettyacademy.com/angularpractice/')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
