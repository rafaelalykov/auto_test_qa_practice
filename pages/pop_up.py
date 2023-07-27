from base_page import BasePage
from selenium.webdriver.common.by import By

launch_pop_up_celector = (By.XPATH, "//button[normalize-space()='Launch Pop-Up']")
check_box_selector = (By.ID, "id_checkbox_0")
send_button_selector = (By.XPATH, "//button[@type='submit']")
check_result = (By.XPATH, "//p[@id='result-text']")

class PopUp(BasePage):
    def __init__(self, browser):
        super(). __init__(browser)

    def open(self):
        self.browser.get("https://www.qa-practice.com/elements/popup/modal")

    def launch_button(self):
        return self.find(launch_pop_up_celector)

    def click_launch(self):
        return self.launch_button().click()

    def check_box(self):
        return self.find(check_box_selector)

    def click_check_box(self):
        return self.check_box().click()

    def send_button(self):
        return self.find(send_button_selector)

    def click_send_button(self):
        return self.send_button().click()

    def result(self):
        return self.find(check_result)
