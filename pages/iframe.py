from base_page import BasePage
from selenium.webdriver.common.by import By

iframe_screen = (By.CLASS_NAME, 'embed-responsive-item')
contact_selector = (By.CLASS_NAME, "navbar-toggler-icon")
album_example = (By.CLASS_NAME, "fw-light")

class Iframe(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/iframe/iframe_page')

    def iframe(self):
        return self.find(iframe_screen)

    def button_contact(self):
        return self.find(contact_selector)

    def click_contact(self):
        return self.button_contact()

    def check_text(self):
        return self.find(album_example)
