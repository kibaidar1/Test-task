from pages.base_page import BasePage
from pages.locators import AboutLocators


class AboutPage(BasePage):

    def find_block_working(self):
        return self.find_element(AboutLocators.BLOCK_WORKING)

    def get_block_working_images(self):
        block_working = self.find_block_working()
        images = block_working.find_elements(*AboutLocators.BLOCK_WORKING_IMAGE)
        return images


