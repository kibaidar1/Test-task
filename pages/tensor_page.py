from pages.base_page import BasePage
from pages.locators import TensorLocators


class TensorPage(BasePage):

    def find_block_the_power_is_in_people(self):
        return self.find_element(TensorLocators.THE_POWER_IS_IN_PEOPLE_BLOCK)

    def go_to_about_block(self):
        about_link = self.find_element(TensorLocators.ABOUT_LINK)
        self.click_element(about_link)
