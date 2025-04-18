import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# @pytest.fixture(scope="session")
# def browser_session():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption("--language", action="store", default="en",
                     help="Choose language: e.g., en, ru, es")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    browser = None
    options = Options()
    if browser_name == "chrome":
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options.set_preference("intl.accept_languages", language)
        driver_browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()
