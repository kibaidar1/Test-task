from pages.base_page import BasePage
from pages.locators import SBISPageLocators


class SBISPage(BasePage):

    def go_to_contacts(self):
        contacts_link = self.find_element(SBISPageLocators.CONTACTS_LINK)
        self.click_element(contacts_link)

