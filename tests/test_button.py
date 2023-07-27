from pages.button import SimpleButtonPage, LikeAButton, SelectEnableButton
from selenium.webdriver.support.ui import Select


def test_simple_button_exist(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    assert simple_page.button_is_displayed()


def test_simple_button_clicked(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    simple_page.click_button()
    assert "Submitted" == simple_page.result().text


def test_looks_like_a_button_exist(browser):
    like_a_button_page = LikeAButton(browser)
    like_a_button_page.open()
    assert like_a_button_page.button_is_displayed()

def test_looks_like_a_button_clicked(browser):
    like_a_button_page = LikeAButton(browser)
    like_a_button_page.open()
    like_a_button_page.click_button()
    assert 'Submitted' == like_a_button_page.result().text

def test_enabled_select_button(browser):
    enabled_select_button = SelectEnableButton(browser)
    enabled_select_button.open()
    select = Select(enabled_select_button.button())
    select.select_by_value('enabled')
    enabled_select_button.click_submit()
    assert 'Submitted' == enabled_select_button.result().text

