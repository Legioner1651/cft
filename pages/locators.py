# вынесли селекторы внешними переменными, переменная - кортеж из двух элементов
from selenium.webdriver.common.by import By


class AppsPageLocators():
    LOGIN_FORM_LINK             = (By.CSS_SELECTOR, 'ul.cft-user-nav > li:nth-child(2) > a')                            # ссылка на "Вход"
    REGISTRATION_FORM_LINK      = (By.CSS_SELECTOR, 'ul.cft-user-nav > li:nth-child(4) > a')                            # ссылка на "Регистрацию"
    
    MAIN_PAGE_LINK              = (By.CSS_SELECTOR, "div.logo > a > img")                                               # ссылка на главную страницу
    SOFTWARE_LINK               = (By.CSS_SELECTOR, "div.header-dropdown.collapsable-control > span")                   # ссылка на страницу "Программное обеспечение"
    GROUP_LINK                  = (By.CSS_SELECTOR, "div.global-wrap > header > a")                                     # ссылка на страницу "Группа компаний"
    
    CATALOGS_PRODUCTS_LINK      = (By.CSS_SELECTOR, '.catalog-link > span')                                             # ссылка на страницу "Каталоги решений и продуктов"
    APPLICATIONS_LINK           = (By.CSS_SELECTOR, "a.active > span")                                                  # ссылка на страницу "Приложения"
    PLATFORMS_LINK              = (By.CSS_SELECTOR, "div.main-nav.all-window-width > div > nav > a:nth-child(3) > span")# ссылка на страницу "Архитектура и платформы"
    SERVICES_LINK               = (By.CSS_SELECTOR, "div.main-nav.all-window-width > div > nav > a:nth-child(4) > span")# ссылка на страницу "Запуск и сопровождение"
    OUTSOURCING_LINK            = (By.CSS_SELECTOR, 'div.main-nav.all-window-width > div > nav > a:nth-child(5) > span')# ссылка на страницу "Аутсорсинг"

    SELECT_DIRECTORY_LINK       = (By.CSS_SELECTOR, 'div.container > div > ul > li:nth-child(1) > a')                   # Выберите каталог
    POTENTIAL_CLIENTS_LINK      = (By.CSS_SELECTOR, 'div.container > div > ul > li:nth-child(2) > a')                   # Потенциальным клиентам

    CFTBANK_LINK                = (By.XPATH, '//*[@id="tab1"]/div/ul/li[1]/a/div/h2')                                   # ЦФТ-Банк
    CFTBANK_TEXT                = (By.XPATH, '//*[@id="tab1"]/div/ul/li[1]/a/div')                                      # ЦФТ-Банк (текст)
    CFT_SYSTEM_APP_LINK         = (By.CSS_SELECTOR, '#tab1 > div > ul > li:nth-child(2) > a > div > h2')                # ЦФТ-Системные приложения
    CFT_SYSTEM_APP_TEXT         = (By.XPATH, '//*[@id="tab1"]/div/ul/li[2]/a/div')                                      # ЦФТ-Системные приложения (текст)
    CFT_RETAIL_BANK_LINK        = (By.CSS_SELECTOR, '#tab1 > div > ul > li:nth-child(3) > a > div > h2')                # ЦФТ-Ритейл банк
    CFT_SERVICE_SUITE_LINK      = (By.CSS_SELECTOR, '#tab1 > div > ul > li:nth-child(4) > a > div > h2')                # ЦФТ-Сервис Сьют (CFT-Service Suite)
    CFT_RETAIL_BANK_DBI_LINK    = (By.CSS_SELECTOR, '#tab1 > div > ul > li:nth-child(5) > a > div > h2')                # ЦФТ-Ритейл банк (РБС)
    PROCESSING_CENTER_LINK      = (By.CSS_SELECTOR, '#tab1 > div > ul > li:nth-child(6) > a > div > h2')                # ЦФТ-Процессинговый центр
    CFT_CORPORATE_LINK          = (By.CSS_SELECTOR, '#tab1 > div > ul > li:nth-child(7) > a > div > h2')                # ЦФТ-Корпорация
    CFT_DIGITAL_ARCHIVE_LINK    = (By.CSS_SELECTOR, '#tab1 > div > ul > li:nth-child(8) > a > div > h2')                # ЦФТ-Электронный архив
    CFT_KONTEKST_INFORM_LINK    = (By.CSS_SELECTOR, '#tab1 > div > ul > li:nth-child(9) > a > div > h2')                # ЦФТ-Контекстное информирование
    CFT_MACHINE_LINK            = (By.CSS_SELECTOR, '#tab1 > div > ul > li:nth-child(10) > a > div > h2')               # ЦФТ-Машина тестирования
    CFT_MANAGEMENT_LINK         = (By.CSS_SELECTOR, '#tab1 > div > ul > li:nth-child(11) > a > div > h2')               # ЦФТ-Управленческий учет
    CFT_BUDGET_LINK             = (By.CSS_SELECTOR, '#tab1 > div > ul > li:nth-child(12) > a > div > h2')               # ЦФТ-Бюджетное планирование
    CFT_AML_LINK                = (By.CSS_SELECTOR, '#tab1 > div > ul > li:nth-child(13) > a > div > h2')               # ЦФТ-AML

    CFT_APPS_ARCHIVE_LINK       = (By.CSS_SELECTOR, '#tab1 > div > div > p > a')                                        # Архивные материалы
    PRICE_LINK                  = (By.CSS_SELECTOR, 'div.footer-top > div > ul > li:nth-child(1) > p:nth-child(1) > a') # Прайс-лист
    STOCK_LINK                  = (By.CSS_SELECTOR, 'div.footer-top > div > ul > li:nth-child(1) > p:nth-child(2) > a') # Акции
    CORPORATE_SECTOR_LINK       = (By.CSS_SELECTOR, 'div.footer-top > div > ul > li:nth-child(1) > p:nth-child(3) > a') # Корпоративному сектору
    PARTNERS_LINK               = (By.CSS_SELECTOR, 'div.footer-top > div > ul > li:nth-child(1) > p:nth-child(4) > a') # Партнерам
    SOLUTIONS_LINK              = (By.CSS_SELECTOR, 'div.footer-top > div > ul > li:nth-child(1) > p:nth-child(5) > a') # Банкам СНГ

    PRESS_CENTER_LINK           = (By.CSS_SELECTOR, 'div.footer-top > div > ul > li:nth-child(2) > p:nth-child(1) > a') # Новости и публикации
    EVENTS_LINK                 = (By.CSS_SELECTOR, 'div.footer-top > div > ul > li:nth-child(2) > p:nth-child(2) > a') # Мероприятия
    TEAM_LINK                   = (By.CSS_SELECTOR, 'div.footer-top > div > ul > li:nth-child(2) > p:nth-child(3) > a') # Карьера
    CONTACTS_LINK               = (By.CSS_SELECTOR, 'div.footer-top > div > ul > li:nth-child(2) > p:nth-child(4) > a') # Контакты

    POLITICS_LINK               = (By.CSS_SELECTOR, 'div.footer-top > div > ul > li:nth-child(3) > p:nth-child(1) > a') # Политика в области обработки персональных данных

    POTENTIAL_CLIENTS_TITLE     = (By.CSS_SELECTOR, '#tab2 > div > h2')                                                 # Потенциальным клиентам (заголовок)
    POTENTIAL_CLIENTS_TEXT01    = (By.CSS_SELECTOR, 'div.content-col > div > div:nth-child(1)')                         # Потенциальным клиентам (текст 01)
    POTENTIAL_CLIENTS_TEXT02    = (By.CSS_SELECTOR, 'div.content-col > div > div:nth-child(3)')                         # Потенциальным клиентам (текст 02)


class MainPageLocators():
    APPLICATIONS_LINK           = (By.CSS_SELECTOR, 'div.main-nav.all-window-width > div > nav > a:nth-child(2) > span')# ссылка на страницу "Приложения"


class LoginFormLocators():
    LOGIN_TITLE                 = (By.CSS_SELECTOR, 'div.cabinet-header > h1')                                          # форма логирования, заголовок
    LOGIN_TEXT01                = (By.CSS_SELECTOR, 'div.col.login-text > p:nth-child(1)')                              # форма логирования, описание содержания
    LOGIN_HEADING1              = (By.CSS_SELECTOR, 'div.col.login-text > p:nth-child(2)')                              # форма логирования, заголовок 1
    LOGIN_TEXT02                = (By.XPATH, '//*[@id="aspnetForm"]/div[3]/div[3]/div[2]/div[4]/div[2]/ul[1]/li[1]/text()') # форма логирования, текст 1
    LOGIN_TEXT03                = (By.XPATH, '//*[@id="aspnetForm"]/div[3]/div[3]/div[2]/div[4]/div[2]/ul[1]/li[2]/text()') # форма логирования, текст 2
    LOGIN_HEADING2              = (By.CSS_SELECTOR, 'div.col.login-text > p:nth-child(4)')                              # форма логирования, заголовок 2
    LOGIN_HEADING3              = (By.CSS_SELECTOR, 'div.col.login-text > p:nth-child(6)')                              # форма логирования, заголовок 3
    LOGIN_NAME_LINK             = (By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_UsernameTextBox')                       # форма логирования, "Имя пользователя"
    LOGIN_PASSWORD_LINK         = (By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_PasswordTextBox')                       # форма логирования, "Пароль"
    LOGIN_CODE_LINK             = (By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_captchaInputtedText')                   # форма логирования, "Код с картинки"
