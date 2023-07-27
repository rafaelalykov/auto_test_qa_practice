from base_page import BasePage
from selenium.webdriver.common.by import By

select_selector = (By.ID, "id_choose_language")
submit_button_selector = (By.ID, "submit-id-submit")
check_result = (By.ID, "result-text")

class SingleSelect(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get("https://www.qa-practice.com/elements/select/single_select")

    def button(self):
        return self.find(select_selector)

    def submit_button(self):
        return self.find(submit_button_selector)

    def click_submit(self):
        return self.submit_button().click()

    def result(self):
        return self.find(check_result)

select_one_selector = (By.ID, "id_choose_the_place_you_want_to_go")
select_two_selector = (By.ID, "id_choose_how_you_want_to_get_there")
select_three_selector = (By.ID, "id_choose_when_you_want_to_go")
submit_selector = (By.ID, "submit-id-submit")
check_mult_result = (By.ID, "result-text")

class MultSelec(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/select/mult_select')

    def select1(self):
        return self.find(select_one_selector)

    def select2(self):
        return self.find(select_two_selector)

    def select3(self):
        return self.find(select_three_selector)

    def submit_button(self):
        return self.find(submit_selector)

    def click_submit(self):
        return self.submit_selector().click

    def result(self):
        return self.find(check_mult_result)






