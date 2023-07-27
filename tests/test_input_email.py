from selenium.webdriver import Keys
from pages.email_input import EmailInput

def test_email_input(browser):
    email_input = EmailInput(browser)
    email = "python@rambled.ru"
    email_input.open()
    string = email_input.email()
    string.send_keys(email)
    string.send_keys(Keys.RETURN)
    assert email == email_input.result().text

def test_email_not_valid_input(browser):
    email_input = EmailInput(browser)
    email = "pythonrambled.ru"
    email_input.open()
    string = email_input.email()
    string.send_keys(email)
    string.send_keys(Keys.RETURN)
    assert email_input.not_valid_result()