import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver(request):
    print("\nstart chrome browser for test..")
    driver = webdriver.Chrome()

    yield driver
    print("\nquit browser..")
    driver.quit()
