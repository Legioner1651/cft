from .base_page import BasePage
from .locators import AppsPageLocators
from pages.locators import MainPageLocators
from pages.locators import LoginFormLocators
import time


class AppsPage(BasePage):
    def click_go_button(self, *arg):                                                                    # клик по кнопке и переход на новую страницу
        assert self.is_element_present(*arg), "Link to button is not presented"                         # проверка существования кнопки
        # переход по ссылке
        element = self.browser.find_element(*arg)                                                       # получение элемента по которому нужно кликнуть
        element.click()
        handles = self.browser.window_handles                                                           # получение списка открытых окон
        # print('self.browser.window_handles = ' + str(handles))                                          # список открытых окон
        self.browser.switch_to.window(handles[len(handles) - 1])                                        # установить ссылку на последние окно
        self.url = self.browser.current_url                                                             # переприсваиваем объекту текущий URL
        # print('self.browser.current_url = ' + str(self.browser.current_url))                            #
        # print('self.browser.current_window_handle = "' + str(self.browser.current_window_handle) + '"') #
        time.sleep(2)

    def get_self_url(self):           # получение url объекта
        return self.url
        
    def get_button_attribute(self, attribute_name, *arg):
        return self.browser.find_element(*arg).get_attribute(attribute_name)

    def get_button_text(self, *arg):
        text = self.browser.find_element(*arg).text
        # print('get_text = "' + text + '"')
        text = str(text.replace("\n", " "))     # обработка случая когда текст распологался на нескольких строках
        # print(text)
        return text

    def get_text(self, *arg):
        #print(self.browser.find_element(*arg).get_attribute('alt'))
        print('get_text = "' + self.browser.find_element(*arg).text + '"')

