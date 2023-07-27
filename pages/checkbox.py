from base_page import BasePage
from selenium.webdriver.common.by import By

single_checkbox_selector = (By.CLASS_NAME, 'form-check-label')
submit_button_selector = (By.ID, 'submit-id-submit')
result_selector = (By.ID, 'result-text')

class CheckBoxSingle(BasePage):
    def __init__(self, browser):
        super(). __init__(browser)

    def open(self):
        self.browser.get("https://www.qa-practice.com/elements/checkbox/single_checkbox")

    def box(self):
        return self.find(single_checkbox_selector)

    def click_box(self):
        return self.find(single_checkbox_selector).click()

    def submit_button(self):
        return self.find(submit_button_selector)

    def click_button(self):
        return self.find(submit_button_selector).click()

    def result(self):
        return self.find(result_selector)

one_checkbox_selector = (By.XPATH, "//input[@value='one']")
two_checkbox_selector = (By.XPATH, "//input[@value='two']")
three_checkbox_selector = (By.XPATH, "//input[@value='three']")
button_selector = (By.ID, 'submit-id-submit')
result_selector_mult = (By.XPATH, "//p[@id='result-text']")


class CheckBoxMult(BasePage):
    def __init__(self, browser):
        super(). __init__(browser)

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/checkbox/mult_checkbox')

    def box1(self):
        return self.find(one_checkbox_selector)

    def box2(self):
        return self.find(two_checkbox_selector)

    def box3(self):
        return self.find(three_checkbox_selector)

    def click_box1(self):
        return self.find(one_checkbox_selector).click()

    def click_box2(self):
        return self.find(two_checkbox_selector).click()

    def click_box3(self):
        return self.find(three_checkbox_selector).click()

    def submit_button(self):
        return self.find(button_selector)

    def click_submit_button(self):
        return self.find(button_selector).click()

    def result(self):
        return self.find(result_selector)