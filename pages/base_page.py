from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def click_element(self, element, time=10):
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(element),
                                               message=f"Element: {element} is not clickable")
        element.click()

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator "
                                                              f"{locator} in {type(self).__name__}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator "
                                                              f"{locator} in {type(self).__name__}")

    def open(self):
        self.driver.get(self.url)

