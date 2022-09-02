from selenium import  webdriver
import pytest

# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     return driver


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
       driver = webdriver.Chrome()
       # driver.maximize_window()
       print("Launching Chrome Browser.....")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        # driver.maximize_window()
        print("Launching Firefox Browser.....")
    else:
        driver = webdriver.Ie()    # Default browser run( not select any browser then)
    return driver

def pytest_addoption(parser):   #This will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):   #This will return the browser value to setup methos
    return request.config.getoption("--browser")



#################### Pytest Report #######################

#It is hook for Adding Environmet info to HTML.
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Model Name'] = 'customer'
    config._metadata['Tester'] = 'Om Chavan'


#It is hook for delet/Modify Enviroment info to HTML Report

def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)




