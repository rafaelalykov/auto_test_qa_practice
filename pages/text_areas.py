from base_page import BasePage
from selenium.webdriver.common.by import By

area_selector = (By.NAME, 'text_area')
submit_button_selector = (By.ID, 'submit-id-submit')
result_selector = (By.XPATH, "//p[@id='result-text']")

class TextAreaInput(BasePage):
    def __init__(self, browser):
        super(). __init__(browser)

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/textarea/single')

    def area(self):
        return self.find(area_selector)

    def select_button(self):
        return self.find(submit_button_selector)

    def click_select_button(self):
        return self.select_button().click()

    def result(self):
        return self.find(result_selector)

first_area_selector = (By.NAME, 'first_chapter')
second_area_selector = (By.NAME, 'second_chapter')
third_area_selector = (By.NAME, 'third_chapter')
submit_button = (By.NAME, 'submit')
result = (By.XPATH,"//p[@id='result-text']")

class ThreeAreasInput(BasePage):
    def __init__(self, browser):
        super(). __init__(browser)

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/textarea/textareas')

    def area_one(self):
        return self.find(first_area_selector)

    def area_two(self):
        return self.find(second_area_selector)

    def area_three(self):
        return self.find(third_area_selector)

    def submit_button(self):
        return self.find(submit_button)

    def click_submit_button(self):
        return self.submit_button().click()

    def result(self):
        return self.find(result)