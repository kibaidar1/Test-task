from pages.about_page import AboutPage
from pages.contacts_page import ContactsPage
from pages.sbis_page import SBISPage
from pages.tensor_page import TensorPage

SBIS_LINK = 'https://sbis.ru/'
ABOUT_LINK = 'https://tensor.ru/about'


def check_equal_dimensions(lst: list) -> bool:
    if len(set(lst)) == 1:
        return True
    else:
        return False


def test_case_one(driver):
    errors = []

    # 1) Перейти на https://sbis.ru/ в раздел "Контакты"
    sbis_page = SBISPage(driver=driver, url=SBIS_LINK)
    sbis_page.open()
    sbis_page.go_to_contacts()

    # 2) Найти баннер Тензор, кликнуть по нему
    contacts_page = ContactsPage(driver=driver, url=driver.current_url)
    contacts_page.click_banner()

    # 3) Перейти на https://tensor.ru/
    tensor_page = TensorPage(driver=driver, url=driver.current_url)

    # 4) Проверить, что есть блок "Сила в людях"
    tensor_page.find_block_the_power_is_in_people()

    # 5) Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается
    # https://tensor.ru/about
    tensor_page.go_to_about_block()
    about_page = AboutPage(driver=driver, url=driver.current_url)
    if not driver.current_url == ABOUT_LINK:
        errors.append(f'about link: {driver.current_url} in block "the power is in people" '
                      f'is not correct should be: {ABOUT_LINK}')

    # 6) Находим раздел Работаем и проверяем, что у всех фотографии
    # хронологии одинаковые высота (height) и ширина (width)
    block_working_images = about_page.get_block_working_images()
    images_width = [image.size['width'] for image in block_working_images]
    images_height = [image.size['height'] for image in block_working_images]
    if not check_equal_dimensions(images_width):
        errors.append("Width of images are not equal")
    if not check_equal_dimensions(images_height):
        errors.append('Height of images are not equal')

    assert not errors, '\n'.join(errors)
