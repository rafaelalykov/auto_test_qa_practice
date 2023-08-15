from base_page import BasePage
from selenium.webdriver.common.by import By

link_button_selector = (By.ID, 'new-page-link')
result_selector = (By.ID, "result-text")

class NewTabLink(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/new_tab/link')

    def link_button(self):
        return self.find(link_button_selector)

    def click_link_button(self):
        return self.link_button().click()

    def result(self):
        return self.find(result_selector)

button_selector = (By.ID, 'new-page-button')
result_text = (By.XPATH, "//p[@class='result-text']")


class NewTabButton(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/new_tab/button')

    def button(self):
        return self.find(button_selector)

    def click_button(self):
        return self.button().click()

    def result(self):
        return self.find(result_text)