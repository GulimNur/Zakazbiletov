from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session')
def browser():
    options = Options()
    # options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    browser.maximize_window()
    yield browser
    #browser.quit()
