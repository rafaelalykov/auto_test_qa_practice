from base_page import BasePage
from selenium.webdriver.common.by import By

string_password_selector = (By.NAME, 'password')
password_result_selector = (By.XPATH, "//p[@class='result-text']")
password_value_warring = (By.XPATH, "//span[@id='error_1_id_password']")

class PasswordInput(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/input/passwd')

    def password(self):
        return self.find(string_password_selector)

    def result(self):
        return self.find(password_result_selector)

    def value_waring(self):
        return self.find(password_value_warring)