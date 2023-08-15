from base_page import BasePage
from selenium.webdriver.common.by import By

button = (By.CLASS_NAME, 'a-button')
class AlertBox(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/alert/alert')

    def button(self):
        return self.find(button)

    def click_button(self):
        return self.button().click()

    def ok_push(self):
        return self.browser.switch_to.alert.accept()

alert_button_conferm = (By.XPATH, "//a[@class='a-button']")
check_result = (By.XPATH, "//p[@class='result-text']")
class AlertConferm(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/alert/confirm')

    def button(self):
        return self.find(alert_button_conferm)

    def click_button(self):
        return self.button().click()

    def switch_to_alert_accept(self):
        return self.browser.switch_to.alert.accept()

    def switch_to_alert_dismiss(self):
        return self.browser.switch_to.alert.dismiss()

    def result(self):
        return self.find(check_result)

alert_button_promt = (By.CLASS_NAME, "a-button")
check_promt_result = (By.ID, "result-text")
class AlertPromt(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get("https://www.qa-practice.com/elements/alert/prompt")

    def button(self):
        return self.find(alert_button_promt)

    def click_button(self):
        return self.button().click()

    def assept_alert(self):
        return self.browser.switch_to.alert.accept()

    def dismiss_alert(self):
        return self.browser.switch_to.alert.dismiss()

    def result(self):
        return self.find(check_promt_result)




