from selenium.webdriver import Keys
from pages.text_areas import TextAreaInput, ThreeAreasInput


def test_text_area_input(browser):
    text = "Hello, authotest is done"
    area_input = TextAreaInput(browser)
    area_input.open()
    string = area_input.area()
    string.send_keys(text)
    area_input.click_select_button()
    assert "Hello, authotest is done" == area_input.result().text

def test_three_areas(browser):
    three_areas = ThreeAreasInput(browser)
    three_areas.open()
    first_chapter = three_areas.area_one()
    second_chapter = three_areas.area_two()
    third_chapter = three_areas.area_three()
    first_chapter.send_keys('qwerty')
    second_chapter.send_keys('qwerty')
    third_chapter.send_keys('qwerty')
    three_areas.submit_button().send_keys(Keys.RETURN)
    assert "Qwert" in three_areas.result().text