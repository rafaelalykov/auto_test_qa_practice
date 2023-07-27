
from pages.select import SingleSelect, MultSelec
from selenium.webdriver.support.ui import Select

def test_single_select(browser):
    single_select = SingleSelect(browser)
    single_select.open()
    language = Select(single_select.button())
    language.select_by_value('1')
    single_select.click_submit()
    assert "Python" == single_select.result().text

def test_mult_select(browser):
    mult_select = MultSelec(browser)
    mult_select.open()
    the_place = Select(mult_select.select1())
    the_place.select_by_value('1')
    how = Select(mult_select.select2())
    how.select_by_value('1')
    when = Select(mult_select.select3())
    when.select_by_value('1')
    mult_select.submit_button().click()
    assert 'to go by car to the sea today' == mult_select.result().text
