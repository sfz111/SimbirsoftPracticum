import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FormPage(BasePage):

    NAME_INPUT = (By.ID, 'name-input')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[type="password"]')
    CHECKBOX_MILK = (By.CSS_SELECTOR, '[value="Milk"]')
    CHECKBOX_COFFEE = (By.CSS_SELECTOR, '[value="Coffee"]')
    YELLOW_RADIO_BTN = (By.CSS_SELECTOR, '[value="Yellow"]')
    DROPDOWN = (By.ID, 'automation')
    EMAIl = (By.ID, "email")
    TOOLS = (By.XPATH, '//form/ul/li')
    MESSAGE_INPUT = (By.ID,'message')
    SUBMIT_BTN = (By.CSS_SELECTOR, '[id = "submit-btn"]')

    @allure.step("Заполняем поле Name")
    def input_name(self, name):
        self.input_field(locator=self.NAME_INPUT, text=name)

    @allure.step("Заполняем поле Password")
    def input_password(self, password):
        self.input_field(locator=self.PASSWORD_INPUT, text=password)

    @allure.step("Выбираем из списка 'What is your favorite drink?' вариант Milk")
    def select_checkbox_milk(self):
        self.click(locator=self.CHECKBOX_MILK)

    @allure.step("Выбираем из списка 'What is your favorite drink?' вариант Сoffe")
    def select_checkbox_coffee(self):
        self.click(locator=self.CHECKBOX_COFFEE)

    @allure.step("Выбираем из списка 'What is your favorite color?' вариант Yellow")
    def select_yellow_radio_btn(self):
        self.scroll_to_element(locator=self.YELLOW_RADIO_BTN)
        self.click(locator=self.YELLOW_RADIO_BTN)

    @allure.step("Выбираем вариант 'yes' в дропдауне 'Do you like automation?'")
    def select_in_dropdown(self):
        self.select_by_value(locator=self.DROPDOWN, value='yes')

    @allure.step("Заполняем поле Email")
    def input_email(self, email):
        self.input_field(locator=self.EMAIl, text=email)

    @allure.step("Вводим количество инструментов и самый длинный инструмент в поле Message")
    def input_message(self):
        elements = self.elements(locator=self.TOOLS)
        tools = [element.text for element in elements]
        longest_tool = max(tools, key=len)

        self.input_field(locator=self.MESSAGE_INPUT, text=f'{str(len(tools))}\n{longest_tool}')

    @allure.step("Нажимаем на кнопку Submit")
    def click_submit(self):
        self.scroll_to_element(locator=self.SUBMIT_BTN)
        self.click(locator=self.SUBMIT_BTN)

    @allure.step("Проверяем текст в появившемся алерте")
    def get_alert_text(self):
        return self.switch_to_alert_and_get_text()
