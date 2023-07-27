from base_page import BasePage
from selenium.webdriver.common.by import By

string_selector = (By.NAME, "text_string")
result_text_selector = (By.CLASS_NAME, "result-text")
word_value_warring_selector = (By.ID, "error_1_id_text_string")

class WordInput(BasePage):
    def __init__(self, browser):
        super(). __init__(browser)

    def open(self):
        self.browser.get("https://www.qa-practice.com/elements/input/simple")

    def string(self):
        return self.find(string_selector)

    def value_warring(self):
        return self.find(word_value_warring_selector)

    def result(self):
        return self.find(result_text_selector).text



