from selenium.webdriver import Keys
from pages.password_input import PasswordInput

def test_password_input(browser):
    password_input = PasswordInput(browser)
    password = 'Qwerty12!'
    password_input.open()
    string = password_input.password()
    string.send_keys(password)
    string.send_keys(Keys.RETURN)
    assert password == password_input.result().text

def test_password_not_valid(browser):
    password_input = PasswordInput(browser)
    password_input.open()
    string = password_input.password()
    string.send_keys('12')
    string.send_keys(Keys.RETURN)
    assert password_input.value_waring()