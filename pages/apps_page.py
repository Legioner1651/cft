from .base_page import BasePage
import time


class AppsPage(BasePage):
    def click_go_button(self, *arg):                                                                    # клик по кнопке и переход на новую страницу
        assert self.is_element_present(*arg), "Link to button is not presented"                         # проверка существования кнопки
        # переход по ссылке
        element = self.browser.find_element(*arg)                                                       # получение элемента по которому нужно кликнуть
        element.click()
        handles = self.browser.window_handles                                                           # получение списка открытых окон
        self.browser.switch_to.window(handles[len(handles) - 1])                                        # установить ссылку на последние окно
        self.url = self.browser.current_url                                                             # переприсваиваем объекту текущий URL
        time.sleep(2)

    def get_self_url(self):           # получение url объекта
        return self.url
        
    def get_button_attribute(self, attribute_name, *arg):
        return self.browser.find_element(*arg).get_attribute(attribute_name)

    def get_button_text(self, *arg):
        text = self.browser.find_element(*arg).text
        text = str(text.replace("\n", " "))     # обработка случая когда текст располагался на нескольких строках
        return text

    def get_text(self, *arg):
        print('get_text = "' + self.browser.find_element(*arg).text + '"')

