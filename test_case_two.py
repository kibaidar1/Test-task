from pages.contacts_page import ContactsPage
from pages.sbis_page import SBISPage

SBIS_URL = 'https://sbis.ru/'
CONTACTS_URL = 'https://sbis.ru/contacts/'
MOSCOW_REGION = 'г. Москва'
KAMCHATKA_REGION = 'Камчатский край'


def test_case_two(driver):
    errors = []

    # 1) Перейти на https://sbis.ru/ в раздел "Контакты"
    sbis_page = SBISPage(driver=driver, url=SBIS_URL)
    sbis_page.open()
    sbis_page.go_to_contacts()

    # 2) Проверить, что определился ваш регион
    contacts_page = ContactsPage(driver=driver, url=driver.current_url)
    contacts_page.get_partners_list()
    region_chooser = contacts_page.get_region_chooser_in_content()
    if not region_chooser.text == MOSCOW_REGION:
        errors.append('The region was determined incorrectly')

    # 3) Изменить регион на Камчатский край
    old_partners_list = contacts_page.get_partners_list()
    contacts_page.set_kamchatka_region()

    # 4) Проверить, что подставился выбранный регион, список партнеров
    # изменился, url и title содержат информацию выбранного региона
    new_partners_list = contacts_page.get_partners_list()
    if not contacts_page.get_region_chooser_in_content().text == KAMCHATKA_REGION:
        errors.append('The region has not changed')
    if not old_partners_list != new_partners_list:
        errors.append('The partners list has not changed')
    if 'kamchatskij-kraj' not in driver.current_url:
        errors.append('The URL does not contain information about the selected region')
    if 'Камчатский край' not in driver.title:
        errors.append('The TITLE does not contain information about the selected region')
    assert not errors, '\n'.join(errors)
