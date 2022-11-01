import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    # options = webdriver.FirefoxOptions()
    # options.add_argument('--headless')
    # browser = webdriver.Firefox(options=options)
    browser = webdriver.Firefox()
    yield browser
    print("\nquit browser for test..")
    browser.quit()
