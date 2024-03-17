from selenium.webdriver.common.by import By


class AboutLocators:
    BLOCK_WORKING = (By.CSS_SELECTOR, 'div.tensor_ru-container.tensor_ru-section.tensor_ru-About__block3')
    BLOCK_WORKING_IMAGE = (By.TAG_NAME, 'img')


class ContactsLocators:
    KAMCHATKA_REGION = (By.CSS_SELECTOR, '[title="Камчатский край"]')
    PARTNERS_ITEM = (By.CSS_SELECTOR, '.sbisru-Contacts-List__item')
    REGION_CHOOSER_IN_CONTENT = (By.CSS_SELECTOR, '.sbis_ru-content_wrapper .sbis_ru-Region-Chooser__text')
    TENSOR_BANNER = (By.CSS_SELECTOR, '[title="tensor.ru"]')


class SBISPageLocators:
    CONTACTS_LINK = (By.CSS_SELECTOR, '[href="/contacts"]')


class TensorLocators:
    ABOUT_LINK = (By.CSS_SELECTOR, '[href="/about"]')
    THE_POWER_IS_IN_PEOPLE_BLOCK = (By.CSS_SELECTOR, 'p.tensor_ru-Index__card-title.tensor_ru-pb-16')
