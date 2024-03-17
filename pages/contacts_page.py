import time

from pages.base_page import BasePage
from pages.locators import ContactsLocators


class ContactsPage(BasePage):

    def click_banner(self):
        banner = self.find_element(ContactsLocators.TENSOR_BANNER)
        self.click_element(banner)
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

    def get_region_chooser_in_content(self):
        return self.find_element(ContactsLocators.REGION_CHOOSER_IN_CONTENT)

    def get_partners_list(self):
        return self.find_elements(ContactsLocators.PARTNERS_ITEM)

    def set_kamchatka_region(self):
        region_chooser = self.get_region_chooser_in_content()
        self.click_element(region_chooser)
        kamchatka_region = self.find_element(ContactsLocators.KAMCHATKA_REGION)
        self.click_element(kamchatka_region)
        time.sleep(1)  # wait for update page



