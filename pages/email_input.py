from base_page import BasePage
from selenium.webdriver.common.by import By

string_selector = (By.XPATH, "//input[@id='id_email']")
result_selector = (By.CLASS_NAME, "result-text")
not_valid_selector = (By.ID, "error_1_id_email")

class EmailInput(BasePage):
    def __init__(self, browser):
        super(). __init__(browser)

    def open(self):
        self.browser.get("https://www.qa-practice.com/elements/input/email")

    def email(self):
        return self.find(string_selector)

    def result(self):
        return self.find(result_selector)

    def not_valid_result(self):
        return self.find(not_valid_selector)