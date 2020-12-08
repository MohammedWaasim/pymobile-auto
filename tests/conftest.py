import configparser
import pytest
from base.webdriverfactory import WebDriverFactory
@pytest.fixture(scope="class")
def oneTimeSetUp(request,apptype):
    print("running ots")
    config=configparser.ConfigParser()
    config.read('properties.ini')
    wdf=WebDriverFactory(apptype)
    driver=wdf.webDriverInstance(config['appium_demo']["apk_file_path"])
    if request.cls is not None:
        request.cls.test_data_path=config['appium_demo']["test_data_path"]
        request.cls.driver=driver
    yield True
    driver.quit()
    print("quiting ots")

def pytest_addoption(parser):
    parser.addoption("--apptype")

@pytest.fixture(scope="session")
def apptype(request):
    return request.config.getoption("--apptype")
