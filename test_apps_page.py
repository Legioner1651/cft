import pytest
import time
from pages.apps_page import AppsPage
from pages.locators import AppsPageLocators
from pages.locators import MainPageLocators
from pages.locators import LoginFormLocators

link = "https://www.cft.ru/apps"

def test_button_2_main_page(browser):	#
    # 1. Инициализация Page Object, передача в конструктор экземпляр драйвера и url адрес.
    locator = AppsPageLocators.MAIN_PAGE_LINK
    page = AppsPage(browser, link)
    # 2. Открытие страницы.
    page.open()
    # 3. Проверка наменования кнопки
    assert page.get_button_attribute('alt', *locator) == 'Центр Финансовых Технологий', "Name button is wrong"
    # 4. Переход по кнопке
    page.click_go_button(*locator)
    # 5. Проверка правильности адреса перехода.
    assert page.get_self_url() == 'https://www.cft.ru/', "URL after transition is wrong"


def test_button_group_page(browser):	#
    # 1. Инициализация Page Object, передача в конструктор экземпляр драйвера и url адрес.
    locator = AppsPageLocators.GROUP_LINK
    page = AppsPage(browser, link)
    # 2. Открытие страницы.
    page.open()
    # 3. Проверка наменования кнопки
    assert page.get_button_text(*locator) == 'ГРУППА КОМПАНИЙ', "Name button is wrong"
    # 4. Переход по кнопке
    page.click_go_button(*locator)
    # 5. Проверка правильности адреса перехода.
    assert page.get_self_url() == 'https://cft.group/', "URL after transition is wrong"


def test_button_catalogs_products_page(browser):	#
    # 1. Инициализация Page Object, передача в конструктор экземпляр драйвера и url адрес.
    locator = AppsPageLocators.CATALOGS_PRODUCTS_LINK
    page = AppsPage(browser, link)
    # 2. Открытие страницы.
    page.open()
    # 3. Проверка наменования кнопки
    #page.get_button_text(*locator)
    assert page.get_button_text(*locator) == 'Каталоги решений и продуктов', "Name button is wrong"
    # 4. Переход по кнопке
    page.click_go_button(*locator)
    # 5. Проверка правильности адреса перехода.
    assert page.get_self_url() == 'https://catalog.cft.ru/', "URL after transition is wrong"


def test_applications_page(browser):	#
    # 1. Инициализация Page Object, передача в конструктор экземпляр драйвера и url адрес.
    locator = AppsPageLocators.APPLICATIONS_LINK
    page = AppsPage(browser, link)
    # 2. Открытие страницы.
    page.open()
    # 3. Проверка наменования кнопки
    #page.get_button_text(*locator)
    assert page.get_button_text(*locator) == 'Приложения', "Name button is wrong"
    # 4. Переход по кнопке
    page.click_go_button(*locator)
    # 5. Проверка правильности адреса перехода.
    assert page.get_self_url() == 'https://www.cft.ru/apps', "URL after transition is wrong"


def test_platforms_page(browser):	#
    # 1. Инициализация Page Object, передача в конструктор экземпляр драйвера и url адрес.
    locator = AppsPageLocators.PLATFORMS_LINK
    page = AppsPage(browser, link)
    # 2. Открытие страницы.
    page.open()
    # 3. Проверка наменования кнопки
    #page.get_button_text(*locator)
    assert page.get_button_text(*locator) == 'Архитектура и платформы', "Name button is wrong"
    # 4. Переход по кнопке
    page.click_go_button(*locator)
    # 5. Проверка правильности адреса перехода.
    assert page.get_self_url() == 'https://www.cft.ru/platforms', "URL after transition is wrong"


def test_services_page(browser):	#
    # 1. Инициализация Page Object, передача в конструктор экземпляр драйвера и url адрес.
    locator = AppsPageLocators.SERVICES_LINK
    page = AppsPage(browser, link)
    # 2. Открытие страницы.
    page.open()
    # 3. Проверка наменования кнопки
    #page.get_button_text(*locator)
    assert page.get_button_text(*locator) == 'Запуск и сопровождение', "Name button is wrong"
    # 4. Переход по кнопке
    page.click_go_button(*locator)
    # 5. Проверка правильности адреса перехода.
    assert page.get_self_url() == 'https://www.cft.ru/services', "URL after transition is wrong"


def test_outsourcing_page(browser):	#
    # 1. Инициализация Page Object, передача в конструктор экземпляр драйвера и url адрес.
    locator = AppsPageLocators.OUTSOURCING_LINK
    page = AppsPage(browser, link)
    # 2. Открытие страницы.
    page.open()
    # 3. Проверка наменования кнопки
    #page.get_button_text(*locator)
    assert page.get_button_text(*locator) == 'Аутсорсинг', "Name button is wrong"
    # 4. Переход по кнопке
    page.click_go_button(*locator)
    # 5. Проверка правильности адреса перехода.
    assert page.get_self_url() == 'https://www.cft.ru/outsourcing', "URL after transition is wrong"


def test_button_cft_bank_page(browser):	#
    # 1. Инициализация Page Object, передача в конструктор экземпляр драйвера и url адрес.
    locator = AppsPageLocators.CFTBANK_LINK
    page = AppsPage(browser, link)
    # 2. Открытие страницы.
    page.open()
    # 3. Проверка наменования кнопки
    assert page.get_button_text(*locator) == 'ЦФТ-Банк', "Name button is wrong"
    # 4. Проверка описания кнопки
    assert page.get_button_text(*AppsPageLocators.CFTBANK_TEXT) == 'ЦФТ-Банк Комплексный учет всех видов деятельности банка', "Description button is wrong"
    # 5. Переход по кнопке
    page.click_go_button(*locator)
    # 6. Проверка правильности адреса перехода.
    assert page.get_self_url() == 'https://catalog.cft.ru/applications/cftbank/overview', "URL after transition is wrong"


def test_button_system_apps_page(browser):	#
    # 1. Инициализация Page Object, передача в конструктор экземпляр драйвера и url адрес.
    locator = AppsPageLocators.CFT_SYSTEM_APP_LINK
    page = AppsPage(browser, link)
    # 2. Открытие страницы.
    page.open()
    # 3. Проверка наменования кнопки
    assert page.get_button_text(*locator) == 'ЦФТ-Системные приложения', "Name button is wrong"
    # 4. Проверка описания кнопки
    assert page.get_button_text(*AppsPageLocators.CFT_SYSTEM_APP_TEXT) == 'ЦФТ-Системные приложения Повышение производительности систем, снижение стоимости эксплуатации', "Description button is wrong"
    # 5. Переход по кнопке
    page.click_go_button(*locator)
    # 6. Проверка правильности адреса перехода.
    assert page.get_self_url() == 'https://catalog.cft.ru/applications/platform/overview#/bn:1', "URL after transition is wrong"
