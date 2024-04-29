import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="class")
def setup(request):
    service_obj = Service("D:\Softwares\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
