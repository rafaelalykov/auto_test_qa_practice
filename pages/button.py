from base_page import BasePage
from selenium.webdriver.common.by import By

simple_button_selector = (By.ID, 'submit-id-submit')
simple_result_selector = (By.CLASS_NAME, "result-text")

class SimpleButtonPage(BasePage):
    def __init__(self, browser):
        super(). __init__(browser)

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/button/simple')

    def button(self):
        return self.find(simple_button_selector)

    def button_is_displayed(self):
        return self.button().is_displayed()

    def click_button(self):
        return self.button().click()

    def result(self):
        return self.find(simple_result_selector)

like_a_button_selector = (By.LINK_TEXT, 'Click')
result_selector = (By.ID, 'result-text')

class LikeAButton(BasePage):
    def __init__(self, browser):
        super(). __init__(browser)

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/button/like_a_button')

    def button(self):
        return self.find(like_a_button_selector)

    def button_is_displayed(self):
        return self.button().is_displayed()

    def click_button(self):
        return self.button().click()

    def result(self):
        return self.find(result_selector)

select_button_selector = (By.CLASS_NAME, "form-select")
submit_selector = (By.ID, "submit-id-submit")
check_result = (By.CLASS_NAME, 'result-text')

class SelectEnableButton(BasePage):
    def __init__(self, browser):
        super(). __init__(browser)

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/button/disabled')

    def button(self):
        return self.find(select_button_selector)

    def select(self):
        return self.find(submit_selector)

    def click_submit(self):
        return self.select().click()

    def result(self):
        return self.find(check_result)