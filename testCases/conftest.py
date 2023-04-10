import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        print("Launching Chrome Browser..........")
        driver = webdriver.Chrome()
    elif browser=="firefox":
        print("Launching Firefox Browser..........")
        driver = webdriver.Firefox()
    else:
        print("Launching Edge Browser..........")
        driver = webdriver.Ie()
    return driver

def pytest_addoption(parser):       # This will get value from CLI / hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):       #This will return browser value to setup method
    return request.config.getoption("--browser")



############## PyTest HTML Report#################
# It is a hook for Adding Environment info to HTML report
def pytest_configure(config):
    config._metadata['Project_Name']='NOP Commerce'
    config._metadata['Module_Name'] = 'Customers'
    config._metadata['Tester_Name'] = 'Amol'

# It is a hook for delete/modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)